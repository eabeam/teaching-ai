"""
Scrape university websites for AI access and policy information relevant to
RESEARCHERS (not student academic integrity policies).

For each institution in institutions.csv:
1. Search for AI tools/access pages (IT, research office, provost)
2. Search for IRB AI guidance
3. Search for enterprise AI agreements (OpenAI, Anthropic, Microsoft)
4. Extract relevant content
5. Output a CSV for human coding

Focus: Does the institution provide AI tools to faculty/researchers?
       Is there policy guidance for research use specifically?
       NOT: student honor code / academic integrity re: AI

Usage:
    python3 scrape_university_access.py
    python3 scrape_university_access.py --institution "Harvard"
    python3 scrape_university_access.py --start-from 20  # resume from row 20

Output: output/university_ai_access.csv
"""

import csv
import json
import re
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import pandas as pd

SCRIPT_DIR = Path(__file__).parent
INSTITUTIONS_CSV = SCRIPT_DIR / "institutions.csv"
OUTPUT_DIR = SCRIPT_DIR / "output"
OUTPUT_CSV = OUTPUT_DIR / "university_ai_access.csv"
OUTPUT_JSON = OUTPUT_DIR / "university_ai_raw.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Academic Research Bot - emily.beam@uvm.edu"
}

REQUEST_DELAY = 3  # seconds between requests (be polite to university sites)

# Keywords for RESEARCHER access (not student policies)
RESEARCH_AI_KEYWORDS = re.compile(
    r"(?:"
    r"faculty.*(?:AI|artificial intelligence|ChatGPT|Claude|Copilot)"
    r"|(?:AI|artificial intelligence).*(?:research|faculty|staff)"
    r"|enterprise.*(?:AI|ChatGPT|OpenAI|Anthropic|Claude)"
    r"|(?:ChatGPT|Claude|Copilot).*(?:licen[sc]e|access|available|provision)"
    r"|institutional.*(?:AI|artificial intelligence).*(?:access|tool|platform)"
    r"|(?:AI|artificial intelligence).*(?:data|privacy|security).*research"
    r"|IRB.*(?:AI|artificial intelligence|ChatGPT)"
    r"|(?:AI|artificial intelligence).*(?:IRB|ethics|human subjects)"
    r"|generative.*AI.*(?:research|policy|guidance)"
    r"|(?:subsidiz|fund|provid).*(?:AI|ChatGPT|Claude|Copilot)"
    r")",
    re.IGNORECASE,
)

# Keywords to EXCLUDE (student-focused pages)
STUDENT_ONLY_KEYWORDS = re.compile(
    r"(?:"
    r"academic.integrity.*AI"
    r"|plagiarism.*AI"
    r"|syllabus.*(?:AI|ChatGPT)"
    r"|honor.code.*(?:AI|ChatGPT)"
    r"|student.*(?:may not|cannot|prohibited).*(?:AI|ChatGPT)"
    r")",
    re.IGNORECASE,
)


def build_search_urls(institution: str) -> list[dict]:
    """
    Build a list of search queries / direct URLs to try for each institution.
    Returns list of {query, search_type} dicts.
    """
    # Clean institution name for search
    clean_name = institution.replace("University of ", "").replace("University", "")

    searches = [
        {
            "query": f"{institution} AI tools faculty research access",
            "search_type": "faculty_access",
        },
        {
            "query": f"{institution} ChatGPT Claude enterprise agreement faculty",
            "search_type": "vendor_agreement",
        },
        {
            "query": f"{institution} IRB artificial intelligence guidance research",
            "search_type": "irb_guidance",
        },
        {
            "query": f"{institution} generative AI policy research faculty",
            "search_type": "research_policy",
        },
        {
            "query": f"{institution} AI research computing services",
            "search_type": "computing_services",
        },
    ]
    return searches


def google_search(query: str, num_results: int = 5) -> list[str]:
    """
    Perform a Google search and return result URLs.
    Uses Google's JSON API if available, otherwise falls back to scraping.

    NOTE: For production use, consider using Google Custom Search API
    or SerpAPI to avoid rate limiting. For now, this returns placeholder
    URLs that need manual verification.
    """
    # Google Custom Search API approach (requires API key)
    # If you have a Google API key, uncomment and configure:
    #
    # API_KEY = os.environ.get("GOOGLE_API_KEY")
    # CX = os.environ.get("GOOGLE_CX")  # Custom Search Engine ID
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}&num={num_results}"
    # resp = requests.get(url)
    # items = resp.json().get("items", [])
    # return [item["link"] for item in items]

    # Fallback: construct likely URLs based on common university patterns
    # This is a starting point — manual verification needed
    return []


