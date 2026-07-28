from pathlib import Path
import csv
import datetime


ROOT=Path(r"E:\football_v")

SRC=ROOT/"99_DOCUMENTATION/migration/FINAL_REAL_DELETE_REVIEW_V3.0.csv"

OUT=ROOT/"99_DOCUMENTATION/migration/FINAL_DELETE_REFERENCE_AUDIT_V4.0.csv"


files=[]

with open(SRC,encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["status"]=="DELETE_REVIEW":
            files.append(r["file"])


print("审核文件:",len(files))


all_text=""

print("建立引用索引...")


for p in ROOT.rglob("*"):

    if p.is_file():

        try:
            all_text += p.read_text(
                encoding="utf-8",
                errors="ignore"
            )
        except:
            pass


rows=[]


for f in files:

    name=Path(f).stem

    count=all_text.count(name)


    if count>1:
        status="REFERENCED"

    else:
        status="NO_REFERENCE"


    rows.append([
        f,
        status,
        count,
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
        "reference_status",
        "reference_count",
        "time"
    ])

    w.writerows(rows)


print("==============================")
print("完成")
print("扫描:",len(rows))

print(
"REFERENCED:",
sum(1 for x in rows if x[1]=="REFERENCED")
)

print(
"NO_REFERENCE:",
sum(1 for x in rows if x[1]=="NO_REFERENCE")
)

print("保存:")
print(OUT)