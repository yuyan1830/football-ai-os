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

result={
    "version":"FOOTBALL_AI_OS_V4.0_FEEDBACK_TABLE_AUDIT",
    "time":str(datetime.now()),
    "database":db,
    "tables":tables,
    "prediction_feedback_exists":
        "prediction_feedback" in tables,
    "feedback_exists":
        "feedback" in tables
}

print(json.dumps(result,indent=4))

conn.close()