def fetch_and_extract(url: str) -> dict:
    """Fetch a URL and extract relevant text blocks."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException as e:
        return {"status": "failed", "error": str(e), "blocks": []}

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    blocks = []
    for el in soup.find_all(["p", "li", "td", "div", "h1", "h2", "h3", "h4", "section"]):
        text = el.get_text(separator=" ", strip=True)
        if len(text) > 40:
            blocks.append(text)

    # Filter to research-relevant blocks
    relevant = []
    for block in blocks:
        if RESEARCH_AI_KEYWORDS.search(block):
            if not STUDENT_ONLY_KEYWORDS.search(block):
                relevant.append(block)

    return {"status": "success", "blocks": relevant, "all_blocks_count": len(blocks)}


def construct_likely_urls(institution: str) -> list[dict]:
    """
    Construct likely URLs where AI policy/access info might live.
    Based on common university website patterns.
    """
    # Map well-known institutions to their domains
    domain_map = {
        "Harvard University": "harvard.edu",
        "MIT": "mit.edu",
        "Stanford University": "stanford.edu",
        "Princeton University": "princeton.edu",
        "University of Chicago": "uchicago.edu",
        "Yale University": "yale.edu",
        "Columbia University": "columbia.edu",
        "UC Berkeley": "berkeley.edu",
        "Northwestern University": "northwestern.edu",
        "University of Pennsylvania": "upenn.edu",
        "NYU": "nyu.edu",
        "University of Michigan": "umich.edu",
        "Duke University": "duke.edu",
        "University of Wisconsin-Madison": "wisc.edu",
        "University of Minnesota": "umn.edu",
        "Brown University": "brown.edu",
        "Cornell University": "cornell.edu",
        "UCLA": "ucla.edu",
        "UC San Diego": "ucsd.edu",
        "University of Virginia": "virginia.edu",
        "Boston University": "bu.edu",
        "University of Maryland": "umd.edu",
        "Ohio State University": "osu.edu",
        "Penn State University": "psu.edu",
        "University of Texas at Austin": "utexas.edu",
        "Indiana University": "indiana.edu",
        "University of North Carolina": "unc.edu",
        "Georgetown University": "georgetown.edu",
        "Dartmouth College": "dartmouth.edu",
        "University of Illinois Urbana-Champaign": "illinois.edu",
        "Vanderbilt University": "vanderbilt.edu",
        "University of Southern California": "usc.edu",
        "Washington University in St. Louis": "wustl.edu",
        "Michigan State University": "msu.edu",
        "University of Pittsburgh": "pitt.edu",
        "University of Iowa": "uiowa.edu",
        "UC Davis": "ucdavis.edu",
        "UC Irvine": "uci.edu",
        "University of Oregon": "uoregon.edu",
        "University of Colorado Boulder": "colorado.edu",
        "Arizona State University": "asu.edu",
        "University of Arizona": "arizona.edu",
        "University of Notre Dame": "nd.edu",
        "Georgia State University": "gsu.edu",
        "University of Georgia": "uga.edu",
        "Rutgers University": "rutgers.edu",
        "University of Washington": "washington.edu",
        "George Mason University": "gmu.edu",
        "Emory University": "emory.edu",
        "University of Florida": "ufl.edu",
        "University of Vermont": "uvm.edu",
        "University of Massachusetts Amherst": "umass.edu",
        "University of Connecticut": "uconn.edu",
        "London School of Economics": "lse.ac.uk",
        "University of Oxford": "ox.ac.uk",
        "University of Cambridge": "cam.ac.uk",
        "UCL": "ucl.ac.uk",
        "University of Warwick": "warwick.ac.uk",
        "University of Edinburgh": "ed.ac.uk",
        "University of Toronto": "utoronto.ca",
        "University of British Columbia": "ubc.ca",
        "Australian National University": "anu.edu.au",
        "University of Melbourne": "unimelb.edu.au",
    }

    domain = domain_map.get(institution)
    if not domain:
        return []

    # Common URL patterns for AI policy/access pages
    url_patterns = [
        f"https://www.{domain}/ai",
        f"https://www.{domain}/artificial-intelligence",
        f"https://it.{domain}/ai",
        f"https://research.{domain}/ai",
        f"https://provost.{domain}/ai",
        f"https://irb.{domain}",
    ]

    return [{"url": url, "source": "constructed"} for url in url_patterns]


def process_institution(row: dict) -> dict:
    """Process a single institution."""
    institution = row["institution"]
    print(f"\nProcessing: {institution}")

    result = {
        "institution": institution,
        "country": row["country"],
        "type": row["type"],
        "econ_rank_bucket": row["econ_rank_bucket"],
        "notes_input": row.get("notes", ""),
        # Output fields (to be filled by scraping + manual coding)
        "has_institutional_ai_access": "",
        "ai_vendor": "",
        "deal_type": "",
        "has_formal_ai_policy": "",
        "policy_scope": "",
        "policy_url": "",
        "restricts_ai_research": "",
        "data_security_restrictions": "",
        "irb_ai_guidance": "",
        "irb_guidance_url": "",
        "faculty_ai_training": "",
        # Scraping output
        "urls_checked": "",
        "relevant_extracts": "",
        "search_queries_used": "",
        "scrape_status": "",
    }

    # Try constructed URLs
    likely_urls = construct_likely_urls(institution)
    urls_checked = []
    all_extracts = []

    for url_info in likely_urls[:4]:  # limit to avoid hammering
        url = url_info["url"]
        urls_checked.append(url)
        extraction = fetch_and_extract(url)

        if extraction["status"] == "success" and extraction["blocks"]:
            for block in extraction["blocks"][:5]:  # limit per page
                all_extracts.append(f"[{url}] {block}")
            print(f"  Found {len(extraction['blocks'])} relevant blocks at {url}")

        time.sleep(REQUEST_DELAY)

    # Record search queries for manual follow-up
    searches = build_search_urls(institution)
    search_queries = [s["query"] for s in searches]

    result["urls_checked"] = " | ".join(urls_checked)
    result["relevant_extracts"] = "\n---\n".join(all_extracts) if all_extracts else "NONE FOUND - MANUAL CHECK NEEDED"
    result["search_queries_used"] = " | ".join(search_queries)
    result["scrape_status"] = "found_content" if all_extracts else "needs_manual"

    if all_extracts:
        print(f"  Total relevant extracts: {len(all_extracts)}")
    else:
        print(f"  No content found via constructed URLs — manual search needed")

    return result


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Parse arguments
    single_institution = None
    start_from = 0

    if "--institution" in sys.argv:
        idx = sys.argv.index("--institution")
        if idx + 1 < len(sys.argv):
            single_institution = sys.argv[idx + 1]

    if "--start-from" in sys.argv:
        idx = sys.argv.index("--start-from")
        if idx + 1 < len(sys.argv):
            start_from = int(sys.argv[idx + 1])

    # Load institution list
    institutions = pd.read_csv(INSTITUTIONS_CSV)
    print(f"Loaded {len(institutions)} institutions from {INSTITUTIONS_CSV}")

    if single_institution:
        institutions = institutions[
            institutions["institution"].str.contains(single_institution, case=False)
        ]
        print(f"Filtered to {len(institutions)} matching '{single_institution}'")
    elif start_from > 0:
        institutions = institutions.iloc[start_from:]
        print(f"Starting from row {start_from}")

    # Process each institution
    results = []
    for i, (_, row) in enumerate(institutions.iterrows()):
        result = process_institution(row.to_dict())
        results.append(result)

        # Save incrementally every 10 institutions
        if (i + 1) % 10 == 0:
            pd.DataFrame(results).to_csv(OUTPUT_CSV, index=False)
            print(f"\n  [Checkpoint saved: {i + 1} institutions processed]")

    # Final save
    results_df = pd.DataFrame(results)
    results_df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved to {OUTPUT_CSV}")

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved raw JSON to {OUTPUT_JSON}")

    # Summary
    found = sum(1 for r in results if r["scrape_status"] == "found_content")
    needs_manual = sum(1 for r in results if r["scrape_status"] == "needs_manual")
    print(f"\n--- SUMMARY ---")
    print(f"Total institutions: {len(results)}")
    print(f"Found content automatically: {found}")
    print(f"Needs manual search: {needs_manual}")


if __name__ == "__main__":
    main()
