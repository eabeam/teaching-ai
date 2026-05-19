"""
Scrape economics journal author guidelines pages for AI policy language.

For each journal in journals.csv:
1. Fetch the author guidelines URL
2. Extract text content
3. Search for AI-related keywords
4. Save extracted paragraphs containing AI language
5. Output a CSV for human coding

Usage:
    python3 scrape_journal_policies.py
    python3 scrape_journal_policies.py --journal "American Economic Review"  # single journal

Output: output/journal_ai_extracts.csv
"""

import csv
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import pandas as pd

SCRIPT_DIR = Path(__file__).parent
JOURNALS_CSV = SCRIPT_DIR / "journals.csv"
OUTPUT_DIR = SCRIPT_DIR / "output"
OUTPUT_CSV = OUTPUT_DIR / "journal_ai_extracts.csv"
OUTPUT_JSON = OUTPUT_DIR / "journal_ai_raw.json"

AI_KEYWORDS = [
    r"\bAI\b",
    r"\bartificial intelligence\b",
    r"\bgenerative\b",
    r"\bChatGPT\b",
    r"\bGPT\b",
    r"\blarge language model\b",
    r"\bLLM\b",
    r"\bClaude\b",
    r"\bCopilot\b",
    r"\bauthor(?:ship)?\b.*\b(?:AI|artificial intelligence|machine)\b",
    r"\bdisclos(?:e|ure)\b.*\b(?:AI|artificial intelligence)\b",
    r"\bmachine.generated\b",
    r"\bAI.generated\b",
    r"\bAI.assisted\b",
]

AI_PATTERN = re.compile("|".join(AI_KEYWORDS), re.IGNORECASE)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Academic Research Bot - emily.beam@uvm.edu"
}

REQUEST_DELAY = 2  # seconds between requests


def fetch_page(url: str) -> str | None:
    """Fetch page content, return text or None on failure."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def extract_text_blocks(html: str) -> list[str]:
    """Extract meaningful text blocks from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove script/style elements
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    blocks = []
    for element in soup.find_all(["p", "li", "td", "div", "section", "h1", "h2", "h3", "h4"]):
        text = element.get_text(separator=" ", strip=True)
        if len(text) > 30:  # skip trivial fragments
            blocks.append(text)

    return blocks


def find_ai_paragraphs(blocks: list[str]) -> list[str]:
    """Return text blocks that contain AI-related keywords."""
    matches = []
    for block in blocks:
        if AI_PATTERN.search(block):
            matches.append(block)
    return matches


def get_surrounding_context(blocks: list[str], match_indices: list[int], window: int = 1) -> list[str]:
    """Get matched blocks plus surrounding context."""
    indices_to_include = set()
    for idx in match_indices:
        for offset in range(-window, window + 1):
            if 0 <= idx + offset < len(blocks):
                indices_to_include.add(idx + offset)

    return [blocks[i] for i in sorted(indices_to_include)]


def process_journal(row: dict) -> dict:
    """Process a single journal: fetch, extract, search."""
    journal_name = row["journal_name"]
    url = row["author_guidelines_url"]

    print(f"Processing: {journal_name}")
    print(f"  URL: {url}")

    result = {
        "journal_name": journal_name,
        "publisher": row["publisher"],
        "field": row["field"],
        "tier": row["tier"],
        "url_fetched": url,
        "fetch_status": "unknown",
        "ai_language_found": False,
        "ai_extracts": "",
        "full_context": "",
        "num_ai_mentions": 0,
    }

    html = fetch_page(url)
    if html is None:
        result["fetch_status"] = "failed"
        return result

    result["fetch_status"] = "success"
    blocks = extract_text_blocks(html)

    if not blocks:
        result["fetch_status"] = "no_content"
        return result

    # Find AI-related paragraphs
    ai_blocks = find_ai_paragraphs(blocks)

    if ai_blocks:
        result["ai_language_found"] = True
        result["num_ai_mentions"] = len(ai_blocks)
        result["ai_extracts"] = "\n---\n".join(ai_blocks)

        # Get surrounding context
        match_indices = [i for i, b in enumerate(blocks) if AI_PATTERN.search(b)]
        context = get_surrounding_context(blocks, match_indices)
        result["full_context"] = "\n---\n".join(context)

        print(f"  FOUND {len(ai_blocks)} AI-related blocks")
    else:
        print(f"  No AI language found")

    return result


PUBLISHER_POLICIES = {
    "Elsevier": "https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals",
    "Wiley": "https://www.wiley.com/en-us/publish/article/ai-guidelines/",
    "OUP": "https://academic.oup.com/pages/authoring/journals/preparing_your_manuscript/ethical-policies",
    "Springer": "https://www.springer.com/us/editorial-policies/artificial-intelligence--ai-",
    "Taylor & Francis": "https://taylorandfrancis.com/our-policies/ai-policy/",
    "Cambridge University Press": "https://www.cambridge.org/core/services/authors/publishing-ethics/research-integrity",
    "UChicago Press": "https://www.journals.uchicago.edu/journals/policies",
    "MIT Press": "https://direct.mit.edu/journals/pages/editorial-policies",
    "AEA": "https://www.aeaweb.org/journals/policies",
    "Econometric Society": "https://www.econometricsociety.org/publications/econometrica/information-authors",
}


