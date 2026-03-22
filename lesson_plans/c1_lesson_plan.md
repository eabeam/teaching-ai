# Lesson Plan: C1 — Literature Review & Synthesis

## Module Overview

- **Title**: Literature Review & Synthesis: Using AI to Survey a Field (and Catching What It Gets Wrong)
- **Time estimate**: 50 min (tight) / 75 min (workshop)
- **Prerequisites**: A1 (hallucination background is essential); A2 recommended (prompting skills help with the exercises)
- **Materials needed**:
  - Projector with live internet access to an AI tool and Google Scholar
  - 1-2 pre-selected topics for the demo (in your subfield, so you can verify on the fly)
  - Exercise worksheets from `exercises/c1/`:
    - `citation_verification_table.md`

**Learning Objectives** (from module):

1. Identify which parts of the lit review process AI can genuinely accelerate and which parts it cannot
2. Implement a practical workflow that uses AI for synthesis while keeping humans in control of sourcing
3. Detect hallucinated citations and misrepresented findings in AI output
4. Use AI to organize, synthesize, and identify gaps in a set of papers you have already verified
5. Articulate why "AI-assisted" is not the same as "AI-generated" in the context of scholarly review

---

## 50-Minute Version (Lecture-Focused)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:07 | **Hook**: Live citation verification demo (see Live Demo Script). Ask AI for 5 citations on a topic in your subfield. Open Google Scholar. Check each one live with the class. Tally results on the board. | Same structure as A1's demo, but now students know *why* hallucination happens. Frame it as: "Now that you understand the mechanism, let's see what it means for real research workflow." |
| 0:07-0:12 | **The promise and the trap**: Walk through the opening section. Key line: "AI can produce something that *looks* like a lit review in 30 seconds. That's exactly the problem." Introduce the survey-data-with-measurement-error analogy. | The analogy lands well with econ students: you wouldn't publish from unvalidated survey data; don't build a lit review on unvalidated citations. |
| 0:12-0:20 | **What AI is good at (5 strengths)**: Cover brainstorming search terms, summarizing verified papers, identifying tensions/gaps, drafting thematic organization, suggesting adjacent fields. Emphasize the core principle: "AI is good at processing text you give it. It's bad at reliably retrieving facts." | Spend most time on #1 (brainstorming) and #2 (summarizing verified papers) — these are the highest-value use cases. |
| 0:20-0:25 | **What AI is bad at**: Cover hallucinated citations (the failure mode table is very effective — show it). Briefly mention comprehensiveness, methodological evaluation, and weighting contributions. | The failure mode table (fabricated, wrong authors, wrong findings, composite, retracted) is the most memorable element. Linger on it. |
| 0:25-0:30 | **The 5-step workflow**: Walk through quickly — brainstorm terms, search real databases, AI-assisted synthesis, gap analysis, verify everything. Emphasize the division of labor: "You curate, AI synthesizes." | If short on time, just state the principle and point students to the module for the full workflow. |
| 0:30-0:42 | **Exercise: Parts 1 + 5 (anti-pattern test)**. Students ask AI for 3 citations on a topic, then verify each in Google Scholar. Use `citation_verification_table.md`. 7 min to generate and verify, 5 min to discuss findings. | This is the highest-priority exercise. If you only have time for one activity, do this one. The moment a student finds a fabricated citation is the learning moment. |
| 0:42-0:48 | **Discussion**: Use Q2 (who bears responsibility for fabricated citations in a published paper?). Or Q1 ("Once AI gets better, will verification be unnecessary?" — the counter-argument comes from A1: the mechanism hasn't changed). | Q2 generates strong engagement because it connects to academic integrity norms students already care about. |
| 0:48-0:50 | **Wrap-up**: 4 takeaways. Emphasize: "AI is a synthesis tool, not a sourcing tool." | End with: "Every citation. Every single one. Check it." |

**If running short**: Cut the 5-step workflow section (0:25-0:30) to a single sentence ("The full workflow is in the module — the key idea is humans control the source list, AI helps with everything else"). Skip discussion.

**Skip entirely**: "Structured AI-Assisted Review: An Emerging Practice" section and the survey-enumerator analogy. These are for advanced/grad audiences.

---

## 75-Minute Version (Workshop-Style)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:10 | **Hook**: Same citation demo, but more thorough. Check all 5 citations. For any that are real, also check whether the AI accurately described the findings. The misrepresented-findings failure mode is harder to catch and worth demonstrating. | If you can find one where the AI gets the paper right but the findings wrong, that's the gold-standard demo moment. |
| 0:10-0:18 | **The promise and the trap + what AI is good/bad at**: Combine these sections. Walk through strengths and weaknesses side by side. | Same content as 50-min, just more tightly integrated. |
| 0:18-0:25 | **The 5-step workflow**: Cover in full. Emphasize Step 2 (real databases) and Step 5 (verify everything). Mention tools: Google Scholar, EconLit, NBER, SSRN. | If students haven't done a lit review before, spend an extra minute on citation chaining ("find a key paper, check its references, check who cited it"). |
| 0:25-0:55 | **Full exercise (30 min, Parts 1-5)**. Walk students through all 5 parts of the exercise. Timing within the exercise: | |
| | Part 1: Brainstorm with AI (5 min) | Students pick a topic and generate search terms. |
| | Part 2: Find 3 real papers in Google Scholar (8 min) | This is the hardest step for students new to lit review. Circulate and help. |
| | Part 3: Paste abstracts, get AI synthesis (5 min) | Students paste their 3 verified abstracts and ask for a thematic synthesis. |
| | Part 4: Evaluate the synthesis (5 min) | Did AI accurately characterize the papers? What did it miss? |
| | Part 5: Anti-pattern test (7 min) | Ask AI to *generate* 3 citations. Verify. Compare to Parts 1-4. Use `citation_verification_table.md`. |
| 0:55-0:68 | **Discussion and debrief**: Students share results from Part 5 (how many were real/fabricated?). Discuss Q1 (will this get better?) and Q3 (where is the line between AI-assisted and AI-generated?). | Collect Part 5 results as an informal poll: "How many of your 3 AI-generated citations were fully correct?" The class average is usually 1-2 out of 3. |
| 0:68-0:75 | **Wrap-up**: 4 takeaways. If this course includes a research paper, introduce the expectation that students submit a source verification log alongside their lit review. | Frame the verification log as standard practice, not punishment. "This is what professional researchers do." |

**Natural break point**: After the 5-step workflow at 0:25 (if teaching back-to-back with A1 or A2).

---

## Live Demo Script

**Setup**: Open your AI tool (projected) and Google Scholar in a second tab. Pick a topic in your subfield where you can verify citations from memory or quickly.

1. Say: "Let's test something. I'm going to ask the AI to give me citations on [topic]. Then we're going to check every single one."

2. Type into the AI tool: `"Give me 5 key academic citations on [your topic]. Include author names, year, journal, and a one-sentence summary of the findings."`

3. Read the first citation aloud. Say: "Sounds right to me. Let's check." Switch to Google Scholar. Search the title. Three outcomes:
   - **It exists and the details are correct**: "This one checks out. Good."
   - **It exists but something is wrong** (wrong year, wrong journal, misrepresented findings): "The paper is real, but the AI got [detail] wrong. This is the 'almost right' failure mode — the hardest to catch."
   - **It doesn't exist**: "This paper was never written. [Author] is a real researcher. [Journal] is a real journal. But this specific paper is fabricated. The AI generated a statistically plausible citation."

4. Repeat for all 5. Keep a running tally on the board:

   | Citation | Fully correct | Partially wrong | Fabricated |
   |----------|:---:|:---:|:---:|
   | #1 | | | |
   | #2 | | | |
   | ... | | | |

5. After checking all 5, say: "Now imagine you're writing a research paper and you used these citations without checking. How many errors would be in your bibliography?"

6. Close with: "This is why the workflow matters. AI can help you *process* papers you've found. It cannot reliably *find* papers for you."

**What to expect**: Results vary by model and topic. Typically 2-3 out of 5 will be fully correct, 1-2 partially wrong, and 0-2 fabricated. Niche topics tend to produce more hallucinations.

**If all 5 are correct** (unusual): "Great — but we had no way to know that without checking. And the next 5 might not be. The verification step isn't about the current batch being wrong; it's about not knowing in advance which ones will be."

---

## "If Students Ask..." FAQ

1. **"Can't I just use Perplexity/Google Scholar AI/Elicit to avoid this problem?"**
   Tools with real-time search are better than pure LLMs for citations. But they still make errors — wrong attributions, misrepresented findings, incomplete coverage. They're a useful supplement to database searching, not a replacement. The verification step remains essential regardless of the tool.

2. **"This seems like a lot of work. Isn't the point of AI to save time?"**
   AI does save time — on the synthesis and organization steps (Steps 3-4 of the workflow). The time cost is in verification (Step 5). But you'd be reading these papers anyway for a real lit review. The workflow doesn't add work; it restructures where the work happens.

3. **"What if I ask the AI to only give me real citations?"**
   You can ask. The model will try. It will still sometimes hallucinate, because it has no internal mechanism for distinguishing real from fabricated citations. Asking nicely doesn't change the architecture.

4. **"How many citations do I need to verify? All of them?"**
   All of them. Every single one. There is no reliable way to identify which citations are likely to be wrong without checking. This is non-negotiable for any work you submit with your name on it.

5. **"My friend used AI for their whole lit review and got an A."**
   That's possible — especially if most of the AI-generated citations happened to be real, or the grader didn't check. But "it worked once" is not a strategy. The risk is reputational: if a fabricated citation is caught by a reviewer, advisor, or employer, the consequences are serious and the excuse "the AI did it" does not help.

---

## Facilitation Notes

- **Exercise format**: Parts 1-3 work well individually or in pairs. Part 5 (anti-pattern test) is most impactful individually — each student should experience verifying their own AI-generated citations. The comparison between "find then synthesize" (Parts 1-4) and "generate directly" (Part 5) is the core lesson.
- **If the AI tool is down or slow**: Have a pre-run example of 5 AI-generated citations on a standard topic (e.g., microfinance and poverty) with verification results prepared. Walk through it as a case study instead of a live exercise.
- **Common sticking point**: Students who haven't done a real lit review before struggle with Part 2 (finding papers in Google Scholar). Spend a moment on mechanics: how to search, how to read a Google Scholar result, how to check "cited by." This is a valuable skill independent of AI.
- **Pro-AI students**: May argue that AI with web search solves the citation problem. Acknowledge the improvement, then ask: "Does it also solve the misrepresentation problem? Can you trust that the AI accurately described a paper's findings without reading the paper?" The answer is no.
- **Skeptical students**: May argue that AI is useless for lit review. Redirect to Steps 1 and 3-4: brainstorming search terms and synthesizing verified papers are genuinely valuable. The module isn't anti-AI; it's about dividing labor correctly.
- **Grad students vs. undergrads**: Grad students will engage more with the "structured AI-assisted review" section and the research-assistant analogy. Undergrads will benefit more from the concrete exercise and the verification drill.
