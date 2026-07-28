from pathlib import Path
import csv
import shutil
import datetime


root = Path(r"E:\football_v")

src = root / "99_DOCUMENTATION" / "migration" / "FINAL_MIGRATION_SAFE_DELETE_LIST_V1.0.csv"

backup = root / "archive" / (
    "migration_delete_backup_" +
    datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
)

backup.mkdir(parents=True, exist_ok=True)


print("开始读取删除清单")
print("=" * 40)


with open(src, encoding="utf-8-sig") as f:
    data = list(csv.DictReader(f))


print("清单数量:", len(data))


count = 0
skip = 0


for r in data:

    file_path = root / r["file"]

    if file_path.is_file():

        target = backup / file_path.relative_to(root)

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


print("=" * 40)
print("备份完成")
print("备份文件:", count)
print("跳过目录:", skip)
print("备份位置:")
print(backup)