-- total songs in all time top 50 per genre
SELECT
  Genre,
  COUNT(Genre) AS Genre_Total
FROM `myportfolio-110818.spotify_trends.unofficial_all_time`
GROUP BY Genre
ORDER BY Genre_Total DESC;

-- total songs in last 6 months top 50 per genre
SELECT
  Genre,
  COUNT(Genre) AS Genre_Total
FROM `myportfolio-110818.spotify_trends.unofficial_6_months`
GROUP BY Genre
ORDER BY Genre_Total DESC;

-- total songs in last 4 weeks top 50 per genre
SELECT
  Genre,
  COUNT(Genre) AS Genre_Total
FROM `myportfolio-110818.spotify_trends.unofficial_last_month`
GROUP BY Genre
ORDER BY Genre_Total DESC;