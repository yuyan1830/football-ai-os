# -*- coding: utf-8 -*-

import sqlite3
import json
from datetime import datetime


DB_PATH=r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"


def save_prediction(
    match_id,
    model_name,
    prediction,
    probability
):

    conn=sqlite3.connect(DB_PATH)

    cursor=conn.cursor()


    cursor.execute(
    """
    INSERT INTO prediction_history
    (
        match_id,
        model_name,
        prediction,
        probability,
        created_time
    )
    VALUES
    (?,?,?,?,?)
    """,
    (
        match_id,
        model_name,
        json.dumps(
            prediction,
            ensure_ascii=False
        ),
        probability,
        datetime.now().isoformat()
    )
    )


    conn.commit()

    conn.close()


    return True



if __name__=="__main__":


    data={

        "home_win_probability":0.425,
        "draw_probability":0.2675,
        "away_win_probability":0.3075

    }


    save_prediction(
        1,
        "FUSION",
        data,
        0.425
    )


    print(
    {
        "module":"Output Manager",
        "status":"SAVED"
    }
    )
