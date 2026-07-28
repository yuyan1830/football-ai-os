from pathlib import Path
import csv
import shutil
import datetime

ROOT=Path(r"E:\football_v")

src=ROOT/"99_DOCUMENTATION/migration/FINAL_MIGRATION_SAFE_DELETE_LIST_V1.0.csv"

backup=ROOT/"archive"/(
    "migration_delete_backup_"+
    datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
)

backup.mkdir(parents=True,exist_ok=True)

rows=list(csv.DictReader(
    open(src,encoding="utf-8-sig")
))

print("读取:",len(rows))

fields=rows[0].keys()

file_field=None

for f in fields:
    if "file" in f.lower() or "path" in f.lower():
        file_field=f
        break

print("路径字段:",file_field)


count=0
skip=0


for row in rows:

    rel=row[file_field]

    p=ROOT/rel

    if p.is_file():

        target=backup/rel

        target.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            p,
            target
        )

        count+=1

    else:
        skip+=1


print("======================")
print("备份完成")
print("文件:",count)
print("跳过:",skip)
print("位置:")
print(backup)