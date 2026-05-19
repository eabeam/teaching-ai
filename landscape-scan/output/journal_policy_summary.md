# Economics Journal AI Policies: Landscape Scan Summary

**Date:** 2026-05-17
**Source:** Automated scrape of 70 economics journal author guidelines pages + 10 publisher-level policy pages
**Script:** `scrape_journal_policies.py`

---

## Executive Summary

Of 70 economics journals surveyed, only **1 journal (JOLE)** has a detailed, journal-specific AI disclosure policy on its author guidelines page. Five Springer journals display Springer's standardized AI/LLM authorship language on their submission guidelines pages. The remaining journals either returned 403 errors (blocking automated access) or had no AI-specific language on their author guidelines pages. However, major publishers (Elsevier, Wiley, Taylor & Francis, Springer) all maintain comprehensive publisher-level AI policies that apply as defaults to their journals.

**Key finding:** The economics discipline is largely relying on publisher-level defaults rather than developing field-specific AI policies. The one exception is JOLE, which has a nuanced, economics-aware policy with specific guidance on code generation, hypothesis generation, and citation format.

---

## Part A: Journals with Explicit Journal-Level AI Policy

### 1. Journal of Labor Economics (UChicago Press) — MOST DETAILED

**Effective:** Manuscripts submitted after October 1, 2024

**Disclosure requirements:**
- **Writing/rewriting:** Must be reported in the acknowledgment footnote. Details of how/where AI was used go in the online appendix.
- **Substantive uses** (hypothesis generation, creating analyzed data): Must be cited in-text AND explained in online appendix.
- **Code generation:** Disclosure NOT required unless LLM use "played a major role in expanding what was feasible in the paper."
- **Grammar/typos/word suggestions:** Disclosure NOT required.

**Citation format specified:**
> OpenAI (2023a). ChatGPT (GPT-4, May 12 Version) [Large language model]. Response to query made on Month/Day/Year. https://chat.openai.com/chat

**Prompt documentation:** Exact prompts must be provided in paper text; if numerous, reported in online appendix including "details of any processes used to generate the prompts."

**AI authorship:** Not explicitly addressed at journal level (defers to UChicago Press ethics statement).

**Peer review policy:** Not addressed.

**Reference cited:** Hosseini, Resnick, and Holmes (2023) "The ethics of disclosing the use of artificial intelligence tools in writing scholarly manuscripts" *Research Ethics* 19(4): 449-465.

---

### 2. Springer Journals (standardized template) — 5 journals

Applies to: **Journal of Economic Growth**, **Journal of Economic Inequality**, **Journal of Population Economics**, **IMF Economic Review**, **Journal of Risk and Uncertainty**

All display identical Springer boilerplate language:

**AI authorship banned:**
> "Large Language Models (LLMs), such as ChatGPT, do not currently satisfy our authorship criteria. Notably an attribution of authorship carries with it accountability for the work, which cannot be effectively applied to LLMs."

**Disclosure required:**
- Use of an LLM should be "properly documented in the Methods section (and if a Methods section is not available, in a suitable alternative part) of the manuscript."

**Exceptions (no disclosure needed):**
- "AI assisted copy editing" defined as: "AI-assisted improvements to human-generated texts for readability and style, and to ensure that the texts are free of errors in grammar, spelling, punctuation and tone."
- Explicitly notes these "do not include generative editorial work and autonomous content creation."

**AI images:** "Please check Springer's policy on generative AI images and make sure your work adheres to the principles described therein."

**Human accountability:** "In all cases, there must be human accountability for the final version of the text and agreement from the authors that the edits reflect their original work."

**Note:** Experimental Economics (also Springer) did NOT display this language on its submission guidelines page, suggesting not all Springer journals have adopted the template uniformly.

---

## Part B: Journals Covered by Publisher-Level Policy Only

These journals had no journal-specific AI language but are covered by their publisher's overarching policy.

### Elsevier (18 journals — all returned 403 errors)

**Publisher policy (comprehensive, successfully scraped):**

| Element | Elsevier Policy |
|---------|----------------|
| AI authorship | Banned. "Authors should not list AI Tools as an author or co-author, nor cite AI Tools as an author." |
| Disclosure | Required. Must include "a separate AI declaration statement" upon submission. Published in final work. |
| Disclosure content | Name of AI tool, purpose of use, extent of oversight |
| Grammar/spelling | No declaration needed for "basic checks of grammar, spelling and punctuation" |
| Research use | "AI use in the research process should be declared and described in detail in the methods section" |
| Images/figures | AI generation or alteration of images is NOT permitted (with narrow exception for AI as research method) |
| Graphical abstracts | AI-generated artwork NOT permitted |
| Human accountability | "Authors are responsible and accountable for the contents of their work" |
| Peer review | Not addressed in scraped content |

