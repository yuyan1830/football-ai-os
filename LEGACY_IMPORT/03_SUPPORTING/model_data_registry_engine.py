import sqlite3

DB_PATH = "data/football.db"


def create_registry():

    print("==============================")
    print("Football AI Model Data Registry")
    print("==============================")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS model_data_registry(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_name TEXT UNIQUE,
        status TEXT,
        reason TEXT,
        usage TEXT

    )
    """)

    data = [

        (
            "elo_history",
            "active",
            "time_series_data",
            "正式模型输入"
        ),

        (
            "dixon_coles_history",
            "active",
            "time_series_version",
            "正式模型输入"
        ),

        (
            "poisson_history",
            "pending",
            "waiting_generation",
            "待生成"
        ),

        (
            "dixon_coles_rating",
            "deprecated",
            "future_data_leakage_risk",
            "禁止用于训练和融合，仅保留分析"
        ),

        (
            "poisson_rating",
            "deprecated",
            "future_data_leakage_risk",
            "禁止用于训练和融合，仅保留分析"
        ),

        (
            "team_form",
            "deprecated",
            "future_data_leakage_risk",
            "禁止用于训练和融合，仅保留分析"
        ),

        (
            "home_away_rating",
            "deprecated",
            "future_data_leakage_risk",
            "禁止用于训练和融合，仅保留分析"
        ),

        (
            "fatigue_rating",
            "deprecated",
            "future_data_leakage_risk",
            "禁止用于训练和融合，仅保留分析"
        )

    ]


    for row in data:

        cursor.execute("""
        INSERT OR REPLACE INTO model_data_registry
        (table_name,status,reason,usage)
        VALUES(?,?,?,?)
        """, row)


    conn.commit()


    print("==============================")
    print("生成表:")
    print("model_data_registry")
    print("==============================")

    rows = cursor.execute(
        "SELECT table_name,status FROM model_data_registry"
    ).fetchall()

    for r in rows:
        print(r[0], "|", r[1])


    conn.close()


if __name__ == "__main__":
    create_registry()
