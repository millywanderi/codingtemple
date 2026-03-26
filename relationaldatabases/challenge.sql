"""
Task: Create a simple table and manipulate its data using DML commands.

Create a Table for a books collection with the following columns:
book_id: INT, AUTO_INCREMENT, Primary Key.
title: VARCHAR(100), NOT NULL.
author: VARCHAR(100), NOT NULL.
published_year: YEAR.
genre: VARCHAR(50).
Insert Data into the table:
A book titled "The Great Gatsby" by "F. Scott Fitzgerald", published 
in 1925 under the "Fiction" genre.
A book titled "1984" by "George Orwell", published in 1949 under the 
"Dystopian" genre.
Update the genre of "1984" to "Political Fiction".
Delete the record for "The Great Gatsby".
"""
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    published_year YEAR,
    genre VARCHAR(50)
);

INSERT INTO books(book_id, title, author, published_year, genre)
VALUES ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"),
       ("1984", "George Orwell", 1949, "Dystopian");

UPDATE books SET genre = "Political Fiction" WHERE title = "1984";
DELETE FROM books WHERE title = "The Great Gatsby";


"""
Use what you've learned to build and manipulate a database for an online store.
Tasks:
Create a customers table with columns for customer_id, name, email, and address.
Insert three customers into the table.
Query for all customers with an email ending in @gmail.com.
Update the address of one of the customers.
Delete one customer record.
"""
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200)
);

INSERT INTO customers(name, email, address)
VALUES ("Mary", "mary@gmail.com", "11 Street Maple"),
       ("John", "John@example.com", "12 Street Maple"),
       ("Ken", "ken@gmail.com", "13 Street Maple");

SELECT * FROM customers
UPDATE customers SET address = "12 MAPLE" WHERE customer_id = 1;
DELETE FROM customers WHERE customer_id = 3;
