import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


DB_PATH = "data/football.db"


def load_data():

    conn = sqlite3.connect(DB_PATH)

    sql = """
    SELECT
        m.home_team,
        m.away_team,
        m.home_score,
        m.away_score,

        tf1.last5_win AS home_last5_win,
        tf1.last5_draw AS home_last5_draw,
        tf1.last5_loss AS home_last5_loss,
        tf1.last5_goals_for AS home_form_attack,
        tf1.last5_goals_against AS home_form_defense,
        tf1.last10_points AS home_points10,

        tf2.last5_win AS away_last5_win,
        tf2.last5_draw AS away_last5_draw,
        tf2.last5_loss AS away_last5_loss,
        tf2.last5_goals_for AS away_form_attack,
        tf2.last5_goals_against AS away_form_defense,
        tf2.last10_points AS away_points10,

        ha1.home_win_rate,
        ha1.home_goals_for,
        ha1.home_goals_against,

        ha2.away_win_rate,
        ha2.away_goals_for,
        ha2.away_goals_against,

        f1.rest_days AS home_rest_days,
        f1.fatigue_score AS home_fatigue,

        f2.rest_days AS away_rest_days,
        f2.fatigue_score AS away_fatigue

    FROM matches_clean m

    LEFT JOIN team_form tf1
    ON m.home_team=tf1.team

    LEFT JOIN team_form tf2
    ON m.away_team=tf2.team

    LEFT JOIN home_away_rating ha1
    ON m.home_team=ha1.team

    LEFT JOIN home_away_rating ha2
    ON m.away_team=ha2.team

    LEFT JOIN fatigue_rating f1
    ON m.home_team=f1.team

    LEFT JOIN fatigue_rating f2
    ON m.away_team=f2.team
    """

    df = pd.read_sql(sql, conn)

    conn.close()

    return df



def create_features(df):

    y=[]

    for _,row in df.iterrows():

        if row.home_score > row.away_score:
            y.append(0)

        elif row.home_score == row.away_score:
            y.append(1)

        else:
            y.append(2)


    drop_cols=[
        "home_team",
        "away_team",
        "home_score",
        "away_score"
    ]


    X=df.drop(columns=drop_cols)

    X=X.fillna(0)

    return X,y



def train():

    print("==============================")
    print("Football AI XGBoost Fusion V2")
    print("==============================")


    df=load_data()

    print("训练数据:",len(df))


    X,y=create_features(df)

    print("特征数量:",len(X.columns))


    X_train,X_test,y_train,y_test=train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    model=XGBClassifier(
        n_estimators=300,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="multi:softmax",
        num_class=3,
        eval_metric="mlogloss"
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


    print("模型准确率:",acc)

    print("==============================")
    print("XGBoost Fusion V2完成")
    print("==============================")


if __name__=="__main__":
    train()