**Elsevier journals affected:** Journal of Development Economics, Journal of Public Economics, Journal of Health Economics, Journal of International Economics, Journal of Monetary Economics, Journal of Financial Economics, European Economic Review, Journal of Econometrics, World Development, Labour Economics, Economics of Education Review, Journal of Urban Economics, Journal of Environmental Economics and Management, Journal of Economic Behavior and Organization, Games and Economic Behavior, Journal of Economic Theory, Review of Economic Dynamics, Journal of Comparative Economics

### Wiley (13 journals — all returned 403 errors)

**Publisher policy (very comprehensive, successfully scraped):**

| Element | Wiley Policy |
|---------|-------------|
| AI authorship | Banned. "Tools cannot be accountable for published work... nor do they have legal standing or the ability to hold or assign copyright. Therefore... these tools cannot fulfil the role of, nor be listed as, an author." |
| Disclosure location | Acknowledgments (for drafting/editing), Methods (for research methodology), Figure captions (for visuals) |
| Disclosure required for | Text generation, substantial rephrasing, translation, restructuring arguments, literature review methodology, code development, data analysis, visual creation |
| Disclosure NOT required for | Grammar correction, formatting, word choice suggestions, conciseness edits, citation formatting |
| Human oversight | Required. "Authors may only use AI Technology as a companion to their writing process, not a replacement." |
| Peer review | Manuscripts must NOT be uploaded to AI tools by reviewers. Reviewers CAN use AI to organize thoughts, improve tone, ask general methods questions without manuscript specifics. Disclosure required if AI used for drafting assistance in reviews. |
| Images/photographs | AI-edited photographs NOT permitted. AI-generated data visualizations and illustrations ARE permitted with disclosure. |
| Editorial stance | "AI use in manuscript development is not grounds for rejection." |

**Wiley journals affected:** Journal of Finance, Journal of Applied Econometrics, Journal of Economic Surveys, Economica, Oxford Bulletin of Economics and Statistics, Canadian Journal of Economics, Journal of Policy Analysis and Management, Economic Inquiry, Rand Journal of Economics, International Economic Review, Journal of Industrial Economics, Journal of Money Credit and Banking, Health Economics

### Taylor & Francis (3 journals — all returned 403 errors)

**Publisher policy (comprehensive, successfully scraped):**

| Element | Taylor & Francis Policy |
|---------|----------------------|
| AI authorship | Banned. "Generative AI tools must not be listed as an author because such tools are unable to assume responsibility for the submitted content or manage copyright and licensing agreements." |
| Disclosure | Required. Must include "full name of the tool used (with version number), how it was used and the reason for use." A specific AI usage disclosure statement must be included in submissions. |
| Permitted uses | Idea generation, copyediting, language improvement, translations, interactive search, literature classification, coding assistance |
| Prohibited uses | Text/code generation without rigorous revision, synthetic data generation to substitute missing data, generation of inaccurate content including abstracts |
| AI images | Permitted for data visualizations and conceptual illustrations. NOT permitted for creation/manipulation of research results or clinical/diagnostic images. |
| Peer review | Reviewers "must not use artificial intelligence tools to generate manuscript and proposal review reports." Reviewers may use AI to improve review language only. Must not upload manuscripts to AI tools. |

**T&F journals affected:** Journal of Development Effectiveness, Journal of Business and Economic Statistics, Econometric Reviews

### Oxford University Press (7 journals — all returned 403 errors)

**Publisher policy page returned 403.** OUP's ethical policies page was blocked. Manual browser check recommended.

**OUP journals affected:** Quarterly Journal of Economics, Review of Economic Studies, Review of Financial Studies, Journal of the European Economic Association, Economic Journal, Journal of African Economies, World Bank Economic Review, Oxford Economic Papers

---

## Part C: Journals with No AI Content Found

### C1: Successfully fetched, genuinely silent on AI

These journals' author guidelines pages were successfully accessed but contain NO AI-specific language:

