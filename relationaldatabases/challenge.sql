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
