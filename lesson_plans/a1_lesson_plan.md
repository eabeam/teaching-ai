# Lesson Plan: A1 — What LLMs Actually Do

## Module Overview

- **Title**: What LLMs Actually Do: Tokens, Prediction, and Mental Models for Economists
- **Time estimate**: 50 min (tight) / 75 min (workshop)
- **Prerequisites**: None
- **Materials needed**:
  - Projector with live internet access to an AI chat tool (e.g., UVM Copilot, ChatGPT)
  - Google Scholar open in a browser tab
  - Exercise worksheets from `exercises/a1/`:
    - `hallucination_verification_worksheet.md`
    - `sycophancy_comparison_worksheet.md`
    - `anchoring_comparison_worksheet.md`
    - `subfield_prompt_bank.md`

**Learning Objectives** (from module):

1. Explain what a large language model does in one sentence (and why that sentence matters)
2. Describe the token-prediction mechanism and why it produces both impressive and unreliable outputs
3. Identify common failure modes (hallucination, sycophancy, anchoring) and connect them to the underlying mechanism
4. Apply an appropriate mental model when deciding whether to trust AI output

---

## 50-Minute Version (Lecture-Focused)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:05 | **Hook**: Run the hallucination demo live (see Live Demo Script below). Project AI tool, ask for 5 citations in your subfield, open Google Scholar, start checking. | Don't reveal the point yet. Just say "Let's try something." |
| 0:05-0:08 | **The one-sentence version**: "An LLM predicts the next token based on statistical patterns." Write it on the board. Say: "Everything we just saw follows from this." | This is the anchor for the entire module. |
| 0:08-0:18 | **How it works (10-min version)**: Cover tokenization (strawberry example), training loop, generation. Use the autocomplete analogy heavily. Skip the $P(\text{next token})$ notation unless the audience is quantitative. | Skip Step 4 (RLHF) if short on time. Mention it as "there's more, but this is the core." |
| 0:18-0:22 | **Mental models table**: Show the "good vs. dangerous mental models" table. Ask students: "Which of these have you been using?" Quick poll, show of hands. | The "it knows things" model is the most common and most dangerous. |
| 0:22-0:35 | **Exercise: Test the failure modes**. Students do the hallucination test (ask for 3 citations, verify in Google Scholar). Pairs or individual. Use `hallucination_verification_worksheet.md`. | If AI tool is slow, have a backup screenshot of a hallucinated citation list ready. |
| 0:35-0:45 | **Discussion**: Use Q1 ("If an LLM produces a correct answer, does it 'understand' the economics?") and Q3 ("My colleague says they always double-check citations..."). Cold-call or think-pair-share. | Q3 is the best one if you only have time for one. The flaw: verification fatigue + you can't verify what you don't know is wrong. |
| 0:45-0:50 | **Wrap-up**: Return to the one sentence. Restate the 4 key takeaways. Preview next module (A2: Prompting). | End with: "Fluent does not equal correct. That's the single most important thing from today." |

**If running short**: Cut the mental models discussion (0:18-0:22) to 2 minutes. Skip Q1 and go straight to Q3.

**Skip entirely**: The "Further Reading" section and Step 4 (RLHF). These are for self-study.

---

## 75-Minute Version (Workshop-Style)

| Time | Activity | Notes |
|------|----------|-------|
| 0:00-0:07 | **Hook**: Same hallucination demo, but let it play out longer. Check all 5 citations with the class. Tally real vs. fabricated on the board. | The class tally is the memorable moment. |
| 0:07-0:12 | **The one-sentence version + autocomplete analogy**. | Same as 50-min version. |
| 0:12-0:25 | **How it works**: Cover all 4 steps, including RLHF. Use the "incentive problem" framing for sycophancy here. The economist's framing ("no cost function for being wrong") lands well. | Spend a beat on the key insight box: "no internal model of truth." |
| 0:25-0:30 | **Mental models table + quick poll**. | Same as 50-min. |
| 0:30-0:55 | **Full exercise set (25 min)**: Students work in pairs through all 3 tests — hallucination, sycophancy, anchoring. Use all three worksheets. Circulate and check in. | Assign one test per pair if time is tight; then jigsaw results at 0:50. |
| 0:55-0:65 | **Debrief**: Each pair shares one surprising finding. Discuss: what patterns did you notice? Were the sycophancy results as strong as expected? | Common finding: anchoring is stronger than expected; sycophancy varies by model. |
| 0:65-0:72 | **Discussion**: Use Q2 (hallucination vs. p-hacking) and Q4 (sycophancy + research quality). | Q2 is great for econometrics students. Q4 is great for everyone. |
| 0:72-0:75 | **Wrap-up and takeaways**. | Same close as 50-min. |

