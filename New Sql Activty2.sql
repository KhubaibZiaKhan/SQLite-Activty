CREATE TABLE IF NOT EXISTS Salesman_table (
    Salesman_Id INTEGER,
    Name  Not NULL,
    City NOT NULL,
    Commission Not NULL
);

INSERT INTO Salesman_table VALUES
(1, 'Ali', 'Lahore', '2000'),
(2,'Ahmed', 'Karachi', '2500'),
(3,'Usman', 'Islamabad', '3000'),
(4, 'Omar', 'Faisalabad', '2200'),
(5, 'Zainab', 'Peshawar', '2800');

CREATE TABLE IF NOT EXISTS Customer_table (
    Customer_Id INTEGER,
    Name  Not NULL,
    City NOT NULL,
    Grade Not NULL
);

INSERT INTO Customer_table VALUES
(1, 'Ayesha', 'Lahore', '1'),
(2, 'Sara', 'Karachi', '2'),
(3, 'Hassan', 'Islamabad', '3'),
(4, 'Ali', 'Faisalabad', '4'),
(5,  'Zainab', 'Peshawar', '5');

CREATE TABLE IF NOT EXISTS Orders_table (
    Order_Id INTEGER,
    Order_date  Not NULL,
    Customer_Id NOT NULL,
    Salesman_Id Not NULL
);

INSERT INTO Orders_table VALUES
(1,'2023-01-01', '21', '12'),
(2,'2023-02-15', '22', '13'),
(3,'2023-03-10', '23', '14'),
(4, '2023-04-05', '24', '15'),
(5, '2023-05-20', '25', '16');

SELECT * FROM Salesman_tablE WHERE Salesman_Id IS NULL;

SELECT * FROM Salesman_table WHERE Salesman_Id BETWEEN 1 AND 5;

