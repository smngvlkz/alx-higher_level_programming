-- Displays average temp ny city in descending order
SELECT state, MAX(max_temp) AS max_temperature
FROM hbtn_0c_0
GROUP BY state
ORDER BY state;
