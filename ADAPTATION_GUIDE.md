# Adaptation Guide

How to customize these modules for different statistical software, student levels, institutional contexts, and delivery formats.

---

## For R Instead of Stata

Three modules use Stata in their primary examples: **C2 (Code Assistance)**, **C3 (Data Exploration & Cleaning)**, and to a lesser extent **C5 (Math & Derivations)** in its discussion of code verification. Here is what to change and what stays the same.

### C2: Code Assistance

**What changes**:

| Stata concept in module | R equivalent |
|------------------------|--------------|
| `merge 1:1 hhid using "file.dta"` | `left_join(df1, df2, by = "hhid")` (or `inner_join`, `full_join`) |
| `egen mean_inc = mean(income), by(district)` | `df %>% group_by(district) %>% mutate(mean_inc = mean(income, na.rm = TRUE))` |
| `gen log_classsize = log(class_size)` | `df <- df %>% mutate(log_classsize = log(class_size))` |
| `reg y x1 x2, robust` | `lm_robust(y ~ x1 + x2, data = df)` (estimatr) or `coeftest(lm(y ~ x1 + x2), vcov = vcovHC)` |
| `i.school` (factor notation) | `factor(school)` or `as.factor(school)` |
| Stata error messages (r(459), etc.) | R tracebacks and warning messages |

**What stays the same**: The entire framework (Section 5: "When to Use AI for Code") is language-agnostic. The categories -- use freely, use but verify, do not outsource -- apply identically to R. The distinction between computation and identification does not depend on the language.

**The debugging exercise**: Rewrite the buggy do-file as a buggy R script with equivalent errors:

```r
# Buggy R equivalent for the C2 exercise
library(tidyverse)

df <- read_csv("student_data.csv")

# Standardize test scores (BUG: wrong formula)
df <- df %>% mutate(test_z = test_score - mean(test_score) / sd(test_score))

# Log of class size
df <- df %>% mutate(log_classsize = log(class_size))

# Merge with school data (BUG: wrong join type or key)
school <- read_csv("school_data.csv")
df <- inner_join(df, school, by = "hhid")  # wrong key

# Regression (BUG: district FE instead of school FE)
model <- lm(test_z ~ log_classsize + factor(district), data = df)
summary(model)
```

**R-specific failure modes to add**: The module already includes a table of R-specific traps (tidyverse vs. base R confusion, silent type coercion, factor level issues, non-standard evaluation). Expand these with examples relevant to your course.

### C3: Data Exploration & Cleaning

**What changes**:

| Stata in module | R equivalent |
|-----------------|--------------|
| `describe` / `summarize` | `str(df)` / `summary(df)` or `skimr::skim(df)` |
| `misstable summarize` | `naniar::miss_var_summary(df)` or `colSums(is.na(df))` |
| `tab treatment survey_round, missing` | `table(df$treatment, df$survey_round, useNA = "always")` |
| `duplicates report` | `df %>% group_by(hhid, survey_round) %>% filter(n() > 1)` |
| `histogram hh_income, by(treatment)` | `ggplot(df, aes(x = hh_income)) + geom_histogram() + facet_wrap(~treatment)` |
| `codebook, compact` | `Hmisc::describe(df)` or `labelled::look_for(df)` |

**What stays the same**: The entire framework (exploration = safe, cleaning decisions = yours, use AI as auditor not decision-maker) is language-agnostic.

### C5: Math & Derivations

**Minimal changes needed.** This module is primarily about mathematical reasoning, not coding. The only software-dependent content is a brief mention of Stata-specific verification. Replace any Stata references with R equivalents for verifying formulas computationally (e.g., using `deriv()` or the `Deriv` package for symbolic differentiation).

---

## For Principles-Level Students

The modules are written for advanced undergraduates with some economics background. Here is how to adapt for intro students.

### General adjustments

