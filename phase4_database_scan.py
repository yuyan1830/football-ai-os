import os
import csv
import sqlite3
import re


ROOT=r"E:\football_v"


OUT=os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_4_Database_Registry"
)


os.makedirs(OUT,exist_ok=True)


db_assets=[]
table_assets=[]
sql_assets=[]


for path,dirs,files in os.walk(ROOT):

    for file in files:


        fp=os.path.join(path,file)


        # 扫描数据库文件

        if file.lower().endswith(
            (".db",".sqlite",".sqlite3")
        ):


            db_assets.append({

                "database":fp

            })


            try:

                conn=sqlite3.connect(fp)

                cur=conn.cursor()


                cur.execute(
                    "select name from sqlite_master where type='table'"
                )


                tables=cur.fetchall()


                for t in tables:

                    table=t[0]


                    cur.execute(
                        f"pragma table_info('{table}')"
                    )


                    columns=cur.fetchall()


                    cur.execute(
                        f"select count(*) from '{table}'"
                    )


                    count=cur.fetchone()[0]


                    table_assets.append({

                        "database":fp,
                        "table":table,
                        "columns":"|".join(
                            [c[1] for c in columns]
                        ),
                        "rows":count

                    })


                conn.close()


            except Exception as e:


                table_assets.append({

                    "database":fp,
                    "error":str(e)

                })



        # 扫描SQL文件

        if file.lower().endswith(".sql"):


            try:

                text=open(
                    fp,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ).read()


                matches=re.findall(
                    r"create\s+table.*",
                    text,
                    re.I
                )


                for m in matches:

                    sql_assets.append({

                        "file":fp,
                        "sql":m

                    })


            except:
                pass





def save(name,data):

    if not data:
        return


    fields=set()


    for r in data:
        fields.update(r.keys())


    with open(
        os.path.join(OUT,name),
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:


        w=csv.DictWriter(
            f,
            fieldnames=list(fields),
            extrasaction="ignore"
        )


        w.writeheader()

        w.writerows(data)



save(
"Database_Asset_Registry_V1.0.csv",
db_assets
)


save(
"Database_Table_Registry_V1.0.csv",
table_assets
)


save(
"Database_SQL_Discovery_V1.0.csv",
sql_assets
)



print("="*60)
print("Phase 4 Database Asset Scan Complete")
print("="*60)

print("Databases:",len(db_assets))
print("Tables:",len(table_assets))
print("SQL:",len(sql_assets))

print("")
print("Output:")
print(OUT)

