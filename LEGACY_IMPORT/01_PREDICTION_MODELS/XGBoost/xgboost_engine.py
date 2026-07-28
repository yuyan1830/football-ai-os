import sqlite3
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier


DATABASE_PATH = "data/football.db"


def load_data():

    conn = sqlite3.connect(DATABASE_PATH)

    sql = """
        SELECT
        home_team,
        away_team,
        home_score AS home_goals,
        away_score AS away_goals
        FROM matches_clean
        """

    df = pd.read_sql(sql, conn)

    conn.close()

    return df



def create_features(df):

    encoder = LabelEncoder()

    teams = pd.concat(
        [
            df["home_team"],
            df["away_team"]
        ]
    )

    encoder.fit(teams)


    df["home_id"] = encoder.transform(
        df["home_team"]
    )

    df["away_id"] = encoder.transform(
        df["away_team"]
    )


    # 比赛结果

    df["result"] = 0

    df.loc[
        df.home_goals > df.away_goals,
        "result"
    ] = 1

    df.loc[
        df.home_goals < df.away_goals,
        "result"
    ] = 2


    X = df[
        [
            "home_id",
            "away_id"
        ]
    ]

    y = df["result"]


    return X,y



def train():

    print("====================")
    print("Football AI XGBoost")
    print("====================")


    df = load_data()

    print(
        "训练数据:",
        len(df)
    )


    X,y=create_features(df)


    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    model=XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05
    )


    model.fit(
        X_train,
        y_train
    )


    pred=model.predict(
        X_test
    )


    acc=accuracy_score(
        y_test,
        pred
    )


    print(
        "准确率:",
        acc
    )


    print(
        "XGBoost完成"
    )


if __name__=="__main__":
    train()