import sqlite3


FEATURE_DB=r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"
MODEL_DB=r"E:\football_v\03_MODEL_LAYER\database\model_store.db"


def load_feature_status():

    conn=sqlite3.connect(FEATURE_DB)

    tables=conn.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()

    conn.close()

    names=[x[0] for x in tables]

    return {

        "elo":
            "elo_history" in names,

        "dixon_coles":
            "dixon_coles_history" in names,

        "poisson":
            "poisson_history" in names,

        "form":
            "team_form_history" in names,

        "fatigue":
            "fatigue_history" in names,

        "home_away":
            "home_away_history" in names,

        "xg":
            "xg_features_history" in names

    }



def load_model_registry():

    conn=sqlite3.connect(MODEL_DB)

    tables=conn.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()

    conn.close()


    return {

        "registry":
            [x[0] for x in tables]

    }



def model_runtime_check():

    return {

        "feature_layer":
            load_feature_status(),

        "model_layer":
            load_model_registry(),

        "status":
            "READY"

    }
