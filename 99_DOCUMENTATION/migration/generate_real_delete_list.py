from pathlib import Path
import csv
import datetime


ROOT = Path(r"E:\football_v")

OUT = ROOT / "99_DOCUMENTATION" / "migration" / "FINAL_REAL_DELETE_LIST_V2.0.csv"


exclude = [
    "05_MODEL_AI",
    "05_AI_Intelligence_Layer",
    "06_PREDICTION_ENGINE",
    "06_PREDICTION_INTELLIGENCE_ENGINE",
    "50_MODEL_REGISTRY",
    ".venv",
    ".git",
    "archive",
    "99_DOCUMENTATION"
]


result=[]


print("开始扫描文件...")


for p in ROOT.rglob("*"):

    if not p.is_file():
        continue

    rel=str(p.relative_to(ROOT))


    if any(x in rel for x in exclude):
        continue


    result.append([
        rel,
        "DELETE_REVIEW",
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
        "scan_time"
    ])

    w.writerows(result)


print("======================")
print("完成")
print("真实文件数量:",len(result))
print("保存:")
print(OUT)