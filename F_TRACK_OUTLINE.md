---
type: outline
project: teaching-ai
track: F
status: draft
created: 2026-03-24
---

# F-Track Outline: Faculty Quick Start

## Positioning

**Audience**: Faculty who have already installed an AI desktop app and want practical payoff quickly.

**What this track is for**: Personal productivity with real course files and documents.

**What this track is not**: A pedagogy sequence, a policy course, or a terminal tutorial.

**Core promise**: You do not need terminal skills to get substantial value. The app-first workflow is enough for most faculty use cases.

## Start Here

| Your situation | Start with |
|---|---|
| I have 15 minutes and want to see what the fuss is about | **F1: Your First Real Task** |
| I'm prepping a course and drowning in materials | **F2: Course Prep Power Hour** |
| It's grading season and I'm behind on feedback | **F3: Feedback at Scale** |
| I need an AI policy before students ask about it | **F4: Make Your Course AI-Ready** |

**Recommended entry point**: F1 — it takes 15 minutes and changes how you think about the rest.

---

## Track-wide Design Rules

- Platform-neutral by default; tool-specific steps appear only in tabsets or side notes
- App-first; no terminal required
- Short modules: 15-30 minutes
- Action-oriented; every module ends with a real task using the reader's own files
- Honest about failure modes, privacy limits, and review responsibility

---

## F1: Your First Real Task

**Subtitle**: Stop copy-pasting. Start pointing.

**Premise**: The first real unlock of a desktop AI app is that it can work from your files directly. This module gives faculty one concrete success experience so the difference from browser chat is immediately obvious.

**This is the recommended entry point for the F-track.**

**Time estimate**: 15 minutes

**What you need**:
- One AI desktop app installed
- One real file you already use for teaching
- 15 uninterrupted minutes

**Learning objectives**:
- See why file-based workflows beat copy-paste for ordinary faculty tasks
- Learn the basic moves: attach a file, attach a folder, drag-and-drop, ask for a revision
- Complete one real teaching task from start to finish
- Notice the quality-control checks needed before using the output

**Section structure**:

### 1. The copy-paste trap
- Browser chat feels useful at first, but the workflow breaks down once formatting, multiple documents, or longer files enter the picture
- Copy-paste strips context, introduces formatting errors, and makes iteration tedious
- The key shift is simple: stop moving text into the AI; point the AI at the file instead

### 2. What "point it at your files" means
- Show the three common patterns: file picker, drag-and-drop, opening a project folder
- Explain that the reader does not need to understand anything technical about "context"
- Define the practical rule: if the file matters, give the app the file instead of a mangled excerpt

### 3. Pick one and go
- Four concrete examples, each with a before/after comparison:
  1. Turn an old exam into a study guide
  2. Generate a rubric from an assignment description
  3. Draft discussion questions from a reading PDF
  4. Summarize student evaluations into themes
- At least one example shows a concrete before/after prompt pair. For instance:
  - **Browser chat (copy-paste)**: You paste a few exam questions, lose the formatting, and type "make a study guide." The AI has no idea about the course level, the other questions, or how topics connect across the exam.
  - **Desktop app (file-based)**: You attach the full exam PDF and say: "Create a study guide for students preparing for this exam. Organize by topic, flag which questions test application vs. recall, and suggest what to review for each section." The AI sees the whole document — structure, notation, difficulty progression — and produces something you can actually hand out.
- Each example should make the quality gap obvious, not just the convenience gap

### 4. What just happened
- The core lesson: **better context → better output**. You didn't write a fancier prompt. You gave the AI the actual file. That's it.
- Revision was easier because the app kept the file in view — you could say "make section 3 harder" without re-explaining what section 3 was
- The workflow killed the copy-paste tax: no reformatting, no truncation, no "here's the rest of the document"
- This is not a trick. It's the reason these apps exist.

### 5. What can go wrong
- The AI may overgeneralize, miss course-specific nuance, or flatten tone
- Summaries can miss edge cases or overstate a pattern
- The reader still checks for accuracy, emphasis, and appropriateness

**Try it now**:
- Pick one file from this semester and ask the app to produce something you would actually use this week
- Revise once by asking for a different format, tone, or level of detail
- Keep or discard the result based on whether it saved real time

**Tool-specific note**: Use tabsets in the eventual `.qmd` for attaching files in Claude Code, Codex, and ChatGPT desktop.

---

## F2: Course Prep Power Hour

**Subtitle**: First drafts in minutes, not hours

**Premise**: Faculty course prep often starts from a pile of half-reusable materials. AI is most helpful here as a fast first-draft engine that works from last semester's files, learning goals, and readings.

**Time estimate**: 25 minutes

**What you need**:
- One set of existing course materials
- A few learning objectives, notes, or a reading assignment
- An AI app that can see multiple files in the same conversation

**Learning objectives**:
- Use AI to generate a working draft from existing teaching materials
- Adapt old materials rather than starting from a blank page
- Build lightweight quality-control checks into prep workflows
- Recognize the most common ways AI course prep drifts off target

**Section structure**:

