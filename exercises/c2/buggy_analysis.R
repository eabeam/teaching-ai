# buggy_analysis.R — Estimate effect of class size on test scores
# Last modified: March 2026
#
# This script should:
#   1. Load student-level data and school-level data
#   2. Merge them on school_id (keep only matched observations)
#   3. Standardize test scores within each district
#   4. Recode school type into a binary urban/rural indicator
#   5. Run a regression of standardized test scores on log class size,
#      controlling for school type, with district fixed effects
#
# Data files:
#   student_data.csv — one row per student (student_id, school_id, district,
#                      test_score, class_size, grade)
#   school_data.csv  — one row per school (school_id, school_type, num_teachers,
#                      pct_free_lunch)

library(tidyverse)

# --- Load data ---
students <- read_csv("student_data.csv")
schools  <- read_csv("school_data.csv",
                      col_types = cols(school_id = col_character()))

# --- Merge student and school data ---
merged <- left_join(students, schools, by = "school_id")

# --- Standardize test scores within district ---
merged <- merged %>%
  group_by(district) %>%
  mutate(test_z = (test_score - mean(test_score, na.rm = TRUE)) /
                   sd(test_score, na.rm = TRUE))

# --- Recode school_type to binary urban/rural ---
# school_type levels: "urban", "suburban", "rural", "remote"
merged <- merged %>%
  mutate(urban = case_when(
    school_type == "urban"    ~ 1,
    school_type == "suburban" ~ 0,
    school_type == "rural"    ~ 0
  ))

# --- Create log of class size ---
merged <- merged %>%
  mutate(log_classsize = log(class_size))

# --- Summary statistics ---
avg_score <- merged %>%
  summarise(mean_test_z = mean(test_z),
            mean_classsize = mean(class_size))

print(avg_score)

# --- Regression: test_z ~ log_classsize + urban + district FE ---
model <- lm(test_z ~ log_classsize + urban + factor(district), data = merged)
summary(model)
