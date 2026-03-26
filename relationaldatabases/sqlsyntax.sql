-- create a database
CREATE DATABASE IF NOT EXISTS myuserdatabase;
USE myuserdatabase;

-- Create a table
CREATE TABLE IF NOT EXISTS userinfo (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Modify the table and column
ALTER TABLE userinfo ADD last_login TIMESTAMP;
ALTER TABLE userinfo MODIFY COLUMN email VARCHAR(150) NOT NULL;

-- Add new rows in the table
INSERT INTO userinfo(username, email)
VALUES ("kylie_kinsley", "kylie@example.com");

-- Update the table
UPDATE userinfo SET email = "kinsley@eample.com" WHERE user_id = 1;
