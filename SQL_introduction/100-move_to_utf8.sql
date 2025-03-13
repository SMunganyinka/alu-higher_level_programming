-- Select the database
USE hbtn_0c_0;

-- Drop the table if it exists (be careful, you will lose existing data)
DROP TABLE IF EXISTS first_table;

-- Recreate the table with the correct collation and charset
CREATE TABLE first_table (
    id INT DEFAULT NULL,
    name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    score INT DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
