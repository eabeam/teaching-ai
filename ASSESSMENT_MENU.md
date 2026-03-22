# Assessment Menu

Assessment options for each module at three effort levels. The core principle: **grade the student's process and judgment, not the AI's output.** AI outputs vary across tools, sessions, and even identical prompts. What stays constant is the student's ability to evaluate, verify, and apply that output.

---

## Grading Philosophy: Process Over Output

### Why process matters more than product

When students use AI tools, the final product (a cleaned dataset, a polished paragraph, a correct derivation) tells you very little about what the student learned. The *process* -- what they asked, how they evaluated the response, what they accepted, rejected, or modified -- tells you everything.

A student who gets the right answer from AI and copies it has learned nothing. A student who gets a wrong answer from AI, identifies the error, and corrects it has demonstrated genuine understanding.

### How to handle variable AI outputs

Two students can submit the same prompt and get meaningfully different responses from the same AI tool. This is expected -- LLMs are probabilistic. Your rubric should evaluate:

- **Did the student evaluate the AI output critically?** (not just accept it)
- **Did the student identify strengths and weaknesses in the AI response?**
- **Did the student demonstrate their own understanding of the material?** (through verification, correction, annotation, or reflection)
- **Is the student's process documented and reproducible?**

---

## Assessment Options by Module

### A1: What LLMs Actually Do

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Failure mode worksheet | Complete the in-module exercise: test hallucination, sycophancy, and anchoring. Submit AI outputs + 1--2 paragraphs reflecting on what surprised you. |
| **Medium** | Hallucination audit report | Ask AI for 5 citations in a specific subfield. Verify each in Google Scholar. Submit a table: citation, exists? (Y/N), details correct?, what was wrong. Plus a paragraph on the pattern of errors. |
| **Substantial** | Mental model essay | Write a 2--3 page essay explaining how LLMs work to a non-technical audience (e.g., a policymaker, a parent, a journalist). Must accurately convey the token-prediction mechanism and at least two failure modes. No AI assistance for the writing. |

