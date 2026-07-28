import sqlite3
from datetime import datetime

DB_PATH = "data/football.db"


def days_between(d1, d2):
    try:
        return (d1 - d2).days
    except:
        return 30


def build_fatigue_history():

    print("==============================")
    print("Football AI Fatigue History Engine")
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
    CREATE TABLE IF NOT EXISTS fatigue_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        team TEXT,
        rest_days INTEGER,
        last7_games INTEGER,
        last14_games INTEGER,
        fatigue_score REAL,
        matches INTEGER

    )
    """)

    cursor.execute("DELETE FROM fatigue_history")

    teams = {}

    for date, home, away, hs, aws in matches:

        try:
            current_date = datetime.strptime(
                date[:10],
                "%Y-%m-%d"
            )
        except:
            continue

        teams.setdefault(home, [])
        teams.setdefault(away, [])

        for team in [home, away]:

            history = teams[team]

            if history:
                last_date = history[-1]["date"]
                rest_days = days_between(
                    current_date,
                    last_date
                )
            else:
                rest_days = 30

            last7 = 0
            last14 = 0

            for item in history:

                diff = days_between(
                    current_date,
                    item["date"]
                )

                if diff <= 7:
                    last7 += 1

                if diff <= 14:
                    last14 += 1


            fatigue = (
                last7 * 10 +
                last14 * 5 -
                min(rest_days, 14) * 0.5
            )

            cursor.execute("""
            INSERT INTO fatigue_history
            VALUES(NULL,?,?,?,?,?,?,?)
            """,
            (
                date,
                team,
                rest_days,
                last7,
                last14,
                fatigue,
                len(history)
            ))


        teams[home].append({
            "date": current_date
        })

        teams[away].append({
            "date": current_date
        })


    conn.commit()

    cursor.execute("""
    UPDATE model_data_registry
    SET status='active',
        reason='time_series_version',
        usage='正式模型输入'
    WHERE table_name='fatigue_history'
    """)

    conn.commit()

    print("==============================")
    print("生成表:")
    print("fatigue_history")
    print("==============================")

    conn.close()


if __name__ == "__main__":
    build_fatigue_history()
