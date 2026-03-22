# Prompt Makeover Worksheet

**Module A2: Prompting as Problem Specification**

## Instructions

1. Read each "before" prompt below.
2. Rewrite it using the ROCS framework (Role/Context, Objective, Constraints, Specifics).
3. Score your rewrite using the self-assessment rubric.
4. Try both the "before" and your rewrite in an AI tool. Compare the outputs.
5. After completing all four, check the sample rewrites at the bottom.

---

## ROCS Quick Reference

| Component | What it is | Scoring |
|---|---|---|
| **R** - Role / Context | Who you are, what you are doing | 0 = absent, 1 = vague, 2 = clear |
| **O** - Objective | What you want the output to be | 0 = absent, 1 = vague, 2 = clear |
| **C** - Constraints | Boundaries, format, level, length | 0 = absent, 1 = vague, 2 = clear |
| **S** - Specifics | Details that shape the answer | 0 = absent, 1 = vague, 2 = clear |

---

## Prompt 1: Research Help

**Before**: "Help me find a topic for my econ research paper."

**Your rewrite**:

&nbsp;

&nbsp;

&nbsp;

### ROCS Self-Assessment

| Component | Score (0/1/2) | Notes |
|---|:---:|---|
| R - Role / Context | | |
| O - Objective | | |
| C - Constraints | | |
| S - Specifics | | |
| **Total** | **/8** | |

**How did the outputs compare?**

&nbsp;

&nbsp;

---

## Prompt 2: Concept Explanation

**Before**: "Explain difference-in-differences."

**Your rewrite**:

&nbsp;

&nbsp;

&nbsp;

### ROCS Self-Assessment

| Component | Score (0/1/2) | Notes |
|---|:---:|---|
| R - Role / Context | | |
| O - Objective | | |
| C - Constraints | | |
| S - Specifics | | |
| **Total** | **/8** | |

**How did the outputs compare?**

&nbsp;

&nbsp;

---

## Prompt 3: Data Analysis

**Before**: "How do I analyze this data?" [pastes variable list]

**Your rewrite**:

&nbsp;

&nbsp;

&nbsp;

### ROCS Self-Assessment

| Component | Score (0/1/2) | Notes |
|---|:---:|---|
| R - Role / Context | | |
| O - Objective | | |
| C - Constraints | | |
| S - Specifics | | |
| **Total** | **/8** | |

**How did the outputs compare?**

&nbsp;

&nbsp;

---

## Prompt 4: Writing Help

**Before**: "Edit my paper."

**Your rewrite**:

&nbsp;

&nbsp;

&nbsp;

### ROCS Self-Assessment

| Component | Score (0/1/2) | Notes |
|---|:---:|---|
| R - Role / Context | | |
| O - Objective | | |
| C - Constraints | | |
| S - Specifics | | |
| **Total** | **/8** | |

**How did the outputs compare?**

&nbsp;

&nbsp;

---

## Sample Rewrites

Check these after you have written your own. There is no single correct answer -- the goal is specificity and clarity.

<details>
<summary>Click to reveal: Sample rewrite for Prompt 1 (Research Help)</summary>

> "I'm a junior economics major starting a 15-page research paper for my Applied Microeconomics course. I'm interested in education policy and labor market outcomes. I need to use publicly available data (like the ACS or CPS) and apply a causal inference method we've covered in class (diff-in-diff, IV, or RDD). Can you suggest 3-4 specific research questions that would be feasible at this scope, and briefly note what data and identification strategy each would require?"

**Why this works**: It specifies the student's level (R), what they need (O), hard constraints like data availability and methods (C), and the topic area and course context (S). The AI can now give targeted, actionable suggestions instead of a generic list.

</details>

<details>
<summary>Click to reveal: Sample rewrite for Prompt 2 (Concept Explanation)</summary>

> "I'm an upper-level undergraduate econ student. I understand OLS regression and omitted variable bias, but I'm seeing difference-in-differences for the first time in my econometrics course. Can you explain the core idea of diff-in-diff in 2-3 paragraphs, using a concrete policy example? Include the key assumption (parallel trends) and explain why it matters, in plain language."

**Why this works**: It tells the AI the student's knowledge level (R), asks for an explanation at the right depth (O), sets format and length constraints (C), and requests a concrete example and the key assumption (S). The result will be pitched correctly instead of defaulting to either a Wikipedia overview or a graduate-level treatment.

</details>

<details>
<summary>Click to reveal: Sample rewrite for Prompt 3 (Data Analysis)</summary>

> "I have a dataset with individual-level observations from US counties. My variables include: a binary treatment indicator for whether the county expanded Medicaid, pre- and post-period indicators, ER visit counts, and demographic controls (age, income, insurance status). I want to estimate the causal effect of Medicaid expansion on ER utilization using a difference-in-differences design. Can you suggest the regression specification I should run in Stata, including what fixed effects and controls to include, and explain why?"

**Why this works**: It describes the data structure and key variables (R/S), states the causal question and method (O), specifies the software and asks for explanation (C), and gives enough context for the AI to write a useful, specific specification rather than generic advice.

</details>

<details>
<summary>Click to reveal: Sample rewrite for Prompt 4 (Writing Help)</summary>

> "I've written a draft introduction for my economics research paper on the effect of school lunch programs on test scores. The paper is for an undergraduate research methods course. Can you review this introduction for: (1) whether the research question is clearly stated in the first two paragraphs, (2) whether the motivation connects to existing literature, and (3) whether the preview of the identification strategy is clear? Please be specific about what to improve -- don't just say 'good job.' Here is the draft: [paste text]"

**Why this works**: It identifies the document type and context (R), asks for specific dimensions of feedback rather than generic editing (O), sets the expectation for critical rather than flattering feedback (C), and provides the actual text for review (S). The AI will give targeted, useful comments instead of vague praise or line-edits you did not ask for.

</details>

---

*From [Teaching AI for Economists](https://eabeam.github.io/teaching-ai/) | Module A2: Prompting as Problem Specification*
