# Instructor Guide: Adopting AI Literacy for Economists

**Who this is for**: Economics instructors at any institution who want to incorporate AI literacy modules into their courses. You do not need to be at UVM, use Stata, or teach any particular course. These modules are open (CC-BY 4.0) and designed to be mixed and matched.

**Time to read**: ~15 minutes.

---

## Overview

This site provides 10 self-contained modules organized into three tracks:

| Track | Modules | Focus | Coding? |
|-------|---------|-------|---------|
| **A: Foundations** | A1, A2, A3 | What AI is, how to use it, when to use it | No |
| **B: Technical** | B1, B2 | Terminal and Git skills for economists | Hands-on |
| **C: Econ Workflows** | C1, C2, C3, C4, C5 | AI applied to lit review, code, data, writing, math | Varies |

Every module can stand alone. There are no hard prerequisites. But if you're assigning multiple modules, the dependency graph below will help you sequence them effectively.

---

## Module Dependency Graph

```
A1: What LLMs Do
  ↓ (recommended)
A2: Prompting
  ↓ (recommended)
A3: When AI Helps/Hurts

B1: Terminal Basics
  ↓ (recommended)
B2: Git & GitHub

A1 or A3 ─ ─ ─ (soft prereq) ─ ─ ─→ C1, C2, C3, C4, C5
```

### What the arrows mean

- **A1 → A2 → A3**: These build on each other conceptually. A1 explains the mechanism (token prediction), A2 builds on that to teach prompting, and A3 uses both to develop metacognitive judgment. Teaching them in order is recommended but not required. Each module recaps the essential ideas from prior modules.

- **B1 → B2**: B2 (Git) assumes students can navigate a terminal. If students have never used the command line, teach B1 first. If your students are comfortable opening a terminal and typing `cd`, `ls`, and `pwd`, you can skip B1 or assign it as pre-work.

- **A1 or A3 as soft prerequisites for C-track**: The C-track modules (lit review, code, data, writing, math) all apply AI to economics workflows. They are more effective when students already understand why AI produces confident-but-wrong output (A1) and when AI use helps vs. hurts learning (A3). But each C module re-introduces these ideas in its domain-specific context, so students who missed A1/A3 will still follow along.

### The bottom line

Every module **can** stand alone. If you only have one class session, pick any module that fits your course. The dependency graph helps you sequence, but it does not create gatekeeping.

---

## Suggested Sequencing by Course Type

### Principles of Micro/Macro (1--2 sessions)

| Session | Module | Time | Rationale |
|---------|--------|------|-----------|
| 1 | A1: What LLMs Do | 50 min | Build accurate mental models before students use AI all semester |
| 1 or 2 | A3: When AI Helps/Hurts | 30 min | Set norms for AI use in the course early |

**Total**: ~80 min (fits in two 50-min classes or one 75-min session + homework).

**Why these**: Principles students need to understand what AI is and develop judgment about when to use it. They don't need code assistance or technical skills yet.

### Intermediate Micro/Macro (2--3 sessions)

| Session | Module | Time | Rationale |
|---------|--------|------|-----------|
| 1 | A1: What LLMs Do | 50 min | Foundation |
| 2 | A3: When AI Helps/Hurts | 30 min | Metacognition |
| 2 or 3 | C5: Math & Derivations | 50 min | Directly relevant: using AI to check optimization, comparative statics |

**Total**: ~130 min.

**Why C5**: Intermediate courses are math-heavy. C5 teaches students to use AI for intuition and LaTeX formatting while building verification habits for derivations.

### Econometrics (3--5 sessions)

| Session | Module | Time | Rationale |
|---------|--------|------|-----------|
| 1 | A1: What LLMs Do | 50 min | Foundation |
| 2 | A2: Prompting | 50 min | Prompt quality is critical for code generation |
| 3 | A3: When AI Helps/Hurts | 30 min | Set norms |
| 3 or 4 | C2: Code Assistance | 50 min | Core module: debugging, translation, silent errors |
| 5 (optional) | C3: Data Exploration | 50 min | AI for data documentation and cleaning audits |

**Optional add-ons** (if you have more time):

| Session | Module | Time | Rationale |
|---------|--------|------|-----------|
| 4 | B1: Terminal Basics | 75 min | If students need command-line skills for the course |
| 5 | B2: Git & GitHub | 75 min | If students will collaborate on code or submit replication packages |

**Total**: 180--380 min depending on selections.

### Senior Seminar / Research Methods (4--6 sessions)

