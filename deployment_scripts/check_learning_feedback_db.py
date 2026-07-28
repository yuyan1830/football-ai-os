import sqlite3
import json
from datetime import datetime

db = r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"

conn = sqlite3.connect(db)

cursor = conn.cursor()

cursor.execute(
    "select * from learning_feedback_registry"
)

rows = cursor.fetchall()

result = {
    "database": db,
    "table": "learning_feedback_registry",
    "count": len(rows),
    "records": rows,
    "time": str(datetime.now())
}

print(json.dumps(result, indent=4, ensure_ascii=False))

conn.close()
