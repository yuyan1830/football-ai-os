import os
import csv


ROOT=r"E:\football_v"


OUT=os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_8_Status_Registry"
)


os.makedirs(OUT,exist_ok=True)


status=[]

migration=[]



scan_dirs=[

"99_DOCUMENTATION",

]



keywords=[

"model",
"predict",
"feature",
"history",
"rating",
"engine",
"runtime",
"database",
"odds",
"bet",
"train"

]



for path,dirs,files in os.walk(ROOT):


    for file in files:


        if not file.endswith(
            (".py",".csv",".db",".json",".yaml")
        ):

            continue


        fp=os.path.join(path,file)


        try:

            size=os.path.getsize(fp)


            score=0


            reason=[]



            # 文件存在有效内容

            if size>100:

                score+=1

                reason.append(
                    "content"
                )



            # python代码

            if file.endswith(".py"):

                text=open(
                    fp,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ).read().lower()


                for k in keywords:

                    if k in text:

                        score+=1

                        reason.append(k)



            # 状态判断


            if score>=5:

                level="A"

                advice="核心资产，优先迁移"


            elif score>=3:

                level="B"

                advice="整理后迁移"


            elif score>=1:

                level="C"

                advice="测试验证"


            else:

                level="D"

                advice="归档"



            status.append({

                "file":fp,

                "size":size,

                "status":level,

                "reason":"|".join(reason)

            })


            migration.append({

                "file":fp,

                "status":level,

                "migration":advice

            })


        except:

            pass




def save(name,data):


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

"Asset_Status_Registry_V1.0.csv",

status

)


save(

"Migration_Precheck_Report_V1.0.csv",

migration

)



print("="*60)

print("Phase 8 Asset Status Scan Complete")

print("="*60)

print("Assets:",len(status))


print("")

print("Output:")

print(OUT)

