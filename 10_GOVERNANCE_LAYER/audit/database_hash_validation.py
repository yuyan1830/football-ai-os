import csv
import hashlib
import os
from datetime import datetime

source = r"E:\football_v\10_GOVERNANCE_LAYER\registry\Database_Registry_V1.0.csv"

output = r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_Hash_Validation_V1.0.csv"

targets = [
    r"E:\football_v\01_DATA_LAYER\database\match_data.db",
    r"E:\football_v\00_System_OS\01_DATA_LAYER\database\match_data.db",
    r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db",
    r"E:\football_v\00_System_OS\02_FEATURE_LAYER\database\feature_store.db",
    r"E:\football_v\03_MODEL_LAYER\database\model_store.db",
    r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


results = []

for path in targets:
    if os.path.exists(path):
        results.append({
            "Path": path,
            "Exists": True,
            "Size_MB": round(os.path.getsize(path)/1024/1024,2),
            "SHA256": sha256_file(path),
            "Validation_Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    else:
        results.append({
            "Path": path,
            "Exists": False,
            "Size_MB": "",
            "SHA256": "",
            "Validation_Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


with open(output,"w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(
        f,
        fieldnames=[
            "Path",
            "Exists",
            "Size_MB",
            "SHA256",
            "Validation_Time"
        ]
    )
    writer.writeheader()
    writer.writerows(results)


print("Database Hash Validation Completed")
print(output)
