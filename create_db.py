import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('Teams.db')

    sql = """ CREATE TABLE IF NOT EXISTS Matches (
                            Team_1 TEXT,
                            Team_2 TEXT,
                            Team_1_points INTEGER,
                            Team_2_points INTEGER,
                            OT BOOLEAN,
                            Winner BOOLEAN,
                            Neutral BOOLEAN,
                            Type TEXT,
                            Arena TEXT,
                            Date DATE,
                            Season INTEGER,
                            PRIMARY KEY (Team_1, Team_2, Date));
                            """
    c = conn.cursor()
    c.execute(sql)
