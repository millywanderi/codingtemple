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
