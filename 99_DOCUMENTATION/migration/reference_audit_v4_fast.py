from pathlib import Path
import csv
import datetime


ROOT = Path(r"E:\football_v")

SRC = ROOT / "99_DOCUMENTATION/migration/FINAL_REAL_DELETE_REVIEW_V3.0.csv"

OUT = ROOT / "99_DOCUMENTATION/migration/FINAL_DELETE_REFERENCE_AUDIT_V4_FAST.csv"


SKIP_DIR = {
    ".venv",
    ".git",
    "__pycache__",
    "archive",
    "Logs",
    "Storage",
    "Database"
}


MAX_SIZE = 50 * 1024 * 1024


print("读取删除审核清单...")


targets=[]

with open(SRC,encoding="utf-8-sig") as f:

    for r in csv.DictReader(f):

        if r["status"]=="DELETE_REVIEW":

            targets.append(
                Path(r["file"]).stem.lower()
            )


print("审核数量:",len(targets))


print("建立文件索引...")


index={}


scan_files=0


for p in ROOT.rglob("*"):

    if not p.is_file():
        continue


    if any(x in p.parts for x in SKIP_DIR):
        continue


    try:

        if p.stat().st_size > MAX_SIZE:
            continue

    except:

        continue


    scan_files+=1


    try:

        text=p.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()


        for t in targets:

            if t in text:

                index.setdefault(t,[]).append(
                    str(p.relative_to(ROOT))
                )


    except:

        pass



print("扫描文件:",scan_files)


rows=[]


for t in targets:


    refs=index.get(t,[])


    if len(refs)>0:

        status="REFERENCED"

    else:

        status="NO_REFERENCE"



    rows.append(
        [
            t,
            status,
            len(refs),
            ";".join(refs[:5]),
            datetime.datetime.now()
        ]
    )



with open(
    OUT,
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:


    w=csv.writer(f)


    w.writerow(
        [
            "file",
            "reference_status",
            "reference_count",
            "sample_reference",
            "time"
        ]
    )


    w.writerows(rows)



print("==============================")
print("完成")

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