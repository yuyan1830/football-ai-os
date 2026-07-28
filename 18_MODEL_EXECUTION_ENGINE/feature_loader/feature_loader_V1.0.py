# -*- coding:utf-8 -*-

import sqlite3


FEATURE_DB=r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"


def load_features(team,date):

    conn=sqlite3.connect(FEATURE_DB)

    cur=conn.cursor()


    tables=[
        "elo_history",
        "dixon_coles_history",
        "poisson_history",
        "team_form_history",
        "fatigue_history",
        "home_away_history",
        "xg_features_history"
    ]


    features={}


    for table in tables:

        try:

            if table=="xg_features_history":

                sql=f"""
                SELECT *
                FROM {table}
                WHERE home_team=?
                OR away_team=?
                ORDER BY date DESC
                LIMIT 1
                """

                cur.execute(sql,(team,team))


            else:

                sql=f"""
                SELECT *
                FROM {table}
                WHERE team=?
                AND date<=?
                ORDER BY date DESC
                LIMIT 1
                """

                cur.execute(sql,(team,date))


            features[table]=cur.fetchone()


        except Exception as e:

            features[table]=str(e)



    conn.close()


    return features



if __name__=="__main__":

    result=load_features(
        "Manchester City",
        "2026-07-01"
    )

    for k,v in result.items():

        print(k,":",v)

