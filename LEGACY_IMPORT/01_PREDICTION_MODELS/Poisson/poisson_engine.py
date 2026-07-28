# -*- coding: utf-8 -*-

"""
Football AI System V0.8.5
Poisson Probability Engine

功能:
1. 读取历史比赛数据
2. 计算球队攻击强度
3. 计算球队防守强度
4. 生成Poisson参数
5. 保存数据库

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

from config import DATABASE_PATH


def poisson_probability(lam, goals):
    """
    泊松分布概率
    P(X=k)=e^-λ * λ^k / k!
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


    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    print("数据库:", DATABASE_PATH)

    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table'
        """)

    tables = cursor.fetchall()

    print("数据库表:")
    for t in tables:
        print(t)

    # 读取比赛数据
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


    print("读取比赛:", len(matches))


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


    print("球队数量:",len(teams))

    print("比赛数量:", len(matches))
    print("主队进球:", total_home_goals)
    print("客队进球:", total_away_goals)

    # 防止数据库没有读取到比赛导致除0错误
    if len(matches) == 0:
        print("错误：没有读取到比赛数据，请检查数据库表和SQL查询")
        return

    league_attack = (
        total_home_goals + total_away_goals
        ) / len(matches)


    print("联赛平均进球:",league_attack)



    # 创建表

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


    # 清空旧数据

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


    print("生成表:")
    print("poisson_rating")

    conn.close()


    print("==============================")
    print("Poisson Engine完成")
    print("==============================")



if __name__=="__main__":

    calculate_poisson()