### 1. The right mindset: directing, not delegating
- Faculty remain the subject-matter expert and final editor
- The AI is a fast intern: useful for momentum, not trusted judgment
- A "working draft you can edit" is the right success standard

### 2. Build a problem set from objectives plus notes
- Attach lecture notes and learning objectives
- Ask for questions at a specified level of difficulty
- Request variety: conceptual, applied, short-answer, computation

### 3. Create an answer key with common mistakes and partial-credit notes
- Use the draft problem set as input
- Ask for common misconceptions, partial-credit logic, and brief explanations
- Emphasize that the instructor verifies every solution before use

### 4. Adapt materials across sections, semesters, or textbooks
- Turn last semester's worksheet into a new version
- Swap examples, change readings, or raise/lower difficulty
- Preserve structure while updating content

### 5. Turn a paper into a "read this for class" guide
- Attach a PDF and ask for discussion prompts, a reading roadmap, and key terms
- Ask for the output in a student-facing format
- Use this to reduce prep friction, not to replace reading the paper

### 6. Quality control
- Check difficulty, terminology, answer accuracy, and fit with course goals
- Watch for invented details, wrong emphasis, and unhelpful verbosity
- Compare the draft against what students actually need to practice
- **Concrete check**: Ask the AI to solve the problem set you just generated. Compare its solutions to your answer key. If the AI gets its own questions wrong, students will too — and not in the way you intended

### 7. Red flags
- Wrong level of difficulty
- Generic wording that ignores your course voice
- Plausible-but-incorrect answers
- Answers that are correct but use methods, notation, or concepts you haven't taught yet
- Misalignment between learning goals and generated tasks

**Try it now**:
- Load one lecture note file and one assignment or objective file
- Ask for a 20-minute in-class activity or short problem set
- Edit the result until it feels like something you would actually hand out

**Tool-specific note**: Use tabsets in the eventual `.qmd` for loading multiple course files into the app.

---

## F3: Feedback at Scale

**Subtitle**: Better feedback, less grading dread

**Premise**: Faculty do not need AI to assign grades. They can use it to organize, standardize, and accelerate feedback so comments are more useful and less exhausting to produce.

**Time estimate**: 20 minutes

**What you need**:
- A rubric, assignment instructions, or sample feedback comments
- One or a few pieces of student work you are allowed to share with the tool
- A clear understanding of your institution's privacy rules

**Learning objectives**:
- Distinguish feedback support from auto-grading
- Generate reusable feedback language anchored to rubric dimensions
- Use AI to identify recurring patterns across submissions
- Recognize privacy and transparency constraints before uploading student work

**Section structure**:

### 1. What this is not
- Not score assignment
- Not unsupervised grading
- Not outsourcing judgment about student learning

### 2. What this is
- Drafting feedback starters
- Turning rubrics into reusable comment banks
- Spotting recurring problems across a set of assignments
- Producing follow-up guidance for students

### 3. Generate feedback templates from your rubric
- Attach the rubric and ask for comment stems by dimension
- Request versions for strong, mixed, and weak performance
- Keep the tone specific and respectful rather than canned

### 4. Draft individualized feedback starters
- Use rubric dimensions plus a short summary of the student's work
- Generate a first paragraph or two that you then edit
- Preserve instructor voice and course priorities

### 5. Identify common patterns across assignments
- Ask for themes: what are students consistently misunderstanding
- Use those patterns to plan reteaching, FAQs, or a review sheet
- This is also a **teaching diagnostic**: if 60% of students miss the same thing, that's a signal about your instruction or materials, not just their preparation. AI can surface the pattern; you decide what it means.
- Keep an eye out for the AI overstating how common a pattern is

### 6. Create "what to review" guides
- Turn repeated issues into a short study guide or class announcement
- Focus on next-step advice students can act on

### 7. The ethical line
- Be clear with yourself and, where appropriate, with students about your process
- Faculty judgment remains central
- If the institution has guidance, follow it

### 8. FERPA and privacy
- Not all tools are equally appropriate for student work. The key distinction: **enterprise/education agreements** (your data is not used for training, access is restricted) vs. **consumer tools** (fewer guarantees).
- Check whether your institution has an enterprise agreement. For example, UVM Copilot has enterprise protections; a free ChatGPT account does not.
- When in doubt: de-identify student work before uploading (remove names, IDs, course section identifiers)
- If the privacy status is unclear, do not upload student materials until you verify policy
- This is not a reason to avoid AI for feedback — it's a reason to use the right tool

**Try it now**:
- Use one rubric to generate a small feedback bank for three common performance patterns
- If privacy rules allow it, test one anonymized submission and edit the result heavily
- Draft one class-wide "what to review before the next assignment" note

**Tool-specific note**: Use tabsets in the eventual `.qmd` for sharing rubrics and anonymized student work in different apps.

---

## F4: Make Your Course AI-Ready

**Subtitle**: Use AI to think about AI in your course

**Premise**: This module is meta by design. Faculty can use AI to pressure-test their own syllabus, assignment design, and policy language before students do it for them.