**Natural break point**: After the exercise set at 0:55 (if teaching back-to-back with A2).

---

## Live Demo Script

**Setup**: Open your AI tool (projected) and Google Scholar in a second tab.

1. Say to the class: "I'm going to ask the AI for citations in [your subfield]. Let's see what happens."
2. Type into the AI tool: `"Give me 5 academic citations on [specific topic in your subfield — e.g., 'the effect of conditional cash transfers on school enrollment in Sub-Saharan Africa']."`
3. Wait for the response. Read the first citation aloud. Say: "Looks legit, right? Let's check."
4. Switch to Google Scholar. Search for the exact title. If it exists, confirm. If not, say: "Doesn't exist. The author is real, the journal is real, but this paper was never written."
5. Repeat for 2-3 more citations. Keep a tally on the board: Real / Partially Wrong / Fabricated.
6. After checking, say: "This is what hallucination looks like. The AI doesn't retrieve facts. It generates text that *looks like* facts. That's the difference."

**What to expect**: Typically 1-3 out of 5 citations will be fully or partially fabricated. Some will be real papers with wrong years or wrong journals. The mix is instructive.

**If everything is correct** (rare but possible): Say "We got lucky this time. But you can't know that in advance without checking — and that's the point."

**Use `exercises/a1/subfield_prompt_bank.md`** for pre-tested prompts if you want to reduce live-demo risk.

---

## "If Students Ask..." FAQ

1. **"Is AI getting better at not hallucinating?"**
   Yes, newer models hallucinate less frequently. Some tools now include web search, which helps. But "less" is not "never." The rate is lower, the risk is unchanged if you don't verify. Think of it like a measurement instrument with lower but nonzero error — you still need validation.

2. **"So is AI just useless for research?"**
   No. It's very useful for tasks where you can verify the output — brainstorming, summarizing text you provide, explaining code, drafting. It's unreliable for tasks where verification is hard, like generating citation lists. The key is matching the tool to the task.

3. **"Does the AI know it's wrong when it hallucinates?"**
   No. There is no internal "confidence signal" that correlates with accuracy. The model produces tokens that are statistically likely. It has no mechanism for distinguishing true from false claims.

4. **"What about tools like Perplexity that cite sources?"**
   These are better because they retrieve documents and then summarize. But they still make errors — wrong attributions, misrepresented findings, incomplete coverage. The verification step remains essential.

5. **"Will AI replace economists?"**
   The short answer: no, because the hard part of economics is not producing text. The hard part is identification, judgment, and interpretation — things that require understanding causality, not just predicting the next word.

---

## Facilitation Notes

- **Exercise format**: Pairs work well. Individual is fine if students have reliable device access. Groups of 3+ tend to have one person driving and others watching.
- **If the AI tool is down or slow**: Have 2-3 screenshots of hallucinated citation responses saved as backup slides. The demo still works — you just can't check live. Frame it as: "Here's what happened when I ran this earlier."
- **Common sticking point**: Students conflate "sometimes correct" with "reliable." Push back: "If a citation is correct 80% of the time, that means 1 in 5 is wrong. Would you submit a paper where 1 in 5 citations is fabricated?"
- **Pro-AI students**: Validate their enthusiasm, then redirect: "AI is genuinely useful. The question is *for what*. Today we're learning where it fails so you can use it where it works."
- **Skeptical students**: Acknowledge the hype problem, then show a genuine use case (e.g., "explain this error message" or "summarize this paragraph"). The point is calibrated trust, not rejection.
