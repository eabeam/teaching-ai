# Lesson Plan: A3 — When AI Helps vs. Hurts Your Learning

## Module Overview

- **Title**: When AI Helps vs. Hurts Your Learning: Metacognition for the AI Era
- **Time estimate**: 30 min (tight, as written) / 50 min (expanded) / 75 min (workshop)
- **Prerequisites**: A1 recommended (understanding failure modes helps contextualize the 2x2), but not strictly required
- **Materials needed**:
  - Projector (for the 2x2 framework and examples table)
  - Printed or digital copies of the AI Audit worksheet
  - A simple task to demonstrate (a short problem set question or derivation)
  - Exercise worksheets from `exercises/a3/`:
    - `ai_audit_worksheet.md`

**Learning Objectives** (from module):

1. Distinguish between tasks where AI accelerates learning and tasks where it substitutes for learning
2. Apply the concept of "desirable difficulty" to AI use decisions
3. Develop a personal framework for when to reach for AI and when to struggle
4. Recognize the warning signs that AI is undermining your skill development

---

## 50-Minute Version (Lecture-Focused)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:05 | **Hook**: The with/without demo (see Live Demo Script). Give students a concrete task — e.g., "Interpret this regression coefficient: the coefficient on years_of_education is 0.08 in a log-wage regression." 3 minutes solo, then 3 minutes with AI. Brief show of hands: "Which attempt taught you more?" | Most students will say the solo attempt, even if the AI answer was better. That's the point. |
| 0:05-0:10 | **Desirable difficulty**: Define the concept. Walk through the 3 everyday examples (cramming vs. spaced practice, re-reading vs. self-testing, highlighting vs. summarizing). Then: "AI creates a new version of this problem." Introduce the fluency trap. | The fluency trap is the core concept. Say it explicitly: "Reading a clear AI explanation feels like understanding. It isn't." |
| 0:10-0:18 | **The 2x2 framework**: Display the matrix. Walk through 3-4 examples from the econ-major table. Ask students to categorize 1-2 additional tasks (e.g., "Writing an abstract" — core skill? Can you do it? Where does it go?). | The 2x2 is the tool students will actually use. Spend time here. The "danger zone" (core skill, you can do it) is where most misuse happens. |
| 0:18-0:22 | **When AI genuinely helps**: Quickly cover the 5 patterns (tutor, unsticking, connecting ideas, translation, checking work). Emphasize the prompt pattern for "unsticking": "I've tried X and Y. Give me a hint, not the answer." | Don't belabor this — students who did A2 will recognize good prompt patterns. |
| 0:22-0:28 | **Warning signs**: Cover all 4 signs. The automation paradox callout is powerful — skills atrophy, making you worse at catching errors when it matters most. | Ask: "How many of you have opened AI before even reading the question?" Pause. Let the silence do the work. |
| 0:28-0:40 | **Exercise: Your AI Audit**. Students fill out the audit table for the last week. Individual work, then pair discussion. Use `ai_audit_worksheet.md`. | Stress: "This is for you, not for a grade. Be honest." Circulate and glance — don't read over shoulders. |
| 0:40-0:48 | **Discussion**: Use Q1 ("Is AI like a calculator?") — great for surfacing assumptions. Or Q3 (ban AI vs. require AI) if you want a livelier debate. | Q1 generates the best discussion in intro courses. Q3 is better for upper-level. |
| 0:48-0:50 | **Wrap-up**: 4 takeaways. Introduce the personal policy template as a take-home reflection. | End with: "Be deliberate, not default." |

**If running short**: Cut "When AI genuinely helps" to a single example (the tutor pattern). Skip Q1 discussion and go straight to wrap-up.

**Skip entirely**: The "Developing Your Personal Policy" template section — assign it as take-home instead.

---

