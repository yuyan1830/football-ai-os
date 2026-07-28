import os
import csv


REGISTER = r"E:\football_v\10_GOVERNANCE_LAYER\registry\Unused_Asset_Register_V1.0.csv"


if not os.path.exists(REGISTER):
    print("未找到改名登记文件")
    exit()


count = 0


with open(
    REGISTER,
    "r",
    encoding="utf-8-sig"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        old_path = row["Old_Path"]
        new_path = row["New_Path"]


        if not os.path.exists(new_path):
            print("跳过，不存在:", new_path)
            continue


        if os.path.exists(old_path):
            print("跳过，原路径已存在:", old_path)
            continue


        os.rename(
            new_path,
            old_path
        )

        print(
            "恢复:",
            new_path,
            "->",
            old_path
        )

        count += 1



print("")
print(
    "回滚完成:",
    count
)

