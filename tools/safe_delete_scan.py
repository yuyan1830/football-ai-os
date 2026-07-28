from pathlib import Path
import csv
import datetime

root = Path(r"E:\football_v")

src = root / "99_DOCUMENTATION" / "migration" / "FINAL_MODEL_MIGRATION_DELETE_PLAN_V1.0.csv"

out = root / "99_DOCUMENTATION" / "migration" / "FINAL_MIGRATION_SAFE_DELETE_LIST_V1.0.csv"

print("读取删除计划...")

if not src.exists():
    print("错误: 删除计划不存在")
    exit()

with open(src, encoding="utf-8") as f:
    data = list(csv.DictReader(f))

print("候选文件:", len(data))


protected = [
    "05_MODEL_AI",
    "05_AI_Intelligence_Layer",
    "06_PREDICTION_ENGINE",
    "06_PREDICTION_INTELLIGENCE_ENGINE",
    "50_MODEL_REGISTRY",
    "04_Data_Processing_AI",
    "02_FEATURE_LAYER"
]


safe = []


for row in data:

    text = str(row)

    blocked = False

    for item in protected:
        if item in text:
            blocked = True
            break

    if not blocked:
        safe.append(row)



with open(out,"w",newline="",encoding="utf-8-sig") as f:

    writer = csv.writer(f)

    writer.writerow(
        [
            "file",
            "status",
            "scan_time"
        ]
    )


    for row in safe:

        writer.writerow(
            [
                row.get("file",""),
                "SAFE_DELETE_REVIEW",
                datetime.datetime.now()
            ]
        )


print("==============================")
print("完成")
print("安全删除候选:",len(safe))
print("保存:",out)
print("==============================")
