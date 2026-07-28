# -*- coding: utf-8 -*-

import sqlite3


DB_PATH = r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"


def normalize(home, draw, away):

    total = home + draw + away

    return {
        "home": round(home / total, 4),
        "draw": round(draw / total, 4),
        "away": round(away / total, 4)
    }



def get_elo(home, away):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    result = {}

    for team in [home, away]:

        cur.execute(
            """
            SELECT elo
            FROM team_rating
            WHERE team=?
            """,
            (team,)
        )

        row = cur.fetchone()

        result[team] = row[0] if row else 1500


    conn.close()


    diff = result[home] - result[away]


    home_prob = 1 / (1 + 10 ** (-diff / 400))


    return normalize(
        home_prob,
        0.25,
        1 - home_prob
    )



def get_dixon(home, away):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    data = {}

    for team in [home, away]:

        cur.execute(
            """
            SELECT
            attack_strength,
            defense_strength
            FROM dixon_coles_rating
            WHERE team=?
            """,
            (team,)
        )

        row = cur.fetchone()

        data[team] = row if row else (1,1)


    conn.close()


    diff = data[home][0] - data[away][0]


    home_prob = 0.5 + diff * 0.05


    return normalize(
        max(min(home_prob,0.8),0.2),
        0.25,
        max(min(1-home_prob,0.8),0.2)
    )



def get_poisson(home, away):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    data = {}

    for team in [home, away]:

        cur.execute(
            """
            SELECT
            attack_strength,
            defense_strength
            FROM poisson_rating
            WHERE team=?
            """,
            (team,)
        )

        row = cur.fetchone()

        data[team] = row if row else (1,1)


    conn.close()


    diff = data[home][0] - data[away][0]


    home_prob = 0.5 + diff * 0.05


    return normalize(
        max(min(home_prob,0.8),0.2),
        0.25,
        max(min(1-home_prob,0.8),0.2)
    )



def get_xgb(home, away):

    return {

        "home":0.47,
        "draw":0.29,
        "away":0.24

    }



def run_models(home, away):

    return {

        "elo":
            get_elo(home, away),

        "dixon":
            get_dixon(home, away),

        "poisson":
            get_poisson(home, away),

        "xgb":
            get_xgb(home, away)

    }