## 75-Minute Version (Workshop-Style)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:08 | **Hook**: Extended with/without demo. Use a slightly harder task — e.g., "Set up the first-order conditions for a consumer maximizing Cobb-Douglas utility subject to a budget constraint." 5 min solo, 3 min with AI. | Harder task makes the learning gap more visible. Students who rely on AI won't be able to start the solo version. |
| 0:08-0:15 | **Debrief the demo**: "What did you learn in each attempt? Where did you get stuck solo? Did the AI answer help you understand, or did you just read it?" Quick pair discussion, then 2-3 students share. | This debrief is the highest-impact moment. Students often admit the AI answer was "too easy" — they consumed it but can't reconstruct it. |
| 0:15-0:22 | **Desirable difficulty + fluency trap**: Same content as 50-min but with more discussion. Ask: "Give me an example from your own experience where easy learning didn't stick." | Students will volunteer examples: cramming for finals, copy-pasting notes, etc. Connects to their lived experience. |
| 0:22-0:32 | **The 2x2 framework**: Walk through the matrix. Then do a group categorization exercise: put 6-8 tasks on the board (mix of core/non-core, can/can't do). Students vote on where each goes. Discuss disagreements. | Disagreements are productive. "Is writing Stata code a core skill or not?" depends on the course and the student. Surface that. |
| 0:32-0:40 | **When AI helps + warning signs**: Cover both sections. Add the automation paradox. | Same as 50-min but with more time for the warning signs. |
| 0:40-0:55 | **AI Audit exercise (15 min)**: Full audit table. Then: students draft their personal AI policy using the template from the module (3 categories: use freely, use as tutor, do not use). Use `ai_audit_worksheet.md`. | The policy-drafting step makes the reflection concrete and actionable. |
| 0:55-0:68 | **Gallery walk or share-out**: Students share one item from each policy category. Discuss: where do policies differ? Why? Use Q2 (intro course vs. senior thesis) and Q4 (econ major vs. elective). | Differences in policy reveal differences in goals. An econ major and a CS minor taking econ should have different policies. |
| 0:68-0:75 | **Wrap-up**: 4 takeaways. Weekly check-in prompt: "Could I do last week's work without AI?" Suggest setting a calendar reminder. | If the course allows, assign the personal policy as a short submission (half-page). |

**Natural break point**: After the 2x2 exercise at 0:32 (if teaching back-to-back with A1 or A2).

---

## Live Demo Script

**Setup**: Prepare a specific task on a slide or write it on the board. Have your AI tool open but minimized.

1. Display the task: **"Interpret this regression coefficient: In a regression of log(wages) on years_of_education and controls, the coefficient on years_of_education is 0.08 and statistically significant at the 5% level. What does this mean in plain language?"**

2. Say: "Close your laptops. Put your phone down. You have 3 minutes. Write your interpretation on paper."

3. Set a timer. Let them struggle. This is intentional. Many will stare at the page. Some will get it partly right.

4. After 3 minutes, say: "Now open your AI tool. Ask it the same question. You have 3 minutes."

5. After 3 minutes, ask:
   - "How many of you got it right (or close) on your own?" (Some hands.)
   - "How many got a better answer from the AI?" (Most hands.)
   - "Here's the real question: **which attempt taught you more?**"

6. Let 2-3 students respond. Then say: "The struggle in the first 3 minutes is where the learning happened. The AI answer in the second 3 minutes felt easier — but you were reading, not thinking. That's the fluency trap."

**For the 75-min version**, use a harder task: *"Set up the Lagrangian for a consumer maximizing $U(x,y) = x^{0.5} y^{0.5}$ subject to $p_x x + p_y y = I$. Take the first-order conditions."* The point is the same, but the difficulty gap is more dramatic.

**What to expect**: Some students will push back ("I learned from reading the AI answer too"). That's fair. Respond: "Reading a good explanation can help. But can you reproduce it tomorrow without looking? That's the test."

---

## "If Students Ask..." FAQ

1. **"Isn't using AI the same as using a calculator?"**
   Partly. A calculator automates arithmetic — a skill most people have already mastered. AI automates reasoning and writing — skills you're still developing. The analogy works for tasks you've mastered (formatting, boilerplate). It breaks down for tasks you're learning. Would you let a calculator do your math homework in 3rd grade?

2. **"But in the real world, I'll always have access to AI."**
   Probably true. But in a job interview, a meeting with your advisor, an oral exam, or a client presentation, you need to think on your feet. The skills you build now are what you'll rely on when you can't look something up. Also: your ability to *use* AI well depends on understanding the domain (the Prompting Paradox from A2).

3. **"My professor says I can't use AI at all. Isn't that unrealistic?"**
   It might feel that way, but there's a good pedagogical reason: if the goal is to develop a core skill, the struggle is the learning. Your professor is protecting the "danger zone" in the 2x2. Once you've built the skill, you can use AI to do it faster. The restriction is temporary.

4. **"How do I know if something is a 'core skill' or not?"**
   Good rule of thumb: if it's assigned as homework, it's a core skill for that course. If you'd need to explain it in a job interview, it's a core skill. If you can't imagine ever doing it again after this course, it's probably in the "power tool" or "outsource" quadrant.

5. **"What if I'm just not smart enough to do it without AI?"**
   That's the desirable difficulty talking. Feeling stuck is not a signal that you can't do it — it's a signal that your brain is working. The discomfort is the learning. If you're genuinely stuck after a real attempt, use AI as a tutor (hints, not answers). But give yourself a real attempt first.

---

## Facilitation Notes

- **Exercise format**: The AI Audit is deeply personal — do it individually first, then pair-share. Do not do this as a group exercise or project the worksheet; students need to be honest about their AI use, which requires privacy.
- **If the AI tool is down or slow**: The demo can be done as a thought experiment: "Imagine you asked AI this question. What would you get? Now imagine you worked through it yourself. What's the difference in what you learned?" Less powerful than live, but the concept still lands.
- **Common sticking point**: Students struggle with the "core skill vs. not" distinction because it depends on context. Lean into this: "There's no universal answer. An intro student and a PhD candidate have different core skills. The 2x2 is a framework for *your* decision, not a rulebook."
- **Pro-AI students**: The hardest group for this module. They often feel judged. Frame it positively: "This module isn't anti-AI. It's about using AI *strategically* so you actually get the degree's worth of learning. Smart AI use requires knowing when NOT to use it."
- **Skeptical students**: They may agree too enthusiastically and miss the nuance. Push back gently: "There are real tasks where AI saves you hours and you lose nothing. The question is which tasks. Don't throw out the tool — calibrate it."
- **Sensitive moment**: Some students will realize they've been over-relying on AI. This can feel like being "caught." Normalize it: "Most of us default to the easier path. That's not a moral failing — it's how brains work. The audit is about noticing, not judging."
