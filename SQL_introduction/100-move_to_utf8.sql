-- Select the database
USE hbtn_0c_0;

-- Convert the database and table to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Temporarily rename the column to break MySQL’s stored charset reference
ALTER TABLE first_table CHANGE name temp_name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Rename it back to 'name' without defining CHARACTER SET
ALTER TABLE first_table CHANGE temp_name name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
