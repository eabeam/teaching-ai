# Lesson Plan: A2 — Prompting as Problem Specification

## Module Overview

- **Title**: Prompting as Problem Specification: Clear Prompts = Clear Thinking
- **Time estimate**: 50 min (tight) / 75 min (workshop)
- **Prerequisites**: A1 (What LLMs Actually Do) — students need to understand next-token prediction and failure modes
- **Materials needed**:
  - Projector with live internet access to an AI chat tool
  - Three versions of the IV prompt (from the module) ready to paste
  - Exercise worksheets from `exercises/a2/`:
    - `prompt_makeover_worksheet.md`
    - `prompt_log_template.md`

**Learning Objectives** (from module):

1. Explain why prompt quality determines output quality (and why this is not obvious)
2. Apply a structured framework (ROCS) for writing effective prompts
3. Diagnose common prompt failures and fix them
4. Use iterative prompting to refine outputs rather than starting over

---

## 50-Minute Version (Lecture-Focused)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:05 | **Hook**: Run the 3-version IV demo live (see Live Demo Script). Show Version 1 response. Ask: "Is this useful?" (Students say no/meh.) Then show Version 3 response. | The contrast is the point. Don't explain yet — let the difference speak. |
| 0:05-0:10 | **Core idea**: "Writing a good prompt is the same skill as specifying a research question." Walk through the identification strategy analogy. Show the vague vs. precise research question example. | This reframes prompting as a thinking skill, not a tech skill. Students who think prompting is beneath them will engage. |
| 0:10-0:18 | **ROCS framework**: Role, Objective, Constraints, Specifics. Show the table. Walk through one example applying all four. Emphasize: "This is a diagnostic tool, not a formula." | Spend 1 min on the "when to keep it simple" section. Simple questions need simple prompts. |
| 0:18-0:25 | **Common failures**: Cover Failures 1-2 (Blank Canvas, Implicit Assumption) in detail. Mention 3-4 briefly. For each, show the bad prompt and the fix side by side. | Skip Failure 4 (Leading Question) if short on time — it was covered in A1 under sycophancy. |
| 0:25-0:35 | **Exercise: Prompt Makeover**. Students rewrite 2 of the 4 "before" prompts from the module using ROCS. Then test both versions (before and after) in their AI tool. Use `prompt_makeover_worksheet.md`. | Assign prompts 1+2 to half the class, 3+4 to the other half. Saves time and creates variety for discussion. |
| 0:35-0:45 | **Discussion**: Ask 2-3 students to share their before/after and the difference in output quality. Use Q3 ("Think of a time you got a bad response — what was missing?") to generalize. | The comparison is the evidence. Let students convince each other. |
| 0:45-0:50 | **Wrap-up**: The Prompting Paradox ("The better you understand a topic, the better your prompts"). Key takeaways. Introduce `prompt_log_template.md` for ongoing use. | End with: "The skill isn't 'prompting.' The skill is clear thinking. AI just makes the feedback loop visible." |

**If running short**: Cut common failures to just Failure 1 (Blank Canvas) as a single example. Skip the discussion and go straight to wrap-up.

**Skip entirely**: The iterative prompting section (Rounds 1-3 lit summary example). Valuable but not essential for the 50-min version — students will discover iteration naturally.

---

## 75-Minute Version (Workshop-Style)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:07 | **Hook**: Same 3-version demo, but run all three versions live with the class watching. Ask students to predict which will get the best response before running them. | The prediction step creates engagement. Students are often surprised that Version 2 (not Version 3) sometimes wins for simpler questions. |
| 0:07-0:15 | **Core idea + ROCS framework**: Same content as 50-min, but with more examples. Ask students to identify which ROCS component is missing from each of the 4 "common failures." | Making students diagnose the failures using ROCS reinforces the framework. |
| 0:15-0:25 | **Common failures (all 4)**: Walk through each with the before/after. For Failure 4 (Leading Question), connect back to A1's sycophancy discussion. | This section pairs naturally with A1. If students did A1 recently, they'll make the connection themselves. |
| 0:25-0:35 | **Iterative prompting**: Walk through the 3-round lit summary example. Demonstrate iteration live if time permits — start with a weak prompt, refine twice based on what comes back. | Key message: "Iteration > perfection. Three rounds of decent beats one round of perfect." |
| 0:35-0:55 | **Full Prompt Makeover exercise (20 min)**: Students rewrite all 4 "before" prompts. Test before and after in AI tool. Then: bring a real question from their own coursework, write a prompt using ROCS, test it, revise once. Use both `prompt_makeover_worksheet.md` and `prompt_log_template.md`. | The "bring your own question" step is the highest-value activity. Circulate and coach. |
| 0:55-0:68 | **Share and discuss**: 3-4 students project their before/after (from the real question, not the worksheet). Class identifies which ROCS components improved. Use Q2 (prompting vs. research questions) and Q4 (risks of getting too good at prompting). | Q4 is underrated: if outputs look polished, students stop evaluating critically. This connects to A1 and A3. |
| 0:68-0:75 | **Wrap-up**: Prompting Paradox. 4 takeaways. Distribute `prompt_log_template.md` for ongoing use. | Optionally: assign the prompt log as a low-stakes ongoing assignment. |

