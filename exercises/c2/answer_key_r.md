# Answer Key: buggy_analysis.R

## Bug 1 (Easy) — Wrong join type loses observations silently

- **Line:** `left_join(students, schools, by = "school_id")` (line 26)
- **What's wrong:** The code uses `left_join`, which keeps all students regardless of whether their school appears in the school file. The comment says the goal is to "keep only students whose school appears in the school file," which requires `inner_join`. Alternatively, if the intent is to keep only matched students, `semi_join` or `inner_join` would be correct.
- **What goes wrong:** Students with no school match get `NA` for all school-level variables (`school_type`, `num_teachers`, `pct_free_lunch`). These NAs propagate silently into the urban/rural recode and regression. The sample is larger than intended and polluted with missing values.
- **The fix:** Change to `inner_join(students, schools, by = "school_id")`. Also add a check: compare `nrow(students)` before and after the merge to verify the number of matched/unmatched observations is sensible.
- **Does AI catch this?** Sometimes. AI will often flag that the join type matters, but it may not notice the mismatch between the comment and the code unless prompted. It is more likely to catch this if you paste the comment along with the code.

---

## Bug 2 (Medium) — Missing `ungroup()` after `group_by()`

- **Lines:** 29-32, the `group_by(district) %>% mutate(...)` block
- **What's wrong:** After computing `test_z` within districts, the data remains grouped by `district`. Every subsequent `mutate`, `summarise`, or `filter` operates within district groups instead of on the full dataset.
- **What goes wrong:** The `summarise` on line 48 computes means *within each district* instead of the overall mean, returning multiple rows instead of one. The `case_when` on lines 36-41 also operates within groups (though its effect there is less visible). More critically, if you later filter or slice the data, you get per-district results without realizing it.
- **The fix:** Add `%>% ungroup()` after the closing parenthesis on line 32.
- **Does AI catch this?** Frequently. This is one of the most well-known tidyverse pitfalls, and AI models are good at flagging it — especially if the `summarise` output looks wrong (multiple rows instead of one).

---

## Bug 3 (Medium) — Silent type mismatch on join key

- **Lines:** 21-23 (data loading) and 26 (the join)
- **What's wrong:** `school_id` is read as numeric from `student_data.csv` (the default) but explicitly read as character from `school_data.csv` (`col_character()`). When `left_join` tries to match a numeric column to a character column, `dplyr` will either throw a warning and coerce (newer versions) or silently produce zero matches (older versions). Either way, all school-level variables become `NA` after the join.
- **What goes wrong:** The merge appears to succeed (no error), but every school-level variable is `NA` for all rows. Downstream, `school_type` is all `NA`, so the urban/rural recode produces all `NA`, and the regression drops those observations or fails.
- **The fix:** Either read both as character (`col_types = cols(school_id = col_character())` in both `read_csv` calls), or convert after loading: `students <- students %>% mutate(school_id = as.character(school_id))`.
- **Does AI catch this?** Rarely on its own. AI tends to look at code structure, not data types. If you paste the error output or mention that all school variables are NA after the merge, AI will diagnose it quickly. But reading the code alone, this is easy to miss — even for experienced R users.

---

## Bug 4 (Hard) — Incomplete `case_when` silently produces NA for unmatched level

- **Lines:** 36-41, the `case_when` block
- **What's wrong:** `school_type` has four levels: "urban", "suburban", "rural", and "remote". The `case_when` maps three of them but omits "remote". In R, `case_when` returns `NA` for any row that does not match any condition -- so observations with `school_type == "remote"` silently get `urban = NA`.
- **What goes wrong:** Remote schools are dropped from the regression (because `urban` is NA for them) without any warning. This reduces the sample and may introduce selection bias, since remote schools likely differ systematically from others. No error, no warning -- just a smaller sample.
- **The fix:** Add a condition for "remote", or use a catch-all default:
  ```r
  mutate(urban = case_when(
    school_type == "urban" ~ 1,
    school_type %in% c("suburban", "rural", "remote") ~ 0,
    TRUE ~ NA_real_
  ))
  ```
  The `TRUE ~ NA_real_` line is a deliberate catch-all that makes unhandled cases explicit. Without it, unmatched rows silently become NA.
- **Does AI catch this?** Sometimes. AI will catch it if it knows the full list of factor levels. If you only paste the code without mentioning that "remote" is a valid level, AI will likely miss this entirely. This is a good example of a bug that requires domain knowledge (knowing your data) to detect.

---

## Bug 5 (Subtle) — `mean()` without `na.rm = TRUE` returns NA

- **Lines:** 48-50, the `summarise` block
- **What's wrong:** `mean(test_z)` and `mean(class_size)` do not specify `na.rm = TRUE`. If even a single value in either column is `NA` (which is likely, given bugs 1, 3, and 4 above), the entire mean is `NA`.
- **What goes wrong:** The summary statistics table prints `NA` for both columns. This is confusing but at least visible. The more dangerous version of this bug is when it appears inside a `mutate` — e.g., `mutate(demeaned = test_z - mean(test_z))` — where the entire new column silently becomes `NA`.
- **The fix:** Use `mean(test_z, na.rm = TRUE)` and `mean(class_size, na.rm = TRUE)`. Note: this fix is necessary but not sufficient — you should also investigate *why* there are NAs (bugs 1, 3, and 4 above).
- **Does AI catch this?** Almost always. This is one of the most common R gotchas in AI training data. AI will reliably suggest adding `na.rm = TRUE`. However, AI may fix the symptom without identifying the upstream cause (the merge and recode bugs that created the NAs in the first place).

---

## Summary Table

| Bug | Difficulty | Type | AI catches it? |
|-----|-----------|------|----------------|
| 1. Wrong join type | Easy | Logic / intent mismatch | Sometimes |
| 2. Missing `ungroup()` | Medium | Tidyverse footgun | Frequently |
| 3. Type mismatch on join key | Medium | Silent coercion | Rarely (without output) |
| 4. Missing factor level in recode | Hard | Domain knowledge required | Sometimes (if levels listed) |
| 5. `mean()` without `na.rm = TRUE` | Subtle | Common R gotcha | Almost always |

## Teaching Notes

- Bugs 1 and 3 interact: even if you fix the join type (bug 1), the type mismatch (bug 3) means zero rows match. Students who fix one but not the other will still get wrong results — a good lesson in debugging systematically.
- Bug 4 is the most "economics-relevant" bug: it introduces sample selection bias. This is a good entry point for discussing how coding errors map to econometric problems.
- Bug 5 is the one AI almost always catches. This makes it useful for demonstrating AI's strengths — but also its tendency to fix surface symptoms rather than root causes.
