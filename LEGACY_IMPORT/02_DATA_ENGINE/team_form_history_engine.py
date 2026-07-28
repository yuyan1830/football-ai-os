import sqlite3

DB_PATH = "data/football.db"


def build_team_form_history():

    print("==============================")
    print("Football AI Team Form History Engine")
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
    CREATE TABLE IF NOT EXISTS team_form_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        team TEXT,
        last5_win INTEGER,
        last5_draw INTEGER,
        last5_loss INTEGER,
        last5_goals_for INTEGER,
        last5_goals_against INTEGER,
        last10_points INTEGER,
        matches INTEGER

    )
    """)

    cursor.execute("DELETE FROM team_form_history")

    teams = {}

    for date, home, away, hs, aws in matches:

        teams.setdefault(home, [])
        teams.setdefault(away, [])

        for team in [home, away]:

            history = teams[team]

            last5 = history[-5:]
            last10 = history[-10:]

            wins = 0
            draws = 0
            losses = 0
            gf = 0
            ga = 0
            points = 0

            for h in last5:

                if h["team"] == team:
                    gf += h["gf"]
                    ga += h["ga"]

                    if h["result"] == "W":
                        wins += 1
                    elif h["result"] == "D":
                        draws += 1
                    else:
                        losses += 1


            for h in last10:

                if h["team"] == team:

                    if h["result"] == "W":
                        points += 3
                    elif h["result"] == "D":
                        points += 1


            cursor.execute("""
            INSERT INTO team_form_history
            VALUES(NULL,?,?,?,?,?,?,?,?,?)
            """,
            (
                date,
                team,
                wins,
                draws,
                losses,
                gf,
                ga,
                points,
                len(history)
            ))


        # 更新比赛结果

        teams[home].append({
            "team": home,
            "gf": hs,
            "ga": aws,
            "result": "W" if hs > aws else ("D" if hs == aws else "L")
        })

        teams[away].append({
            "team": away,
            "gf": aws,
            "ga": hs,
            "result": "W" if aws > hs else ("D" if hs == aws else "L")
        })


    conn.commit()

    print("==============================")
    print("生成表:")
    print("team_form_history")
    print("==============================")

    conn.close()


if __name__ == "__main__":
    build_team_form_history()
