-- This script displays the maximum temperature for each state, ordered by State name.
SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
