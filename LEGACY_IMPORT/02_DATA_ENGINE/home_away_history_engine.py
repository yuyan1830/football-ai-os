import sqlite3

DB_PATH = "data/football.db"


def build_home_away_history():

    print("==============================")
    print("Football AI Home Away History Engine")
    print("==============================")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    matches = cursor.execute("""
    SELECT
        match_date,
        home_team,
        away_team,
        home_score,
        away_score
    FROM matches_clean
    ORDER BY match_date
    """).fetchall()

    print("比赛数量:", len(matches))

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS home_away_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        team TEXT,
        home_games INTEGER,
        home_wins INTEGER,
        home_win_rate REAL,
        home_goals_for REAL,
        home_goals_against REAL,
        away_games INTEGER,
        away_wins INTEGER,
        away_win_rate REAL,
        away_goals_for REAL,
        away_goals_against REAL

    )
    """)

    cursor.execute("DELETE FROM home_away_history")

    teams = {}

    for date, home, away, hs, aws in matches:

        teams.setdefault(home, {
            "home": [],
            "away": []
        })

        teams.setdefault(away, {
            "home": [],
            "away": []
        })


        for team in [home, away]:

            t = teams[team]

            home_games = len(t["home"])
            home_wins = sum(
                1 for x in t["home"] if x["result"]=="W"
            )

            away_games = len(t["away"])
            away_wins = sum(
                1 for x in t["away"] if x["result"]=="W"
            )


            cursor.execute("""
            INSERT INTO home_away_history
            VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                date,
                team,

                home_games,
                home_wins,
                home_wins/max(home_games,1),
                sum(x["gf"] for x in t["home"])/max(home_games,1),
                sum(x["ga"] for x in t["home"])/max(home_games,1),

                away_games,
                away_wins,
                away_wins/max(away_games,1),
                sum(x["gf"] for x in t["away"])/max(away_games,1),
                sum(x["ga"] for x in t["away"])/max(away_games,1)
            ))


        # 更新比赛后的主客场记录

        teams[home]["home"].append({
            "gf": hs,
            "ga": aws,
            "result":
                "W" if hs>aws else
                ("D" if hs==aws else "L")
        })


        teams[away]["away"].append({
            "gf": aws,
            "ga": hs,
            "result":
                "W" if aws>hs else
                ("D" if hs==aws else "L")
        })


    conn.commit()

    print("==============================")
    print("生成表:")
    print("home_away_history")
    print("==============================")

    conn.close()


if __name__ == "__main__":
    build_home_away_history()
