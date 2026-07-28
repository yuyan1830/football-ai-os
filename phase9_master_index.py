import os
import csv


ROOT=r"E:\football_v\99_DOCUMENTATION\Legacy_Asset_Index"


OUT=os.path.join(
    ROOT,
    "Final_Master_Index"
)


os.makedirs(OUT,exist_ok=True)



master=[]

migration=[]


phase_dirs=[]


for d in os.listdir(ROOT):

    p=os.path.join(ROOT,d)

    if os.path.isdir(p):

        phase_dirs.append(p)



for phase in phase_dirs:


    for path,dirs,files in os.walk(phase):


        for file in files:


            if not file.endswith(".csv"):

                continue


            fp=os.path.join(path,file)


            try:


                with open(
                    fp,
                    "r",
                    encoding="utf-8-sig"
                ) as f:


                    reader=csv.DictReader(f)


                    for row in reader:


                        record={}

                        record["source"]=file


                        for k,v in row.items():

                            record[k]=v



                        master.append(record)



            except:

                pass




for item in master:


    text=str(item).lower()


    status=""

    advice=""


    if "status" in item:

        status=item["status"]



    if status=="A":

        advice="优先迁移"


    elif status=="B":

        advice="整理迁移"


    elif status=="C":

        advice="验证后决定"


    elif status=="D":

        advice="归档"



    migration.append({

        "asset":
        item.get("file",""),

        "status":
        status,

        "migration":
        advice

    })





def save(name,data):


    if not data:

        return


    fields=set()


    for r in data:

        fields.update(r.keys())


    with open(

        os.path.join(
            OUT,
            name
        ),

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

"Football_AI_OS_Legacy_Master_Index_V1.0.csv",

master

)



save(

"Migration_Candidate_List_V1.0.csv",

migration

)



report=os.path.join(

OUT,

"Football_AI_OS_Architecture_Asset_Report_V1.0.txt"

)


with open(report,"w",encoding="utf-8") as f:


    f.write(
"""
Football AI OS V2.0 Legacy Asset Report

=====================================

Total Asset Records:
{}

Scanned Phase:
1-8

Generated:
Phase 9 Master Index

=====================================
""".format(len(master))
    )



print("="*60)

print("Phase 9 Master Index Complete")

print("="*60)

print("Records:",len(master))

print("Output:")

print(OUT)

