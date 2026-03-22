* explore_labor_survey.do — Initial exploration of labor force survey data
* Last modified: March 2026
*
* Purpose: Generate descriptive output to understand the data BEFORE cleaning.
*          This script explores — it does NOT clean or modify data.
*
* Data: labor_survey.csv
*   - 10,000 observations (5,000 individuals x 2 survey rounds)
*   - Variables: person_id, round, treatment, employed, earnings,
*                age, female, education

clear all
set more off

* --- Load data ---
import delimited "labor_survey.csv", clear

* --- Basic structure ---
describe
summarize

* --- Check panel structure: is person_id unique within round? ---
duplicates report person_id round
duplicates tag person_id round, gen(_dup)
list person_id round if _dup > 0, sepby(person_id)
drop _dup

* --- Missingness patterns ---
misstable summarize

* Is missingness in earnings related to employment status?
tab employed, missing
bysort employed: summarize earnings

* --- Flag: negative or extreme earnings ---
list person_id round earnings employed if earnings < 0
summarize earnings, detail
list person_id round earnings age education if earnings > r(p99) & earnings < .

* --- Flag: implausible ages ---
list person_id round age if age < 15 | age > 80

* --- Treatment balance ---
tab treatment if round == 1

* --- Distribution of key variables by round and treatment ---
bysort round treatment: summarize earnings employed, detail

* ===================================================================
* YOUR TASK: Review the output below and document cleaning decisions
* ===================================================================
* Based on this exploration, write a brief cleaning memo that addresses:
*   1. What will you do about the negative earnings values?
*   2. How will you handle the extreme earnings outlier(s)?
*   3. Is the missingness in earnings/employed random or systematic?
*   4. Are there age values that need investigation?
*   5. Does the treatment variable look correct for an RCT?
*   6. Are there duplicate observations that need resolution?
*
* Do NOT start cleaning until you have documented and justified
* each decision. Undocumented cleaning is not reproducible research.