| Session | Module | Time | Rationale |
|---------|--------|------|-----------|
| 1 | A1: What LLMs Do | 50 min | Foundation |
| 2 | A2: Prompting | 50 min | Essential for research-oriented AI use |
| 3 | A3: When AI Helps/Hurts | 30 min | Critical for students writing theses |
| 3 or 4 | C1: Lit Review & Synthesis | 50 min | Verification-first approach to AI-assisted literature review |
| 4 or 5 | C2: Code Assistance | 50 min | Debugging and code review for research code |
| 5 or 6 | C4: Writing & Revision | 50 min | AI as revision partner, maintaining voice |

**Total**: ~280 min.

**Why this set**: Research-oriented students need the full foundation (A1--A3), plus the three C-track modules most relevant to producing a research paper: finding literature, writing code, and revising prose.

### Standalone AI Workshop (full day, ~6 hours)

| Block | Module | Time |
|-------|--------|------|
| Morning 1 | A1: What LLMs Do | 50 min |
| Morning 2 | A2: Prompting | 50 min |
| Morning 3 | A3: When AI Helps/Hurts | 30 min |
| *Break* | | 15 min |
| Afternoon 1 | Pick 2 from C-track based on audience | 50 min each |
| Afternoon 2 | Discussion and personal AI policy development | 30 min |

**How to choose the C modules**: Pick based on your audience's primary work:
- Applied micro / empirical researchers → C1 (Lit Review) + C2 (Code Assistance)
- Theory-oriented → C4 (Writing) + C5 (Math)
- Methods / econometrics → C2 (Code Assistance) + C3 (Data Exploration)
- Mixed → C1 (Lit Review) + C4 (Writing)

---

## Minimum Viable Subsets

If you have limited time, here are the smallest useful combinations:

| Available time | Modules | What students get |
|----------------|---------|-------------------|
| **One session** (50--80 min) | A1 + A3 | Mental model for AI + metacognitive framework for when to use it |
| **Two sessions** (~130 min) | A1 + A3 + one C module | Foundation + one applied domain (pick the C module most relevant to your course) |
| **Three sessions** (~180 min) | A1 + A2 + A3 + one C module | Full foundations + one applied domain |
| **One session, applied focus** | Any single C module | If students already have AI experience, jump straight to a workflow module. Each C module recaps enough foundation to work standalone. |

---

## Software & Account Requirements

| Module | AI Tool Access | Terminal | Git | Stata or R | GitHub Account |
|--------|---------------|----------|-----|------------|----------------|
| A1: What LLMs Do | Required | -- | -- | -- | -- |
| A2: Prompting | Required | -- | -- | -- | -- |
| A3: When AI Helps/Hurts | Helpful but not required | -- | -- | -- | -- |
| B1: Terminal Basics | -- | Required | -- | -- | -- |
| B2: Git & GitHub | -- | Required | Required | -- | Required |
| C1: Lit Review | Required | -- | -- | -- | -- |
| C2: Code Assistance | Required | -- | -- | Helpful (examples in Stata; R section included) | -- |
| C3: Data Exploration | Required | -- | -- | Helpful (examples in Stata; R alternatives shown) | -- |
| C4: Writing & Revision | Required | -- | -- | -- | -- |
| C5: Math & Derivations | Required | -- | -- | -- | -- |

**AI tool access**: Any general-purpose LLM will work: ChatGPT, Claude, Gemini, Microsoft Copilot, institutional AI tools, etc. Students do not need paid accounts; free tiers are sufficient for all exercises.

---

## Pre-Class Setup Checklist

### Before B1 (Terminal Basics)

**Mac students**:
- [ ] Locate Terminal.app (Applications > Utilities, or Cmd+Space and type "Terminal")
- [ ] Open it and type `pwd` to verify it works
- No installation required -- macOS ships with a terminal.