- **Remove or simplify econometric references.** Modules frequently use instrumental variables, diff-in-diff, and causal inference as examples. For principles students, replace these with supply/demand, elasticity, and basic market analysis examples.
- **Replace "research" framing with "learning" framing.** Instead of "for your research paper," say "for your problem set" or "for understanding this concept."
- **Slow down the math.** C5 (Math & Derivations) assumes comfort with constrained optimization. For principles, reframe around algebra and graphical analysis -- e.g., AI checking whether a supply/demand equilibrium calculation is correct.

### Module-specific cuts and simplifications

| Module | What to cut | What to simplify | What to add |
|--------|------------|-------------------|-------------|
| **A1** | The $P(\text{next token} \mid \cdot)$ notation. The RLHF details. | Lean harder on the "autocomplete" analogy. Simplify the training description to "it learned patterns from lots of text." | More relatable examples: ask AI about a concept from their current chapter. |
| **A2** | The identification strategy analogy. The ROCS acronym can stay but simplify examples. | Replace econometrics examples with principles examples: "Explain supply and demand to me" vs. "Explain why the demand curve for gasoline is relatively inelastic, using a real-world example a college student would understand." | Scaffold the rewriting exercise more heavily -- provide example rewrites, not just prompts. |
| **A3** | The research-oriented examples in the 2x2 (IV estimates, coding exercises). | Reframe the 2x2 with principles examples: "Understanding why price floors cause surplus" (core skill) vs. "Formatting a graph in Excel" (not core). | Add more concrete examples of the fluency trap from intro-level studying. |
| **C1** | The entire module may be too advanced. Consider skipping or doing a 15-minute version focused on "always verify citations." | If using: cut the structured review workflow and focus on the verification demonstration. | Replace the research-oriented exercise with "ask AI to explain a concept from this week's reading and check whether it's accurate." |
| **C2** | The debugging exercise assumes intermediate coding. Skip or replace. | Focus only on the "explaining code" use case: paste in code from the textbook or problem set, ask AI to explain it. | Replace with a simpler exercise: "Use AI to explain what this Excel formula does" or "Ask AI to help you interpret a regression table from your textbook." |
| **C3** | Too advanced for principles. Skip. | -- | -- |
| **C4** | The economics-specific writing sections (identification strategy paragraphs, results descriptions). | Focus on the general revision techniques: reverse outlining, concision editing, paragraph diagnostics. These apply to any writing assignment. | Add an exercise using a 5-paragraph essay or short response rather than a research paper. |
| **C5** | Too advanced for principles unless your course is calculus-based. | If your principles course uses calculus: simplify to "check my derivative" and "verify my optimization" with basic supply/demand problems. | -- |

### Recommended subset for principles

**Minimum** (1 session): A1 + A3 -- every principles student benefits from understanding what AI is and developing judgment about when to use it.

**With more time** (2--3 sessions): A1 + A2 + A3 + C4 (simplified). Prompting skills and writing revision are immediately useful regardless of level.

---

## For Graduate Students

### What is too basic

- **A1 (What LLMs Do)**: The content is fine but the pacing may feel slow. Consider assigning A1 as pre-reading and spending class time on discussion questions only. Graduate students can handle the mechanism explanation in 10 minutes instead of 50.
- **A2 (Prompting)**: The ROCS framework is useful but the "Prompt Makeover" exercise with "Help me find a topic for my econ research paper" is undergraduate-coded. Replace with prompts from graduate-level tasks: "Help me think about the exclusion restriction for this IV," "Suggest robustness checks for this RDD."
- **A3 (When AI Helps/Hurts)**: The 2x2 framework is fine. The homework examples need upgrading to qualifier prep, paper writing, and refereeing.

### What to extend

