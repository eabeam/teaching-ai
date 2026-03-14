---
type: plan
project: teaching-ai
status: to-process
created: 2026-03-14
---

# Teaching AI for Economists — Full Module Catalog

## How to Read This Document

Each module is tagged with a **stability rating**:

- **Stable**: Core concepts unlikely to change significantly. These modules will age well and need only minor updates over time. Write these first.
- **Slow-moving**: Underlying ideas are durable, but examples/tools/interfaces will need periodic refreshes (annually or so).
- **Fast-moving**: Content is tied to specific tools, platforms, or capabilities that evolve rapidly. These modules need active maintenance and will feel dated within 6-12 months if not updated.

The stability rating matters for prioritization: **start with stable modules** to build a durable foundation, then layer in fast-moving content that you're prepared to maintain.

---

## Track A: Foundations

Core concepts about what AI is, how to use it, and how to think about it. Mostly stable — these are the modules that will still be relevant in 5 years.

### A1: What LLMs Actually Do ✅ DRAFTED
**Stability: Stable**

Tokens, prediction, training, fine-tuning, RLHF. Mental models for economists. Why hallucination, sycophancy, and anchoring are features of the mechanism, not bugs.

- ~50 min, no coding required
- *Why stable*: The transformer architecture and core mechanism haven't changed since 2017. New models are bigger/better but the conceptual foundation is the same. May need a brief update if a fundamentally different architecture emerges, but that's not imminent.
- *Update trigger*: Major architectural shift (not just a new model release)

### A2: Prompting as Problem Specification ✅ DRAFTED
**Stability: Stable**

Clear prompts = clear thinking. ROCS framework (Role, Objective, Constraints, Specifics). Common failures and fixes. Iterative prompting. The "prompt as identification strategy" analogy.

- ~50 min, no coding required
- *Why stable*: The principle that clear specification produces better outputs is model-agnostic and timeless. The specific prompting tricks (chain-of-thought, etc.) may evolve, but the core skill of precise communication will not.
- *Update trigger*: If models become so good that prompt quality stops mattering (unlikely near-term)

### A3: When AI Helps vs. Hurts Your Learning ✅ DRAFTED
**Stability: Stable**

