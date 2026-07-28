# -*- coding:utf-8 -*-

import sqlite3


MODEL_DB=r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"



def query_one(table,team,date):

    conn=sqlite3.connect(MODEL_DB)

    cur=conn.cursor()

    result={}


    if table=="elo_history":

        cur.execute(
        """
        SELECT elo_home,elo_away
        FROM elo_history
        WHERE team=?
        AND created_time<=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (team,date)
        )

        row=cur.fetchone()

        if row:
            result={
                "elo_before":row[0],
                "elo_after":row[1]
            }


    elif table=="dixon_coles_history":

        cur.execute(
        """
        SELECT attack,defense
        FROM dixon_coles_history
        WHERE team=?
        AND created_time<=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (team,date)
        )

        row=cur.fetchone()

        if row:
            result={
                "attack":row[0],
                "defense":row[1]
            }


    elif table=="poisson_history":

        cur.execute(
        """
        SELECT lambda
        FROM poisson_history
        WHERE team=?
        AND created_time<=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (team,date)
        )

        row=cur.fetchone()

        if row:
            result={
                "lambda":row[0]
            }


    conn.close()

    return result



def load_features(home,away,date):


    return {

        "home_team":home,

        "away_team":away,

        "date":date,


        "home":{

            "elo":
            query_one(
                "elo_history",
                home,
                date
            ),

            "dixon_coles":
            query_one(
                "dixon_coles_history",
                home,
                date
            ),

            "poisson":
            query_one(
                "poisson_history",
                home,
                date
            )

        },


        "away":{

            "elo":
            query_one(
                "elo_history",
                away,
                date
            ),

            "dixon_coles":
            query_one(
                "dixon_coles_history",
                away,
                date
            ),

            "poisson":
            query_one(
                "poisson_history",
                away,
                date
            )

        }

    }



if __name__=="__main__":


    result=load_features(
        "Manchester City",
        "Aston Villa",
        "2022-08-17 00:00:00"
    )


    print(result)