| Module | Extension for graduate students |
|--------|-------------------------------|
| **A1** | Add a discussion of attention mechanisms, transformer architecture, and scale laws. Assign Vaswani et al. (2017) or a summary. Discuss: what are the implications of the training data composition for AI's knowledge of economics? |
| **A2** | Teach system prompts / custom instructions. Discuss building reusable prompt templates for recurring research tasks (literature summaries, code review, LaTeX formatting). |
| **C1** | Assign as a serious component of the qualifying exam or field paper process. Require students to compare AI-generated literature maps to their own reading lists. Discuss: how would a referee evaluate a literature review they suspect was AI-assisted? |
| **C2** | Add a section on using AI for structural estimation code, simulation design, and replication verification. Discuss AI-assisted code review in the context of co-author collaboration and pre-publication auditing. |
| **C3** | Extend to include AI-assisted data pipeline documentation for replication packages. Discuss the AEA Data Editor's requirements and how AI tools can help meet them. |
| **C4** | Focus on referee response drafting, grant writing, and job market paper revision. Add exercises using real (anonymized) referee reports. |
| **C5** | Extend to proofs, not just derivations. Discuss AI's limitations with novel mathematical arguments -- relevant for theory papers. Add a section on formal proof assistants (Lean, Coq) vs. LLMs for verification. |

### Additional readings for graduate courses

- Korinek, A. (2023). "Generative AI for Economic Research: Use Cases and Implications for Economists." *Journal of Economic Literature*.
- Dell, M. (2024). "Deep Learning for Economists." Working paper.
- Agrawal, A., Gans, J., & Goldfarb, A. (2018). *Prediction Machines*. (For the economics of AI framing.)
- Bender et al. (2021). "On the Dangers of Stochastic Parrots." (Already in A1 further reading.)

---

## For a Standalone Workshop vs. Semester-Long Integration

### Standalone workshop (half day or full day)

**Pacing**: Move faster through content, slower through exercises. The exercises are where learning happens.

| Duration | Schedule |
|----------|----------|
| **Half day (3 hours)** | A1 (30 min, condensed) + A3 (20 min) + one C module (50 min) + discussion (20 min) |
| **Full day (6 hours)** | See the schedule in INSTRUCTOR_GUIDE.md. Morning: A1 + A2 + A3. Afternoon: two C modules + wrap-up. |

**What to cut for time**:
- In A1: Skip the "Further Reading" section and the 4th discussion question. Condense the RLHF explanation.
- In A2: Skip the "Kitchen Sink" and "Leading Question" failure examples. Keep "Blank Canvas" and "Implicit Assumption" -- they land hardest.
- In A3: Skip the "Developing Your Personal Policy" template. Use the 2x2 as the main takeaway.
- In C modules: Do the exercise as an instructor-led demo rather than having each participant work independently. This cuts 15--20 minutes per module.

**Logistics**:
- Ensure wifi access and AI tool access before the workshop starts.
- For B1/B2 workshops: send setup instructions 1 week in advance and offer a 30-minute drop-in setup session the day before.
- Provide a single-page "cheat sheet" handout for each module -- key frameworks, commands, or checklists that participants can take with them.

### Semester-long integration

**Pacing**: One module every 1--2 weeks, with homework exercises between sessions.

**Recommended semester arc**:

| Weeks | Modules | Rationale |
|-------|---------|-----------|
| 1--2 | A1 + A3 | Set norms early. Students understand what AI is and develop their AI use policy before the first problem set. |
| 3--4 | A2 | Prompting skills, useful immediately for homework. |
| 5--6 | B1 (if needed) | Terminal skills, prerequisite for B2 or useful in its own right for data work. |
| 7--8 | One C module | Pick the one most aligned with current course content. |
| 9--10 | A second C module | Reinforce the framework with a different domain. |
| 11--12 | B2 or a third C module | If students are doing a final project, B2 (Git) is valuable. Otherwise, another C module. |

**Integration tips**:
- Assign A3's "Personal AI Policy" in week 2 and revisit it in week 8 -- students' views will have changed.
- Use module exercises as graded homework, not just in-class activities.
- Reference the module frameworks when giving feedback on other assignments: "This is a case where the 2x2 from A3 applies -- you used AI for a core skill."

### Sequencing across multiple weeks

If you're teaching multiple modules over a semester, here are natural pairings by week:

| Pairing | Time | Why they work together |
|---------|------|----------------------|
| A1 + A3 | 80 min | Mental model + metacognition in one block |
| B1 + B2 | 150 min | Terminal + Git in the same week (or back-to-back sessions) |
| A2 + C2 | 100 min | Prompt quality matters most when generating code |
| C1 + C4 | 100 min | Both are about AI processing YOUR text, not generating from scratch |
| C3 + C2 | 100 min | Data exploration flows naturally into code assistance |

---

## For Non-US Institutions

### What is US-specific

| Content | Where it appears | How to localize |
|---------|-----------------|-----------------|
| **UVM Copilot** reference | A1 exercise section, about.qmd | Replace with your institution's AI tool or a generic reference (see INSTRUCTOR_GUIDE.md) |
| **UVM email** in Git config | B2 setup instructions | Replace `your.email@uvm.edu` with your institution's email domain |
| **AEA / NBER / SSRN** references | C1 (Lit Review), C2 (Code Assistance) | AEA and NBER are international resources, but add your region's equivalents: CEPR (Europe), BREAD (development), IZA (labor), your national economics association's working paper series |
| **Google Scholar** | C1 (Lit Review) | Google Scholar is available globally but may have different coverage by region. Add any regional databases your students use. |
| **US-centric examples** | Various: Medicaid, state minimum wage, ACS data, EITC | Replace with locally relevant policy examples. The economics is the same -- swap the institutional context. |
| **Dollar amounts** | C3 (Data Exploration: income in KES), C2 (income thresholds) | Already somewhat international (Kenya shillings appear in several examples). Adjust currency and magnitudes to your context. |
| **Stata/R dominance** | C2, C3 | Stata is standard in US economics but less universal elsewhere. Some programs emphasize R, Python, or Julia. See the "For R Instead of Stata" section above. |

### What is already international

Most of the content is not US-specific:

- The mechanism of LLMs (A1) is universal.
- Prompting skills (A2) are language-agnostic (though all examples are in English -- translate exercises if teaching in another language).
- The metacognitive framework (A3) applies everywhere.
- Terminal and Git (B1, B2) are identical across countries.
- The lit review workflow (C1) works for any field and any database.
- The code assistance framework (C2) applies to any language and any coding environment.
- Writing and math (C4, C5) are universal skills.

### Language considerations

All modules are written in English. If teaching in another language:

- The conceptual content translates directly.
- Exercises that involve prompting AI may work differently in non-English languages (LLMs perform best in English; performance in other languages varies by model and language).
- Consider adding a discussion of how AI performance varies across languages -- this is a real limitation students should understand.

### Regulatory and policy differences

- **Data privacy**: B6 (Data Privacy, not yet drafted) will reference FERPA, which is US-specific. European institutions should reference GDPR instead. Other regions have their own frameworks.
- **Academic integrity norms**: Institutional AI policies vary widely. The A3 framework (be deliberate about your AI use) is universal, but the specific rules students must follow depend on your institution.
- **Access to AI tools**: In some countries, certain AI tools are blocked or restricted. Survey your students' access before assigning modules that require AI interaction. Free-tier availability also varies by region.

---

## Quick Reference: Adaptation Checklist

Before teaching any module, run through this checklist:

- [ ] **Software**: Do students have access to the required tools? (See INSTRUCTOR_GUIDE.md requirements table)
- [ ] **Level**: Is the module pitched at the right level for your students? (See principles/graduate sections above)
- [ ] **Examples**: Are the economics examples familiar to your students? Swap if needed.
- [ ] **Institutional references**: Have you replaced UVM-specific content with your own institution's information?
- [ ] **Language/region**: Are there currency, data source, or policy references that need localizing?
- [ ] **Time**: Do you have enough class time for the full module, or do you need to cut? (See workshop section for what to cut)
- [ ] **Assessment**: Have you chosen an assessment from the ASSESSMENT_MENU.md that fits your course?