**Time estimate**: 25 minutes

**What you need**:
- Your syllabus or assignment sheet
- One assignment you currently use
- A willingness to revise policy language or assignment structure

**Learning objectives**:
- Audit course documents for missing or unclear AI guidance
- Use AI to test whether current assignments are vulnerable to shallow AI completion
- Draft policy language in your own voice
- Decide whether a given assignment should become more AI-resistant or more AI-integrated

**Section structure**:

### 1. Audit your syllabus
- Ask the AI what is missing, vague, or contradictory in the current policy language
- Look for places where students could reasonably say they did not know the rules

### 2. The policy spectrum
- Ban, permit, require
- Clarify that the choice depends on course goals, not ideology
- Ask the AI to compare what each approach would imply in practice

### 3. Test your assignments
- Paste or attach one assignment and ask: could a student get a strong grade from a shallow AI workflow?
- Identify where the current task invites generic output
- Use the answer as a diagnostic, not as an accusation
- Important flip side: some assignments are *fine* to be AI-assisted — and recognizing that is part of the exercise. Not everything needs to be AI-proof. The goal is intentional design, not blanket resistance

### 4. Redesign one assignment
- Choose either AI-resistant or AI-enhanced (both are valid — the choice depends on the learning goal)
- AI-resistant options: process evidence, oral defense, local data, staged drafts, reflection on decisions
- AI-enhanced options: explicit AI-use documentation, verification logs, critique-and-revise tasks, "use AI to generate X, then evaluate whether X is correct"
- Most existing resources lean heavily on AI-resistant strategies. The AI-enhanced path is underexplored and often more honest about how students will actually work

### 5. Draft guidelines in your voice
- Use your current syllabus tone as a model
- Ask for short, direct language rather than policy boilerplate
- Keep room for course-specific examples

### 6. Common objections and responses
- "Students will use it anyway"
- "I do not have time to redesign everything"
- "This will vary too much by course"
- Use the AI to brainstorm tradeoffs without letting it decide for you

### 7. What can go wrong
- Overly broad policy language
- Rules that are impossible to enforce
- Assignment redesign that adds busywork rather than learning value
- Letting the AI produce generic policy text with no connection to your course

**Try it now**:
- Attach one syllabus or assignment sheet
- Ask the AI to identify the three biggest ambiguity points in your current AI guidance
- Revise one paragraph of policy or redesign one assignment element

---

## Companion Page: When to Move to the Terminal

**Type**: Standalone reference page, not a full module

**Tone**: Reassuring, not recruiting

**Purpose**: Help faculty understand that the desktop app is enough for most use cases while naming the situations where terminal workflows become worthwhile.

**Structure**:

### 1. The app is enough
- Lead with the main reassurance: most faculty do not need the terminal
- Name the common app-first wins: document drafting, summarizing, course prep, brainstorming, feedback support

### 2. Signs you might want more
- "I keep doing the same thing to dozens of files" -> batch processing
- "I wish this were part of my Stata or R workflow" -> command-line integration
- "I want to track what changed and why" -> version control
- "I'm building something students will use" -> development tools
- "I want finer control over what the AI sees" -> context management

### 3. Signs the app is the right choice
- One-off document tasks
- Anything centered in Word or Google Docs
- Quick Q&A and brainstorming
- Tasks where file picker or drag-and-drop already works well

### 4. The bridge to B1
- If the "want more" list feels familiar, start with `B1: Terminal Basics`
- Set expectations honestly: one module is enough to tell whether the terminal is worth pursuing
- The goal is not conversion; it is informed choice

### 5. What terminal-based AI looks like
- Focus on the **workflow**, not the interface: "You type a question in plain English. The AI reads your project files, suggests edits, and you approve or reject each one. It's a conversation — just in text instead of a chat window. The difference is that it can touch your files directly, run your code, and remember the whole project structure."
- Brief description plus 2-3 screenshots or annotated examples later in the `.qmd` build
- Emphasize that it is not "harder" — it is different, and it pays off for different tasks

**Try it now**:
- Ask yourself whether you have a real repeat task that the app handles poorly
- If yes, queue `B1: Terminal Basics`; if not, keep using the app without guilt

---

## Implementation Notes for Build Phase

### Tabsets

Use Quarto `panel-tabset` blocks only where click-by-click steps genuinely diverge:

- F1: attaching files / opening folders
- F2: loading multiple course materials
- F3: sharing rubrics and anonymized student work

F4 should stay mostly tool-agnostic and avoid interface detail unless clearly needed.

### Companion Resources Page

Build `modules/resources.qmd` later as a living, annotated link page with these categories:

- AI desktop apps
- Web-based AI tools
- Academic AI tools
- AI policy resources
- Learning more
- Privacy and data

Each entry should include:
- Name
- One-sentence description
- Link
- One-line "when to use this" note

Flag the page clearly as a semester-refresh item.

Cross-link back to F-track modules where relevant (e.g., "AI desktop apps" section links to F1; "AI policy resources" links to F4; "Privacy and data" links to F3's FERPA section).