Desirable difficulty framework. The 2x2 (core skill vs. not × can do vs. can't yet). Warning signs. Personal AI use policy development.

- ~30 min, no coding required
- *Why stable*: Grounded in learning science (desirable difficulty, fluency illusion), not in any specific tool. The framework applies regardless of which AI tool exists.
- *Update trigger*: Significant new learning science research about AI and cognition

### A4: Verifying AI Output
**Stability: Stable**

Systematic verification strategies. Citation checking. Quantitative claim verification. Detecting confident wrongness. Economics-specific failure patterns (fake elasticities, plausible-but-wrong mechanisms, fabricated empirical results).

- ~50 min, no coding required
- *Why stable*: Verification is a permanent skill. Even as models improve, the *process* of checking outputs remains essential. Examples may need updating as models get better at specific tasks.
- *Update trigger*: Refresh examples every 1-2 years as models improve

### A5: AI Ethics and Economics
**Stability: Slow-moving**

Bias in training data and outputs. Labor market implications of AI (automation, complementarity, distributional effects). Environmental costs of training. IP and attribution questions. How economists should think about AI externalities.

- ~50 min, no coding required
- *Why slow-moving*: The ethical frameworks are stable, but the empirical evidence on labor market effects, regulation, and environmental costs is actively evolving. The economics-specific angle (thinking about this as an externality/market failure problem) is durable.
- *Update trigger*: Major regulatory changes, significant new labor market evidence

### A6: How AI Models Are Trained (Deep Dive)
**Stability: Stable**

Pre-training, fine-tuning, RLHF, constitutional AI, distillation. How training data shapes outputs. What "alignment" means and why it matters. Scale laws and emergent capabilities.

- ~75 min, no coding required (optional technical supplement with coding)
- *Why stable*: Training methodology has been broadly consistent. New techniques add to rather than replace the core pipeline. This is the "A1 for students who want more depth."
- *Update trigger*: Fundamental training paradigm shift

### A7: AI and Academic Integrity
**Stability: Slow-moving**

What counts as appropriate AI use in academic work. How to cite AI assistance. Navigating different instructor policies. The difference between AI as tool vs. AI as substitute. Building a professional practice around AI use.

- ~30 min, no coding required
- *Why slow-moving*: Norms are actively being established. Institutional policies are in flux. The underlying ethical framework (honesty about your process) is stable, but the specific expectations are shifting.
- *Update trigger*: Updated UVM or disciplinary policies, new norms in economics profession

---

## Track B: Technical Foundations

Skills that make students capable of using AI (and doing economics) beyond point-and-click interfaces. Mixed stability — the concepts are stable but the specific tools evolve.

### B1: Terminal / Command Line Basics
**Stability: Stable**

What is a shell. Navigating the filesystem (ls, cd, pwd). Reading and searching files (cat, head, grep). Pipes and redirection. Why the command line matters for reproducibility in economics.

- ~75 min, hands-on
- *Why stable*: Unix commands have been essentially unchanged for 50 years. Bash/zsh fundamentals are as stable as any technology gets. The "why this matters for economists" framing (reproducibility, automation) is also durable.
- *Update trigger*: Effectively never for core content

### B2: Git & GitHub Essentials
**Stability: Stable**

Version control concepts. The Git mental model (staging, commits, branches). Basic workflow (clone, add, commit, push, pull). Reading diffs. Why economists should version-control their code. Connecting to GitHub.

- ~75 min, hands-on
- *Why stable*: Git has been the dominant VCS for 15+ years with no challenger. The concepts (snapshots, branches, distributed version control) are stable. GitHub's UI changes but the workflow doesn't.
- *Update trigger*: If a Git successor emerges (not on the horizon)

### B3: Your AI Toolbox — What's Available and When to Use What
**Stability: Fast-moving**

Overview of available AI tools: UVM Copilot (GPT-4), free tiers (ChatGPT, Claude, Gemini, Perplexity), specialized tools (GitHub Copilot for code, Elicit/Consensus for literature), local models. When to use which. Privacy and data considerations. Setting up accounts.

- ~50 min, hands-on
- *Why fast-moving*: New tools launch constantly. Pricing changes. Models are updated. UVM's offerings may expand. This module is essentially a living document.
- *Update trigger*: Every semester — review tool landscape, update pricing, add/remove tools
- *Maintenance strategy*: Keep the "principles for choosing tools" section stable; maintain a separate "current tool landscape" table that's easy to update

### B4: Working with AI in the Terminal (Claude Code, CLI tools)
**Stability: Fast-moving**

Using AI directly in the terminal. Claude Code, GitHub Copilot CLI, Aider, open-source alternatives. When terminal-based AI beats chat interfaces. Building workflows that combine CLI skills with AI assistance.

- ~75 min, hands-on (requires B1)
- *Why fast-moving*: This category of tools barely existed a year ago. Capabilities, interfaces, and pricing are changing rapidly. But the *concept* of AI-augmented terminal work is likely durable.
- *Update trigger*: Every semester
- *Prerequisite*: B1

### B5: APIs and Programmatic AI Access
**Stability: Slow-moving**

What an API is. Making API calls (curl, Python requests). Structured vs. conversational AI use. When programmatic access beats a chat interface. Cost management. Basic Python for API interaction.

- ~75 min, hands-on (requires B1)
- *Why slow-moving*: The concept of APIs is totally stable. The specific API formats (OpenAI-style, Anthropic-style) have converged on similar patterns. Pricing and model names change, but the skill of "calling an API" is durable.
- *Update trigger*: If API paradigms shift significantly; refresh model names/pricing annually

### B6: Data Privacy and Security with AI Tools
**Stability: Slow-moving**

What happens to your data when you use different AI tools. Enterprise vs. consumer protections. FERPA and research data considerations. IRB implications. Practical rules: what you can and can't paste into an AI tool. UVM's specific protections.

- ~30 min, no coding required
- *Why slow-moving*: Privacy frameworks (FERPA, IRB) are stable. Tool-specific policies change. UVM's enterprise agreements evolve. The core principles (know where your data goes, protect human subjects data) are permanent.
- *Update trigger*: UVM policy changes, new tool privacy policies

---

## Track C: AI for Economics Workflows

Applied modules showing how AI fits into the actual work economists do. Stability varies — the workflows are stable but the "how AI helps" evolves as capabilities improve.

### C1: Literature Review & Synthesis
**Stability: Slow-moving**

Using AI to survey a field, summarize papers, identify gaps. Specialized tools (Elicit, Consensus, Semantic Scholar, Connected Papers). Fact-checking AI-generated summaries against actual papers. Building annotated bibliographies. When AI helps vs. when it sends you down a rabbit hole.

- ~50 min, hands-on
- *Why slow-moving*: The lit review workflow is stable. Specific AI tools for academic search are evolving rapidly, but the skill of "use AI to find and summarize, then verify" is durable.
- *Update trigger*: New dominant academic AI tools; refresh tool recommendations annually

### C2: Code Assistance — Stata
**Stability: Slow-moving**

Using AI to write, debug, and document Stata code. Common patterns: translating pseudocode to Stata, debugging error messages, understanding unfamiliar commands, generating data cleaning pipelines. What AI gets wrong about Stata (version-specific syntax, obscure options, path handling).

- ~50 min, hands-on
- *Why slow-moving*: Stata itself changes slowly. AI's Stata capabilities will improve, but the workflow (write → debug → document with AI help) and the failure modes (hallucinated options, wrong syntax) are relatively stable.
- *Update trigger*: Major Stata version releases; refresh as AI gets better at Stata

### C3: Code Assistance — R
**Stability: Slow-moving**

Same as C2 but for R/tidyverse. Using AI for package selection, pipeline construction, ggplot customization, debugging. What AI gets wrong about R (outdated package recommendations, base R vs. tidyverse confusion, version-specific breaking changes).

- ~50 min, hands-on
- *Why slow-moving*: R's ecosystem changes faster than Stata's but the workflow is similar. The tidyverse conventions are fairly stable now.
- *Update trigger*: Major tidyverse/R changes; refresh as AI's R capabilities evolve

### C4: Code Assistance — Python for Economists
**Stability: Slow-moving**

Python for data analysis: pandas, statsmodels, linearmodels. Using AI to translate Stata/R workflows to Python. When Python is the right choice for economists (large datasets, ML, text data, APIs). What AI gets wrong (deprecated pandas syntax, incorrect econometric implementations).

- ~50 min, hands-on
- *Why slow-moving*: Python's data science ecosystem is relatively stable (pandas, numpy, scikit-learn). The specific libraries for economics (linearmodels, etc.) are less well-known to AI.
- *Update trigger*: Major pandas/ecosystem changes

### C5: Data Exploration & Cleaning
**Stability: Slow-moving**

Using AI to understand datasets: describing variables, identifying anomalies, generating summary statistics, detecting data quality issues. Guardrails: what to verify, what AI misses (context-dependent coding, survey design artifacts, merge issues). Using AI to write data documentation.

- ~50 min, hands-on (tool-agnostic: Stata, R, or Python)
- *Why slow-moving*: Data cleaning workflows are very stable. AI's ability to help will improve, but the core lesson (AI can suggest, you must verify against codebooks and context) is permanent.
- *Update trigger*: As AI gets better at data tasks, examples may need to be harder

### C6: Writing & Revision for Economists
**Stability: Stable**

Using AI for drafting, editing, restructuring arguments, improving clarity. Maintaining your voice and style. The "AI as copy editor, not ghostwriter" framework. Specific economist writing tasks: abstract writing, lit review paragraphs, results interpretation, referee response drafting. What AI does poorly (original argumentation, field-specific conventions, concision).

- ~50 min, no coding required
- *Why stable*: Good writing principles don't change. The skill of using AI as an editing tool (rather than a writing-replacement tool) is durable. Economics writing conventions are stable.
- *Update trigger*: Rarely — refresh examples occasionally

### C7: Math, Derivations, and Formal Reasoning
**Stability: Slow-moving**

Using AI to check proofs, work through optimization problems, verify algebra, understand intuition behind results. Where AI is strong (standard derivations, step-by-step algebra) and where it fails (novel proofs, subtle errors in multi-step reasoning, LaTeX formatting of complex expressions). Wolfram Alpha vs. LLMs for math.

- ~50 min, lightly technical
- *Why slow-moving*: Mathematical reasoning in LLMs is improving rapidly — today's failure examples may be tomorrow's successes. But the framework (use AI to check/explore, not to substitute for understanding) is stable.
- *Update trigger*: As math capabilities improve, refresh failure examples

### C8: Economic Modeling and Simulation
**Stability: Slow-moving**

Using AI to build simple economic models: supply/demand simulations, game theory payoff matrices, Monte Carlo experiments, agent-based models. From concept to code with AI assistance. Understanding what the AI-generated model actually assumes.

- ~75 min, hands-on (Python or R)
- *Why slow-moving*: Modeling concepts are stable. AI's ability to generate working simulations will improve. The critical skill (auditing assumptions) is permanent.
- *Update trigger*: Refresh as AI produces better simulations

### C9: Presentation and Data Visualization
**Stability: Slow-moving**

Using AI to create charts, improve slide design, generate visualization code (ggplot, matplotlib, Plotly). Design principles for economic data visualization. When AI-generated visualizations mislead. Accessibility considerations.

- ~50 min, hands-on
- *Why slow-moving*: Visualization principles are stable. Tool capabilities evolve. The lesson "don't blindly trust AI-generated charts" is permanent.
- *Update trigger*: New visualization tools or capabilities

### C10: Working with Text Data (NLP for Economists)
**Stability: Fast-moving**

Using AI to classify, summarize, and extract information from text data (surveys, policy documents, news articles). Embeddings for similarity and clustering. Sentiment analysis. When LLMs replace traditional NLP pipelines. Research applications in economics (classifying job ads, coding open-ended survey responses, analyzing policy text).

- ~75 min, hands-on (Python)
- *Why fast-moving*: LLM capabilities for text analysis are improving dramatically and rapidly. Best practices are shifting. The research applications are genuinely new.
- *Update trigger*: Every semester — this is an active research frontier

### C11: Causal Inference and AI
**Stability: Fast-moving**

AI-assisted causal inference: using LLMs to brainstorm identification strategies, evaluate exclusion restrictions, suggest robustness checks. ML methods for causal inference (causal forests, double ML, LASSO for variable selection). The boundary between AI-assisted reasoning and AI-generated analysis.

- ~75 min, moderately technical
- *Why fast-moving*: Causal ML is an active research area. LLM capabilities for causal reasoning are improving rapidly. Best practices haven't stabilized.
- *Update trigger*: As the literature evolves — this is a research frontier

---

## Track D: Instructor Resources

Modules designed for faculty/instructors who want to use AI in their teaching or adapt their courses. These are inherently slower to develop and depend on demand.

### D1: Building Interactive Demos with AI
**Stability: Fast-moving**

Using AI to create classroom demonstrations: supply/demand shifters, game theory simulations, regression visualization, market equilibrium animations. Tools: Shinylive, Observable JS, Streamlit, basic HTML/JS. From concept to working demo in 30 minutes.

- Format: Tutorial + example gallery
- *Why fast-moving*: AI's ability to generate working interactive content is improving rapidly. Today's workflow may be obsolete in a year. But the *demand* for good econ demos is permanent.
- *Update trigger*: Every semester
- *Strategy*: Maintain a gallery of working demos; update the "how to build these" process as tools evolve

### D2: AI-Assisted Assessment Design
**Stability: Slow-moving**

Rethinking problem sets, exams, and projects in an AI world. Design principles: test understanding, not recall; make AI use visible, not hidden; graduated AI autonomy across a semester. Using AI to generate and evaluate assessment items. Bloom's taxonomy in the AI era.

- Format: Guide + examples
- *Why slow-moving*: Pedagogical principles are stable. Specific strategies will evolve as we learn what works. The "graduated autonomy" framework is durable.
- *Update trigger*: Annually, as we accumulate experience

### D3: Syllabus Language and Course Policies
**Stability: Slow-moving**

Model AI policies for economics courses. Spectrum from "no AI" to "AI required." How to communicate expectations clearly. Handling edge cases and violations. Example policy language for different course types (intro, intermediate, capstone, methods).

- Format: Templates + commentary
- *Why slow-moving*: Institutional norms are still forming. Individual policies need updating as norms solidify. The template approach (choose your position on a spectrum) is durable.
- *Update trigger*: As disciplinary/institutional norms evolve

### D4: Adapting Existing Courses for AI
**Stability: Slow-moving**

A practical guide for instructors who want to integrate AI into an existing course without redesigning everything. Identifying which assignments to modify. Adding AI-literacy moments to existing content. The "minimal viable integration" approach.

- Format: Guide + checklist
- *Why slow-moving*: The principles of backward design and minimal integration are stable. Specific tool recommendations will change.
- *Update trigger*: Annually

### D5: Creating Reusable Demos and Simulations
**Stability: Fast-moving**

Step-by-step guides for building specific demonstrations: elasticity calculator, comparative advantage simulator, Phillips curve visualizer, regression diagnostics explorer. Designed so instructors can use them as-is or modify them.

- Format: Gallery of working demos with source code
- *Why fast-moving*: The tools for building these change rapidly. But the demos themselves, once built, are relatively stable if they use simple tech (HTML/JS).
- *Strategy*: Build in simple, durable tech stacks (plain JS, no heavy frameworks) so demos age well even if the build process changes

---

## Track E: Special Topics

Standalone modules that don't fit neatly into other tracks. Build these opportunistically based on demand or inspiration.

### E1: AI for Job Market Preparation
**Stability: Slow-moving**

Using AI for job/grad school applications: resume/CV review, cover letter drafting, interview preparation, research statement feedback. What AI does well (structure, clarity) and poorly (voice, field-specific conventions). Ethics of AI-assisted applications.

- ~30 min, no coding required
- *Why slow-moving*: Job market conventions change slowly. AI capabilities improve but the advice (use for polish, not substance) is durable.

### E2: AI for Research Proposals and Grant Writing
**Stability: Slow-moving**

Using AI to structure proposals, identify gaps, strengthen methodology sections, draft budgets. What reviewers can and can't detect. Field-specific conventions in economics.

- ~50 min, no coding required
- *Why slow-moving*: Grant writing conventions are very stable. AI's ability to help will improve, but the workflow is durable.

### E3: Replication and Reproducibility with AI
**Stability: Slow-moving**

Using AI to build and verify replication packages. Checking code against paper claims. Generating documentation. The role of AI in the replication crisis (both as helper and as risk). Version control for replication (connects to B2).

- ~50 min, hands-on
- *Why slow-moving*: Reproducibility standards are evolving but the direction is clear (more rigor, more documentation). AI's role as a replication helper is novel and growing.

### E4: Prompt Engineering for Research (Advanced)
**Stability: Fast-moving**

Advanced prompting techniques: chain-of-thought, few-shot learning, system prompts, structured output. When and why these matter. Building custom GPTs / Claude Projects for research workflows. Prompt libraries and templates.

- ~75 min, hands-on
- *Why fast-moving*: Specific techniques evolve as models change. Some techniques become unnecessary as models improve (e.g., chain-of-thought may be automatic in future models). The meta-skill of systematic prompting is more durable than any specific technique.
- *Update trigger*: With each major model generation

### E5: AI Tools for Teaching Assistants
**Stability: Fast-moving**

How TAs can use AI responsibly: grading assistance, generating feedback, creating practice problems, office hours support. Boundaries and policies. Efficiency without replacing the human element.

- ~30 min, no coding required
- *Why fast-moving*: TA tools and institutional policies are evolving rapidly. Grading-specific AI tools are emerging and changing.

### E6: The Economics of AI
**Stability: Slow-moving**

AI as an economic phenomenon: market structure of AI industry, labor market effects, productivity evidence, regulation, competition policy. Connecting AI developments to standard economics frameworks (externalities, public goods, market power, innovation incentives).

- ~75 min, no coding required
- *Why slow-moving*: The economic frameworks are stable, but the empirical evidence and market structure are evolving. This is a natural fit for an economics department but needs periodic updates.
- *Update trigger*: Major empirical studies, policy changes, market shifts

---

## Prioritization Matrix

### Recommended build order (balancing stability, usefulness, and uniqueness)

**Tier 1 — Build first** (stable, foundational, high value):
| Module | Stability | Why first |
|---|---|---|
| A1: What LLMs Do | Stable | ✅ Done. Everything builds on this |
| A2: Prompting | Stable | ✅ Done. Immediately useful to every student |
| A3: When AI Helps/Hurts | Stable | ✅ Done. Sets norms early |
| B1: Terminal Basics | Stable | Fills a real gap. Almost no econ programs teach this. Ages extremely well |
| B2: Git & GitHub | Stable | Same — foundational, unique, durable |
| A4: Verifying Output | Stable | Critical safety skill |

**Tier 2 — Build next** (high value, mostly stable):
| Module | Stability | Why next |
|---|---|---|
| C6: Writing & Revision | Stable | Every student writes. High immediate value |
| C2: Code Assistance (Stata) | Slow-moving | Immediately useful for your students |
| C5: Data Exploration | Slow-moving | Practical, easy to demonstrate |
| A5: AI Ethics/Econ | Slow-moving | Important framing, pairs well with A3 |

**Tier 3 — Build when inspired** (valuable, moderate maintenance):
| Module | Stability | Notes |
|---|---|---|
| C1: Lit Review | Slow-moving | Very practical, good demo potential |
| C3: Code (R) | Slow-moving | Expand audience beyond Stata shops |
| C7: Math & Derivations | Slow-moving | Good for methods-heavy courses |
| C8: Modeling & Simulation | Slow-moving | Fun to build, great demos |
| B5: APIs | Slow-moving | Powerful but niche audience |
| B6: Data Privacy | Slow-moving | Important but short — could fold into B3 or A7 |

**Tier 4 — Build on demand** (high maintenance or niche):
| Module | Stability | Notes |
|---|---|---|
| B3: AI Toolbox | Fast-moving | Necessary but requires constant updates |
| B4: Terminal AI | Fast-moving | Cool but very bleeding-edge |
| C10: Text Data/NLP | Fast-moving | Research frontier — exciting but high maintenance |
| C11: Causal Inference + AI | Fast-moving | Research frontier |
| E4: Advanced Prompting | Fast-moving | Will need constant revision |
| D1-D5: Instructor modules | Mixed | Build after student modules prove their value |
| E1-E6: Special topics | Mixed | Opportunistic |

---

## Maintenance Calendar

| Frequency | What to review |
|---|---|
| **Every semester** | B3 (tool landscape), B4 (terminal AI), C10-C11 (research frontiers), D1/D5 (demos), E4-E5 (advanced prompting, TA tools) |
| **Annually** | C1-C5, C7-C9 (workflow modules — refresh examples, update tool recommendations), A5/A7 (ethics/integrity — check for policy changes), D2-D4, E1-E3, E6 |
| **Rarely** | A1-A4 (foundations), B1-B2 (terminal/git), C6 (writing) — review every 2-3 years or on major paradigm shift |

---

## Module Count Summary

| Track | Count | Stability Mix |
|---|---|---|
| A: Foundations | 7 | 4 stable, 2 slow, 1 slow |
| B: Technical | 6 | 2 stable, 2 slow, 2 fast |
| C: Econ Workflows | 11 | 1 stable, 8 slow, 2 fast |
| D: Instructor | 5 | 0 stable, 3 slow, 2 fast |
| E: Special Topics | 6 | 0 stable, 4 slow, 2 fast |
| **Total** | **35** | **7 stable, 19 slow, 9 fast** |
