import sqlite3
import json
import os
from datetime import datetime

db = r"E:\football\Football_AI_System\02_Database\football.db"

out = r"E:\football_v\00_System_OS\01_DATA_LAYER\reports"

os.makedirs(out, exist_ok=True)

conn = sqlite3.connect(db)
cur = conn.cursor()

tables = cur.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

result = {
    "framework":
    "Football AI OS Ultimate Fusion Framework V1.5",

    "module":
    "DATABASE_INSPECTION_LAYER",

    "database":
    db,

    "tables":[],
    
    "time":
    str(datetime.now())
}


for t in tables:

    name=t[0]

    try:
        count=cur.execute(
            f"SELECT COUNT(*) FROM [{name}]"
        ).fetchone()[0]

    except:
        count=-1


    if any(x in name.lower() for x in [
        "elo",
        "poisson",
        "dixon",
        "form",
        "fatigue",
        "feature"
    ]):
        category="feature_data"

    elif any(x in name.lower() for x in [
        "model",
        "weight",
        "calibration",
        "prediction"
    ]):
        category="model_data"

    else:
        category="match_data"


    result["tables"].append(
        {
            "name":name,
            "rows":count,
            "category":category
        }
    )


conn.close()


file=os.path.join(
    out,
    "database_inspection_report.json"
)

with open(file,"w",encoding="utf-8") as f:
    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print("==============================")
print("Football AI OS Database Inspection")
print("==============================")
print("Database:")
print(db)
print("")
print("Tables:",len(result["tables"]))

for x in result["tables"]:
    print(
        x["name"],
        "|",
        x["rows"],
        "|",
        x["category"]
    )

print("==============================")
print("REPORT:")
print(file)
