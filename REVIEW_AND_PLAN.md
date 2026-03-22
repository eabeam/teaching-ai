# Teaching AI Modules: Review and Improvement Plan

**Date**: 2026-03-21
**Reviewer**: Claude (requested by Emily Beam)
**Scope**: All 10 modules (A1-A3, B1-B2, C1-C5)
**Criteria**: Specifics/Relevance, Timelessness, Hands-On Practice, Portability

---

## 1. Executive Summary

- **Biggest strength: Conceptual framing.** Every module grounds AI use in economics-specific reasoning. The "economist's analogies" are consistently strong -- identification strategy for prompting (A2), measurement error for hallucinated citations (C1), computation vs. identification for code assistance (C2). These are genuinely illuminating, not forced.

- **Biggest strength: Honest about limitations.** The modules avoid both techno-hype and Luddism. The 2x2 in A3, the "silent errors" framing in C2, the "you curate, AI synthesizes" principle in C1 -- these are durable frameworks that will age well regardless of which models exist.

- **Biggest gap: No downloadable exercise materials.** Every module describes exercises in-line, but none provide downloadable files -- no buggy `.do` files, no sample datasets, no handout PDFs, no starter code. Instructors would need to build all exercise materials from scratch.

- **Biggest gap: The C-track modules are conceptually dense but exercise-light.** C1, C3, C4, and C5 have thorough "what to do / what not to do" frameworks but the exercises are mostly "go try this with AI and reflect." Students need more structured, verifiable tasks with concrete deliverables.

- **Risk: UVM Copilot reference.** A1 links to `go.uvm.edu/copilot`. This is the only institution-specific reference, but it appears in the first module students encounter. Other instructors will hit this immediately.

- **Gap: No instructor-facing infrastructure.** The `instructor-note` divs are helpful but brief. There are no lesson plans, no timing guides, no slide decks, no answer keys, no setup checklists. An instructor at another university would need to do significant prep work to teach any module.

- **Opportunity: The B-track modules are the most hands-on and closest to "ready to teach."** B1 and B2 have structured, step-by-step exercises with sample output. The C-track should adopt the same pattern.

---

## 2. Module-by-Module Review

### A1: What LLMs Actually Do

**Current strengths**: The one-sentence framing ("predicts the next token") is effective and repeated well. The "Good vs. Dangerous mental models" tables are immediately usable teaching tools. The failure mode taxonomy (hallucination, sycophancy, anchoring, confident wrongness) is well-structured with economics-relevant examples. The p-hacking analogy for hallucination in Discussion Q2 is sharp. Further reading list is well-curated.

**Weakest criterion: Hands-on practice.** The exercises are "try this with AI and see what happens" -- observational, not evaluative. Students paste prompts and observe outputs but have no structured framework for recording, comparing, or evaluating what they see. There is no deliverable beyond "notice that this happens."

**Top improvements**:

1. Add a **structured worksheet** for the failure-mode exercises. For the hallucination test: provide a table where students record each citation, then columns for "Author exists? (Y/N)", "Paper exists? (Y/N)", "Journal correct? (Y/N)", "Finding accurate? (Y/N)", and a notes column. For the sycophancy test: a side-by-side comparison template where students paste both responses and highlight where the AI agrees with each contradictory premise. This turns "observe" into "document and evaluate."

2. Replace the generic cash-transfers citation prompt with a **specific subfield prompt bank** -- 3-4 options across different economics fields (labor, development, health, trade) so students can pick something closer to their interests, and instructors in different subfields can choose the most relevant one.

3. Add a **live demo script** for instructors: "Ask the model for 5 citations on [your subfield]. Project the output. Open Google Scholar. Check each one aloud with the class. Tally the results on the board." The instructor note hints at this but doesn't script it.

---

### A2: Prompting as Problem Specification

**Current strengths**: The identification-strategy analogy is the best in the series -- it reframes prompting as a research skill rather than a tech trick. The ROCS framework is simple, memorable, and genuinely useful. The three-version IV example (vague / better / specific) is concrete and progressively builds the point. The "Prompting Paradox" callout is an important insight that is often missing from prompting guides. The iterative prompting section is practical and realistic.

**Weakest criterion: Hands-on practice.** The "Prompt Makeover" exercise gives four before-prompts but no rubric, no sample rewrites, and no systematic way for students to evaluate which rewrite is better. It is a good idea executed loosely.

