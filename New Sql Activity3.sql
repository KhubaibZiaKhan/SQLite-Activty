CREATE TABLE IF NOT EXISTS Resturant (
  Name TEXT,
  Neighborhood TEXT,
  cuisine TEXT,
  review REAL,
  price TEXT,
  health TEXT
  );

  INSERT INTO Resturant (Name, Neighborhood, cuisine, review, price, health) VALUES
  ('The Gourmet Kitchen', 'Downtown', 'Italian', 4.5, '$$$', 'A'),
  ('Sushi World', 'Uptown', 'Japanese', 4.7, '$$$$', 'A'),
  ('Taco Fiesta', 'Midtown', 'Mexican', 4.2, '$$', 'B'),
  ('Burger Haven', 'Suburbs', 'American', 4.0, '$', 'C'),
  ('Curry Palace', 'Downtown', 'Indian', 4.3, '$$$', 'A');
  
  SELECT DISTINCT Neighborhood FROM Resturant;

  SELECT DISTINCT cuisine FROM Resturant;

  SELECT *
  FROM Resturant
    WHERE cuisine = 'Chinese';

  SELECT * FROM Resturant
    WHERE review >= 4.5;

    SELECT *
    FROM Resturant
    WHERE cuisine = 'Italian' AND price IN ('$$','$$$');

    SELECT *
    FROM Resturant
    WHERE price = '$$$';

    SELECT *
    FROM Resturant
    WHERE name LIKE '%Candy%';

    SELECT *
    FROM Resturant
    WHERE neighborhood IN ('Downtown', 'Uptown', 'Midtown');

    SELECT *
    FROM Resturant
    WHERE health = '' OR health IS NULL;

    SELECT *
    FROM Resturant
    ORDER BY review DESC
    LIMIT 5;
    
    