import sqlite3

from model_config import DB_PATH


def build_poisson_history():

    print("==============================")
    print("Football AI Poisson History Engine")
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
    CREATE TABLE IF NOT EXISTS poisson_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        team TEXT,
        attack_strength REAL,
        defense_strength REAL,
        avg_goals REAL,
        matches INTEGER

    )
    """)

    cursor.execute("DELETE FROM poisson_history")

    teams = {}

    for date, home, away, hs, aws in matches:

        teams.setdefault(home, {
            "gf": 0,
            "ga": 0,
            "games": 0
        })

        teams.setdefault(away, {
            "gf": 0,
            "ga": 0,
            "games": 0
        })


        for team in [home, away]:

            t = teams[team]

            avg_goals = (
                (t["gf"] + t["ga"]) /
                max(t["games"], 1)
            )

            attack = (
                t["gf"] /
                max(t["games"], 1)
            )

            defense = (
                t["ga"] /
                max(t["games"], 1)
            )


            cursor.execute("""
            INSERT INTO poisson_history
            VALUES(NULL,?,?,?,?,?,?)
            """,
            (
                date,
                team,
                attack,
                defense,
                avg_goals,
                t["games"]
            ))


        # 比赛结束后更新数据

        teams[home]["gf"] += hs
        teams[home]["ga"] += aws
        teams[home]["games"] += 1


        teams[away]["gf"] += aws
        teams[away]["ga"] += hs
        teams[away]["games"] += 1


    conn.commit()


    # 更新数据注册表

    cursor.execute("""
    UPDATE model_data_registry
    SET status='active',
        reason='time_series_version',
        usage='正式模型输入'
    WHERE table_name='poisson_history'
    """)


    conn.commit()


    print("==============================")
    print("生成表:")
    print("poisson_history")
    print("==============================")

    conn.close()



if __name__ == "__main__":
    build_poisson_history()

