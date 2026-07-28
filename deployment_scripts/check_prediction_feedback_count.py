import sqlite3
import json
from datetime import datetime

db=r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"

conn=sqlite3.connect(db)
cursor=conn.cursor()

cursor.execute("select count(*) from prediction_feedback")

count=cursor.fetchone()[0]

cursor.execute("select * from prediction_feedback limit 5")

rows=cursor.fetchall()

result={
    "version":"FOOTBALL_AI_OS_V4.0_PREDICTION_FEEDBACK_COUNT_CHECK",
    "time":str(datetime.now()),
    "count":count,
    "records":rows
}

print(json.dumps(result,indent=4,ensure_ascii=False))

conn.close()
