# AI Landscape Scan — Scraping Infrastructure

**Project**: Thinking with Agents / NBER AI Commentary follow-up
**Goal**: Build two structured datasets that don't currently exist:
1. Economics journal AI policies (what journals require re: AI disclosure)
2. University researcher AI access (does the institution provide/subsidize AI tools for faculty)

## What This Is NOT About

- Student academic integrity policies (not our focus)
- Whether universities ban AI for coursework (not our question)
- Teaching-focused AI policies (secondary interest only)

## What This IS About

- Can a researcher at [university] access Claude/ChatGPT/Copilot through their institution?
- Is it subsidized or do they pay out of pocket?
- Does the institution have guidance for using AI in *research* specifically?
- What do IRBs say about AI tools touching research data?
- What do *economics journals* require for AI disclosure?

---

## Quick Start

```bash
cd landscape-scan/

# Dataset 1: Journal policies
python3 scrape_journal_policies.py                          # all journals
python3 scrape_journal_policies.py --journal "AER"          # single journal test

# Dataset 2: University access
python3 scrape_university_access.py                         # all institutions
python3 scrape_university_access.py --institution "Harvard" # single test
python3 scrape_university_access.py --start-from 20         # resume
```

## Directory Structure

```
landscape-scan/
├── README.md                      # this file
├── journals.csv                   # input: journal list + author guideline URLs
├── institutions.csv               # input: institution list + metadata
├── scrape_journal_policies.py     # script 1: fetch journal pages, extract AI language
├── scrape_university_access.py    # script 2: fetch university pages, extract access info
├── code_results.py                # script 3: (TODO) structured coding from extracts
├── data/                          # reference data (existing compilations, etc.)
└── output/                        # generated output
    ├── journal_ai_extracts.csv    # raw extracts from journal pages
    ├── journal_ai_raw.json        # full JSON output
    ├── university_ai_access.csv   # raw extracts from university pages
    └── university_ai_raw.json     # full JSON output
```

## Workflow

### Dataset 1: Journal Policies

1. **Run scraper**: `python3 scrape_journal_policies.py`
   - Fetches each journal's author guidelines page
   - Searches for AI-related keywords
   - Extracts relevant paragraphs
   - Many journals will inherit publisher-level policies (Elsevier, Wiley, etc.)

2. **Check publisher defaults**: The script prints publisher policy URLs at the end.
   Fetch those manually and note the default policy for each publisher.

3. **Human coding**: Open `output/journal_ai_extracts.csv` and code each journal:
   - `ai_disclosure_required`: Y / N / unclear / silent (no mention at all)
   - `disclosure_location`: methods / acknowledgments / cover letter / separate section
   - `ai_authorship_banned`: Y / N / not addressed
   - `ai_peer_review_policy`: text summary
   - `ai_generated_code_policy`: addressed Y/N + text
   - `reproducibility_ai_addressed`: Y/N + text

4. **For journals with no content found**: Check manually. The script will flag these.
   Common reasons: page requires JavaScript rendering, policy is in a PDF, or
   the journal genuinely has no AI policy.

### Dataset 2: University Researcher Access

1. **Run scraper**: `python3 scrape_university_access.py`
   - Tries common URL patterns (it.{domain}/ai, research.{domain}/ai, etc.)
   - Extracts text blocks mentioning AI + research/faculty
   - Filters OUT student-only academic integrity content
   - Prints suggested Google searches for manual follow-up

2. **Manual follow-up** (the scraper will miss ~50-70% of institutions):
   - Use the printed search queries for each institution
   - Check IT services pages, research office pages, provost announcements
   - Look for press releases about enterprise AI deals
   - Check IRB websites specifically

3. **Human coding**: Fill in the empty columns in `output/university_ai_access.csv`:
   - `has_institutional_ai_access`: Y / N / unclear
   - `ai_vendor`: OpenAI / Anthropic / Microsoft / Google / multiple / none / unknown
   - `deal_type`: enterprise / pilot / departmental / individual-reimbursement / none
   - `has_formal_ai_policy`: Y / N (for research specifically)
   - `policy_scope`: research / teaching / both / all activities
   - `restricts_ai_research`: Y / N / unclear
   - `data_security_restrictions`: Y / N + text (re: research data in AI tools)
   - `irb_ai_guidance`: Y / N
   - `faculty_ai_training`: Y / N + text

---

## What's Already Working (tested 2026-05-16)

**Publisher-level scraping** (Phase 1 of journals):
- Elsevier: 20+ relevant blocks extracted
- Wiley: 20+ relevant blocks extracted  
- Springer: 13 relevant blocks extracted
- Taylor & Francis: 20+ relevant blocks extracted
- These 4 publishers cover ~45 of the 70 journals in the list

**Needs browser/manual check** (returns 403 or is JS-rendered):
- OUP (403) — covers QJE, REStud, JEEA, EJ, WBER, JAE
- UChicago Press (403) — covers JPE, EDCC, JLE, NTJ, AJHE, JHC
- MIT Press (403) — covers REStat
- AEA (JS-rendered) — covers AER, AEJ series, JEL, JEP
- Econometric Society (no AI text on that page) — covers Econometrica, QE, TE

**For Codex**: The 403/JS pages need either:
- `playwright` (headless browser): `pip3 install playwright && playwright install`
- Or: manual copy-paste of the page content into a text file for parsing

---

## Known Limitations

- **University scraper hit rate will be low** (~30-50%). University AI info lives in
  inconsistent locations. The constructed-URL approach catches well-organized IT
  departments but misses announcements, news pages, provost memos. Manual search
  is essential.

- **Journal scraper may miss JS-rendered content**. Some publisher sites (especially
  OUP, Wiley) render author guidelines via JavaScript. If the scraper returns empty
  for a journal you know has a policy, try fetching with a headless browser.

- **Publisher-level vs journal-level**: Most journals inherit their publisher's AI
  policy. The journal-specific page may not mention AI at all — that doesn't mean
  "no policy," it means "check the publisher default."

## Sampling Frame Rationale

### Journals (~70)
- All top-5 (5)
- Major field journals across labor, development, health, public, macro, micro, IO, finance, metrics (25-30)
- Broader field journals (30-40)
- Covers the journals where economists actually publish

### Institutions (~90)
- Top-50 US econ departments (R1 research universities)
- Teaching-intensive institutions (R2, M1, CSU system, regional publics)
- HBCUs (Howard, Morehouse, Spelman, FAMU, NC A&T)
- International top departments (UK, France, Switzerland, Italy, Netherlands, Canada, Australia, Singapore, China, South Africa, India)
- Rationale: captures the full distribution from elite to "some but not all resources"

## Dependencies

```
python3 >= 3.10
requests
beautifulsoup4
pandas
```

Install: `pip3 install requests beautifulsoup4 pandas`
