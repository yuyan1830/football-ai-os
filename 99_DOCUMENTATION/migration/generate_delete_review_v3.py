from pathlib import Path
import csv
import datetime


ROOT=Path(r"E:\football_v")

SRC=ROOT/"99_DOCUMENTATION/migration/FINAL_REAL_DELETE_LIST_V2.0.csv"

OUT=ROOT/"99_DOCUMENTATION/migration/FINAL_REAL_DELETE_REVIEW_V3.0.csv"


keep_rules=[
    "05_MODEL_AI",
    "05_AI_Intelligence_Layer",
    "06_PREDICTION_ENGINE",
    "06_PREDICTION_INTELLIGENCE_ENGINE",
    "50_MODEL_REGISTRY",
    "MODEL_LAYER",
    "checkpoint",
    "migration",
    "CLAUDE.md",
    "CHANGELOG.md",
    "AI_PROJECT_CONTEXT.md",
    "AI_START_HERE.md"
]


delete_ext=[
    ".py",
    ".json",
    ".csv",
    ".txt",
    ".md"
]


rows=[]


data=list(csv.DictReader(
    open(SRC,encoding="utf-8-sig")
))


print("读取:",len(data))


for r in data:

    f=r["file"]

    status="UNKNOWN"


    if any(x.lower() in f.lower() for x in keep_rules):
        status="KEEP"


    elif Path(f).suffix.lower() in delete_ext:
        status="DELETE_REVIEW"


    rows.append([
        f,
        status,
        datetime.datetime.now()
    ])



with open(
    OUT,
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:

    w=csv.writer(f)

    w.writerow([
        "file",
        "status",
        "time"
    ])

    w.writerows(rows)



print("==============================")
print("完成")
print("总文件:",len(rows))

print(
"KEEP:",
sum(1 for x in rows if x[1]=="KEEP")
)

print(
"DELETE_REVIEW:",
sum(1 for x in rows if x[1]=="DELETE_REVIEW")
)

print(
"UNKNOWN:",
sum(1 for x in rows if x[1]=="UNKNOWN")
)

print("保存:")
print(OUT)