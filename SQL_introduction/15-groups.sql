-- This script lists the number of records for each score in second_table, sorted by the count of records (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
