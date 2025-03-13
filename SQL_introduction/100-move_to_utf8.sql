-- Select the correct database
USE hbtn_0c_0;

-- Alter the 'name' column to remove CHARACTER SET and keep COLLATE only
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
