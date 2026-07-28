import sqlite3
from datetime import datetime

DB_PATH = "data/football.db"


def calculate_form():

    print("==============================")
    print("Football AI Team Form Engine")
    print("==============================")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    sql = """
    SELECT
        match_date,
        home_team,
        away_team,
        home_score,
        away_score
    FROM matches_clean
    ORDER BY match_date
    """

    matches = cursor.execute(sql).fetchall()

    print("比赛数量:", len(matches))

    teams = {}

    for date, home, away, hs, aws in matches:

        teams.setdefault(home, [])
        teams.setdefault(away, [])

        if hs > aws:
            home_result = 3
            away_result = 0
        elif hs == aws:
            home_result = 1
            away_result = 1
        else:
            home_result = 0
            away_result = 3

        teams[home].append({
            "date": date,
            "gf": hs,
            "ga": aws,
            "points": home_result
        })

        teams[away].append({
            "date": date,
            "gf": aws,
            "ga": hs,
            "points": away_result
        })

    print("球队数量:", len(teams))

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS team_form(

        team TEXT PRIMARY KEY,

        last5_games INTEGER,
        last5_win INTEGER,
        last5_draw INTEGER,
        last5_loss INTEGER,

        last5_goals_for REAL,
        last5_goals_against REAL,

        last10_games INTEGER,
        last10_points REAL,

        avg_goals REAL,
        avg_conceded REAL,

        update_time TEXT
    )
    """)

    cursor.execute("DELETE FROM team_form")

    for team, games in teams.items():

        games = sorted(games, key=lambda x: x["date"])

        last5 = games[-5:]
        last10 = games[-10:]

        win = sum(1 for g in last5 if g["points"] == 3)
        draw = sum(1 for g in last5 if g["points"] == 1)
        loss = sum(1 for g in last5 if g["points"] == 0)

        goals_for = sum(g["gf"] for g in last5)
        goals_against = sum(g["ga"] for g in last5)

        points10 = sum(g["points"] for g in last10)

        avg_goals = sum(g["gf"] for g in games) / len(games)
        avg_conceded = sum(g["ga"] for g in games) / len(games)

        cursor.execute("""
        INSERT INTO team_form VALUES
        (?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            team,
            len(last5),
            win,
            draw,
            loss,
            goals_for / max(len(last5), 1),
            goals_against / max(len(last5), 1),
            len(last10),
            points10,
            avg_goals,
            avg_conceded,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

    conn.commit()

    print("==============================")
    print("生成表:")
    print("team_form")
    print("==============================")

    conn.close()


if __name__ == "__main__":
    calculate_form()
