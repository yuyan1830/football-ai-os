import sqlite3
import os
import json
import shutil
from datetime import datetime


SOURCE_DB = r"E:\football\Football_AI_System\02_Database\football.db"


BASE = r"E:\football_v"


TARGETS = {

    "match_data":
    os.path.join(
        BASE,
        "01_DATA_LAYER",
        "database",
        "match_data.db"
    ),

    "feature_store":
    os.path.join(
        BASE,
        "02_FEATURE_LAYER",
        "database",
        "feature_store.db"
    ),

    "model_store":
    os.path.join(
        BASE,
        "03_MODEL_LAYER",
        "database",
        "model_store.db"
    )
}


MATCH_TABLES = [

    "matches_full",
    "matches_clean",
    "matches",
    "fixtures",
    "teams",
    "competitions",
    "seasons",
    "leagues",
    "match_stats",
    "odds_history",
    "odds_history_clean",
    "xg_match_history",
    "xg_shot_history",
    "xg_shot_history_clean",
    "data_audit_report",
    "data_update_log"

]


FEATURE_TABLES = [

    "elo_history",
    "team_rating",
    "dixon_coles_rating",
    "dixon_coles_history",
    "poisson_rating",
    "poisson_history",
    "team_form",
    "team_form_history",
    "fatigue_rating",
    "fatigue_history",
    "home_away_rating",
    "home_away_history",
    "xg_features_history",
    "xg_features_temp"

]


MODEL_TABLES = [

    "model_data_registry"

]


def create_db(path):

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    if os.path.exists(path):

        os.remove(path)

    sqlite3.connect(path).close()



def migrate_tables(source, target, tables):

    src = sqlite3.connect(source)
    dst = sqlite3.connect(target)

    sc = src.cursor()
    dc = dst.cursor()


    for table in tables:

        exists = sc.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table,)
        ).fetchone()


        if not exists:
            continue


        sql = sc.execute(
            "SELECT sql FROM sqlite_master WHERE name=?",
            (table,)
        ).fetchone()[0]


        if sql:

            dc.execute(sql)


        rows = sc.execute(
            f"SELECT * FROM [{table}]"
        ).fetchall()


        if rows:

            columns=len(rows[0])

            placeholders=",".join(
                ["?"]*columns
            )

            dc.executemany(
                f"INSERT INTO [{table}] VALUES ({placeholders})",
                rows
            )


        print(
            table,
            "migrated",
            len(rows)
        )


    dst.commit()

    src.close()
    dst.close()



report={

    "framework":
    "Football AI OS Ultimate Fusion Framework V1.5",

    "module":
    "16_DATABASE_MIGRATION_LAYER",

    "version":
    "V1.0",

    "source":
    SOURCE_DB,

    "targets":{},


    "time":
    str(datetime.now())

}



for name,path in TARGETS.items():

    create_db(path)

    report["targets"][name]=path



migrate_tables(
    SOURCE_DB,
    TARGETS["match_data"],
    MATCH_TABLES
)


migrate_tables(
    SOURCE_DB,
    TARGETS["feature_store"],
    FEATURE_TABLES
)


migrate_tables(
    SOURCE_DB,
    TARGETS["model_store"],
    MODEL_TABLES
)



out=r"E:\football_v\00_System_OS\01_DATA_LAYER\reports"

os.makedirs(out,exist_ok=True)


with open(
    os.path.join(
        out,
        "database_migration_report.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )



print("==============================")
print("Football AI OS Database Migration")
print("==============================")
print("STATUS: COMPLETED")
print("==============================")

