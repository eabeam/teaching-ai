"""
generate_labor_survey.py — Create simulated labor force survey data for C3 exercise

Generates:
  - labor_survey.csv: 500 observations with built-in data quality issues

This is SIMULATED data for teaching purposes only. It is designed to have
realistic-looking structure with intentional data quality problems that
students should discover during exploration and cleaning.

Usage:
    python generate_labor_survey.py

Requires: pandas, numpy
"""

import pandas as pd
import numpy as np

np.random.seed(2026)

n = 500

# -----------------------------------------------------------------------
# Base variables
# -----------------------------------------------------------------------
respondent_id = list(range(1001, 1001 + n))
district = np.random.choice(['Dhaka', 'Chittagong', 'Rajshahi', 'Khulna', 'Sylhet'],
                            size=n, p=[0.25, 0.20, 0.20, 0.20, 0.15])
survey_round = np.random.choice([1, 2], size=n, p=[0.50, 0.50])
female = np.random.choice([0, 1], size=n, p=[0.48, 0.52])
age = np.random.normal(35, 10, size=n).clip(18, 65).round().astype(int)
education_years = np.random.choice(range(0, 17), size=n,
                                    p=[0.05, 0.02, 0.03, 0.03, 0.04, 0.05,
                                       0.06, 0.05, 0.08, 0.07, 0.10, 0.08,
                                       0.12, 0.06, 0.06, 0.05, 0.05])

# Treatment assignment (roughly 50/50 but slightly imbalanced in Sylhet)
treatment = np.zeros(n, dtype=int)
for i in range(n):
    if district[i] == 'Sylhet':
        treatment[i] = np.random.choice([0, 1], p=[0.35, 0.65])  # imbalanced
    else:
        treatment[i] = np.random.choice([0, 1], p=[0.50, 0.50])

# Employment: correlated with treatment, education, age
employed_prob = 0.55 + 0.08 * treatment + 0.015 * (education_years - 8) / 8 + 0.005 * (age - 35) / 10
employed_prob = np.clip(employed_prob, 0.1, 0.95)
employed = np.array([np.random.binomial(1, p) for p in employed_prob])

# Hours worked: conditional on employment
hours_worked = np.where(employed == 1,
                        np.random.normal(40, 10, size=n).clip(5, 60).round(),
                        0).astype(float)

# Earnings: conditional on employment, correlated with education and treatment
base_earnings = 15000 + 2000 * education_years + 5000 * treatment + np.random.normal(0, 8000, size=n)
earnings = np.where(employed == 1, base_earnings.clip(1000, None).round(), np.nan)

# -----------------------------------------------------------------------
# GROUND TRUTH: Planted data quality issues
# -----------------------------------------------------------------------

# Issue 1: One data entry error — negative earnings
# Respondent at index 47 has earnings = -500 (impossible, likely data entry)
if not np.isnan(earnings[47]):
    earnings[47] = -500
else:
    # Make sure this person is employed so the error shows up
    employed[47] = 1
    hours_worked[47] = 35
    earnings[47] = -500

# Issue 2: Outlier earnings (3-4 values that are extremely high)
# These could be real (wealthy business owners) or errors
outlier_indices = [12, 156, 301, 422]
for idx in outlier_indices:
    employed[idx] = 1
    hours_worked[idx] = np.random.choice([45, 50, 55])
    earnings[idx] = np.random.choice([520000, 680000, 540000, 750000])

# Issue 3: Higher missingness in earnings for round 2
# Round 1: ~5% missing among employed; Round 2: ~15% missing among employed
for i in range(n):
    if employed[i] == 1 and not np.isnan(earnings[i]):  # don't overwrite planted values
        if i in outlier_indices or i == 47:
            continue
        if survey_round[i] == 1 and np.random.random() < 0.05:
            earnings[i] = np.nan
        elif survey_round[i] == 2 and np.random.random() < 0.15:
            earnings[i] = np.nan

