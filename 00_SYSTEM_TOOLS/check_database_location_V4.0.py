import os

paths=[

r"E:\football\data\football.db",

r"E:\football_v\data\football.db",

r"E:\FOOTBALL_V\data\football.db",

r"E:\football\data",

r"E:\football_v\data"

]


print("="*60)

print("FOOTBALL DATABASE LOCATION CHECK")

print("="*60)


for p in paths:

    print()

    print(p)

    print("EXISTS:",os.path.exists(p))


