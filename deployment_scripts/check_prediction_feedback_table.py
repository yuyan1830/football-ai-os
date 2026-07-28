import sqlite3
import json
from datetime import datetime

db=r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"

conn=sqlite3.connect(db)
cursor=conn.cursor()

cursor.execute("""
SELECT name 
FROM sqlite_master
WHERE type='table'
""")

tables=[x[0] for x in cursor.fetchall()]

columns={}

if "prediction_feedback" in tables:
    cursor.execute("""
    PRAGMA table_info(prediction_feedback)
    """)
    
    columns["prediction_feedback"]=[
        {
            "name":row[1],
            "type":row[2]
        }
        for row in cursor.fetchall()
    ]

result={
    "version":"FOOTBALL_AI_OS_V4.0_PREDICTION_FEEDBACK_TABLE_CHECK",
    "time":str(datetime.now()),
    "database":db,
    "tables":tables,
    "prediction_feedback_exists":
        "prediction_feedback" in tables,
    "columns":columns
}

print(json.dumps(result,indent=4,ensure_ascii=False))

conn.close()