### A2: Prompting as Problem Specification

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Prompt makeover | Complete the in-module exercise: rewrite 4 "before" prompts, try both versions, submit the comparison. |
| **Medium** | Prompt log | For a real homework assignment or research question, submit a log showing: (1) initial prompt, (2) AI response, (3) what was wrong or missing, (4) revised prompt, (5) improved response. Minimum 3 rounds of iteration. |
| **Substantial** | Prompt quality analysis | Collect 10 prompts from classmates (anonymous). Diagnose each using the ROCS framework (what's missing: Role, Objective, Constraints, Specifics?). Rewrite each. Test both versions. Write up the patterns you observed. |

### A3: When AI Helps vs. Hurts Your Learning

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Personal AI policy | Complete the "Your AI Audit" exercise and draft a personal AI use policy using the template in the module. Submit the policy (1 page). |
| **Medium** | AI use diary | Track your AI use for one week. For each instance: what task, which quadrant of the 2x2, did it help or replace your learning, what would you do differently? Submit diary + 1-page reflection. |
| **Substantial** | Learning experiment | Do one assignment two ways: (1) without AI, (2) with AI. Document both processes. One week later, test yourself on the material (without AI). Write a 2--3 page analysis of the difference in process, product, and retention. |

### B1: Terminal Basics

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Exercise completion | Complete the "Exploring a Replication Package" exercise. Submit a screenshot or text file of your terminal session showing the commands and outputs. |
| **Medium** | Terminal scavenger hunt | Given a project folder (provided by instructor), answer 8--10 questions using only the terminal (e.g., "How many .do files are in this project?", "Which file was modified most recently?", "How many observations mention district X?"). Submit commands and answers. |
| **Substantial** | Replication package audit | Download a real replication package from a published paper (AEA registry, journal website). Using only the terminal, document: folder structure, file types, line counts, key variables used across files, any potential issues (hardcoded paths, missing files). Submit a 1--2 page audit memo. |

### B2: Git & GitHub Essentials

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | First repository | Create a GitHub repository with at least 3 meaningful commits. Submit the repository URL. Graded on: commit messages are descriptive, commits represent logical units of work. |
| **Medium** | Version-controlled analysis | Complete a short data analysis (provided by instructor). Use Git throughout. Submit the GitHub repository. Must have 5+ commits showing progression from setup through analysis, with clear commit messages. |
| **Substantial** | Collaborative workflow | In pairs, use a shared GitHub repository to complete an analysis. Each partner contributes commits. Submit: the repo URL, a brief write-up of the workflow (who did what, how you coordinated), and a reflection on how version control changed the collaboration process. |

### C1: Literature Review & Synthesis

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Citation verification worksheet | Ask AI for 5 citations on a topic. Verify each. Submit the verification table (exists?, authors correct?, findings correct?). |
| **Medium** | Lit review process document | Follow the 5-step workflow in the module. Submit: (1) AI-generated search terms, (2) databases searched, (3) 5 verified papers with full citations, (4) AI synthesis of those papers (with your annotations of what it got right/wrong), (5) your evaluation of the synthesis quality. |
| **Substantial** | Full AI-assisted literature review | Produce a 3--5 page literature review on a topic of your choice using the module's workflow. Submit both the final review AND a process log documenting every AI interaction, every citation verification, and every editorial decision. The process log is graded alongside the review. |

### C2: Code Assistance

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Debugging exercise | Complete the in-module debugging exercise. Submit: bugs you found yourself, bugs AI found, comparison. |
| **Medium** | Code review report | Take an AI-generated script (provided or self-generated) for a data analysis task. Annotate every line: is it correct? What does it do? What could go wrong? Would you change it? Submit the annotated script + a 1-page summary of findings. |
| **Substantial** | Debugging case study | Encounter a real bug in your own coursework or research code. Document: (1) the error, (2) your debugging attempt, (3) AI's debugging suggestion, (4) what worked, (5) what was wrong with AI's suggestion (if anything). Write a 2--3 page case study of the process. |

### C3: Data Exploration & Cleaning

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Exploration worksheet | Run `describe` and `summarize` on a dataset (provided). Paste the output into AI and ask it to flag issues. Submit: AI's flags + your evaluation of which flags are genuine issues and which are not. |
| **Medium** | Cleaning memo | Given a dataset and an AI-generated cleaning script, evaluate every decision the script makes. Submit: (1) annotated script identifying each decision, (2) your assessment of each decision (appropriate? why or why not?), (3) a cleaning memo documenting what you would do and why. |
| **Substantial** | Data pipeline audit | Take a full data cleaning pipeline (from your own work or a replication package). Have AI review it for risks (merge diagnostics, hardcoded paths, undocumented decisions). Write a 2--3 page audit report: what AI caught, what it missed, what you found yourself, and recommendations. |

### C4: Writing & Revision

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Revision exercise | Complete the in-module exercise (write a paragraph, try three AI revision types, reflect). Submit all versions + reflection. |
| **Medium** | Revision log | For a paper or assignment, submit a revision log showing every AI interaction: (1) what you asked, (2) what AI suggested, (3) what you accepted/rejected/modified, and why. Submit alongside the final paper. |
| **Substantial** | Writing revision portfolio | Collect 3--4 pieces of your own writing from the semester. For each: (1) original draft, (2) AI-assisted revision (using targeted edits, not full rewrites), (3) final version, (4) reflection on what AI improved and what you had to do yourself. Include a 1-page summary of what you learned about your own writing. |

### C5: Math & Derivations

| Level | Assessment | Description |
|-------|-----------|-------------|
| **Light** | Verification exercise | Complete the in-module exercise: solve a problem yourself, compare to AI's solution, introduce an intentional error and test whether AI catches it. Submit your work + comparison. |
| **Medium** | Verification table | Given 3 AI-generated derivations (some with errors, some correct), verify each step. Submit a verification table: step number, correct? (Y/N), if incorrect what's wrong, how you verified (boundary case, units check, special case, etc.). |
| **Substantial** | Math verification case study | Take a non-trivial derivation from your coursework. (1) Solve it yourself. (2) Ask AI to solve it. (3) Compare approaches. (4) Run all 5 verification checks (boundary cases, dimensions, special cases, work backwards, check signs). Write a 2--3 page report on where AI was helpful, where it was wrong, and what verification strategy was most effective. |

---

## Sample Rubric: Medium-Level Assessments

This rubric applies to any "process document" assessment (prompt logs, code review reports, cleaning memos, verification tables, revision logs).

| Criterion | Excellent (A) | Good (B) | Adequate (C) | Insufficient (D/F) |
|-----------|--------------|----------|--------------|---------------------|
| **Documentation completeness** | Every AI interaction is recorded: prompt, response, evaluation. Nothing is missing. | Most interactions recorded. Minor gaps that don't affect understanding. | Partial documentation. Key interactions missing. | Little or no documentation of the process. |
| **Critical evaluation** | Student identifies specific strengths and weaknesses of each AI output. Evaluations demonstrate deep understanding. | Student evaluates most outputs with reasonable specificity. Some generic assessments. | Surface-level evaluation. "Looked right" or "seemed wrong" without explanation. | No evaluation. Student accepted all AI output without comment. |
| **Domain knowledge** | Student's evaluations demonstrate mastery of the subject matter (correct identification of errors, accurate judgment calls). | Good subject knowledge. Occasional errors in evaluation but overall sound. | Basic subject knowledge. Misses some issues, misidentifies others. | Evaluation reveals significant gaps in subject understanding. |
| **Reflection quality** | Thoughtful meta-analysis of when AI was helpful vs. not. Generalizable insights about AI use. | Good reflection with some generalizable insights. | Brief reflection without much depth. | No reflection or perfunctory. |
| **Independence** | Clear evidence student did substantial thinking before and after AI interaction. | Mostly student-driven process with appropriate AI support. | Over-reliance on AI. Student appears to be following AI's lead rather than evaluating. | Student appears to have copied AI output with minimal engagement. |

### Suggested point allocation

These are suggestions; adjust to your course weighting.

| Assessment level | Suggested weight | Typical point value (in a 100-point course) |
|------------------|-----------------|----------------------------------------------|
| Light (participation) | 2--5% each | 5--10 points |
| Medium (process document) | 5--10% each | 10--20 points |
| Substantial (portfolio piece) | 10--20% each | 20--40 points |

---

## Grading Tips

### On grading process vs. output

Explicitly tell students that you are grading their evaluation of AI, not the AI's output. A student who gets a bad AI response and writes a thorough critique earns a higher grade than a student who gets a good AI response and writes "looks correct."

### On the variability of AI outputs

When two students submit very similar process documents, it's more likely they used similar prompts (or the same AI tool on the same day) than that they copied from each other. AI outputs cluster. Look at the *evaluation* for evidence of independent thinking, not the AI output itself.

### On academic integrity

These assessments are designed to make AI use visible, not hidden. Students submit their AI interactions as part of the work. This transforms AI from a potential cheating tool into an assessed skill. If students fabricate their process logs (inventing AI interactions they didn't have), that's the same category of dishonesty as fabricating lab data -- address it the same way.

### On effort calibration

- **Light assessments** should take 20--40 minutes, including the exercise itself.
- **Medium assessments** should take 1--2 hours.
- **Substantial assessments** should take 3--5 hours and produce a document the student could include in a portfolio or show to an employer.
