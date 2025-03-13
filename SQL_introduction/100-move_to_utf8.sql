-- Select the correct database
USE hbtn_0c_0;

-- Modify the 'name' column to ensure it only has COLLATE without CHARACTER SET
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Verify the structure of the table to check for the correct output
SHOW CREATE TABLE first_table;
