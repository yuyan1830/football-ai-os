import os
import csv
import ast


ROOT=r"E:\football_v"


OUT=os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_6_Feature_Registry"
)


os.makedirs(OUT,exist_ok=True)



feature_keywords=[

"feature",
"features",
"feature_store",
"feature_engine",

"transform",
"encoder",
"scaler",
"normalization",

"history",
"historical",
"recent",
"previous",
"h2h",
"head_to_head",

"rating",
"rank",
"ranking",
"strength",
"power",

"form",
"team_form",
"momentum",
"trend",
"streak",

"fatigue",
"fitness",
"rest",
"recovery",
"schedule",
"travel"

]



feature_assets=[]
code_map=[]
data_map=[]



for path,dirs,files in os.walk(ROOT):

    for file in files:


        if not file.endswith(".py"):
            continue


        fp=os.path.join(path,file)


        try:


            code=open(
                fp,
                "r",
                encoding="utf-8",
                errors="ignore"
            ).read()


            lower=code.lower()


            tree=ast.parse(code)


            classes=[]
            functions=[]


            for node in ast.walk(tree):


                if isinstance(node,ast.ClassDef):

                    classes.append(node.name)


                if isinstance(node,ast.FunctionDef):

                    functions.append(node.name)



            hits=[]


            for k in feature_keywords:

                count=lower.count(k.lower())


                if count>0:


                    hits.append(k)


                    code_map.append({

                    "file":fp,
                    "keyword":k,
                    "count":count

                    })



            if hits:


                feature_assets.append({

                    "file":fp,

                    "features":
                    "|".join(
                        sorted(set(hits))
                    ),

                    "classes":
                    "|".join(classes),

                    "functions":
                    "|".join(functions)

                })



            # 数据访问关联

            for line in code.splitlines():

                l=line.lower()


                if any(

                    x in l

                    for x in
                    [
                    "select",
                    "insert",
                    "feature",
                    "history",
                    "rating"
                    ]

                ):


                    data_map.append({

                    "file":fp,

                    "line":
                    line.strip()

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

"Feature_Asset_Registry_V1.0.csv",

feature_assets

)


save(

"Feature_Code_Map_V1.0.csv",

code_map

)


save(

"Feature_Data_Map_V1.0.csv",

data_map

)



print("="*60)

print("Phase 6 Feature Asset Scan Complete")

print("="*60)


print("Feature Files:",len(feature_assets))

print("Keyword Hits:",len(code_map))

print("Data Lines:",len(data_map))


print("")

print("Output:")

print(OUT)

