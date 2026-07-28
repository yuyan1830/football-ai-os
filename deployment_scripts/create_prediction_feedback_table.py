import sqlite3
import json
from datetime import datetime

db=r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"

conn=sqlite3.connect(db)
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction_feedback
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    prediction_time TEXT,

    home_team TEXT,
    away_team TEXT,
    league TEXT,

    prediction_home REAL,
    prediction_draw REAL,
    prediction_away REAL,

    decision TEXT,

    actual_result TEXT,
    correct INTEGER,

    odds_home REAL,
    odds_draw REAL,
    odds_away REAL,

    roi REAL,

    confidence REAL,
    risk_level TEXT,

    model_version TEXT,

    created_time TEXT
)
""")

conn.commit()

cursor.execute("""
PRAGMA table_info(prediction_feedback)
""")

columns=[
    {
        "name":row[1],
        "type":row[2]
    }
    for row in cursor.fetchall()
]


result={
    "version":"FOOTBALL_AI_OS_V4.0_PREDICTION_FEEDBACK_TABLE_V1.0",
    "time":str(datetime.now()),
    "database":db,
    "table":"prediction_feedback",
    "columns":columns,
    "status":"CREATED"
}

print(json.dumps(result,indent=4,ensure_ascii=False))

conn.close()