**Natural break point**: After the iterative prompting section at 0:35.

---

## Live Demo Script

**Setup**: Open your AI tool (projected). Have three prompts pre-typed in a notes app, ready to paste.

1. Say: "I'm going to ask the AI the same question three different ways. Before I run each one, tell me: what do you think the response will look like?"

2. **Paste Version 1**: `"Tell me about instrumental variables."`
   - Run it. Skim the output together. Ask: "Is this useful to you right now? What level is it pitched at? What's missing?"
   - Expected response: generic, textbook-level, no concrete example or too basic.

3. **Paste Version 2**: `"Explain instrumental variables to an upper-level undergraduate economics student who understands OLS and omitted variable bias but hasn't seen IV before. Use a concrete example."`
   - Run it. Compare to Version 1. Ask: "What improved? What ROCS components did I add?" (Answer: Role/Context, Constraints)

4. **Paste Version 3**: `"I'm an econ major working on a paper about the effect of immigration on wages. I want to use an instrumental variable approach but I'm struggling to think of valid instruments. Can you: 1. Explain what makes an instrument valid (relevance + exclusion restriction) in plain language 2. Suggest 2-3 instruments that have been used in the immigration-wages literature 3. For each, explain the argument for why the exclusion restriction might or might not hold"`
   - Run it. Compare to both previous versions. Ask: "Which response would you actually use? What changed?"

5. Wrap up: "The model didn't get smarter. I got clearer about what I needed. That's the entire lesson."

**What to expect**: The contrast between Version 1 and Version 3 is usually dramatic. Version 2 vs. 3 is subtler — Version 3 wins on actionability but Version 2 may be "better" for a pure explanation. That's a useful nuance to surface.

**If a response is surprisingly good for a vague prompt**: Say "We got lucky. But notice: you can't control what 'lucky' looks like. With a specific prompt, you're not relying on luck."

---

## "If Students Ask..." FAQ

1. **"Do I really need all this context in every prompt?"**
   No. Simple questions need simple prompts. "What's the formula for the HHI?" doesn't need ROCS. The framework is for when you're getting bad output and need to diagnose why. Think of it as a debugging tool, not a requirement.

2. **"Isn't prompt engineering going to be obsolete soon?"**
   The specific tricks might change, but the underlying skill — specifying what you want clearly — never goes obsolete. That's the same skill as writing a good research question, giving a good briefing to a colleague, or writing a clear email. AI just makes the feedback loop faster.

3. **"What if I don't know enough about the topic to write a good prompt?"**
   That's the Prompting Paradox. AI is most useful when you already know enough to ask good questions and evaluate answers. If you're starting from zero, use AI for orientation ("What are the main debates about X?") but verify everything. You're in the "learning zone" from A3.

4. **"Should I use one long prompt or break it into a conversation?"**
   Both work. For well-defined tasks, a single detailed prompt is efficient. For exploratory or complex tasks, a conversation with iteration is better. Start with a reasonable first prompt and refine based on what comes back.

5. **"Can I just tell the AI to 'be an expert economist'?"**
   You can, and it sometimes helps. But it's less effective than providing actual context about your specific situation. "Be an expert" is vague — expert at what level? For what audience? On what topic? Specifics beat role-play.

---

## Facilitation Notes

- **Exercise format**: Individual works best for the rewrite portion (each student needs to think through their own ROCS). Pairs work well for the "bring your own question" step and for comparing before/after outputs.
- **If the AI tool is down or slow**: Have pre-run screenshots of the 3 IV prompt versions and their outputs. The demo still works as a static comparison — it's less dramatic but the point comes through.
- **Common sticking point**: Students write prompts that are long but still vague. The fix: "Length is not the same as specificity. A 3-sentence prompt with all 4 ROCS components beats a paragraph that's just more words around the same vague request."
- **Pro-AI students**: They often resist the idea that prompt quality matters — "the AI figures it out." The live demo is the counter-evidence. Let the outputs speak for themselves.
- **Skeptical students**: They may see prompting as pointless busywork. Redirect: "This isn't about the AI. It's about learning to specify problems clearly. That skill matters whether you use AI or not."
- **Assessment tie-in**: The `prompt_log_template.md` can be assigned as a low-stakes weekly reflection. Students log one prompt, one revision, and what they learned from the revision. Grade on process, not output quality.
