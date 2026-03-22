* buggy_analysis.do — Estimate treatment effects on student test scores
* Last modified: March 2026
*
* PURPOSE: Load student-level data, merge with school characteristics,
*          standardize test scores using the control group mean/SD,
*          and estimate the treatment effect on standardized test scores.
*
* DATA:
*   - student_data.csv: Student-level data (multiple students per school)
*     Variables: student_id, school_id, test_score, treatment, female, age
*   - school_data.csv: School-level characteristics (one row per school)
*     Variables: school_id, district, school_type, num_teachers
*
* EXPECTED OUTPUT: Treatment effect on standardized test scores,
*                  controlling for student demographics and district FE.

clear all
set more off

* -----------------------------------------------------------------------
* Step 1: Load student data
* -----------------------------------------------------------------------
import delimited "student_data.csv", clear

* -----------------------------------------------------------------------
* Step 2: Merge with school characteristics
* Use 1:1 merge since we want one school record per student
* -----------------------------------------------------------------------
merge 1:1 student_id using "school_data.csv"

* Keep only matched observations
keep if _merge == 3
drop _merge

* -----------------------------------------------------------------------
* Step 3: Standardize test scores
* Create z-scores so treatment effects are in SD units
* -----------------------------------------------------------------------
egen mean_score = mean(test_score)
egen sd_score = sd(test_score)
gen test_z = (test_score - mean_score) / sd_score
drop mean_score sd_score

* -----------------------------------------------------------------------
* Step 4: Create outcome variables
* high_performer: 1 if student scored above the median
* -----------------------------------------------------------------------
gen high_performer = (test_score > 75)

* -----------------------------------------------------------------------
* Step 5: Run analysis
* Estimate treatment effect with district FE and demographic controls
* -----------------------------------------------------------------------
reg test_z treatment i.district female age, robust

* Display key results
display "Treatment effect: " _b[treatment]
display "SE: " _se[treatment]
