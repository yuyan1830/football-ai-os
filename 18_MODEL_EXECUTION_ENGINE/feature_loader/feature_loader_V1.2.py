# -*- coding:utf-8 -*-

import sqlite3


FEATURE_DB=r"E:\football_v\00_System_OS\02_FEATURE_LAYER\database\feature_store.db"



def get_feature(table,team,date):

    conn=sqlite3.connect(FEATURE_DB)

    cur=conn.cursor()


    result=None


    if table=="elo_history":

        cur.execute(
        """
        SELECT elo
        FROM elo_history
        WHERE team=?
        AND created_time<=?
        ORDER BY created_time DESC
        LIMIT 1
        """,
        (team,date)
        )

        row=cur.fetchone()

        if row:
            result={"elo":row[0]}


    elif table=="dixon_coles_history":

        cur.execute(
        """
        SELECT attack,defense
        FROM dixon_coles_history
        WHERE team=?
        AND created_time<=?
        ORDER BY created_time DESC
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
        ORDER BY created_time DESC
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

        "home":{
            "elo":
            get_feature(
                "elo_history",
                home,
                date
            ),

            "dixon":
            get_feature(
                "dixon_coles_history",
                home,
                date
            ),

            "poisson":
            get_feature(
                "poisson_history",
                home,
                date
            )
        },


        "away":{
            "elo":
            get_feature(
                "elo_history",
                away,
                date
            ),

            "dixon":
            get_feature(
                "dixon_coles_history",
                away,
                date
            ),

            "poisson":
            get_feature(
                "poisson_history",
                away,
                date
            )
        }

    }



if __name__=="__main__":


    print(
        load_features(
            "Manchester City",
            "Aston Villa",
            "2026-07-01"
        )
    )
