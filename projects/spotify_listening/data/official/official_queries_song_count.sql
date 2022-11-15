-- total times listened to a song in the past year
SELECT
  Title,
  Artist,
  COUNT(Title) AS Times_Listened
FROM `myportfolio-110818.spotify_trends.official_1_year`
GROUP BY Title, Artist
ORDER BY Times_Listened DESC;