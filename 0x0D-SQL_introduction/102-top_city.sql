-- Displays the top 3 city temperatures during July and August by descending order
SELECT city, AVG(avg_temp) AS avg_temperature
FROM hbtn_0c_0
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temperature DESC
LIMIT 3;
