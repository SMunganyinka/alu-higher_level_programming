-- Select the correct database
USE hbtn_0c_0;

-- Query to display average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM weather_data
GROUP BY city
ORDER BY avg_temp DESC;
