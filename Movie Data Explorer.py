import sqlite3
import pandas as pd
conn = sqlite3.connect('movie_data.db')
cursor = conn.cursor()
cursor.executescript("""

DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Movie_Actor;
CREATE TABLE Movie (
    Movie_id INTEGER PRIMARY KEY,
    Title TEXT,
    Genre TEXT,
    Year INTEGER,
    Rating Real,
    Duration INTEGER
);
CREATE TABLE Actor (
    Actor_id INTEGER PRIMARY KEY,
    Actor_Name TEXT,
    Birth_Year INTEGER,
    country TEXT
);
CREATE TABLE Movie_Actor (
    Movie_id INTEGER,
    Actor_id INTEGER
);
INSERT INTO Movie (Movie_id, Title, Genre, Year, Rating, Duration) VALUES
(1, 'Inception', 'Sci-Fi', 2010, 8.8, 148),
(2, 'The Dark Knight', 'Action', 2008, 9.0, 152),
(3, 'Interstellar', 'Sci-Fi', 2014, 8.6, 169),
(4, 'The Matrix', 'Sci-Fi', 1999, 8.7, 136),
(5, 'Pulp Fiction', 'Crime', 1994, 8.9, 154),
(6, 'The Shawshank Redemption', 'Drama', 1994, 9.3, 142),
(7, 'The Godfather', 'Crime', 1972, 9.2, 175),
(8, 'The Lord of the Rings: The Return of the King', 'Fantasy', 2003, 8.9, 201);

INSERT INTO Actor (Actor_id, Actor_Name, Birth_Year, country) VALUES
(1, 'Leonardo DiCaprio', 1974, 'USA'),
(2, 'Christian Bale', 1974, 'UK'),
(3, 'Matthew McConaughey', 1969, 'USA'),
(4, 'Keanu Reeves', 1964, 'Canada'),
(5, 'John Travolta', 1954, 'USA'),
(6, 'Morgan Freeman', 1937, 'USA'),
(7, 'Marlon Brando', 1924, 'USA'),
(8, 'Elijah Wood', 1981, 'USA');

INSERT INTO Movie_Actor (Movie_id, Actor_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);

""")

conn.commit()
print('Database Ready!')

genres = pd.read_sql("""SELECT DISTINCT (Genre) FROM Movie""", conn)
print(genres)
top_movies = pd.read_sql("""SELECT Title, Rating FROM Movie ORDER BY Rating DESC LIMIT 5""", conn)
print(top_movies)

action_count = pd.read_sql("""SELECT COUNT(*) as Action_Movie_Count FROM Movie WHERE Genre = 'Action'""", conn)
print(action_count)

avg_rating = pd.read_sql("""SELECT AVG(Rating) as Average_Rating FROM Movie""", conn)
print(avg_rating)