import sqlite3
from datetime import datetime

DB_PATH = "data/football.db"


def calculate_home_away():

    print("==============================")
    print("Football AI Home Away Engine")
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

    teams = {}

    for date, home, away, hs, aws in matches:

        teams.setdefault(home, {"home": [], "away": []})
        teams.setdefault(away, {"home": [], "away": []})

        if hs > aws:
            hp, ap = 3, 0
        elif hs == aws:
            hp, ap = 1, 1
        else:
            hp, ap = 0, 3

        teams[home]["home"].append({
            "gf": hs,
            "ga": aws,
            "points": hp
        })

        teams[away]["away"].append({
            "gf": aws,
            "ga": hs,
            "points": ap
        })

    print("球队数量:", len(teams))

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS home_away_rating(

        team TEXT PRIMARY KEY,

        home_games INTEGER,
        home_wins INTEGER,
        home_draws INTEGER,
        home_losses INTEGER,
        home_win_rate REAL,

        home_goals_for REAL,
        home_goals_against REAL,

        home_attack_strength REAL,
        home_defense_strength REAL,

        away_games INTEGER,
        away_wins INTEGER,
        away_draws INTEGER,
        away_losses INTEGER,
        away_win_rate REAL,

        away_goals_for REAL,
        away_goals_against REAL,

        away_attack_strength REAL,
        away_defense_strength REAL,

        update_time TEXT
    )
    """)

    cursor.execute("DELETE FROM home_away_rating")

    for team, data in teams.items():

        home = data["home"]
        away = data["away"]

        hg = len(home)
        ag = len(away)

        hw = sum(1 for x in home if x["points"] == 3)
        hd = sum(1 for x in home if x["points"] == 1)
        hl = sum(1 for x in home if x["points"] == 0)

        aw = sum(1 for x in away if x["points"] == 3)
        ad = sum(1 for x in away if x["points"] == 1)
        al = sum(1 for x in away if x["points"] == 0)

        cursor.execute("""
        INSERT INTO home_away_rating VALUES
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            team,

            hg,
            hw,
            hd,
            hl,
            hw / max(hg, 1),

            sum(x["gf"] for x in home) / max(hg, 1),
            sum(x["ga"] for x in home) / max(hg, 1),

            sum(x["gf"] for x in home) / max(hg, 1),
            sum(x["ga"] for x in home) / max(hg, 1),

            ag,
            aw,
            ad,
            al,
            aw / max(ag, 1),

            sum(x["gf"] for x in away) / max(ag, 1),
            sum(x["ga"] for x in away) / max(ag, 1),

            sum(x["gf"] for x in away) / max(ag, 1),
            sum(x["ga"] for x in away) / max(ag, 1),

            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

    conn.commit()

    print("==============================")
    print("生成表:")
    print("home_away_rating")
    print("==============================")

    conn.close()


if __name__ == "__main__":
    calculate_home_away()
