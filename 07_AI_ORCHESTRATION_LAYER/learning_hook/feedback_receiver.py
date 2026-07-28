# -*- coding:utf-8 -*-

import sqlite3
from datetime import datetime


class FeedbackReceiver:


    def __init__(self):

        self.database = (
            r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"
        )

        self.table = "prediction_feedback"



    def receive(self):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()


        cursor.execute(
            f"""
            SELECT
            home_team,
            away_team,
            league,
            decision,
            confidence,
            risk_level,
            model_version

            FROM {self.table}

            ORDER BY id DESC

            LIMIT 1
            """
        )


        row = cursor.fetchone()


        cursor.execute(
            f"""
            SELECT COUNT(*)
            FROM {self.table}
            """
        )


        count = cursor.fetchone()[0]


        conn.close()


        latest = None


        if row:

            latest = {

                "home_team": row[0],
                "away_team": row[1],
                "league": row[2],
                "decision": row[3],
                "confidence": row[4],
                "risk_level": row[5],
                "model_version": row[6]

            }


        return {

            "status":"FEEDBACK_RECEIVED",

            "count":count,

            "latest":latest,

            "time":str(datetime.now())

        }
