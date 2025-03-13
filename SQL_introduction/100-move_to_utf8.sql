-- Select the correct database
USE hbtn_0c_0;

-- Convert the table to utf8mb4 if not already done
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the name column to only have the correct collation (removes CHARACTER SET utf8mb4)
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Verify the table structure to ensure everything is correct
SHOW CREATE TABLE first_table;
