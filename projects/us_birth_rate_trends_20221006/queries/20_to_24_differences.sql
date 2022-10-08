/*
These queries use my personal BigQuery project to calculate
the difference in values within the birth rates for each race
within the 20-24 age group. These values were then manually
written into a Google Spreadsheet and formatted as percentages.
"All" refers to the section labeled "All races" as provided by
the CDC dataset. Unsure what "Single Race" is meant to refer
to, but will continue to calculate the data separately and
include it in the spreadsheets.
*/

-- All races
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_all`
ORDER BY Year;

-- Asian, not Hispanic or Latina (Single Race)
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_asian_not_hl_single_race`
ORDER BY Year;

-- Asian, Pacific Islander
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_asian_pi`
ORDER BY Year;

-- Asian, Pacific Islander, not Hispanic or Latina
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_asian_pi_not_hl`
ORDER BY Year;

-- Black, African American
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_black`
ORDER BY Year;

-- Black, African American (Single Race)
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_black_single_race`
ORDER BY Year;

-- Black, African American, not Hispanic or Latina
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_black_not_hl`
ORDER BY Year;

-- Black, African American, not Hispanic or Latina (Single Race)
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_black_not_hl_single_race`
ORDER BY Year;

-- Hispanic or Latina
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_hispanic_latina`
ORDER BY Year;

-- American Indian, Alaska Native
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_native`
ORDER BY Year;

-- American Indian, Alaska Native, not Hispanic or Latina
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_native_not_hl`
ORDER BY Year;

-- American Indian, Alaska Native, not Hispanic or Latina (Single Race)
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_native_not_hl_single_race`
ORDER BY Year;

-- White
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_white`
ORDER BY Year;

-- White, not Hispanic or Latina
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_white_not_hl`
ORDER BY Year;

-- White, not Hispanic or Latina (Single Race)
SELECT
  _20_24_years__percentage_ - LAG(_15_19_years__percentage_) OVER (ORDER BY Year) AS diff_curr_prev_percentage
FROM `myportfolio-110818.us_birth_rate_trends.birth_rates_white_not_hl_single_race`
ORDER BY Year;