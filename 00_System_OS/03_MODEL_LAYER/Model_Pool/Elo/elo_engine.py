# -*- coding: utf-8 -*-

import sqlite3
from collections import defaultdict


from model_config import DB_PATH



def calculate_elo():


    print("==============================")
    print("Football AI V0.8.3 Elo Engine")
    print("==============================")


    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        match_date,
        home_team,
        away_team,
        home_score,
        away_score

        FROM matches_clean

        ORDER BY match_date
        """
    )


    matches = cursor.fetchall()


    print(
        "读取比赛:",
        len(matches)
    )



    elo = defaultdict(lambda:1500)


    history=[]


    K = 30

    HOME_ADVANTAGE = 60



    for match in matches:


        date, home, away, hg, ag = match


        home_before = elo[home]

        away_before = elo[away]



        # 主场修正

        home_rating = home_before + HOME_ADVANTAGE


        expected_home = (
            1 /
            (
            1 +
            10 ** (
            (away_before-home_rating)/400
            )
            )
        )


        expected_away = 1-expected_home



        # 结果

        if hg > ag:

            result_home = 1

            result_away = 0


        elif hg == ag:

            result_home = 0.5

            result_away = 0.5


        else:

            result_home = 0

            result_away = 1



        # 更新

        elo[home] += K * (
            result_home-expected_home
        )


        elo[away] += K * (
            result_away-expected_away
        )



        history.append(
            (
            date,
            home,
            home_before,
            elo[home],
            away,
            away_before,
            elo[away]
            )
        )



    print(
        "Elo计算完成"
    )



    # 删除旧表

    cursor.execute(
        "DROP TABLE IF EXISTS elo_history"
    )


    cursor.execute(
    """
    CREATE TABLE elo_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        team TEXT,

        elo_before REAL,

        elo_after REAL,

        opponent TEXT

    )
    """
    )



    for row in history:


        date,home,hb,ha,away,ab,aa=row


        cursor.execute(
        """
        INSERT INTO elo_history

        (
        date,
        team,
        elo_before,
        elo_after,
        opponent
        )

        VALUES (?,?,?,?,?)
        """,
        (
        date,
        home,
        hb,
        ha,
        away
        )
        )


        cursor.execute(
        """
        INSERT INTO elo_history

        (
        date,
        team,
        elo_before,
        elo_after,
        opponent
        )

        VALUES (?,?,?,?,?)
        """,
        (
        date,
        away,
        ab,
        aa,
        home
        )
        )



    # 当前排名表


    cursor.execute(
        "DROP TABLE IF EXISTS team_rating"
    )


    cursor.execute(
    """
    CREATE TABLE team_rating(

        team TEXT PRIMARY KEY,

        elo REAL

    )
    """
    )



    for team,rating in elo.items():

        cursor.execute(
        """
        INSERT INTO team_rating

        VALUES (?,?)
        """,
        (
        team,
        rating
        )
        )



    conn.commit()

    conn.close()



    print(
        "生成表:"
    )

    print(
        "elo_history"
    )

    print(
        "team_rating"
    )


    print("==============================")
    print("Elo Engine 完成")
    print("==============================")



if __name__=="__main__":

    calculate_elo()
