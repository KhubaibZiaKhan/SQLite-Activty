import sqlite3
import pandas as pd

conn = sqlite3.connect('cricket_data.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;
    
Create Table Team (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT
);

Create Table Match (
    match_id INTEGER PRIMARY KEY,
    Season_id INTEGER,
    Match_Winner INTEGER,
    Win_Margin INTEGER,
);

Create Table Player_Match (
    Match_id INTEGER,                 
    Player_id INTEGER,
);

INSERT INTO Team (team_id, team_name) VALUES
(1, 'India'),
(2, 'Australia'),
(3, 'England'),
(4, 'South Africa'),
(5, 'New Zealand'),
(6, 'Pakistan'),
(7, 'Sri Lanka'),
(8, 'West Indies');

INSERT INTO Match (match_id, Season_id, Match_Winner, Win_Margin) VALUES
(1, 2020, 1, 50),
(2, 2020, 2, 30),
(3, 2020, 3, 20),
(4, 2020, 4, 10),
(5, 2020, 5, 40),
(6, 2020, 6, 60),
(7, 2020, 7, 70),
(8, 2020, 8, 80);

INSERT INTO Player_Match (Match_id, Player_id) VALUES
(1, 101),
(1, 102),
(2, 103),
(2, 104),
(3, 105),
(3, 106),
(4, 107),
(4, 108),
(5, 109),
(5, 110),
(6, 111),
(6, 112),
(7, 113),
(7, 114),
(8, 115),
(8, 116);
""")         

conn.commit()
print('Database ready!')

teams = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(teams)

matches = pd.read_sql_query("SELECT * FROM Match;", conn)
print(matches)
print('Rows and Columns:', matches.shape)


