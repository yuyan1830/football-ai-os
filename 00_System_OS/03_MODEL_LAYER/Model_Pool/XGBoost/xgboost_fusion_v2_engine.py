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
        f"ATTACH DATABASE '{FEATURE_DB}' AS feature"
    )


    conn.execute(
        f"ATTACH DATABASE '{MODEL_DB}' AS model"
    )


    sql="""

    SELECT

    m.home_team,
    m.away_team,

    m.home_score,
    m.away_score,


    tf1.last5_win AS home_last5_win,
    tf1.last5_draw AS home_last5_draw,
    tf1.last5_loss AS home_last5_loss,


    tf2.last5_win AS away_last5_win,
    tf2.last5_draw AS away_last5_draw,
    tf2.last5_loss AS away_last5_loss,


    ha1.home_win_rate,
    ha1.home_goals_for,
    ha1.home_goals_against,


    ha2.away_win_rate,
    ha2.away_goals_for,
    ha2.away_goals_against,


    f1.rest_days AS home_rest_days,
    f1.fatigue_score AS home_fatigue,


    f2.rest_days AS away_rest_days,
    f2.fatigue_score AS away_fatigue,


    tr1.elo AS home_elo,
    tr2.elo AS away_elo,


    dc1.attack_strength AS home_dc_attack,
    dc2.attack_strength AS away_dc_attack,


    p1.attack_strength AS home_poi_attack,
    p2.attack_strength AS away_poi_attack


    FROM matches_clean m


    LEFT JOIN feature.team_form tf1
    ON m.home_team=tf1.team


    LEFT JOIN feature.team_form tf2
    ON m.away_team=tf2.team


    LEFT JOIN feature.home_away_rating ha1
    ON m.home_team=ha1.team


    LEFT JOIN feature.home_away_rating ha2
    ON m.away_team=ha2.team


    LEFT JOIN feature.fatigue_rating f1
    ON m.home_team=f1.team


    LEFT JOIN feature.fatigue_rating f2
    ON m.away_team=f2.team


    LEFT JOIN model.team_rating tr1
    ON m.home_team=tr1.team


    LEFT JOIN model.team_rating tr2
    ON m.away_team=tr2.team


    LEFT JOIN model.dixon_coles_rating dc1
    ON m.home_team=dc1.team


    LEFT JOIN model.dixon_coles_rating dc2
    ON m.away_team=dc2.team


    LEFT JOIN model.poisson_rating p1
    ON m.home_team=p1.team


    LEFT JOIN model.poisson_rating p2
    ON m.away_team=p2.team


    """


    df=pd.read_sql(sql,conn)


    conn.close()


    return df



def create_features(df):


    df["result"]=0


    df.loc[
        df.home_score>df.away_score,
        "result"
    ]=0


    df.loc[
        df.home_score==df.away_score,
        "result"
    ]=1


    df.loc[
        df.home_score<df.away_score,
        "result"
    ]=2



    drop=[

        "home_team",
        "away_team",
        "home_score",
        "away_score",
        "result"

    ]


    X=df.drop(columns=drop)

    X=X.fillna(0)


    y=df["result"]


    return X,y



def train():


    print("==============================")

    print("Football AI XGBoost Fusion V2")

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

        max_depth=5,

        learning_rate=0.05,

        subsample=0.8,

        colsample_bytree=0.8,

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
        "模型准确率:",
        acc
    )


    model.save_model(
        r"E:\football_v\00_System_OS\03_MODEL_LAYER\Model_Pool\XGBoost\xgboost_fusion_v2.json"
    )


    print(
        "模型保存完成"
    )



if __name__=="__main__":

    train()

