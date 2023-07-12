-- Ranks country origins of bands
-- Displays country with hisghest number of Fans
SELECT origin, SUM(fans) As nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;