# Issue 4: Treatment imbalance in Sylhet is already built in above
# (65% treated vs 50% elsewhere)

# Issue 5: One duplicate respondent_id
# Make respondent at index 200 have the same ID as index 50
respondent_id[200] = respondent_id[50]

# Issue 6: Impossible values
# age = 3 for one person (data entry error)
age[88] = 3
# hours_worked = 168 for one person (entered weekly hours as if it were all hours in a week)
if employed[315] == 1:
    hours_worked[315] = 168
else:
    employed[315] = 1
    hours_worked[315] = 168
    earnings[315] = 22000

# -----------------------------------------------------------------------
# Assemble and save
# -----------------------------------------------------------------------
df = pd.DataFrame({
    'respondent_id': respondent_id,
    'district': district,
    'treatment': treatment,
    'survey_round': survey_round,
    'age': age,
    'female': female,
    'earnings': earnings,
    'education_years': education_years,
    'employed': employed,
    'hours_worked': hours_worked
})

df.to_csv('labor_survey.csv', index=False)

# -----------------------------------------------------------------------
# Print summary and ground truth
# -----------------------------------------------------------------------
print("=" * 60)
print("LABOR SURVEY DATA — SUMMARY")
print("=" * 60)
print(f"Total observations: {len(df)}")
print(f"Variables: {', '.join(df.columns)}")
print()
print("Variable summaries:")
print(df.describe().round(1).to_string())
print()
print(f"District distribution:")
print(df['district'].value_counts().to_string())
print()
print(f"Treatment by district:")
print(pd.crosstab(df['district'], df['treatment'], margins=True).to_string())
print()

print("=" * 60)
print("GROUND TRUTH — PLANTED DATA QUALITY ISSUES")
print("=" * 60)
print()
print("1. NEGATIVE EARNINGS (data entry error)")
print(f"   Row index 47, respondent_id = {respondent_id[47]}")
print(f"   earnings = -500 (should be positive)")
print()
print("2. OUTLIER EARNINGS (possibly real, possibly errors)")
print(f"   Indices: {outlier_indices}")
print(f"   Values: {[earnings[i] for i in outlier_indices]}")
print(f"   These are 10-20x the median. Could be wealthy business owners,")
print(f"   or data entry errors (extra zeros). Requires judgment.")
print()
print("3. DIFFERENTIAL MISSINGNESS IN EARNINGS BY ROUND")
round1_employed = df[(df['survey_round'] == 1) & (df['employed'] == 1)]
round2_employed = df[(df['survey_round'] == 2) & (df['employed'] == 1)]
print(f"   Round 1 employed: {len(round1_employed)}, "
      f"missing earnings: {round1_employed['earnings'].isna().sum()} "
      f"({round1_employed['earnings'].isna().mean()*100:.1f}%)")
print(f"   Round 2 employed: {len(round2_employed)}, "
      f"missing earnings: {round2_employed['earnings'].isna().sum()} "
      f"({round2_employed['earnings'].isna().mean()*100:.1f}%)")
print()
print("4. TREATMENT IMBALANCE IN SYLHET")
sylhet = df[df['district'] == 'Sylhet']
print(f"   Sylhet treatment rate: {sylhet['treatment'].mean():.2f}")
print(f"   Other districts treatment rate: {df[df['district'] != 'Sylhet']['treatment'].mean():.2f}")
print()
print("5. DUPLICATE RESPONDENT_ID")
print(f"   respondent_id {respondent_id[50]} appears at indices 50 and 200")
print(f"   Total unique IDs: {df['respondent_id'].nunique()} (should be {len(df)})")
print()
print("6. IMPOSSIBLE VALUES")
print(f"   age = 3 at index 88 (respondent_id = {respondent_id[88]})")
print(f"   hours_worked = 168 at index 315 (respondent_id = {respondent_id[315]})")
print()
print("File written: labor_survey.csv")
