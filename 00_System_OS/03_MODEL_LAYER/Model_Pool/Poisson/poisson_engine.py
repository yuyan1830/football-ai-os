# -*- coding: utf-8 -*-

"""
Football AI System V0.8.5
Poisson Probability Engine

鍔熻兘:
1. 璇诲彇鍘嗗彶姣旇禌鏁版嵁
2. 璁＄畻鐞冮槦鏀诲嚮寮哄害
3. 璁＄畻鐞冮槦闃插畧寮哄害
4. 鐢熸垚Poisson鍙傛暟
5. 淇濆瓨鏁版嵁搴?

"""

import sqlite3
import os
import math
from datetime import datetime


import sys

ROOT_PATH = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(ROOT_PATH)

from model_config import DB_PATH


def poisson_probability(lam, goals):
    """
    娉婃澗鍒嗗竷姒傜巼
    P(X=k)=e^-位 * 位^k / k!
    """

    return (
        math.exp(-lam)
        * pow(lam, goals)
        / math.factorial(goals)
    )


def calculate_poisson():

    print("==============================")
    print("Football AI V0.8.5 Poisson")
    print("==============================")


    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    print("鏁版嵁搴?", DB_PATH)

    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table'
        """)

    tables = cursor.fetchall()

    print("鏁版嵁搴撹〃:")
    for t in tables:
        print(t)

    # 璇诲彇姣旇禌鏁版嵁
    cursor.execute("""
        SELECT
            home_team,
            away_team,
            home_score,
            away_score
        FROM matches_clean
        WHERE home_score IS NOT NULL
    """)

    matches = cursor.fetchall()


    print("璇诲彇姣旇禌:", len(matches))


    teams = {}

    total_home_goals = 0
    total_away_goals = 0


    for home, away, hs, aws in matches:


        if home not in teams:
            teams[home]={
                "gf":0,
                "ga":0,
                "games":0
            }


        if away not in teams:
            teams[away]={
                "gf":0,
                "ga":0,
                "games":0
            }


        teams[home]["gf"] += hs
        teams[home]["ga"] += aws
        teams[home]["games"] += 1


        teams[away]["gf"] += aws
        teams[away]["ga"] += hs
        teams[away]["games"] += 1


        total_home_goals += hs
        total_away_goals += aws


    print("鐞冮槦鏁伴噺:",len(teams))

    print("姣旇禌鏁伴噺:", len(matches))
    print("涓婚槦杩涚悆:", total_home_goals)
    print("瀹㈤槦杩涚悆:", total_away_goals)

    # 闃叉鏁版嵁搴撴病鏈夎鍙栧埌姣旇禌瀵艰嚧闄?閿欒
    if len(matches) == 0:
        print("閿欒锛氭病鏈夎鍙栧埌姣旇禌鏁版嵁锛岃妫€鏌ユ暟鎹簱琛ㄥ拰SQL鏌ヨ")
        return

    league_attack = (
        total_home_goals + total_away_goals
        ) / len(matches)


    print("鑱旇禌骞冲潎杩涚悆:",league_attack)



    # 鍒涘缓琛?

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS poisson_rating(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        team TEXT,

        attack_strength REAL,

        defense_strength REAL,

        avg_goals REAL,

        update_time TEXT

    )
    """)


    # 娓呯┖鏃ф暟鎹?

    cursor.execute(
        "DELETE FROM poisson_rating"
    )



    for team,data in teams.items():


        avg_gf = (
            data["gf"]
            /
            data["games"]
        )


        avg_ga = (
            data["ga"]
            /
            data["games"]
        )


        attack = (
            avg_gf /
            league_attack
        )


        defense = (
            avg_ga /
            league_attack
        )


        cursor.execute("""
        INSERT INTO poisson_rating
        VALUES(
        NULL,
        ?,
        ?,
        ?,
        ?,
        ?
        )
        """,
        (
            team,
            attack,
            defense,
            avg_gf,
            datetime.now()
        ))



    conn.commit()


    print("鐢熸垚琛?")
    print("poisson_rating")

    conn.close()


    print("==============================")
    print("Poisson Engine瀹屾垚")
    print("==============================")



if __name__=="__main__":

    calculate_poisson()
