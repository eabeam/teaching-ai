# C3 Exercise Materials: Data Exploration & Cleaning

These materials support the exercises in [Module C3: Data Exploration & Cleaning](../../modules/c3-data-exploration.qmd).

## Contents

- **`generate_labor_survey.py`** — Python script that generates `labor_survey.csv`, a simulated labor force survey dataset with 500 observations and built-in data quality issues.

- **`cleaning_decision_log.md`** — Template for documenting data cleaning decisions. Students use this to record what they found, what they decided, and why.

## The Data

**This is SIMULATED data for teaching purposes only.** It does not represent real individuals or real survey responses.

`labor_survey.csv` contains 500 observations of a hypothetical labor force survey with the following variables:

| Variable | Description | Type |
|----------|-------------|------|
| `respondent_id` | Unique respondent identifier | Numeric |
| `district` | District name (5 districts) | String |
| `treatment` | Treatment assignment (0/1) | Binary |
| `survey_round` | Survey round (1 or 2) | Numeric |
| `age` | Respondent age | Numeric |
| `female` | Female indicator (0/1) | Binary |
| `earnings` | Monthly earnings in local currency | Numeric |
| `education_years` | Years of education (0-16) | Numeric |
| `employed` | Employment indicator (0/1) | Binary |
| `hours_worked` | Weekly hours worked (0-60) | Numeric |

## Setup

To generate the dataset:

```bash
cd exercises/c3/
python generate_labor_survey.py
```

This creates `labor_survey.csv` in the same directory and prints a summary with the planted issues listed (for instructor reference).

**Requirements**: Python 3 with pandas and numpy.

## Data Quality Issues (Instructor Reference)

The dataset contains the following planted issues. Students should discover these through exploration, not by reading this list.

1. **Negative earnings**: One respondent has earnings = -500 (data entry error)
2. **Extreme outlier earnings**: 3-4 respondents with earnings > 500,000 (ambiguous — could be real or errors)
3. **Differential missingness**: Earnings are missing ~5% in round 1 but ~15% in round 2 among employed respondents
4. **Treatment imbalance**: One district (Sylhet) has ~65% treated vs ~50% in other districts
5. **Duplicate respondent_id**: One respondent_id appears twice
6. **Impossible values**: One respondent with age = 3; one with hours_worked = 168

## How to Use

1. Students generate the data (or receive `labor_survey.csv` pre-generated)
2. Students explore the data in Stata or R, optionally with AI assistance for generating exploratory code
3. Students identify data quality issues and document their cleaning decisions using `cleaning_decision_log.md`
4. Class discussion: compare what different students found and how they decided to handle each issue
