-- Use the specified database
USE hbtn_0c_0;

-- Set the database character set to utf8mb4 (if not already set)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table character set to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the 'name' column to remove CHARACTER SET but keep COLLATE
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Final check - you can run this to verify later
SHOW CREATE TABLE first_table;