def get_publisher_for_journal(publisher_field: str) -> str | None:
    """Match a journal's publisher field to a PUBLISHER_POLICIES key."""
    for key in PUBLISHER_POLICIES:
        if key.lower() in publisher_field.lower():
            return key
    return None


def check_publisher_policy(publisher: str) -> dict | None:
    """
    Check publisher-level AI policies (these apply as defaults to all journals
    under that publisher unless the journal has its own override).
    """
    for key in PUBLISHER_POLICIES:
        if key.lower() in publisher.lower():
            return {"publisher": key, "policy_url": PUBLISHER_POLICIES[key]}
    return None


def scrape_publishers() -> dict:
    """
    Scrape publisher-level AI policies first. These serve as defaults
    for all journals under that publisher.
    Returns dict of {publisher_name: extracted_text}
    """
    print("\n=== PHASE 1: Publisher-Level Policies ===\n")
    publisher_results = {}

    for publisher, url in PUBLISHER_POLICIES.items():
        print(f"Fetching: {publisher}")
        print(f"  URL: {url}")

        html = fetch_page(url)
        if html is None:
            print(f"  FAILED (may be JS-rendered)")
            publisher_results[publisher] = {
                "status": "failed",
                "url": url,
                "extracts": [],
                "note": "Page may require JavaScript — check manually",
            }
            time.sleep(REQUEST_DELAY)
            continue

        blocks = extract_text_blocks(html)
        ai_blocks = find_ai_paragraphs(blocks)

        if ai_blocks:
            print(f"  Found {len(ai_blocks)} AI-related blocks")
            publisher_results[publisher] = {
                "status": "found",
                "url": url,
                "extracts": ai_blocks[:20],  # cap at 20 most relevant
            }
        else:
            # Check if page is mostly empty (JS-rendered)
            total_text = sum(len(b) for b in blocks)
            if total_text < 500:
                print(f"  Page appears JS-rendered (only {total_text} chars extracted)")
                publisher_results[publisher] = {
                    "status": "js_rendered",
                    "url": url,
                    "extracts": [],
                    "note": "Page requires JavaScript — open in browser to verify",
                }
            else:
                print(f"  No AI language found ({len(blocks)} blocks, {total_text} chars)")
                publisher_results[publisher] = {
                    "status": "no_ai_language",
                    "url": url,
                    "extracts": [],
                }

        time.sleep(REQUEST_DELAY)

    # Save publisher results
    pub_output = OUTPUT_DIR / "publisher_policies.json"
    with open(pub_output, "w") as f:
        json.dump(publisher_results, f, indent=2)
    print(f"\nPublisher results saved to {pub_output}")

    return publisher_results


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Parse arguments
    single_journal = None
    publishers_only = "--publishers-only" in sys.argv
    skip_publishers = "--skip-publishers" in sys.argv

    if "--journal" in sys.argv:
        idx = sys.argv.index("--journal")
        if idx + 1 < len(sys.argv):
            single_journal = sys.argv[idx + 1]

    # Phase 1: Publisher-level policies
    if not skip_publishers:
        publisher_results = scrape_publishers()
        if publishers_only:
            return
    else:
        publisher_results = {}

    # Phase 2: Individual journal pages
    print("\n=== PHASE 2: Individual Journal Pages ===\n")

    journals = pd.read_csv(JOURNALS_CSV)
    print(f"Loaded {len(journals)} journals from {JOURNALS_CSV}")

    if single_journal:
        journals = journals[journals["journal_name"].str.contains(single_journal, case=False)]
        print(f"Filtered to {len(journals)} matching '{single_journal}'")

    # Process each journal
    results = []
    for _, row in journals.iterrows():
        result = process_journal(row.to_dict())

        # Add publisher default info
        pub_key = get_publisher_for_journal(row["publisher"])
        if pub_key and pub_key in publisher_results:
            pub_info = publisher_results[pub_key]
            result["publisher_policy_status"] = pub_info["status"]
            result["publisher_policy_url"] = pub_info.get("url", "")
            if not result["ai_language_found"] and pub_info["status"] == "found":
                result["inherits_publisher_policy"] = True
            else:
                result["inherits_publisher_policy"] = False
        else:
            result["publisher_policy_status"] = "not_checked"
            result["publisher_policy_url"] = ""
            result["inherits_publisher_policy"] = False

        results.append(result)
        time.sleep(REQUEST_DELAY)

    # Save results
    results_df = pd.DataFrame(results)
    results_df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved extracts to {OUTPUT_CSV}")

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved raw JSON to {OUTPUT_JSON}")

    # Summary
    found = results_df["ai_language_found"].sum()
    inherits = results_df.get("inherits_publisher_policy", pd.Series()).sum()
    total = len(results_df)
    failed = (results_df["fetch_status"] == "failed").sum()
    js_issue = (results_df["fetch_status"] == "success") & (~results_df["ai_language_found"])

    print(f"\n--- SUMMARY ---")
    print(f"Total journals: {total}")
    print(f"AI language found on journal page: {found}")
    print(f"No journal-level language but inherits publisher policy: {inherits}")
    print(f"Fetch failures: {failed}")
    print(f"No AI language found anywhere: {total - found - int(inherits) - failed}")
    print(f"\nNote: AEA, OUP, and some Wiley pages are JS-rendered.")
    print(f"For those, check the publisher policy URL in a browser.")


if __name__ == "__main__":
    main()
