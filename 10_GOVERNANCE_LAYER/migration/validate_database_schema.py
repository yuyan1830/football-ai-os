import sqlite3
import csv


input_file = r"E:\football_v\10_GOVERNANCE_LAYER\registry\Database_Inventory.csv"

output_file = r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_Schema_Validation.csv"


results=[]


with open(input_file,"r",encoding="utf-8") as f:

    reader=csv.DictReader(f)

    for row in reader:

        path=row["FullName"]

        result={
            "Database":path,
            "Status":"",
            "Tables":""
        }


        try:

            conn=sqlite3.connect(path)

            cur=conn.cursor()

            cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )


            tables=[
                t[0]
                for t in cur.fetchall()
            ]


            result["Status"]="PASS"
            result["Tables"]=";".join(tables)


            conn.close()


        except Exception as e:

            result["Status"]="FAILED"
            result["Tables"]=str(e)


        results.append(result)



with open(output_file,"w",newline="",encoding="utf-8") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=[
            "Database",
            "Status",
            "Tables"
        ]
    )

    writer.writeheader()

    writer.writerows(results)



print("Schema Validation Completed")
print(output_file)