**Top improvements**:

1. For the Prompt Makeover exercise, add **sample "good" rewrites** in a collapsible section (like the bug answers in C2), plus a **simple rubric**: "Does your rewrite specify R (role/context)? O (objective)? C (constraints)? S (specifics)? Rate each 0-2." This makes the exercise self-assessable and discussion-ready.

2. Add a **"prompt log" template** that students can use for any homework assignment going forward -- columns for: original prompt, AI output quality (1-5), what was missing (R/O/C/S), revised prompt, improved output quality. This connects the module to ongoing practice rather than being a one-off exercise.

3. Replace or supplement the generic "Help me find a topic" exercise with a **paired prompt competition**: students each write a prompt for the same task (e.g., "explain the difference between fixed and random effects"), compare AI outputs side by side, and vote on which prompt produced the more useful output. Then discuss why. This adds a social/competitive element and makes the quality difference vivid.

---

### A3: When AI Helps vs. Hurts Your Learning

**Current strengths**: The 2x2 framework (core skill vs. not / can do vs. can't yet) is the strongest single framework in the entire module set -- it is simple, memorable, and genuinely decision-relevant. The "desirable difficulty" grounding in learning science is well-done and gives the module intellectual weight beyond "be careful with AI." The warning signs section is specific and honest. The "personal policy" template is a practical output students can actually use.

**Weakest criterion: Hands-on practice.** The "Your AI Audit" exercise is reflective but entirely self-reported and unstructured. There is no mechanism for students to test their own assessments -- they could fill out the table and learn nothing if they are not honest or self-aware.

**Top improvements**:

1. Add a **concrete "can you still do it?" self-test**. Pick 3-5 specific tasks that students in the target course should be able to do (e.g., "Set up a Lagrangian for a constrained optimization problem," "Interpret a diff-in-diff coefficient," "Write a Stata merge command from memory"). Have students attempt each for 3 minutes without AI, then rate their confidence. This makes the audit tangible and sometimes uncomfortable -- which is the point.

2. Pair the personal policy exercise with a **"policy swap"**: students write their policy, trade with a partner, and each person identifies one place where the other's policy is too permissive or too restrictive. This adds external accountability.

3. Add a **"one week later" follow-up prompt**: after students write their personal AI policies, suggest instructors revisit in 1-2 weeks with the question "Did you follow your policy? Where did you deviate? Why?" This connects the module to actual behavior change rather than being a one-time reflection.

---

### B1: Terminal Basics

**Current strengths**: This is the most "ready to teach" module in the set. The progression from `pwd` through pipes is well-scaffolded. The Stata analogies are effective (terminal as Stata's command window, `cat`/`head`/`less` mapped to `list`). The exercise includes setup commands to create practice data, sample solutions, and a logical progression of tasks. The instructor note is the most detailed of any module, including common student issues and a shorter-session adaptation. The `rm` warning is well-placed and appropriately alarming.

**Weakest criterion: Specifics and relevance.** The example data (household survey in Kenya) is good but could be richer. The exercise creates a 4-row CSV, which limits what students can meaningfully explore. With slightly more rows and variables, students could answer more interesting questions with pipes.

**Top improvements**:

1. **Provide a downloadable sample CSV** with 50-100 rows and 6-8 variables (e.g., a simulated household survey with hhid, district, treatment, income, n_children, female_head, survey_round, consumption). Host it in the repo at `exercises/b1/household_survey.csv`. This replaces the `echo` commands in the setup and gives students enough data to make `grep | wc -l` and pipes feel genuinely useful. Include a `README.md` in the exercise folder describing the simulated data.

2. Add a **"scavenger hunt" exercise variant**: give students a list of 8-10 questions about a dataset or project folder that can each be answered with 1-2 terminal commands (e.g., "How many .do files are in the code/ directory?", "What is the last line of the log file?", "Which files mention the variable `consumption`?"). Students race to answer them all. This is more engaging than the current sequential walkthrough and works well as a timed in-class activity.

3. Add a **Windows setup guide** as a separate downloadable document. The module mentions Git Bash and WSL but doesn't walk through installation. Windows students will be blocked if setup instructions aren't sent in advance. A one-page PDF with screenshots would prevent the most common first-day problem.

---

### B2: Git & GitHub Essentials

**Current strengths**: The opening (the `analysis_v2_final_REAL_oct12_after_meeting.do` list) is the best hook in any module -- every student and instructor has lived this. The "missing data problem" analogy is creative and accurate. The staged workflow diagram is clear. The commit message good/bad table is immediately usable. The "What We're Not Covering" table is honest and well-scoped. The diff-reading section is practical and often skipped in Git tutorials aimed at economists.

**Weakest criterion: Hands-on practice.** The exercise asks students to clone the `teaching-ai` repo itself, which is clever but creates a problem: students can't push to it. Parts 1-3 work, but Part 4 ("push if you have a remote") is hand-wavy. Students don't create their own repo, so they don't experience the full workflow. The exercise also doesn't involve any collaboration, which is Git's primary value proposition for economists.

**Top improvements**:

1. **Restructure the exercise so each student creates their own repo.** Step 1: `git init my-research-project && cd my-research-project`. Step 2: Create a simple `analysis.do` file. Step 3: `git add`, `git commit`. Step 4: Edit the file, `git diff`, `git add`, `git commit`. Step 5 (optional, requires GitHub account): Create a repo on GitHub, add remote, push. This gives students ownership and a repo they can keep using. Provide exact commands for each step.

2. Add a **"time travel" mini-exercise**: after students have 3+ commits, have them use `git log --oneline`, then `git show <hash>:analysis.do` to see an earlier version, then `git diff <hash1> <hash2>` to compare two versions. This demonstrates the core value proposition (you can always go back) in a way students can feel.

3. Create a **downloadable `.gitignore` template for economics projects** (ignores `.dta`, `.csv`, `.log`, `.pdf`, `*.aux`, `*.synctex.gz`, `.DS_Store`, etc.) and include it in the exercise. The module mentions `.gitignore` as "skipped" but it's essential for economics projects where students will immediately try to commit 500MB data files. A ready-made template removes this friction point.

---

### C1: Literature Review & Synthesis

**Current strengths**: The "AI is good at processing text you give it, bad at retrieving facts" principle is the sharpest framing in the module set for this topic. The five-step workflow (brainstorm terms, search databases, summarize verified papers, identify gaps, verify everything) is practical and well-sequenced. The hallucination failure-mode table (fabricated, wrong authors, wrong findings, composite, outdated) is comprehensive. The citation verification exercise is well-designed with realistic prompts.

**Weakest criterion: Hands-on practice.** The exercise asks students to find 3 papers and paste abstracts, which is good, but it's entirely open-ended -- there's no way to know if students did it well or poorly. The "For the Ambitious" anti-pattern exercise is the most valuable part and should be required, not optional.

**Top improvements**:

1. **Make the anti-pattern exercise mandatory and structured.** Provide a specific prompt: "Ask your AI tool: 'Give me 5 key citations on [the topic you chose].' For each citation, fill in this verification table: Author(s), Year, Title, Journal, Exists? (Y/N), Finding Accurate? (Y/N), Notes." Then compare: How many of the 5 were real? How many had accurate findings? This produces a concrete, gradeable artifact and viscerally demonstrates the hallucination problem. Provide a blank downloadable verification table as a PDF/Word doc.

2. Add a **curated list of 3-4 real papers for each of the three suggested topics** (teacher quality, immigration, microfinance) so that instructors who want a more structured exercise can distribute actual abstracts rather than having students search. This also enables a standardized "compare your AI synthesis to the actual abstracts" evaluation.

3. Add a section on **AI-powered search tools** (Semantic Scholar, Elicit, Consensus, Connected Papers) with a brief honest assessment of each: what they do well, what they miss, how they compare to Google Scholar + EconLit. These tools sit between "ask ChatGPT for citations" and "search databases yourself" and students will encounter them. The module should acknowledge they exist and help students evaluate them critically.

---

### C2: Code Assistance

**Current strengths**: The debugging exercise is the best single exercise in the entire module set. It has a concrete buggy do-file, specific bugs at multiple difficulty levels, a "find bugs yourself first" step, an "ask AI" comparison step, and a collapsible answer key. The silent-errors framing is important and well-illustrated. The Stata-specific and R-specific trap tables are practical and fill a real gap -- most AI-and-code guides ignore language-specific pitfalls. The "computation vs. identification" distinction is the key idea and it's articulated clearly.

**Weakest criterion: Portability.** The exercise is embedded in the module text rather than being a standalone file. There's no downloadable `buggy_analysis.do` that students could open in their editor and actually run. The answer key is in a collapsible div, which works on the web but not as a handout. An instructor would need to extract the code, create the do-file, and format the answer key separately.

**Top improvements**:

1. **Create a downloadable exercise package** at `exercises/c2/`:
   - `buggy_analysis.do` -- the buggy code from the exercise, ready to open in Stata
   - `student_data.dta` and `school_data.dta` -- small simulated datasets (20-30 obs) so students can actually *run* the buggy code and see errors/silent failures
   - `bug_hunt_worksheet.md` -- a structured worksheet: "Bug 1: Line ___, Issue: ___, Fix: ___" for each bug, plus space for "Bugs I found" vs. "Bugs AI found"
   - `answer_key.md` -- instructor-only answer key with all 5 bugs explained
   This transforms a conceptual exercise into one students can actually execute.

2. Add a **second exercise focused on code review** (the module argues AI is better at reviewing than writing). Give students a 30-line do-file that runs correctly but has 3-4 best-practice violations (hardcoded path, missing `_merge` check, no `set seed` before a random operation, unlabeled variables). Task: "Use AI to review this code for reproducibility risks. Then evaluate: did AI catch the real issues, or did it flag irrelevant things?" This exercises the "AI as code reviewer" concept that the module advocates.

3. **Add an R version of the buggy code exercise.** The module covers R-specific traps but the exercise is Stata-only. A parallel `buggy_analysis.R` with equivalent bugs (wrong join type, silent type coercion, factor issues, ungrouped mutate) would make the module usable in R-based courses. Store at `exercises/c2/buggy_analysis.R`.

---

### C3: Data Exploration & Cleaning

**Current strengths**: The distinction between exploration (safe, descriptive) and cleaning (dangerous, judgment-laden) is the core insight and it's well-argued. The "adversarial data auditing" concept -- having AI review your work rather than doing the work -- is sophisticated and genuinely useful advice for research practice. The outlier-handling options table (drop, winsorize, keep, investigate, log-transform) maps decisions to justifications, which is exactly what students need. The cleaning exercise with simulated `summarize` output is well-designed.

**Weakest criterion: Hands-on practice.** The exercise asks students to paste simulated summary statistics into AI, which is good for demonstrating the concept, but students never touch actual data. They read a table of numbers, ask AI to comment on it, and evaluate the AI's comments. There's no moment where a student runs code, sees output, and makes a decision.

**Top improvements**:

1. **Create a simulated dataset** at `exercises/c3/labor_survey.dta` (and `.csv`) containing the exact data described in the exercise -- 10,000 obs, two rounds, the negative earnings value, the suspicious treatment split, the missingness patterns. Include a `README.md` describing the data-generating process (so instructors know the "ground truth"). This lets students actually run `summarize`, actually see the missingness, actually confront the -500 earnings value in their own Stata/R session. The ground truth README lets instructors create answer keys.

2. Add a **"cleaning decision log" template** -- a structured document where students record each cleaning decision: What did you find? What did you decide? Why? What is the alternative you rejected? How does this affect your sample size? This is the "cleaning memo" mentioned in passing but should be a formal, downloadable template that students fill in. Format: markdown or Word doc at `exercises/c3/cleaning_decision_log.md`.

3. Add a **before/after comparison exercise**: provide the same simulated dataset with and without a set of undocumented cleaning decisions applied (different `.dta` files: `labor_survey_raw.dta` and `labor_survey_cleaned.dta`). Task: "Compare the raw and cleaned datasets. What changed? Can you reverse-engineer what cleaning decisions were made? Do you agree with all of them?" This makes the "undocumented cleaning is dangerous" argument visceral rather than hypothetical.

---

### C4: Writing & Revision

**Current strengths**: The "writing IS thinking" argument is the strongest conceptual point in the C-track. The writing spectrum table (brainstorming through drafting, with risk levels) is a practical decision framework. The before/after/targeted-edit demonstration is excellent pedagogy -- students can see exactly how a broad rewrite destroys voice while a targeted edit preserves it. The economics-specific writing prompts (results description, identification strategy paragraph, table notes, abstract) are immediately usable. The reverse outlining technique is genuinely valuable and undersold in most writing guides.

**Weakest criterion: Specifics and relevance.** The module is somewhat generic in its writing examples. The migration finding example is good but it's the only fully-worked economics example. The identification strategy prompt uses a minimum-wage DID that is fine but could be more specific (real states, real years, real data sources). The table notes prompt is described but no example table is shown.

**Top improvements**:

1. **Add 2-3 more before/after/targeted-edit demonstrations** using different economics writing genres: (a) a results paragraph from a regression table, showing how AI rewrites lose precision about magnitudes and significance while the targeted edit sharpens them; (b) a literature review transition that connects two specific real papers; (c) a policy implications paragraph where AI's version adds unwarranted generalization. Store these as downloadable examples at `exercises/c4/`.

2. **Provide a sample regression table** (even a mock one) for the "table notes" exercise, so students can actually practice writing notes for a concrete table rather than imagining one. Include the table as an image or formatted markdown, plus a sample AI-generated note and an instructor-written note for comparison.

3. Add a **"spot the AI" exercise**: provide 4 short paragraphs (2 student-written, 2 AI-generated) on the same economics topic and have students identify which are AI-generated and why. Then discuss: what features gave it away? This makes the "AI prose is recognizable" claim testable and helps students internalize the tells (excessive hedging, generic transitions, false balance, lack of specificity).

---

### C5: Math & Derivations

**Current strengths**: The three worked examples (Cobb-Douglas demand, labor supply elasticity, comparative statics with SOC) are progressively more difficult and each illustrates a different failure mode. The verification framework (boundary cases, dimensional analysis, special cases, work backwards, check signs) is practical and transferable. The "introduce an error and see if AI catches it" exercise is clever and produces genuinely surprising results. The distinction between "AI gets the algebra right but the interpretation wrong" is an important insight specific to economics.

**Weakest criterion: Hands-on practice.** The exercise is well-structured (solve yourself, ask AI, introduce error, test AI as checker) but all four parts happen in the same session and there's no deliverable. Students do the work but produce nothing an instructor can evaluate or that they can refer back to. The "introduce an error" instruction in Part 4 is confusing -- the example walks itself into a correction mid-sentence, which will confuse students.

**Top improvements**:

1. **Create a downloadable "verification report" template** at `exercises/c5/verification_report.md` with structured sections: "Problem Statement", "My Solution (key steps)", "AI's Solution (key steps)", "Discrepancies", "Verification Checks Performed" (with checkboxes for boundary cases, units, special cases, work backward, sign checks), "Conclusion: Is the AI solution correct?" This makes the exercise produce a gradeable artifact.

2. **Provide 2-3 pre-made "AI derivations with errors"** that students can evaluate. For example: (a) a Cobb-Douglas derivation with a sign error in the MRS step; (b) a profit maximization where the SOC is not checked and the production function actually has increasing returns; (c) an elasticity derivation that gets the formula right but misinterprets income vs. substitution effects. Provide these as formatted PDFs at `exercises/c5/`. This standardizes the exercise and ensures every student encounters meaningful errors, rather than depending on what AI happens to produce in real time.

3. **Clean up the Part 4 exercise text.** The current text includes a parenthetical that corrects itself mid-sentence: `"[*intentional error: should be $\frac{p_y}{p_x}$*... wait, actually should be $\frac{p_x}{p_y}$ -- double-check your own error!]"`. This is confusing. Replace with a clean instruction: "Write out a derivation with one deliberate error -- for example, swap two terms in the MRS condition. Paste it into AI and ask 'Is each step correct?' Record whether AI catches your error, misses it, or incorrectly flags a correct step."

---

## 3. Cross-Cutting Themes

### Theme 1: The exercise gap

Every module has exercises, but the C-track modules (C1-C5) rely heavily on "paste something into AI and evaluate the output." This is a legitimate exercise format, but it produces highly variable results depending on which AI tool, which session, and which prompt the student uses. There is no standardized baseline for comparison or grading.

The B-track modules (B1, B2) show a better pattern: structured tasks with specific commands, expected outputs, and verifiable results. The C-track should adopt this pattern by providing downloadable exercise materials with known "ground truth" answers.

### Theme 2: No materials for instructors who don't use Stata

The modules reference Stata throughout (A2, B1, B2, C2, C3, C5 all have Stata-specific content). R appears in C2's trap table and occasionally elsewhere, but there are no R-equivalent exercises. Python is absent entirely. An instructor teaching in R or Python would need to translate every code example and exercise.

### Theme 3: The "economist's analogy" pattern works -- protect it

Every module uses economics-specific analogies to explain AI concepts, and they are consistently the strongest element. The identification-strategy analogy for prompting, the measurement-error analogy for hallucination, the computation-vs-identification distinction for code -- these are what make the modules distinctive and valuable. Any revision should preserve and extend this pattern, not dilute it with generic tech-focused framing.

### Theme 4: Timelessness is generally strong, with a few exceptions

The modules avoid naming specific models or tools in most places. The references to "GPT-4 and Claude" in A1 (Step 4: Fine-tuning and RLHF) and the `go.uvm.edu/copilot` link in A1's exercise section are the main exceptions. The conceptual frameworks (next-token prediction, hallucination, sycophancy, the 2x2, computation vs. identification) are durable. The biggest timelessness risk is actually in C1, where the claim that "AI hallucinates citations routinely" may become less true as tools improve -- but the module wisely addresses this with the "not getting better fast enough to trust" callout, which can be updated as needed.

### Theme 5: Missing scaffolding for semester-long integration

Each module is designed as a standalone session, but there's no guidance on sequencing, cumulative skill-building, or semester-long integration. An instructor who wants to weave these into an existing course (rather than teaching them as a standalone workshop) gets no help with: Which modules are prerequisites for others? What's the minimum viable subset? How do these connect to specific points in an econometrics or micro syllabus?

---

## 4. Improvement Plan

### Criterion 1: Specifics and Relevance

| Action Item | Module(s) | Effort | Priority |
|---|---|---|---|
| Create a downloadable 50-100 row simulated household survey CSV for B1 exercises | B1 | Quick fix | High |
| Create simulated `labor_survey.dta`/`.csv` with known data quality issues for C3 | C3 | Half-day | High |
| Create `buggy_analysis.do` + simulated `.dta` files so students can run the C2 exercise | C2 | Half-day | High |
| Create parallel `buggy_analysis.R` with equivalent R-specific bugs | C2 | Half-day | Medium |
| Add 2-3 subfield-specific citation prompt options to A1 hallucination exercise | A1 | Quick fix | Medium |
| Add 2-3 more before/after/targeted-edit writing examples for C4 | C4 | Half-day | Medium |
| Add a sample regression table for the C4 "table notes" exercise | C4 | Quick fix | Medium |
| Provide curated real-paper lists for C1's three suggested topics | C1 | Half-day | Medium |
| Add a section on AI-powered literature search tools (Semantic Scholar, Elicit, etc.) to C1 | C1 | Half-day | Low |
| Create pre-made "AI derivations with errors" for C5 exercises | C5 | Half-day | Medium |

### Criterion 2: Timelessness

| Action Item | Module(s) | Effort | Priority |
|---|---|---|---|
| Replace "GPT-4 and Claude" in A1 Step 4 with generic phrasing: "Modern chat models go through additional training" | A1 | Quick fix | High |
| Move the UVM Copilot link from inline text to a configurable callout: "Your institution may provide an AI tool -- check with your instructor. At UVM, this is go.uvm.edu/copilot." Make the callout easy for other instructors to swap. | A1 | Quick fix | High |
| Add a "last reviewed" date and a note about which claims may change (e.g., citation hallucination rates) to C1 | C1 | Quick fix | Medium |
| In C1's "This Is Not Getting Better Fast Enough to Trust" callout, add language that acknowledges improvement trajectory: "Check the latest evidence on hallucination rates for the tool you're using, but verify citations regardless." | C1 | Quick fix | Medium |
| Review the 2023 lawyer anecdote in C1 -- it's already 3 years old. Consider framing as "early examples" rather than recent news | C1 | Quick fix | Low |
| Ensure all further-reading citations in A1 include enough info to find them if URLs change (author, year, title, publication) | A1 | Quick fix | Low |

### Criterion 3: Hands-On and Real-World Practice

| Action Item | Module(s) | Effort | Priority |
|---|---|---|---|
| Create structured worksheets for A1 failure-mode exercises (hallucination verification table, sycophancy comparison template) | A1 | Half-day | High |
| Make C1's anti-pattern exercise (ask AI for citations, then verify) required instead of optional; add downloadable verification table | C1 | Quick fix | High |
| Add sample "good" rewrites to A2's Prompt Makeover exercise in collapsible sections, plus a self-assessment rubric | A2 | Half-day | High |
| Create "can you still do it?" self-test with 3-5 timed micro-tasks for A3 | A3 | Half-day | High |
| Build a "scavenger hunt" exercise variant for B1 with 8-10 terminal-answerable questions | B1 | Half-day | Medium |
| Restructure B2 exercise so students create their own repo + add "time travel" mini-exercise | B2 | Half-day | High |
| Add a code-review exercise to C2 (clean but non-reproducible do-file for students to review with AI) | C2 | Half-day | Medium |
| Create before/after dataset comparison exercise for C3 (raw vs. undocumented-cleaned) | C3 | Half-day | Medium |
| Add "spot the AI" exercise to C4 (4 paragraphs, identify which are AI-generated) | C4 | Half-day | Medium |
| Create downloadable verification report template for C5 | C5 | Quick fix | High |
| Clean up C5 Part 4 exercise text (remove the confusing self-correcting parenthetical) | C5 | Quick fix | High |
| Add a prompt log template (reusable across modules) for A2 that students use all semester | A2 | Quick fix | Medium |
| Add a "policy swap" pair activity to A3 | A3 | Quick fix | Medium |

### Criterion 4: Portability

| Action Item | Module(s) | Effort | Priority |
|---|---|---|---|
| Create a master "Instructor Setup Guide" covering: prerequisites, software needed, accounts needed, suggested sequencing, minimum viable module subsets, and how to adapt for R vs. Stata | All | Multi-session | High |
| Create a `.gitignore` template for economics projects (downloadable, referenced in B2) | B2 | Quick fix | High |
| Create a Windows terminal setup guide (Git Bash installation with screenshots) as a standalone PDF | B1 | Half-day | High |
| For each module, extract exercises into standalone downloadable files (worksheets, handouts, starter code) in `exercises/<module>/` | All | Multi-session | High |
| Create answer keys / discussion guides for each module's exercises (instructor-only, could be distributed via a separate repo or gated folder) | All | Multi-session | High |
| Add timing estimates to each exercise step (not just the module total) | All | Half-day | Medium |
| Create a "Module Adaptation Guide" for each module: 3 variants (50-min lecture, 75-min workshop, take-home assignment) with different exercise selections | All | Multi-session | Medium |
| Create a suggested syllabus integration document: "If you're teaching Intro Micro, use modules A1-A3 + C5 in weeks 2, 4, 6, 10. If you're teaching Econometrics, use A1-A3 + B1-B2 + C2-C3 in weeks 1-3 + 5-6." | All | Half-day | Medium |
| Add R-equivalent examples alongside Stata examples in C2, C3, and C5 (either inline with tabs or as separate downloadable files) | C2, C3, C5 | Multi-session | Medium |
| Create slide decks (or at minimum, slide outlines) for the 5 most commonly taught modules (A1, A2, A3, C1, C2) | A1-A3, C1, C2 | Multi-session | Low |

---

## 5. Instructor Adoption Kit Proposal

To make these modules maximally portable -- teachable by any economics instructor at any university with minimal prep -- the following supplementary materials should be created.

### 5.1 Tier 1: Essential (needed for basic portability)

**File: `INSTRUCTOR_GUIDE.md`**
- Module dependency graph (A1 -> A2 -> A3 as a sequence; B1 -> B2 as a sequence; A1-A3 as prerequisites for all C modules)
- Suggested sequencing for different course types (principles, intermediate micro, econometrics, senior seminar)
- Minimum viable subsets: "If you only have one class session, teach A1+A3. If you have three, add A2+C1 or A2+C2."
- Software/account requirements per module (terminal, Git, GitHub account, AI tool access, Stata or R)
- Pre-class setup checklist (what students need to install/configure before each module)
- How to swap out the UVM Copilot reference for your institution's tool

**Folder: `exercises/` with per-module subfolders**

| Folder | Contents |
|---|---|
| `exercises/a1/` | `hallucination_verification_table.pdf`, `sycophancy_comparison_template.pdf`, `failure_modes_worksheet.pdf` |
| `exercises/a2/` | `prompt_makeover_worksheet.pdf` (with rubric), `prompt_log_template.md` (reusable) |
| `exercises/a3/` | `ai_audit_worksheet.pdf`, `personal_ai_policy_template.md`, `self_test_tasks.pdf` (3-5 timed micro-tasks, with versions for micro, metrics, and principles) |
| `exercises/b1/` | `household_survey.csv` (50-100 rows), `scavenger_hunt.pdf` (8-10 questions + answer key), `windows_setup_guide.pdf` |
| `exercises/b2/` | `git_exercise_walkthrough.pdf` (create-your-own-repo version), `econ_gitignore_template` (ready to copy), `git_cheatsheet.pdf` (one-page reference) |
| `exercises/c1/` | `citation_verification_table.pdf`, `curated_paper_lists/` (3-4 topics with real citations and abstracts) |
| `exercises/c2/` | `buggy_analysis.do`, `student_data.dta`, `school_data.dta`, `bug_hunt_worksheet.pdf`, `answer_key.pdf`, `buggy_analysis.R` (R equivalent) |
| `exercises/c3/` | `labor_survey.dta`, `labor_survey.csv`, `cleaning_decision_log.md`, `data_readme.md` (ground truth), `labor_survey_cleaned.dta` (for before/after exercise) |
| `exercises/c4/` | `writing_examples/` (3 before/after/targeted-edit sets), `spot_the_ai.pdf` (4 paragraphs exercise), `sample_regression_table.pdf` |
| `exercises/c5/` | `verification_report_template.md`, `ai_derivations_with_errors/` (2-3 PDF problem sets with planted errors), `answer_keys/` |

### 5.2 Tier 2: Enhanced (significantly improves teachability)

**File: Per-module lesson plans** (`lesson_plans/<module>_lesson_plan.md`)
- Minute-by-minute timing for a 50-min and 75-min version
- Which sections to skip in a shorter session
- Suggested live-demo scripts (what to type/show, what to expect)
- "If students ask..." FAQ with 3-5 common questions and suggested responses
- How to run the exercise: individual vs. pairs vs. groups, timing per step, what to discuss after

**File: `ASSESSMENT_MENU.md`**
- For each module: 2-3 assessment options at different levels of effort
  - Low: participation/reflection (submit the completed worksheet)
  - Medium: process document (submit prompt log, verification table, cleaning memo)
  - High: portfolio piece (code review report, lit review process document, writing revision log)
- Sample rubrics for the medium and high options
- How to grade process, not just output

**File: `ADAPTATION_GUIDE.md`**
- How to teach the C-track modules in R instead of Stata (specific code translations)
- How to adapt for principles-level students (what to cut, what to simplify, what to add)
- How to adapt for graduate students (what to cut as too basic, what to extend)
- How to teach as a standalone workshop vs. embedded in a semester-long course

### 5.3 Tier 3: Polished (for wide adoption)

**Slide decks** (`slides/<module>_slides.qmd`)
- Quarto-based slides matching the site theme
- Key figures and tables from each module
- Speaker notes embedded
- 5 modules minimum: A1, A2, A3, C1, C2

**Video walkthroughs** (linked, not hosted in repo)
- 5-10 min screencasts for B1 and B2 exercises (terminal and Git are hardest to learn from text alone)
- Live demo recordings of the A1 hallucination exercise and C2 debugging exercise

**Pre-configured student environments**
- A GitHub Classroom template repo for B2 exercises
- A Codespace or cloud-based terminal option for B1 (for students who can't install anything)

### Priority Sequencing

If implementing in phases:

1. **Phase 1** (1-2 working days): Quick fixes across all modules (timelessness edits, exercise text cleanup, UVM reference handling) + create `INSTRUCTOR_GUIDE.md` + downloadable exercise files for the 3 most-taught modules (A1, C2, B1)
2. **Phase 2** (3-4 working days): Exercise materials for remaining modules + lesson plans for A1-A3 + C1-C2 + `ASSESSMENT_MENU.md`
3. **Phase 3** (1-2 weeks): R equivalents for C-track exercises + `ADAPTATION_GUIDE.md` + slide decks for top 5 modules
4. **Phase 4** (ongoing): Video walkthroughs, GitHub Classroom integration, community feedback incorporation
