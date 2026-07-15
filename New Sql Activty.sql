CREATE TABLE IF NOT EXISTS book (
book_Id INTEGER PRIMARY KEY, 
    title TEXT Not NULL,
    Genera TEXT NOT NULL,
    Rating TEXT Not NULL,
    pages INTEGER Not NULL,
    pub_year INTEGER Not NULL
);

INSERT INTO book VALUES
(1, 'The Great Gatsby', 'Fiction', '4.2', 180, 1925),
(2, 'To Kill a Mockingbird', 'Fiction', '4.3', 281, 1960),
(3, '1984', 'Dystopian', '4.2', 328, 1949),
(4, 'Pride and Prejudice', 'Romance', '4.3', 279, 1813),
(5, 'The Catcher in the Rye', 'Fiction', '3.8', 214, 1951);

SELECT * FROM book;

SELECT title,rating From book ORDER BY RATING ASC;
SELECT title,pub_year From book ORDER BY pub_year ASC LIMIT 5;
SELECT genera, COUNT(*) AS book_count FROM book GROUP BY genera;
SELECT genera, COUNT(*) AS book_count FROM book GROUP BY genera HAVING COUNT(*) > 2;