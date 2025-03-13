-- This script lists all records from second_table where score >= 10, ordered by score (top first), displaying score and name

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
