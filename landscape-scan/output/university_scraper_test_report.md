# University AI Access Scraper - Test Report

**Date:** 2026-05-17
**Test institutions:** 5 (Harvard, UVM, California State University, Howard University, LSE)

---

## Results Summary

| Institution | Status | URLs Checked | Extracts Found | Content Quality |
|---|---|---|---|---|
| Harvard University | found_content | 4 | 10 | Good - AI hub page with research/faculty info |
| University of Vermont | found_content | 4 | 5 | Good - tools, guidelines, AI Innovation Fund |
| California State University system | needs_manual | 0 | 0 | Failed - not in domain map |
| Howard University | needs_manual | 0 | 0 | Failed - not in domain map |
| London School of Economics | found_content | 4 | 5 | Mixed - mostly research/DSI info, not access info |

**Success rate:** 3/5 (60%) found content automatically

---

## Detailed Findings by Institution

### Harvard University
- **Source:** `https://www.harvard.edu/ai` and `/artificial-intelligence`
- **Content found:** "Generative AI @ Harvard" hub page - mentions research, faculty, teaching use
- **Useful for coding:** Yes - confirms institutional AI engagement, though specific vendor/access details need deeper page crawl
- **Gap:** Does not reach IT pages with specific tool provisioning details (e.g., harvard.edu/ithelp or huit.harvard.edu)

### University of Vermont
- **Source:** `https://www.uvm.edu/ai`
- **Content found:** AI guidelines for faculty/researchers/staff/students; Microsoft Copilot access; VACC locally hosted LLMs; AI Innovation Fund; AI Task Force
- **Useful for coding:** High quality - captures specific tools (Copilot, VACC LLMs), governance (Task Force), and funding (Innovation Fund)
- **Gap:** Some duplicate extracts (nav menu counted as separate blocks)

### California State University system
- **Source:** No URLs attempted
- **Root cause:** "California State University system" not in `domain_map` dictionary. Domain would be `calstate.edu`.
- **Known info (from institutions.csv notes):** CSU $17M OpenAI deal - this is high-value and should have been captured.

### Howard University
- **Source:** No URLs attempted
- **Root cause:** "Howard University" not in `domain_map`. Domain would be `howard.edu`.
- **Implication:** 31/94 institutions (33%) have no domain mapping and will all return `needs_manual`.

### London School of Economics
- **Source:** `https://www.lse.ac.uk/ai`
- **Content found:** DSI overview, AI partnerships (Anthropic education partnership mentioned), faculty expertise, research groups
- **Useful for coding:** Partial - confirms AI engagement and Anthropic partnership, but focused on research ABOUT AI rather than AI ACCESS for researchers
- **Gap:** Need IT/digital services pages for tool provisioning info

---

## Scraper Reliability Assessment

### What works
1. **Domain map approach** is sound for well-known institutions (63/94 covered)
2. **URL pattern guessing** (`/ai`, `/artificial-intelligence`) catches many AI hub pages
3. **Keyword filtering** (RESEARCH_AI_KEYWORDS) correctly surfaces faculty/research content and excludes student honor code pages
4. **Rate limiting** (3s delay) is polite and avoids blocks
5. **Error handling** works - failed URLs don't crash the process

### What does not work
1. **33% of institutions have no domain mapping** (31/94) - these return zero results
2. **No actual search** - `google_search()` returns empty list; relies entirely on constructed URLs
3. **Duplicate extracts** - same page content matched multiple times by different HTML elements (nav, header, body all match)
4. **Content too broad** - pages about AI research (studying AI) conflated with AI access (providing AI tools)
5. **Single-institution mode overwrites output** - running `--institution X` replaces the CSV each time
6. **Missing deeper pages** - IT service pages, IRB sites, procurement pages not reached from `/ai` hub
7. **No JS rendering** - institutions using React/Angular SPAs for IT portals won't return content

---

## Recommendations

### Before full 70-institution run (blocking)

1. **Expand domain_map** to cover all 94 institutions. The 31 unmapped ones include important cases (HBCUs, CSU system, international). ~30 min manual work.

2. **Add Google Custom Search API** or SerpAPI integration. The `google_search()` function is currently a no-op. This is the single biggest improvement — it would find actual AI access pages regardless of URL patterns. Cost: ~$5/1000 queries, so ~$2-3 for full run.

3. **Deduplicate extracts** - The regex matches the same content from parent and child HTML elements. Add deduplication (e.g., skip blocks that are substrings of already-captured blocks).

4. **Add more URL patterns** specific to IT services:
   - `https://it.{domain}/generative-ai`
   - `https://it.{domain}/ai-tools`
   - `https://services.{domain}/ai`
   - `https://www.{domain}/information-technology/ai`
   - `https://www.{domain}/it/ai`

### After first run (non-blocking improvements)

5. **Refine keyword regex** to better distinguish "AI as research subject" from "AI tools for researchers" (e.g., require words like "access", "tool", "available", "license", "provision")

6. **Fix append mode** - When running individual institutions, append to existing CSV rather than overwrite

7. **Add a second-pass scraper** that follows links FROM the hub page to find deeper IT/procurement pages

8. **Consider headless browser** (Playwright/Selenium) for the ~10-15% of institutions whose IT portals are JS-rendered

---

## Verdict: Fix issues first, then run

The scraper in its current state would produce:
- ~60% of institutions with some content (those in domain_map where `/ai` pages exist)
- ~33% with zero data due to missing domain mappings
- Content quality that's useful but noisy (duplicates, overly broad matches)

**Recommendation:** Spend 1-2 hours on fixes #1-4 above, then run the full batch. The search API integration (#2) is the highest-impact improvement. Without it, the scraper is essentially a URL-pattern guesser rather than a true web scraper.

If search API is not feasible short-term, at minimum fix #1 (domain map) and #3 (deduplication) before the full run. That would get you from 60% to ~90% attempted, with cleaner extracts for human coding.
