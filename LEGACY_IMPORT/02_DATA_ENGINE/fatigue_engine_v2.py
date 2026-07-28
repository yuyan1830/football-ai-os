import sqlite3
from datetime import datetime

DB_PATH = "data/football.db"


def parse_date(value):
    """
    支持:
    YYYY-MM-DD
    YYYY-MM-DD HH:MM:SS
    """
    value = str(value)

    if " " in value:
        value = value.split(" ")[0]

    return datetime.strptime(value, "%Y-%m-%d")


def calculate_fatigue():

    print("==============================")
    print("Football AI Fatigue Engine")
    print("==============================")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    matches = cursor.execute("""
    SELECT
        match_date,
        home_team,
        away_team
    FROM matches_clean
    ORDER BY match_date
    """).fetchall()

    print("比赛数量:", len(matches))

    teams = {}

    for date, home, away in matches:

        teams.setdefault(home, [])
        teams.setdefault(away, [])

        teams[home].append(date)
        teams[away].append(date)


    print("球队数量:", len(teams))


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fatigue_rating(

        team TEXT PRIMARY KEY,

        last_match_date TEXT,
        rest_days INTEGER,

        recent_7_days_games INTEGER,
        recent_30_days_games INTEGER,

        fatigue_score REAL,

        update_time TEXT

    )
    """)


    cursor.execute("DELETE FROM fatigue_rating")


    all_dates = [
        parse_date(x[0])
        for x in matches
    ]

    current_date = max(all_dates)


    for team, dates in teams.items():

        dates = sorted(
            dates,
            key=lambda x: parse_date(x)
        )

        last_date = dates[-1]

        last_match = parse_date(last_date)


        rest_days = (
            current_date - last_match
        ).days


        recent_7 = 0
        recent_30 = 0


        for d in dates:

            diff = (
                current_date - parse_date(d)
            ).days


            if diff <= 7:
                recent_7 += 1

            if diff <= 30:
                recent_30 += 1


        fatigue_score = (
            recent_7 * 0.6
            +
            recent_30 * 0.2
            -
            rest_days * 0.05
        )


        cursor.execute("""
        INSERT INTO fatigue_rating VALUES
        (?,?,?,?,?,?,?)
        """,
        (
            team,
            last_date,
            rest_days,
            recent_7,
            recent_30,
            fatigue_score,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))


    conn.commit()

    print("==============================")
    print("生成表:")
    print("fatigue_rating")
    print("==============================")

    conn.close()


if __name__ == "__main__":
    calculate_fatigue()
