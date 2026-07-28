# -*- coding: utf-8 -*-

import os
import sys
import sqlite3
import pandas as pd


# ������Ŀ·��

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


DB_PATH = "data/football.db"

DATA_PATH = "data/raw/full_data.csv"



def check_file():

    if not os.path.exists(DATA_PATH):

        print(
            "û���ҵ�CSV�ļ�:",
            DATA_PATH
        )

        return False

    return True



def create_matches_table():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS matches(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        league TEXT,

        season TEXT,

        home_team TEXT,

        away_team TEXT,

        home_score INTEGER,

        away_score INTEGER

    )
    """
    )


    conn.commit()
    conn.close()



def import_csv():


    print(
        "��ȡCSV..."
    )


    df=pd.read_csv(
        DATA_PATH
    )


    print(
        "�ֶ�:"
    )

    print(
        list(df.columns)
    )


    print(
        "������:",
        len(df)
    )



    print(
        "��һ�������ֶ��Զ�ӳ��"
    )



if __name__=="__main__":


    print(
        "Football AI �������ݵ��� V0.7.3.1"
    )


    if check_file():

        create_matches_table()

        import_csv()