import os
import csv
import ast


ROOT=r"E:\football_v"


OUT=os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_5_Model_Registry"
)


os.makedirs(OUT,exist_ok=True)


model_assets=[]
code_map=[]
lifecycle=[]


keywords=[

"elo",
"dixon",
"dixon_coles",
"poisson",
"xgboost",
"XGB",
"lightgbm",
"lgb",
"randomforest",
"randomforestclassifier",
"bayesian",
"bayes",
"model",
"train",
"fit",
"predict",
"predict_proba",
"evaluate",
"save_model",
"load_model",
"pickle",
"joblib",
"registry"

]


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


            for k in keywords:

                if k.lower() in lower:

                    hits.append(k)



            if hits:


                model_assets.append({

                    "file":fp,
                    "keywords":"|".join(
                        sorted(set(hits))
                    ),
                    "classes":"|".join(classes),
                    "functions":"|".join(functions)

                })



                for h in hits:

                    code_map.append({

                        "file":fp,
                        "keyword":h

                    })



            for f in functions:

                lf=f.lower()

                if any(
                    x in lf
                    for x in
                    [
                    "train",
                    "fit",
                    "predict",
                    "evaluate",
                    "load",
                    "save"
                    ]
                ):


                    lifecycle.append({

                        "file":fp,
                        "function":f

                    })



        except Exception as e:

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
"Model_Asset_Registry_V1.0.csv",
model_assets
)


save(
"Model_Code_Map_V1.0.csv",
code_map
)


save(
"Model_Lifecycle_Map_V1.0.csv",
lifecycle
)



print("="*60)
print("Phase 5 Model Asset Scan Complete")
print("="*60)

print("Model Files:",len(model_assets))
print("Keyword Hits:",len(code_map))
print("Lifecycle Functions:",len(lifecycle))

print("")
print("Output:")
print(OUT)

