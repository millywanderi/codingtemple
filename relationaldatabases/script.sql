CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS users(
    user_id INT AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
);

-- Add new column
ALTER TABLE users ADD last_login TIMESTAMP;

INSERT INTO users(username, email)
VALUES
('kylie', 'kylie@gmail.com'),
('lyle', 'lyle@gmail.com');

SELECT * FROM users;
