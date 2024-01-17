-- Script that lists all records with a score >= 10 in the table second_table in your MySQL server.
-- Results should display both the score and the name (in this order)
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
