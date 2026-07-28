import sqlite3
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


DATA_DB=r"E:\football_v\00_System_OS\01_DATA_LAYER\database\match_data.db"

FEATURE_DB=r"E:\football_v\00_System_OS\02_FEATURE_LAYER\database\feature_store.db"

MODEL_DB=r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"



def load_data():

    conn=sqlite3.connect(DATA_DB)


    conn.execute(
        "ATTACH DATABASE ? AS feature",
        (FEATURE_DB,)
    )


    sql="""

    SELECT

    m.home_team,
    m.away_team,

    m.home_score,
    m.away_score,


    eh1.elo AS home_elo,
    eh2.elo AS away_elo,


    dc1.attack AS home_dc_attack,
    dc2.attack AS away_dc_attack,


    p1.lambda AS home_poi_attack,
    p2.lambda AS away_poi_attack,


    tf1.last5_win AS home_form_win,
    tf2.last5_win AS away_form_win,


    f1.fatigue_score AS home_fatigue,
    f2.fatigue_score AS away_fatigue,


    ha1.home_win_rate,
    ha2.away_win_rate


    FROM matches_clean m


    LEFT JOIN feature.elo_history eh1
    ON m.home_team=eh1.team


    LEFT JOIN feature.elo_history eh2
    ON m.away_team=eh2.team


    LEFT JOIN feature.dixon_coles_history dc1
    ON m.home_team=dc1.team


    LEFT JOIN feature.dixon_coles_history dc2
    ON m.away_team=dc2.team


    LEFT JOIN feature.poisson_history p1
    ON m.home_team=p1.team


    LEFT JOIN feature.poisson_history p2
    ON m.away_team=p2.team


    LEFT JOIN feature.team_form_history tf1
    ON m.home_team=tf1.team


    LEFT JOIN feature.team_form_history tf2
    ON m.away_team=tf2.team


    LEFT JOIN feature.fatigue_rating f1
    ON m.home_team=f1.team


    LEFT JOIN feature.fatigue_rating f2
    ON m.away_team=f2.team


    LEFT JOIN feature.home_away_history ha1
    ON m.home_team=ha1.team


    LEFT JOIN feature.home_away_history ha2
    ON m.away_team=ha2.team

    """


    df=pd.read_sql(sql,conn)


    conn.close()


    return df



def create_features(df):


    df["result"]=0


    df.loc[
        df.home_score>df.away_score,
        "result"
    ]=1


    df.loc[
        df.home_score<df.away_score,
        "result"
    ]=2



    features=[

        "home_elo",
        "away_elo",

        "home_dc_attack",
        "away_dc_attack",

        "home_poi_attack",
        "away_poi_attack",

        "home_form_win",
        "away_form_win",

        "home_fatigue",
        "away_fatigue",

        "home_win_rate",
        "away_win_rate"

    ]


    X=df[features].fillna(0)

    y=df["result"]


    return X,y




def train():


    print("==============================")
    print("Football AI XGBoost Fusion V3")
    print("==============================")


    df=load_data()


    print(
        "训练数据:",
        len(df)
    )


    X,y=create_features(df)


    print(
        "特征数量:",
        len(X.columns)
    )


    X_train,X_test,y_train,y_test=train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    model=XGBClassifier(

        n_estimators=300,

        max_depth=6,

        learning_rate=0.05,

        objective="multi:softprob",

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


    print(
        "XGBoost Fusion V3准确率:",
        acc
    )


    model.save_model(
        MODEL_DB.replace(
            ".db",
            "_xgb_v3.json"
        )
    )


    print(
        "模型保存完成"
    )



if __name__=="__main__":

    train()

