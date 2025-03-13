-- Select the database
USE hbtn_0c_0;

-- Convert the database to utf8mb4 (charset and collation)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table to utf8mb4 (charset and collation)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Rename the current column (to remove explicit charset reference)
ALTER TABLE first_table CHANGE name old_name VARCHAR(256);

-- Add a new 'name' column without specifying CHARACTER SET, only COLLATE
ALTER TABLE first_table ADD name VARCHAR(256) COLLATE utf8mb4_unicode_ci AFTER id;

-- Copy data from old column to new column
UPDATE first_table SET name = old_name;

-- Drop the old column
ALTER TABLE first_table DROP COLUMN old_name;
