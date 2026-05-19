---
date: 2026-05-17
type: brief
project: teaching-ai
tags: [research-brief, ai-landscape, phase-9]
status: to-process
serves_module: [A1, A2, C1]
---

# Research Brief: AI-in-Economics Landscape Scan

**Phase 9 — Post-Literature-Scan Synthesis**
**Date**: 2026-05-17
**Author**: Emily Beam (with Claude)
**Project**: Thinking with Agents / NBER Commentary Follow-up

---

## Research Question / Motivation

How are economists actually encountering, using, and being governed around AI tools in their research workflows — and where are the critical information gaps?

The broader motivation is twofold:

1. **For the NBER commentary**: Provide an empirical foundation for claims about the current state of AI adoption and governance in economics research. Without data, the commentary relies on anecdote and assumption.

2. **For the Thinking with Agents bootcamp**: Understand what participants' institutional contexts look like so that training content addresses real constraints (e.g., "your university may not provide access" vs. "here's how to use the tool your institution already gives you").

The 5-dimension literature scan conducted 2026-05-16 reveals that the landscape is characterized more by absence than presence — the most striking finding is how little systematic documentation exists about AI in the economics research pipeline.

---

## Key Gaps Identified

The literature scan covered five dimensions. Each revealed a distinct gap:

### Gap 1: No Economist-Specific AI Adoption Survey Exists

General workforce surveys (McKinsey, Pew, Nature) report headline AI adoption figures, but no survey has specifically asked economists about their research workflows. We do not know:
- What fraction of economists use AI for coding, writing, data analysis, or literature review
- Whether usage differs by rank, field, or institution type
- What the modal use case is (copy-editing? debugging Stata code? brainstorming research designs?)

**Implication**: Any claim about "how economists are using AI" is currently extrapolation from adjacent fields.

### Gap 2: General Surveys Show High Headline Adoption but Shallow Depth

Existing surveys (e.g., Nature 2024, McKinsey Global Survey 2024) report 60-80% of researchers/knowledge workers "use AI." But these figures collapse heterogeneous behaviors — someone who asked ChatGPT one question and someone who has integrated Claude into their daily workflow both count as "users." No survey measures:
- Frequency or intensity of use
- Integration into core research tasks vs. peripheral tasks
- Skill level or sophistication of prompting

**Implication**: Headline adoption numbers are nearly meaningless for understanding actual research practice transformation.

### Gap 3: ~80% of Universities Lack Formal AI Research Policy

The Springer 2025 study (343 universities, 5 countries) and cross-referencing with GradPilot/Thesify compilations suggest that roughly 80% of institutions either have no formal AI policy for research, or have policies that address only teaching/student use. Where policies exist, they are typically:
- Generic acceptable-use statements with no research-specific guidance
- Teaching-focused (academic integrity framing)
- Aspirational rather than operational

**Implication**: Faculty are operating in a policy vacuum. Individual researchers are making ad hoc decisions about AI use in their research without institutional guidance or constraints.

### Gap 4: No Federal IRB Regulations for AI Use in Research

There is no OHRP, NSF, or NIH regulation specifically addressing AI tool use in human subjects research. The Common Rule does not mention AI. Individual IRBs are issuing guidance sporadically, but:
- Most IRB websites have no AI-specific content
- Where guidance exists, it is typically advisory (not binding)
- There is no consensus on whether using AI to analyze interview transcripts, code survey responses, or draft consent forms requires protocol amendments

**Implication**: A researcher who feeds identifiable data into an AI tool faces no regulatory barrier — only whatever their institution's data security policy (if any) says. This is a significant governance gap given that commercial AI tools may retain training data.

### Gap 5: AEA Requires Journal Disclosure but Nothing Else

The AEA's policy (covering AER, AEJ series, JEL, JEP) requires authors to disclose AI use. However:
- Disclosure location and format are not standardized
- No verification mechanism exists
- The policy does not restrict AI use — only mandates acknowledgment
- Most other economics journals either inherit publisher-level defaults (Elsevier, Wiley, Springer) or are silent
- No journal addresses AI-assisted data analysis, AI-generated code reproducibility, or AI in peer review in a substantive way

