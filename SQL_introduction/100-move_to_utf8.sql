-- Select the database
USE hbtn_0c_0;

-- Modify the column by explicitly setting only the COLLATE
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
