# Bug Hunt Worksheet

## Instructions

This exercise uses `buggy_analysis.do`, a Stata do-file that is supposed to:

1. Load student-level test score data
2. Merge it with school-level characteristics
3. Standardize test scores using the **control group** mean and standard deviation
4. Create a binary "high performer" variable based on the **median** score
5. Estimate the treatment effect on standardized test scores with district fixed effects

The do-file contains **5 bugs** at different difficulty levels. Some will cause Stata to throw an error. Others will run silently and produce wrong results.

---

## Part 1: Find Bugs Yourself (15 min)

Read through `buggy_analysis.do` carefully. For each bug you find, record it below.

**Tip**: Read the comments describing what the code *should* do, then check whether the code actually does that.

## Part 2: Ask AI to Review (10 min)

Paste the full do-file into your AI tool with a prompt like:

> "This Stata do-file has several bugs. Can you identify them and explain what's wrong?"

Record what AI finds in the table below.

---

## Bug Tracking Table

| Bug # | Line(s) | Issue | Fix | Found by me? | Found by AI? |
|:-----:|---------|-------|-----|:------------:|:------------:|
| 1     |         |       |     | Y / N        | Y / N        |
| 2     |         |       |     | Y / N        | Y / N        |
| 3     |         |       |     | Y / N        | Y / N        |
| 4     |         |       |     | Y / N        | Y / N        |
| 5     |         |       |     | Y / N        | Y / N        |

---

## Reflection

1. Which bugs did you catch that AI missed (if any)?


2. Which bugs did AI catch that you missed (if any)?


3. Were any of the bugs "silent" — meaning the code would run without an error message but produce wrong results?


4. What does this tell you about the strengths of human vs. AI code review?


5. If you had run this code without reviewing it, which bug would have been most harmful to your analysis? Why?
