# -*- coding:utf-8 -*-

import sqlite3
import json
from datetime import datetime


class FeedbackConnector:


    def __init__(self):

        self.database = (
            r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"
        )

        self.table = "prediction_feedback"



    def feedback(self, data):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()


        match=data.get("match",{})

        prediction=data.get("prediction",{})

        risk=data.get("risk",{})

        odds=match.get("odds",{})


        sql="""

        INSERT INTO prediction_feedback
        (
        prediction_time,
        home_team,
        away_team,
        league,
        prediction_home,
        prediction_draw,
        prediction_away,
        decision,
        actual_result,
        correct,
        odds_home,
        odds_draw,
        odds_away,
        roi,
        confidence,
        risk_level,
        model_version,
        created_time
        )

        VALUES
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

        """


        values=(

            data.get(
                "time",
                str(datetime.now())
            ),

            match.get("home_team"),

            match.get("away_team"),

            match.get("league"),

            prediction.get("home_win"),

            prediction.get("draw"),

            prediction.get("away_win"),

            data.get("decision"),

            None,

            None,

            odds.get("home"),

            odds.get("draw"),

            odds.get("away"),

            None,

            risk.get("confidence"),

            risk.get("level"),

            data.get("version"),

            str(datetime.now())

        )


        cursor.execute(sql,values)

        conn.commit()

        conn.close()


        return {

            "status":"FEEDBACK_STORED",

            "table":self.table,

            "time":str(datetime.now())

        }
