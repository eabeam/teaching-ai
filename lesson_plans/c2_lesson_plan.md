# Lesson Plan: C2 — Code Assistance

## Module Overview

- **Title**: Code Assistance: AI Can Write Your Stata Code — But Should You Let It?
- **Time estimate**: 50 min (tight) / 75 min (workshop)
- **Prerequisites**: A1 (why AI produces plausible-but-wrong output); A2 (prompt quality); A3 recommended (danger zone for core skills). Students need basic Stata or R familiarity.
- **Materials needed**:
  - Projector with live access to an AI tool and (ideally) Stata or RStudio
  - The buggy do-file from the module (copy onto a slide or handout)
  - `exercises/c2/` (directory exists but is currently empty — use the buggy code from the module as the exercise)

**Learning Objectives** (from module):

1. Identify the types of coding tasks where AI assistance is most and least appropriate
2. Recognize "silent errors" — AI-generated code that runs without error but produces wrong results
3. Apply a practical framework for when to use AI for code, when to verify carefully, and when to write it yourself
4. Use AI effectively for debugging, translation, and code explanation without outsourcing analytical judgment

---

## 50-Minute Version (Lecture-Focused)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:07 | **Hook**: Project the buggy do-file (see Live Demo Script). Say: "This do-file has at least 5 bugs. You have 5 minutes to find as many as you can. Write them down." Cold — no hints yet. | Don't identify the number of bugs exactly. "At least 5" creates urgency without a hard target. Hand out or project the code. |
| 0:07-0:10 | **Quick tally**: "How many bugs did you find? Raise your hand: 1? 2? 3? 4? 5?" Don't reveal answers yet. | This creates stakes for the AI comparison. |
| 0:10-0:15 | **AI's turn**: Paste the same code into the AI tool live. Prompt: "This Stata do-file has several bugs. Can you identify them and explain what's wrong?" Read through the AI's response with the class. | AI will usually catch 3-4 of the 5 bugs. It often catches the syntax issues (merge, order of operations) but misses the analytical issues (wrong fixed effects, wrong merge key). |
| 0:15-0:20 | **Compare**: "What did the AI catch that you missed? What did YOU catch that the AI missed?" Reveal the full bug list (from the module's collapsible answer section). Discuss the pattern: AI catches mechanical errors, humans catch analytical errors. | The merge key bug (hhid vs. school_id) and the fixed effects bug (district vs. school) are the ones AI often misses. These require understanding the research design, not just Stata syntax. |
| 0:20-0:28 | **Where AI shines vs. where it's dangerous**: Walk through the 5 strong use cases (debugging, translation, explanation, boilerplate, documentation) and the 3 silent error examples. The RA analogy: "You wouldn't ask a new RA to decide your regression specification." | The diff-in-diff specification example (treatment + FEs but missing the interaction) is the best silent error example. It *looks* like a DiD but isn't. |
| 0:28-0:33 | **The framework**: Use freely / Use but verify / Do not outsource. Walk through the three tiers. Emphasize the gray zone: "never run AI-generated code without reading every line." | The "if you can't explain a line, you don't get to use it" rule is concrete and memorable. |
| 0:33-0:43 | **Exercise Step 3**: Students ask AI to rewrite the buggy do-file ("fix all bugs and follow best practices"). Then they read the AI's version line by line, looking for: correct fixes, unnecessary changes, and anything new the AI introduced. | This is the "subtle trap" step. AI will often change the regression specification, add controls, or alter the sample in ways that change the research question. Students need to catch this. |
| 0:43-0:48 | **Discussion**: Use Q1 ("I always read the AI's code, so I'm safe" — what's the flaw?). The answer: you need to know enough to evaluate code you didn't write, which requires the same skills as writing it yourself. | Or use Q4 ("Should econ programs still require coding?") for a broader discussion. |
| 0:48-0:50 | **Wrap-up**: 4 takeaways. "AI is a coding tool, not a thinking tool." | End with: "Silent errors are the real risk. Code that crashes is safe. Code that runs but is wrong is dangerous." |

**If running short**: Cut the framework section (0:28-0:33) to one sentence ("the full framework is in the module"). Skip the discussion.

**Skip entirely**: The "Case Study: AI-Powered Code Review in Research" section and the R-specific traps table (unless the class uses R). The Stata-specific traps table is worth keeping if students use Stata.

---

## 75-Minute Version (Workshop-Style)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:10 | **Hook**: Same buggy code exercise, but give students 8 minutes instead of 5. Students work in pairs. | Pairs produce better bug lists — two sets of eyes catch more, and the discussion between partners is itself valuable. |
| 0:10-0:15 | **Tally + AI comparison**: Same as 50-min. Paste code into AI tool live, compare results. | Same approach, same pattern emerges. |
| 0:15-0:22 | **Reveal and discuss the full bug list**: Walk through all 5 bugs in detail. For each, explain *why* the AI did or didn't catch it. Connect to A1: the model is pattern-matching on text, not reasoning about research design. | Spend extra time on the merge key bug (hhid is a household ID, not a school ID) — this requires understanding the data structure, which the AI can't infer from the code alone. |
| 0:22-0:32 | **Where AI shines (with demos)**: Walk through 2-3 of the strong use cases with live demos. E.g., paste the Stata loop code from the module and ask AI to explain it step by step. Paste the R code and ask for a Stata translation. Show that these work well. | The explanation demo is impressive — AI is genuinely good at explaining unfamiliar code. Students see a concrete positive use case alongside the bugs exercise. |
| 0:32-0:38 | **Silent errors deep dive**: Walk through all 3 examples (wrong merge type, missing value division, fake diff-in-diff). Show the Stata-specific traps table. | If the class uses R, swap in the R-specific traps table. Both are in the module. |
| 0:38-0:43 | **The framework**: 3 tiers. Quick but thorough. | Same as 50-min. |
| 0:43-0:60 | **Full debugging exercise (Steps 1-4, 17 min)**: Students work through all 4 steps — find bugs themselves, ask AI to find bugs, ask AI to rewrite, then critically review the rewrite. Pairs or individual. | Circulate during Step 4. The common finding: AI fixes the mechanical bugs but introduces a new analytical issue (changed specification, added controls, different sample restriction). When students find this, it's a powerful learning moment. |
| 0:60-0:70 | **Discussion**: Use Q2 (line between using AI to code faster vs. avoiding learning to code) and Q3 (slow hand-coder vs. fast AI-user — who produces better research?). These get at the deeper question of what coding skills are *for*. | Q3 is great for advanced students. The answer depends on experience level — which connects to A3's 2x2 framework. |
| 0:70-0:75 | **Wrap-up**: 4 takeaways. Mention that AI is better at reviewing code than writing it — suggest students try using AI to *review* their own code before submitting, rather than generating code from scratch. | This is the actionable takeaway: "Write it yourself, then ask AI to review it." Reverses the typical student workflow. |

**Natural break point**: After the framework section at 0:43 (if teaching back-to-back with another module).

---

## Live Demo Script

**Setup**: Project the buggy do-file on screen. Have your AI tool open in another tab. Optionally have Stata open to show the code would actually fail or produce wrong results.

**Part 1: Students find bugs (5-8 min)**

1. Display the buggy code (from the module's exercise section). Say: "This do-file is supposed to load student data, standardize test scores, merge with school data, and run a regression with school fixed effects. It has bugs. Find as many as you can."

2. Give students the code on a handout or slide:
   ```stata
   use "student_data.dta", clear
   gen test_z = test_score - mean(test_score) / sd(test_score)
   gen log_classsize = log(class_size)
   merge hhid using "school_data.dta"
   keep if _merge == 3
   label var test_z "Standardized test score"
   label var log_classsize "Log class size"
   reg test_z log_classsize i.district, robust
   ```

3. Timer running. Students write down bugs. After time is up, quick poll: "How many did you find?"

**Part 2: AI finds bugs (5 min)**

4. Switch to the AI tool. Paste the code. Type: `"This Stata do-file has several bugs. Can you identify them and explain what's wrong?"`

5. Read the AI's response aloud. For each bug it identifies, check off against what students found. Note what it catches and what it misses.

**Part 3: Compare (5 min)**

6. Reveal the full bug list:
   - **Bug 1**: Standardization formula — order of operations wrong, and `mean()`/`sd()` aren't valid Stata functions (need `egen`)
   - **Bug 2**: Merge syntax — old Stata syntax, needs merge type (m:1), and `hhid` is the wrong key variable (should be `school_id`)
   - **Bug 3**: No merge diagnostics — should `tab _merge` before dropping
   - **Bug 4**: Regression uses `i.district` but the comment says "school fixed effects" — these are different
   - **Bug 5**: `log()` with potential zeros or missing values — needs a check

7. Ask: "Notice the pattern? The AI caught the syntax bugs (1, partly 2). It may have caught the merge type. But did it catch that `hhid` is the wrong merge key? Did it catch that district FE aren't school FE? Those require understanding the *research design*, not just the code."

**Part 4 (75-min version only): AI rewrites**

8. Type: `"Rewrite this do-file to fix all bugs and follow best practices."`

9. Display the rewrite. Ask students: "Read every line. What did it fix? What did it change that it shouldn't have? Did it introduce anything new?"

---

## "If Students Ask..." FAQ

1. **"Can I use AI for my homework code?"**
   That depends on your instructor's policy, and you should follow it exactly. But regardless of the policy, ask yourself: is the goal of this assignment to produce correct code, or to learn how to write code? If it's the latter, using AI to generate the code defeats the purpose — even if the output is correct.

2. **"AI writes better Stata code than I do. Why should I learn?"**
   Two reasons. First, you need to be able to evaluate whether AI code is correct for *your specific analysis* — and you can't do that without understanding Stata. Second, the analytical decisions (what to estimate, how to specify the model, what sample to use) are yours. AI handles the mechanics; you handle the thinking. You need enough coding skill to bridge the two.

3. **"Is it okay to use AI to debug my code?"**
   Generally yes — this is one of the best use cases. You wrote the code, you understand the intent, and AI is helping you understand an error message. That's like asking a TA "what does this error mean?" The key: make sure you understand the fix, don't just paste it in and move on.

4. **"What about GitHub Copilot / code completion tools?"**
   These are in-editor suggestions based on the same underlying technology. They're useful for boilerplate and repetitive patterns. The same rules apply: understand every line, verify the logic, don't let autocomplete make analytical decisions for you. They're a power tool for experienced coders; they're a crutch for beginners.

5. **"Won't all coding be done by AI soon anyway?"**
   Maybe some of it. But empirical research requires understanding what code *does* and whether it answers the right question. Even if AI writes all the Stata code in 2030, someone needs to specify the research design, evaluate the output, and catch silent errors. That someone needs to understand code.

---

## Facilitation Notes

- **Exercise format**: The debugging exercise works best in pairs. Two people reading code catch more bugs, and the discussion ("Is that actually a bug?") is where learning happens. The AI comparison step should be done together — one person drives the AI tool while both evaluate.
- **If the AI tool is down or slow**: The human-side of the exercise (finding bugs yourself) still works perfectly. Have a pre-run AI response saved as a screenshot or text file. The comparison still works; you just lose the live drama.
- **If students don't know Stata**: The module mentions that the exercise can be adapted to R. The same bugs translate: wrong formula, wrong join type, missing data handling, wrong fixed effects, no diagnostics. Alternatively, run the exercise as a walkthrough rather than hands-on.
- **Common sticking point**: Students often can't articulate *why* `i.district` vs. `i.school_id` matters. This is a research design question, not a Stata question. Take a moment to explain: "District FE control for 50 things. School FE control for 500 things. They answer different questions. The AI doesn't know which question you're asking."
- **Pro-AI students**: They'll want to argue that AI just needs a better prompt. Fair enough — try it live. Give AI more context ("This is a study of class size effects using within-school variation. Fix the code to implement this correctly."). The results improve, but the point remains: *you* needed to know the right specification to write the right prompt.
- **Skeptical students**: They may resist using AI for any code. Show the debugging and explanation use cases — these are genuinely time-saving with low risk. The framework isn't "never use AI for code." It's "use AI for mechanics, not judgment."
- **Assessment tie-in**: The module suggests a "code review report" assignment: students paste AI-generated code, annotate each line, and flag issues. This is a strong assessment because it tests understanding, not just output. The annotation reveals whether the student actually understands the code.
