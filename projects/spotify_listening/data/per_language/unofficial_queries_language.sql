-- total songs in all time top 50 per language
SELECT
  Language,
  COUNT(Language) AS Total_Language
FROM `myportfolio-110818.spotify_trends.unofficial_all_time`
GROUP BY Language
ORDER BY Total_Language DESC;

-- total songs in last 6 months top 50 per language
SELECT
  Language,
  COUNT(Language) AS Total_Language
FROM `myportfolio-110818.spotify_trends.unofficial_6_months`
GROUP BY Language
ORDER BY Total_Language DESC;

-- total songs in last 4 weeks top 50 per language
SELECT
  Language,
  COUNT(Language) AS Total_Language
FROM `myportfolio-110818.spotify_trends.unofficial_last_month`
GROUP BY Language
ORDER BY Total_Language DESC;