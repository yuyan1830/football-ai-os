from pathlib import Path
import csv
import shutil
import datetime


ROOT = Path(r"E:\football_v")

SRC = ROOT / "99_DOCUMENTATION" / "migration" / "FINAL_MIGRATION_SAFE_DELETE_LIST_V1.0.csv"

BACKUP = ROOT / "archive" / (
    "DELETE_FILE_BACKUP_" +
    datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
)

BACKUP.mkdir(parents=True, exist_ok=True)


print("=" * 50)
print("读取删除清单")

rows = list(
    csv.DictReader(
        open(SRC, encoding="utf-8")
    )
)

print("清单数量:", len(rows))


count = 0
skip = 0


for row in rows:

    file_path = ROOT / row["file"]

    if file_path.is_file():

        target = BACKUP / file_path.relative_to(ROOT)

        target.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            file_path,
            target
        )

        count += 1

    else:
        skip += 1


print("=" * 50)
print("备份完成")
print("备份文件:", count)
print("跳过:", skip)
print("位置:", BACKUP)