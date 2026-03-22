# Data Cleaning Decision Log

## Dataset Information

- **Dataset**: _______________________________________________
- **Date**: _______________________________________________
- **Analyst**: _______________________________________________
- **Original sample size**: _______________________________________________

---

## Instructions

For each data quality issue you identify, document your decision below. There are no universally "correct" answers to cleaning decisions — but every decision must be justified and its consequences understood.

Before filling this out, explore the data using `summarize`, `tabulate`, `codebook`, or equivalent commands. Ask AI to help you flag potential issues, but make all final decisions yourself.

---

## Cleaning Decisions

| Issue # | What I Found | Decision | Justification | Alternative Considered | Sample Size Impact |
|:-------:|-------------|----------|---------------|----------------------|-------------------|
| 1       |             |          |               |                      |                   |
| 2       |             |          |               |                      |                   |
| 3       |             |          |               |                      |                   |
| 4       |             |          |               |                      |                   |
| 5       |             |          |               |                      |                   |
| 6       |             |          |               |                      |                   |
| 7       |             |          |               |                      |                   |
| 8       |             |          |               |                      |                   |

---

## Column Guide

- **What I Found**: Describe the issue precisely (e.g., "3 respondents with earnings > 500,000; median earnings is 17,000")
- **Decision**: What you did (e.g., "Winsorized at 99th percentile", "Dropped observation", "Recoded to missing", "Kept as-is")
- **Justification**: Why this is the right call for your analysis (e.g., "Likely data entry error based on context", "Value is plausible for a business owner")
- **Alternative Considered**: What else you could have done and why you didn't
- **Sample Size Impact**: How many observations are affected (e.g., "3 observations recoded", "Dropped 12 obs, N goes from 500 to 488")

---

## Final Sample Summary

- **Final sample size**: _______________________________________________
- **Total observations dropped**: _______________________________________________
- **Total observations with recoded values**: _______________________________________________
- **Percentage of sample affected by any cleaning decision**: _______________________________________________

---

> **Every cleaning decision is a research decision. If you can't justify it, don't do it.**