**Implication**: The disclosure norm is emerging but thin. It addresses transparency without addressing the harder questions about reproducibility, data security, and research integrity.

---

## Data Collection Strategy

The scraping infrastructure (built 2026-05-16, documented in `landscape-scan/README.md`) will produce two structured datasets:

### Dataset 1: Economics Journal AI Policies (~70 journals)

| What we collect | How |
|---|---|
| Disclosure requirements | Scrape author guidelines pages |
| Authorship restrictions | Keyword extraction + human coding |
| AI-in-peer-review policies | Manual check of editorial policies |
| Code/reproducibility AI provisions | Cross-reference data availability policies |

**Current status**: Publisher-level scraping works for Elsevier, Wiley, Springer, Taylor & Francis (~45 journals). OUP, AEA, UChicago Press, MIT Press require headless browser or manual extraction.

### Dataset 2: University AI Access & Research Policy (~90 institutions)

| What we collect | How |
|---|---|
| Institutional AI tool access | IT pages, press releases, vendor announcements |
| Research-specific AI policy | Provost/research office pages |
| IRB AI guidance | IRB websites |
| Data security restrictions | IT security policies |
| Econ-department-specific resources | Department websites |

**Sampling frame**: Top-50 US econ departments, teaching-intensive institutions (R2/M1/CSU), HBCUs, top-25 international departments. Captures the full distribution from elite to resource-constrained.

**Current status**: Scraper infrastructure built and tested. Low automated hit rate expected (~30-50%) for universities; manual search essential.

---

## Expected Contribution

1. **First structured dataset of AI policies across economics journals** — currently no machine-readable compilation exists. Enables statements like "X% of top-field journals require AI disclosure" with actual evidence.

2. **First economics-focused institutional AI access database** — existing compilations (GradPilot, Thesify) are narrative, not coded, and focus on teaching. Ours focuses on research access and governance.

3. **Foundation for survey design** — knowing the institutional landscape enables better survey questions. Instead of asking "do you use AI?" we can ask "does your institution provide access?" and "are you aware of your journal's disclosure requirements?"

4. **Direct input to NBER commentary** — empirical claims about the policy vacuum, rather than assertions.

5. **Bootcamp teaching material** — real examples of institutional variation that participants can relate to their own contexts.

---

## Limitations / Caveats

- **Snapshot problem**: AI policies are changing rapidly. Any dataset is outdated within months. Need to timestamp everything and plan for updates.
- **Coding ambiguity**: "Silent" vs. "no policy" is hard to distinguish. A journal that doesn't mention AI may be intentionally permissive or simply hasn't updated its guidelines since 2022.
- **Scraper limitations**: JS-rendered pages, PDFs, and inconsistently structured university websites mean automated coverage will be incomplete. Budget for significant manual effort.
- **Selection on observability**: We can only code what's publicly documented. Informal norms, email guidance from editors, and verbal IRB conversations are invisible to this method.
- **Not a survey**: This documents *institutional* policies and access, not *individual* behavior. The adoption gap (Gap 1) requires a separate survey instrument.

---

## Next Steps

| Step | Timeline | Dependencies |
|---|---|---|
| Complete journal scraping (headless browser for OUP/AEA) | This week | `playwright` install |
| Human coding of journal extracts | This week | Output from step above |
| Build institution list + find correct URLs | Next week | Decision on sampling frame |
| Run university scraper + manual follow-up | Next 2 weeks | Institution list |
| Human coding of university data | 2-3 weeks | University extracts |
| Descriptive statistics + key figures | 3-4 weeks | Both coded datasets |
| Draft commentary section with empirical claims | 4 weeks | Descriptive stats |
| Consider survey instrument design | 6-8 weeks | Landscape data to inform questions |

### Immediate decisions needed (from Emily):

1. **Sampling frame**: Option C (hybrid) recommended — captures full distribution
2. **International scope**: Include from the start (top-25 non-US) — adds 1-2 days, high value for commentary
3. **RA involvement**: Coding is the bottleneck; consider RA for manual URL finding + coding with clear protocol
4. **Springer 343-university data**: Worth emailing authors for replication data — could save 1+ week

---

*Generated 2026-05-17 as Phase 9 synthesis of the 5-dimension literature scan (2026-05-16).*