**Windows students** (choose one):
- [ ] **Option A -- Git Bash** (easier): Install [Git for Windows](https://gitforwindows.org/). This provides both Git and a Unix-like terminal.
- [ ] **Option B -- WSL** (more powerful): Install Windows Subsystem for Linux via [Microsoft's guide](https://learn.microsoft.com/en-us/windows/wsl/install). Recommended for students who plan to do more computational work.

**Suggestion**: Send setup instructions at least one week before the session. Budget 5--10 minutes of class time for troubleshooting.

### Before B2 (Git & GitHub)

- [ ] Complete B1 setup (terminal access)
- [ ] Install Git:
  - Mac: Run `xcode-select --install` in the terminal (installs Git with Xcode Command Line Tools)
  - Windows: Comes with Git for Windows (if using Git Bash) or install via `sudo apt install git` in WSL
- [ ] Verify: run `git --version` in the terminal
- [ ] Create a free [GitHub](https://github.com) account
- [ ] Configure Git identity:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@university.edu"
  ```

**Authentication note**: Students will need to authenticate with GitHub to push commits. The simplest approach is a personal access token (Settings > Developer settings > Personal access tokens on GitHub). SSH keys are more permanent but harder to set up in class. Consider a brief setup guide or office hours session before the B2 module.

---

## Customizing Institutional References

### How to swap the UVM Copilot reference

Module A1 contains a reference to UVM's institutional AI tool in the exercise section:

> Try each of these with your preferred AI tool (UVM Copilot at [go.uvm.edu/copilot](https://go.uvm.edu/copilot), or another tool)

**To adapt**: Replace the parenthetical with your institution's equivalent. For example:

> Try each of these with your preferred AI tool ([YourUniversity]'s [ToolName] at [URL], or another tool such as ChatGPT or Claude)

If your institution does not provide an enterprise AI tool, simply remove the institutional reference:

> Try each of these with your preferred AI tool (ChatGPT, Claude, Gemini, or another tool)

The `about.qmd` page also has a "UVM Context" section describing UVM's enterprise Microsoft Copilot setup. Replace or remove this section to describe your own institution's AI tool landscape.

### Other institution-specific content

- The `about.qmd` page lists Emily Beam / University of Vermont as the creator. Add your own attribution alongside or fork the project.
- B2 (Git) uses `your.email@uvm.edu` in the Git config example. Replace with your institution's email domain.

---

## How Exercises Work

Every module includes at least one exercise. Exercise materials are stored in `exercises/<module>/` (e.g., `exercises/a1/`, `exercises/c2/`).

### Structure

- Exercises are embedded in the module text with clear step-by-step instructions.
- Where exercises require downloadable materials (datasets, code files, worksheets), they are in the corresponding `exercises/` subdirectory.
- Answer keys and instructor notes are provided where applicable.

### Delivery formats

Exercises can be run in any of these modes:

| Format | Best for | Notes |
|--------|----------|-------|
| **Individual** | Homework, pre-class prep | Students work through at their own pace |
| **Pairs** | In-class workshops | Think-pair-share; one person drives, one evaluates |
| **Instructor-led demo** | Large lectures, time-constrained sessions | Instructor projects the AI tool and walks through the exercise with class input |
| **Small group** | Discussion-heavy modules (A3, C4) | Groups of 3--4 compare their AI outputs and discuss |

### Tips for in-class exercises

- **A1 exercises** (failure mode tests): Work well as live demos. The "aha moment" when a fabricated citation looks real is very effective projected on screen.
- **A2 exercises** (prompt makeover): Have students bring a real question from their coursework. Comparing "before" and "after" prompts with live AI output is compelling.
- **B1/B2 exercises** (terminal and Git): These require students to follow along on their own machines. Go slowly. Budget time for troubleshooting.
- **C1 exercises** (lit review): The verification step is the learning moment. Have students actually check citations in Google Scholar during class.
- **C2 exercises** (debugging): Designed so that AI catches some bugs students miss and vice versa. The comparison is the point.
- **C3 exercises** (data cleaning evaluation): The class discussion about different AI tools making different cleaning decisions is usually the most productive part.
- **C4 exercises** (writing revision): Most effective when students bring their own writing. The contrast between broad rewrite and targeted edit is striking.
- **C5 exercises** (math verification): Parts 3--4 (introducing intentional errors) consistently produce surprising results that drive good discussion.

---

## Module Quick Reference

| Module | Time | Coding? | Key Takeaway |
|--------|------|---------|--------------|
| A1: What LLMs Do | 50 min | No | LLMs predict tokens, not truth. Failure modes follow from the mechanism. |
| A2: Prompting | 50 min | No | Clear prompts = clear thinking. Iterate, don't optimize. |
| A3: When AI Helps/Hurts | 30 min | No | Use the 2x2: core skill vs. not, can do vs. can't yet. Be deliberate. |
| B1: Terminal Basics | 75 min | Yes (terminal) | `pwd`, `ls`, `cd`, `grep`, pipes. The foundation for everything else. |
| B2: Git & GitHub | 75 min | Yes (terminal + Git) | Clone, add, commit, push, pull. Version control is a research integrity tool. |
| C1: Lit Review | 50 min | No | AI is a synthesis tool, not a sourcing tool. Verify every citation. |
| C2: Code Assistance | 50 min | Yes (Stata/R) | AI is better at reviewing code than writing it. Silent errors are the real risk. |
| C3: Data Exploration | 50 min | Yes (Stata/R) | Exploration = safe. Cleaning decisions = yours. Use AI as auditor, not decision-maker. |
| C4: Writing & Revision | 50 min | No | The sweet spot is revision, not generation. Writing is thinking. |
| C5: Math & Derivations | 50 min | No (math) | AI math looks confident whether or not it's correct. Build verification habits. |

---

## License

All materials are licensed [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to use, adapt, and redistribute with attribution.

Suggested citation:

> Beam, Emily. (2026). *AI Literacy for Economists*. University of Vermont. https://github.com/eabeam/teaching-ai. Licensed CC-BY 4.0.
