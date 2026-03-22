# explore_labor_survey.R — Initial exploration of labor force survey data
# Last modified: March 2026
#
# Purpose: Generate descriptive output to understand the data BEFORE cleaning.
#          This script explores — it does NOT clean or modify data.
#
# Data: labor_survey.csv
#   - 10,000 observations (5,000 individuals x 2 survey rounds)
#   - Variables: person_id, round, treatment, employed, earnings,
#                age, female, education

library(tidyverse)

# --- Load data ---
df <- read_csv("labor_survey.csv")

# --- Basic structure ---
glimpse(df)
summary(df)

# --- Check panel structure: is person_id unique within round? ---
df %>% count(person_id, round) %>% filter(n > 1)

# --- Missingness patterns ---
df %>%
  summarise(across(everything(), ~ sum(is.na(.)))) %>%
  pivot_longer(everything(), names_to = "variable", values_to = "n_missing") %>%
  mutate(pct_missing = round(100 * n_missing / nrow(df), 1)) %>%
  print(n = Inf)

# Is missingness in earnings related to employment status?
df %>% group_by(employed) %>%
  summarise(n = n(), earnings_missing = sum(is.na(earnings)),
            pct_missing = round(100 * earnings_missing / n, 1))

# --- Flag: negative or extreme earnings ---
df %>% filter(earnings < 0) %>% select(person_id, round, earnings, employed)
df %>% filter(earnings > quantile(earnings, 0.99, na.rm = TRUE)) %>%
  select(person_id, round, earnings, age, education)

# --- Flag: implausible ages ---
df %>% filter(age < 15 | age > 80) %>%
  select(person_id, round, age)

# --- Treatment balance ---
df %>% filter(round == 1) %>% count(treatment) %>%
  mutate(pct = round(100 * n / sum(n), 1))

# --- Distribution of key variables by round and treatment ---
df %>% group_by(round, treatment) %>%
  summarise(n = n(),
            mean_earnings = mean(earnings, na.rm = TRUE),
            median_earnings = median(earnings, na.rm = TRUE),
            mean_employed = mean(employed, na.rm = TRUE),
            .groups = "drop")

# ===================================================================
# YOUR TASK: Review the output below and document cleaning decisions
# ===================================================================
# Based on this exploration, write a brief cleaning memo that addresses:
#   1. What will you do about the negative earnings values?
#   2. How will you handle the extreme earnings outlier(s)?
#   3. Is the missingness in earnings/employed random or systematic?
#   4. Are there age values that need investigation?
#   5. Does the treatment variable look correct for an RCT?
#   6. Are there duplicate observations that need resolution?
#
# Do NOT start cleaning until you have documented and justified
# each decision. Undocumented cleaning is not reproducible research.
