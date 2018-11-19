import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('Teams.db')

    sql = """ CREATE TABLE IF NOT EXISTS Scores (
                            Team_1 TEXT NOT NULL,
                            Team_2 TEXT NOT NULL,
                            Team_1_points INTEGER NOT NULL,
                            Team_2_points INTEGER NOT NULL,
                            OT BOOLEAN NOT NULL,
                            Winner BOOLEAN NOT NULL,
                            Neutral BOOLEAN NOT NULL,
                            Type TEXT NOT NULL,
                            Arena TEXT NOT NULL,
                            Date DATE NOT NULL,
                            Season INTEGER NOT NULL,
                            PRIMARY KEY (Team_1, Team_2, Date));
                            """
    c = conn.cursor()
    c.execute(sql)
