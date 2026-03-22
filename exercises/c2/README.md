# C2 Exercise Materials: Code Assistance

These materials support the exercises in [Module C2: Code Assistance](../../modules/c2-code-assistance.qmd).

## Contents

- **`buggy_analysis.do`** — A Stata do-file with 5 bugs at different difficulty levels. The code is supposed to load student data, merge it with school characteristics, standardize test scores, and estimate a treatment effect. Students find bugs themselves, then compare their results with AI's review.

- **`generate_sample_data.py`** — A Python script that creates `student_data.csv` and `school_data.csv` for the buggy do-file to run on. The data is designed so the bugs actually matter (e.g., the merge has non-matches, sort order is randomized, the median is not 75).

- **`bug_hunt_worksheet.md`** — Structured worksheet for the bug hunt exercise. Students record bugs they found, bugs AI found, and reflect on the comparison.

- **`answer_key.md`** — Full answer key with all 5 bugs explained: line numbers, what's wrong, why it matters, the fix, and typical AI catch rates. **For instructor use.**

## Setup

To generate the sample data:

```bash
cd exercises/c2/
python generate_sample_data.py
```

This creates `student_data.csv` and `school_data.csv` in the same directory. Students need these files to run the buggy do-file in Stata.

**Requirements**: Python 3 with pandas and numpy.

## The 5 Bugs (Quick Reference)

1. **Wrong merge type** (Easy) — Uses `1:1` when it should be `m:1`, and merges on the wrong key variable
2. **No merge diagnostics** (Medium) — Drops non-matches without examining `_merge`
3. **Z-score base group** (Medium) — Uses overall mean/SD instead of control group mean/SD
4. **Sort-order dependence** (Hard) — No explicit sort command; data order is arbitrary
5. **Hard-coded threshold** (Subtle) — Uses `> 75` instead of computing the actual median

## Note for Instructors

The bugs are designed so that AI tools typically catch Bug 1 reliably, Bugs 2 and 5 sometimes, and Bugs 3 and 4 rarely. The comparison between human and AI bug detection is the pedagogical point of the exercise.

If students don't have Stata access, the exercise can still be done as a code-reading exercise — the bugs are identifiable by reading the code carefully without running it.
