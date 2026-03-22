# Answer Key: Buggy Analysis Exercise

> **For instructor use.** This document explains all 5 bugs in `buggy_analysis.do`.

---

## Bug 1 (Easy): Wrong merge type

**Line**: `merge 1:1 student_id using "school_data.csv"`

**What's wrong**: The code merges on `student_id`, but the school data doesn't contain `student_id` — it contains `school_id`. Even if the key variable were correct, a `1:1` merge is wrong because there are multiple students per school. The merge should be many-to-one on `school_id`.

**Why it matters**: As written, this merge will fail with an error because the using dataset doesn't contain `student_id`. If the student fixed the variable name but not the merge type (changing to `merge 1:1 school_id using...`), Stata would throw error r(459) because `school_id` is not unique in the master data. The code needs both fixes.

**The fix**:
```stata
merge m:1 school_id using "school_data.csv"
```

**AI detection**: AI almost always catches this bug. It's a syntax/logic error that maps to well-known Stata merge patterns. **Typical AI catch rate: High.**

---

## Bug 2 (Medium): No merge diagnostics before dropping

**Lines**: `keep if _merge == 3` / `drop _merge`

**What's wrong**: The code drops non-matching observations without first examining the merge results. There is no `tab _merge` or any diagnostic check. In this dataset, 2 students belong to school 107, which doesn't appear in the school data. These students are silently dropped.

**Why it matters**: Silently losing observations can bias your results, especially if the non-matching observations are systematically different. In a real project, you need to understand *why* observations didn't match before deciding what to do with them. Maybe school 107 was supposed to be in the school data and the file is incomplete. Maybe those students should be excluded for a good reason — but that should be a documented decision, not an accident.

**The fix**:
```stata
tab _merge
* Investigate any non-matches before proceeding
list student_id school_id if _merge != 3
* Then, after review:
keep if _merge == 3
drop _merge
```

**AI detection**: AI sometimes catches this, but often only mentions it as a "best practice" rather than flagging it as a bug. **Typical AI catch rate: Medium.** AI is more likely to catch it if you specifically ask about merge diagnostics.

---

## Bug 3 (Medium): Z-score uses overall mean/SD instead of control group mean/SD

**Lines**:
```stata
egen mean_score = mean(test_score)
egen sd_score = sd(test_score)
gen test_z = (test_score - mean_score) / sd_score
```

**What's wrong**: The comments say to standardize test scores, and the code does this correctly in a mechanical sense — it computes z-scores. But for estimating a treatment effect, the standard practice is to standardize relative to the **control group** mean and standard deviation. Using the overall sample mean/SD conflates the treatment effect with the standardization, which attenuates the estimated treatment effect in standard deviation units.

**Why it matters**: This is a conceptual/statistical error, not a syntax error. If the treatment has an effect on test scores, the overall mean includes the treatment effect, so the z-scores are centered on a shifted mean. The control-group SD may also differ from the overall SD. The result: your treatment effect in SD units is biased toward zero.

**The fix**:
```stata
summarize test_score if treatment == 0
local ctrl_mean = r(mean)
local ctrl_sd = r(sd)
gen test_z = (test_score - `ctrl_mean') / `ctrl_sd'
```

**AI detection**: AI rarely catches this bug on its own. It requires understanding the purpose of standardization in a treatment effect context, which is domain knowledge that goes beyond syntax checking. **Typical AI catch rate: Low.** This is the kind of bug that highlights why you need to understand your own analysis.

---

## Bug 4 (Hard): Sort-order dependence

**What's wrong**: There is no explicit `sort` command anywhere in the do-file. After the merge and the `keep if _merge == 3` operation, the data is in whatever order Stata's merge left it in. This doesn't cause a problem with the current code as written — but it would if anyone added operations that depend on sort order (like `gen row_id = _n`, or `by school_id:` operations without a preceding `sort`).

More concretely: the data arrives from the CSV in a shuffled order (the Python script randomizes it). If a student later adds code like `gen rank = _n` or uses `_n` or `_N` to construct variables, the results will depend on the arbitrary data order. The do-file should establish a deterministic sort order early on.

**Why it matters**: Sort-order dependence is one of the most common sources of non-reproducible results in Stata. Two people running the same code on the same data can get different results if the sort order differs (e.g., due to different Stata versions or operating systems handling ties differently). Good practice is to sort explicitly and, if using random operations, to set a seed.

**The fix**: Add an explicit sort after loading or after the merge:
```stata
sort school_id student_id
```

**AI detection**: AI sometimes mentions sort order as a general best practice but rarely identifies it as a concrete bug in this specific code, since no operation *currently* depends on sort order. **Typical AI catch rate: Low to Medium.** This bug tests whether students and AI tools think about code *robustness* beyond just "does it run right now."

---

## Bug 5 (Subtle): Hard-coded threshold for binary variable

**Line**: `gen high_performer = (test_score > 75)`

**What's wrong**: The comment says `high_performer` should equal 1 if a student scored above the **median**. But the code uses a hard-coded value of 75 instead of computing the actual median. In this dataset, the median test score is around 60 (not 75), so the hard-coded threshold classifies far fewer students as high performers than intended.

**Why it matters**: This creates a binary variable that doesn't measure what it claims to measure. If you use `high_performer` as an outcome variable in a regression, you're estimating the treatment effect on scoring above 75, not on scoring above the median. These are different quantities with different interpretations. The hard-coded value also makes the code fragile — if the data changes, the threshold doesn't update.

**The fix**:
```stata
summarize test_score, detail
gen high_performer = (test_score > r(p50))
```

Or equivalently:
```stata
egen median_score = median(test_score)
gen high_performer = (test_score > median_score)
drop median_score
```

**AI detection**: AI may or may not catch this. It depends on whether the AI reads the comment describing the intent and compares it to the code. If the comment weren't there, AI would have no way to know 75 is wrong. **Typical AI catch rate: Medium.** This bug illustrates why comments matter — they let both humans and AI check code against intent.

---

## Summary

| Bug | Difficulty | Type | Stata Error? | AI Catch Rate |
|-----|-----------|------|:------------:|:-------------:|
| 1. Wrong merge type/key | Easy | Syntax + Logic | Yes (r(459)) | High |
| 2. No merge diagnostics | Medium | Best Practice | No (silent) | Medium |
| 3. Z-score base group | Medium | Conceptual/Statistical | No (silent) | Low |
| 4. Sort-order dependence | Hard | Reproducibility | No (silent) | Low-Medium |
| 5. Hard-coded threshold | Subtle | Logic (intent vs. code) | No (silent) | Medium |

**Key takeaway**: Only Bug 1 produces a Stata error message. Bugs 2-5 all run silently and produce output that looks reasonable — you'd only catch them by understanding what the code is supposed to do. This is exactly the kind of risk that makes AI-generated code dangerous: it optimizes for "code that runs" rather than "code that does what you intend."
