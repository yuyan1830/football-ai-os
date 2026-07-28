import sqlite3
import pandas as pd
import numpy as np

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


from model_config import DATABASE_PATH


def load_data():

    conn = sqlite3.connect(DATABASE_PATH)

    sql = """
    SELECT
        m.home_team,
        m.away_team,
        m.home_score,
        m.away_score,

        m.home_odds,
        m.draw_odds,
        m.away_odds,

        m.home_shots,
        m.away_shots,

        m.home_shots_on_goal,
        m.away_shots_on_goal,

        m.home_possession,
        m.away_possession,

        m.home_corners,
        m.away_corners,

        m.home_dangerous_attacks,
        m.away_dangerous_attacks

    FROM matches_clean m
    """

    df = pd.read_sql(sql, conn)


    # Elo
    elo = pd.read_sql(
        """
        SELECT
            team,
            elo
        FROM team_rating
        """,
        conn
    )


    # Dixon-Coles
    dc = pd.read_sql(
        """
        SELECT
            team,
            attack_strength AS dc_attack,
            defense_strength AS dc_defense
        FROM dixon_coles_rating
        """,
        conn
    )


    # Poisson
    poi = pd.read_sql(
        """
        SELECT
            team,
            attack_strength AS poi_attack,
            defense_strength AS poi_defense,
            avg_goals
        FROM poisson_rating
        """,
        conn
    )


    conn.close()


    # 合并主队数据

    df = df.merge(
        elo,
        left_on="home_team",
        right_on="team",
        how="left"
    )

    df.rename(
        columns={
            "elo":"home_elo"
        },
        inplace=True
    )

    df.drop(
        columns=["team"],
        inplace=True
    )


    # 客队 Elo

    df = df.merge(
        elo,
        left_on="away_team",
        right_on="team",
        how="left"
    )

    df.rename(
        columns={
            "elo":"away_elo"
        },
        inplace=True
    )

    df.drop(
        columns=["team"],
        inplace=True
    )


    # Dixon

    for side in ["home","away"]:

        df = df.merge(
            dc,
            left_on=f"{side}_team",
            right_on="team",
            how="left"
        )

        df.rename(
            columns={
                "dc_attack":f"{side}_dc_attack",
                "dc_defense":f"{side}_dc_defense"
            },
            inplace=True
        )

        df.drop(
            columns=["team"],
            inplace=True
        )


    # Poisson

    for side in ["home","away"]:

        df = df.merge(
            poi,
            left_on=f"{side}_team",
            right_on="team",
            how="left"
        )

        df.rename(
            columns={
                "poi_attack":f"{side}_poi_attack",
                "poi_defense":f"{side}_poi_defense",
                "avg_goals":f"{side}_avg_goals"
            },
            inplace=True
        )

        df.drop(
            columns=["team"],
            inplace=True
        )


    return df



def create_features(df):

        # 数值字段转换
    numeric_cols = [
        "home_odds",
        "draw_odds",
        "away_odds",

        "home_shots",
        "away_shots",

        "home_shots_on_goal",
        "away_shots_on_goal",

        "home_possession",
        "away_possession",

        "home_corners",
        "away_corners",

        "home_dangerous_attacks",
        "away_dangerous_attacks"
    ]


    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )
        
    # 比赛结果

    df["result"] = 0

    df.loc[
        df.home_score > df.away_score,
        "result"
    ] = 1


    df.loc[
        df.home_score < df.away_score,
        "result"
    ] = 2



    # 差值特征

    df["elo_diff"] = (
        df.home_elo -
        df.away_elo
    )


    df["dc_attack_diff"] = (
        df.home_dc_attack -
        df.away_dc_attack
    )


    df["dc_defense_diff"] = (
        df.home_dc_defense -
        df.away_dc_defense
    )


    df["poi_attack_diff"] = (
        df.home_poi_attack -
        df.away_poi_attack
    )


    df["poi_defense_diff"] = (
        df.home_poi_defense -
        df.away_poi_defense
    )


    df["shots_diff"] = (
        df.home_shots -
        df.away_shots
    )


    df["shots_on_goal_diff"] = (
        df.home_shots_on_goal -
        df.away_shots_on_goal
    )


    df["possession_diff"] = (
        df.home_possession -
        df.away_possession
    )


    df["corner_diff"] = (
        df.home_corners -
        df.away_corners
    )


    df["danger_attack_diff"] = (
        df.home_dangerous_attacks -
        df.away_dangerous_attacks
    )


    features = [

        "elo_diff",

        "dc_attack_diff",
        "dc_defense_diff",

        "poi_attack_diff",
        "poi_defense_diff",

        "home_odds",
        "draw_odds",
        "away_odds",

        "shots_diff",
        "shots_on_goal_diff",

        "possession_diff",

        "corner_diff",

        "danger_attack_diff"

    ]


    X = df[features]

    y = df["result"]


    X = X.fillna(0)


    return X,y



def train():

    print("==============================")
    print("Football AI XGBoost Fusion")
    print("==============================")


    df = load_data()


    print(
        "数据:",
        len(df)
    )


    X,y = create_features(df)


    print(
        "特征数量:",
        len(X.columns)
    )


    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        objective="multi:softmax",
        num_class=3
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
        "融合模型准确率:",
        acc
    )


    print("==============================")
    print("XGBoost Fusion完成")
    print("==============================")



if __name__=="__main__":
    train()
