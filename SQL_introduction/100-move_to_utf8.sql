-- Select the correct database
USE hbtn_0c_0;

-- Drop the 'name' column
ALTER TABLE first_table DROP COLUMN name;

-- Recreate the 'name' column with the correct collation and NO charset definition
ALTER TABLE first_table ADD COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Convert the table to the correct character set and collation.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Check if the changes have been applied correctly
SHOW CREATE TABLE first_table;
