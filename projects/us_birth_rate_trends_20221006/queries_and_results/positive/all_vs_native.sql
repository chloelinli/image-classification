/*
These queries output all positive percentage differences,
comparing "all races" with American Indian or Alaskan Native
races in the U.S. by age.
*/

-- 15 to 17
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.15_to_17`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);

-- 15 to 19
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.15_to_19`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);

-- 18 to 19
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.18_to_19`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);

-- 20 to 24
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.20_to_24`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);

-- 25 to 29
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.25_to_29`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);

-- 30 to 34
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.30_to_34`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);

-- 35 to 39
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.35_to_39`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);

-- 40 to 44
SELECT
  Start_Year,
  End_Year,
  `All`,
  Native,
  Native_not_HL,
  Native_not_HL_Single_Race
FROM `myportfolio-110818.us_birth_rate_trends.40_to_44`
WHERE
  (`All` > 0)
  OR (Native > 0)
  OR (Native_not_HL > 0)
  OR (Native_not_HL_Single_Race > 0);