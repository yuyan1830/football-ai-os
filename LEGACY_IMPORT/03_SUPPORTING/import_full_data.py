# -*- coding: utf-8 -*-

import os
import sys
import sqlite3
import pandas as pd


DB_PATH = "data/football.db"

CSV_PATH = "data/raw/full_data.csv"



def create_table():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches_full(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        league TEXT,

        match_date TEXT,

        home_team TEXT,

        away_team TEXT,

        home_score INTEGER,

        away_score INTEGER,

        ht_home_score INTEGER,

        ht_away_score INTEGER,

        home_odds REAL,

        draw_odds REAL,

        away_odds REAL,

        home_possession REAL,

        away_possession REAL,

        home_shots REAL,

        away_shots REAL,

        home_shots_on_goal REAL,

        away_shots_on_goal REAL,

        home_attacks REAL,

        away_attacks REAL,

        home_dangerous_attacks REAL,

        away_dangerous_attacks REAL,

        home_corners REAL,

        away_corners REAL,

        home_yellow REAL,

        away_yellow REAL

    )
    """)


    conn.commit()
    conn.close()



def import_data():

    print("读取CSV...")


    df = pd.read_csv(
        CSV_PATH
    )


    print(
        "比赛数量:",
        len(df)
    )


    # 日期转换

    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%d.%m.%Y",
        errors="coerce"
    )


    print(
        "日期转换完成"
    )


    conn = sqlite3.connect(
        DB_PATH
    )


    print(
        "开始写入数据库..."
    )


    for _, row in df.iterrows():

        conn.execute(
        """
        INSERT INTO matches_full
        (
        league,
        match_date,
        home_team,
        away_team,
        home_score,
        away_score,
        ht_home_score,
        ht_away_score,
        home_odds,
        draw_odds,
        away_odds,
        home_possession,
        away_possession,
        home_shots,
        away_shots,
        home_shots_on_goal,
        away_shots_on_goal,
        home_attacks,
        away_attacks,
        home_dangerous_attacks,
        away_dangerous_attacks,
        home_corners,
        away_corners,
        home_yellow,
        away_yellow
        )

        VALUES
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,

        (

        row.get("League"),

        str(row.get("Date")),

        row.get("Home"),

        row.get("Away"),

        row.get("H_Score"),

        row.get("A_Score"),

        row.get("HT_H_Score"),

        row.get("HT_A_Score"),

        row.get("H_BET"),

        row.get("X_BET"),

        row.get("A_BET"),

        row.get("H_Ball_Possession"),

        row.get("A_Ball_Possession"),

        row.get("H_Goal_Attempts"),

        row.get("A_Goal_Attempts"),

        row.get("H_Shots_on_Goal"),

        row.get("A_Shots_on_Goal"),

        row.get("H_Attacks"),

        row.get("A_Attacks"),

        row.get("H_Dangerous_Attacks"),

        row.get("A_Dangerous_Attacks"),

        row.get("H_Corner_Kicks"),

        row.get("A_Corner_Kicks"),

        row.get("H_Yellow_Cards"),

        row.get("A_Yellow_Cards")

        ))


    conn.commit()

    conn.close()


    print("")
    print("======================")
    print("导入完成")
    print(
        "共导入:",
        len(df),
        "场比赛"
    )
    print("======================")




if __name__=="__main__":

    print(
        "Football AI 数据入库 V0.7.3.2"
    )


    create_table()

    import_data()