# -*- coding: utf-8 -*-

import sqlite3
import math
from collections import defaultdict


DB_PATH = "data/football.db"



def calculate_dixon_coles():


    print("==============================")
    print("Football AI V0.8.4 Dixon-Coles")
    print("==============================")


    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT
    home_team,
    away_team,
    home_score,
    away_score,
    match_date

    FROM matches_clean

    ORDER BY match_date
    """)


    matches = cursor.fetchall()


    print(
        "读取比赛:",
        len(matches)
    )


    teams = set()


    for m in matches:

        teams.add(m[0])
        teams.add(m[1])



    print(
        "球队数量:",
        len(teams)
    )



    # 初始化攻防参数

    attack = defaultdict(lambda:1.0)

    defense = defaultdict(lambda:1.0)


    games = defaultdict(int)



    # 简化Dixon-Coles迭代计算

    for home,away,hg,ag,date in matches:


        if hg is None or ag is None:
            continue



        games[home]+=1
        games[away]+=1



        # 攻击调整

        attack[home] += (
            hg-1
        )*0.002


        attack[away] += (
            ag-1
        )*0.002



        # 防守调整

        defense[home] += (
            1-ag
        )*0.002


        defense[away] += (
            1-hg
        )*0.002



    print(
        "攻防参数计算完成"
    )



    cursor.execute(
        "DROP TABLE IF EXISTS dixon_coles_rating"
    )



    cursor.execute("""
    CREATE TABLE dixon_coles_rating(

        team TEXT PRIMARY KEY,

        attack_strength REAL,

        defense_strength REAL,

        matches INTEGER

    )
    """)



    for team in teams:


        cursor.execute("""
INSERT INTO dixon_coles_rating

VALUES (?,?,?,?)

""",
(
team,
round(attack[team],4),
round(defense[team],4),
games[team]
)
)



    conn.commit()

    conn.close()



    print(
        "生成表:"
    )

    print(
        "dixon_coles_rating"
    )


    print("==============================")
    print("Dixon-Coles 完成")
    print("==============================")



if __name__=="__main__":

    calculate_dixon_coles()