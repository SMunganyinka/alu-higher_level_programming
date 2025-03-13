-- This script lists all records from second_table where name is not NULL, ordered by score in descending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
