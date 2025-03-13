-- Select the correct database
USE hbtn_0c_0;

-- Drop the 'name' column (this will remove the column but not the data)
ALTER TABLE first_table DROP COLUMN name;

-- Recreate the 'name' column with the correct collation and **no charset** definition
ALTER TABLE first_table ADD COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Check if the changes have been applied correctly
SHOW CREATE TABLE first_table;
