# -*- coding: utf-8 -*-

import sqlite3


DB_PATH = "data/football.db"



def clean_matches():

    print("==============================")
    print("Football AI V0.8.2 数据清洗")
    print("==============================")


    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    # 创建清洗表

    cursor.execute("""
    DROP TABLE IF EXISTS matches_clean
    """)


    cursor.execute("""
    CREATE TABLE matches_clean AS

    SELECT *

    FROM matches_full

    WHERE

    home_team IS NOT NULL

    AND away_team IS NOT NULL

    AND home_score IS NOT NULL

    AND away_score IS NOT NULL

    AND league IS NOT NULL

    """)


    conn.commit()



    # 统计清洗后数量

    cursor.execute(
        "SELECT COUNT(*) FROM matches_clean"
    )


    total = cursor.fetchone()[0]


    print(
        "清洗后比赛数量:",
        total
    )



    # 删除数量

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM matches_full
        """
    )

    old_total = cursor.fetchone()[0]


    print(
        "原始数量:",
        old_total
    )


    print(
        "删除异常:",
        old_total-total
    )


    conn.close()


    print("==============================")
    print("数据清洗完成")
    print("==============================")



if __name__ == "__main__":

    clean_matches()