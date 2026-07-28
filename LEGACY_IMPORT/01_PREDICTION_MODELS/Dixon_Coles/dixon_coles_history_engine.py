import sqlite3

DB_PATH = "data/football.db"


def build_dixon_coles_history():

    print("==============================")
    print("Football AI Dixon Coles History Engine")
    print("==============================")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    matches = cursor.execute("""
    SELECT match_date, home_team, away_team, home_score, away_score
    FROM matches_clean
    ORDER BY match_date
    """).fetchall()

    print("比赛数量:", len(matches))

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dixon_coles_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        team TEXT,
        attack_strength REAL,
        defense_strength REAL,
        matches INTEGER
    )
    """)

    cursor.execute("DELETE FROM dixon_coles_history")

    teams = {}

    for date, home, away, hs, aws in matches:

        teams.setdefault(home, {"gf":0, "ga":0, "games":0})
        teams.setdefault(away, {"gf":0, "ga":0, "games":0})

        for team in [home, away]:

            t = teams[team]

            cursor.execute("""
            INSERT INTO dixon_coles_history
            VALUES(NULL,?,?,?,?,?)
            """, (
                date,
                team,
                t["gf"] / max(t["games"], 1),
                t["ga"] / max(t["games"], 1),
                t["games"]
            ))

        teams[home]["gf"] += hs
        teams[home]["ga"] += aws
        teams[home]["games"] += 1

        teams[away]["gf"] += aws
        teams[away]["ga"] += hs
        teams[away]["games"] += 1

    conn.commit()

    print("==============================")
    print("生成表:")
    print("dixon_coles_history")
    print("==============================")

    conn.close()


if __name__ == "__main__":
    build_dixon_coles_history()
