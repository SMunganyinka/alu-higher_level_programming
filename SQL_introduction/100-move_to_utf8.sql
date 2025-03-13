-- Select the database
USE hbtn_0c_0;

-- Create a backup table with the correct structure
CREATE TABLE first_table_backup AS SELECT * FROM first_table;

-- Drop the original table
DROP TABLE first_table;

-- Recreate the table with the correct format
CREATE TABLE first_table (
    id INT DEFAULT NULL,
    name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    score INT DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Restore data from the backup
INSERT INTO first_table (id, name, score) SELECT id, name, score FROM first_table_backup;

-- Drop the backup table
DROP TABLE first_table_backup;