| Journal | Publisher | Likely Explanation |
|---------|-----------|-------------------|
| American Economic Review | AEA | AEA has no published AI policy across any journal |
| AER: Insights | AEA | Same as above |
| AEJ: Applied Economics | AEA | Same as above |
| AEJ: Economic Policy | AEA | Same as above |
| AEJ: Macroeconomics | AEA | Same as above |
| AEJ: Microeconomics | AEA | Same as above |
| American Economic Journal: Economic Policy | AEA | Same as above (duplicate entry in CSV) |
| Econometrica | Wiley/Econometric Society | Econometric Society manages its own policies; none found |
| Quantitative Economics | Wiley/Econometric Society | Same as above |
| Theoretical Economics | Econometric Society | Same as above |
| Experimental Economics | Springer | Springer journal but did NOT display standard AI template |

**Key observation:** The AEA (publisher of 7 journals in sample including the flagship AER) has NO published AI policy. The AEA general policies page was successfully scraped (6,243 chars of content) but contains no AI/LLM language. This is a notable gap for the most prominent economics publisher.

### C2: Fetch failures (403 Forbidden) — likely bot protection

| Publisher | # Journals Blocked | Reason |
|-----------|-------------------|--------|
| Elsevier (ScienceDirect) | 18 | Bot protection on guide-for-authors pages |
| Wiley (Wiley Online Library) | 13 | Bot protection on forauthors.html pages |
| OUP (academic.oup.com) | 7 | Bot protection on General_Instructions pages |
| UChicago Press | 6 | Bot protection on /instruct pages |
| Taylor & Francis | 3 | Bot protection on authorSubmission pages |
| MIT Press | 1 | Bot protection (Review of Economics and Statistics) |
| UW Press | 1 | 404 error (Journal of Human Resources — likely URL change) |
| Brookings | 1 | 404 error (BPEA — likely URL change) |
| AEA (JEL, JEP only) | 2 | 404 error (URL format may have changed) |

**Note:** All Elsevier, Wiley, OUP, UChicago, T&F, and MIT Press sites return 403 to automated requests. These are definitively bot-protection blocks, not evidence of missing content. These sites all render normally in browsers.

---

## Cross-Cutting Analysis

### Disclosure Spectrum (from most to least permissive)

1. **AEA / Econometric Society** — No policy at all (fully silent)
2. **JOLE (UChicago)** — Nuanced: code generation exempt; grammar exempt; substantive use requires citation + appendix
3. **Springer journals** — Methods section disclosure; copy-editing exempt
4. **Wiley** — Acknowledgments/Methods/Captions depending on use type; grammar/formatting exempt
5. **Elsevier** — Separate AI declaration statement required; grammar exempt; images banned
6. **Taylor & Francis** — Statement required; peer reviewers cannot use AI for report generation

### AI Authorship Consensus

All publishers with policies agree: **AI cannot be listed as an author.** Rationale is consistent: accountability, copyright, and inability to consent to publication.

### Peer Review Restrictions

| Publisher | Reviewers can upload manuscripts to AI? | Reviewers can use AI for own writing? |
|-----------|---------------------------------------|--------------------------------------|
| Wiley | No | Yes (with disclosure) |
| Taylor & Francis | No | Only for language improvement |
| Elsevier | Not addressed in scraped content | Not addressed |
| Springer | Not addressed in scraped content | Not addressed |

### Notable Gaps

1. **AEA (including AER):** No AI policy whatsoever. This is the most significant gap given AEA's role as the largest economics journal publisher.
2. **Econometric Society (Econometrica, QE, TE):** Silent on AI despite hosting detailed author guidelines.
3. **Cambridge University Press:** Publisher page on research integrity contains no AI language.
4. **Economics-specific nuance:** Only JOLE addresses the distinctive use cases in economics (code generation for data analysis, hypothesis generation, LLMs as research subjects/data-generators).

---

## Methodology Notes

- **Scraper:** Python requests + BeautifulSoup, 2-second delay between requests
- **Date of scrape:** 2026-05-17
- **Success rate:** 17/70 journal pages fetched (24%); 6/10 publisher pages fetched (60%)
- **High 403 rate:** ScienceDirect, Wiley Online Library, OUP, UChicago Press, and T&F all block automated requests. A browser-based or Selenium approach would be needed for comprehensive coverage.
- **Publisher policy pages** provided the most valuable data since they were more accessible and contain the binding policies.

---

## Recommendations for Follow-Up

1. **Manual browser check** for OUP, UChicago Press general AI policy pages
2. **AEA inquiry** — confirm whether AEA has an internal/unpublished policy or is genuinely silent
3. **Selenium/Playwright scraper** for journal-level pages that block requests
4. **Compare to COPE guidance** — several publishers reference COPE; worth tracking COPE's evolving position
5. **Track evolution** — re-run quarterly; policies are changing rapidly (JOLE's is dated Oct 2024; Wiley's references Claude 4 Sonnet accessed July 2025)
