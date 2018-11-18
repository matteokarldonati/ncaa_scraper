import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('Teams.db')

    sql = """ CREATE TABLE IF NOT EXISTS Matches (
                            Team_1 NOT NULL TEXT,
                            Team_2 NOT NULL TEXT,
                            Team_1_points NOT NULL INTEGER,
                            Team_2_points NOT NULL INTEGER,
                            OT NOT NULL BOOLEAN,
                            Winner NOT NULL BOOLEAN,
                            Neutral NOT NULL BOOLEAN,
                            Type NOT NULL TEXT,
                            Arena TEXT,
                            Date NOT NULL DATE,
                            Season NOT NULL INTEGER,
                            PRIMARY KEY (Team_1, Team_2, Date));
                            """
    c = conn.cursor()
    c.execute(sql)
