import sqlite3

db=r"E:\football_v\00_SYSTEM_OS\01_DATA_LAYER\database\football_ai_os.db"


conn=sqlite3.connect(db)

cur=conn.cursor()


cols=cur.execute(
"pragma table_info(model_registry)"
).fetchall()


names=[c[1] for c in cols]


if "version" not in names:
    cur.execute(
    """
    alter table model_registry
    add column version TEXT
    """
    )


if "description" not in names:
    cur.execute(
    """
    alter table model_registry
    add column description TEXT
    """
    )


conn.commit()


print("MODEL_REGISTRY_SCHEMA_UPGRADE PASS")


print(
cur.execute(
"pragma table_info(model_registry)"
).fetchall()
)


conn.close()

