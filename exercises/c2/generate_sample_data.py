"""
generate_sample_data.py — Create sample datasets for the C2 buggy analysis exercise

Generates:
  - student_data.csv: Student-level data (~30 rows, multiple students per school)
  - school_data.csv: School-level characteristics (one row per school)

The data is designed so that the bugs in buggy_analysis.do actually matter:
  - Multiple students per school (so 1:1 merge on student_id fails)
  - Some school_ids in student data don't appear in school data (non-matches)
  - Sort order matters for certain operations
  - The median test score is not 75 (so the hard-coded threshold is wrong)

Usage:
    python generate_sample_data.py

Requires: pandas (or modify to use csv module only)
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# -----------------------------------------------------------------------
# School data: 6 schools across 3 districts
# -----------------------------------------------------------------------
school_data = pd.DataFrame({
    'school_id': [101, 102, 103, 104, 105, 106],
    'district': [1, 1, 2, 2, 3, 3],
    'school_type': ['public', 'public', 'private', 'public', 'public', 'private'],
    'num_teachers': [12, 8, 15, 10, 9, 20]
})

# -----------------------------------------------------------------------
# Student data: ~30 students across the 6 schools (+ 2 in a 7th school
# that doesn't appear in school_data, to create non-matches)
# -----------------------------------------------------------------------

students = []
student_id = 1000

# Schools 101-106: 4-6 students each
for sch in [101, 102, 103, 104, 105, 106]:
    n_students = np.random.randint(4, 7)
    treatment = 1 if sch in [101, 103, 105] else 0
    for _ in range(n_students):
        student_id += 1
        students.append({
            'student_id': student_id,
            'school_id': sch,
            'test_score': round(np.random.normal(60, 15), 1),
            'treatment': treatment,
            'female': np.random.choice([0, 1]),
            'age': np.random.choice([14, 15, 16, 17])
        })

# Add 2 students from school 107 (no match in school_data)
for _ in range(2):
    student_id += 1
    students.append({
        'student_id': student_id,
        'school_id': 107,
        'test_score': round(np.random.normal(55, 12), 1),
        'treatment': 1,
        'female': np.random.choice([0, 1]),
        'age': np.random.choice([15, 16])
    })

student_data = pd.DataFrame(students)

# Shuffle the student data so it's NOT sorted by school_id or student_id
# This makes sort-order dependence bugs visible
student_data = student_data.sample(frac=1, random_state=99).reset_index(drop=True)

# -----------------------------------------------------------------------
# Adjust test scores so treatment group is slightly higher on average
# (to give a meaningful treatment effect to estimate)
# -----------------------------------------------------------------------
student_data.loc[student_data['treatment'] == 1, 'test_score'] += 5

# Make the control group mean clearly different from overall mean
# (so using overall mean/SD vs control-group mean/SD matters for z-scores)
student_data.loc[student_data['treatment'] == 0, 'test_score'] -= 3

# -----------------------------------------------------------------------
# Save to CSV
# -----------------------------------------------------------------------
student_data.to_csv('student_data.csv', index=False)
school_data.to_csv('school_data.csv', index=False)

# -----------------------------------------------------------------------
# Print summary for verification
# -----------------------------------------------------------------------
print("=== Student Data ===")
print(f"  Rows: {len(student_data)}")
print(f"  Unique student_ids: {student_data['student_id'].nunique()}")
print(f"  Unique school_ids: {student_data['school_id'].nunique()}")
print(f"  Schools in student data: {sorted(student_data['school_id'].unique())}")
print(f"  Treatment split: {student_data['treatment'].value_counts().to_dict()}")
print(f"  Test score range: {student_data['test_score'].min():.1f} - {student_data['test_score'].max():.1f}")
print(f"  Test score mean: {student_data['test_score'].mean():.1f}")
print(f"  Test score median: {student_data['test_score'].median():.1f}")
print()
print(f"  Control group mean: {student_data.loc[student_data['treatment']==0, 'test_score'].mean():.1f}")
print(f"  Treatment group mean: {student_data.loc[student_data['treatment']==1, 'test_score'].mean():.1f}")
print()

print("=== School Data ===")
print(f"  Rows: {len(school_data)}")
print(f"  Schools in school data: {sorted(school_data['school_id'].unique())}")
print()

print("=== Bug-Relevant Features ===")
print(f"  Bug 1 (merge type): Multiple students per school -> 1:1 merge will fail")
print(f"  Bug 2 (_merge check): School 107 has no match in school_data -> {len(student_data[student_data['school_id']==107])} students lost silently")
print(f"  Bug 3 (z-score): Overall mean = {student_data['test_score'].mean():.1f}, "
      f"Control mean = {student_data.loc[student_data['treatment']==0, 'test_score'].mean():.1f} "
      f"(difference matters)")
print(f"  Bug 4 (sort order): Data is shuffled, not sorted by student_id or school_id")
print(f"  Bug 5 (threshold): Median = {student_data['test_score'].median():.1f}, "
      f"but code uses 75 as threshold for high_performer")
print()
print("Files written: student_data.csv, school_data.csv")
