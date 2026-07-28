import os
import csv
import ast


ROOT = r"E:\football_v"

OUT = os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_2_Function_Registry"
)

os.makedirs(OUT, exist_ok=True)


keywords = {

"DATA_LAYER":[
"data","dataset","load","read","csv","json",
"database","sqlite","db","query"
],

"FEATURE_LAYER":[
"feature","history","rating","form",
"fatigue","momentum","strength"
],

"MODEL_LAYER":[
"elo","dixon","poisson",
"xgboost","lightgbm",
"randomforest","bayesian",
"model","train","fit"
],

"PREDICTION_LAYER":[
"predict","prediction",
"forecast","simulation",
"simulate","probability",
"score"
],

"MARKET_LAYER":[
"odds","market",
"handicap","asian",
"bookmaker",
"movement","capital"
],

"VALUE_LAYER":[
"value","ev","fair",
"roi"
],

"BETTING_LAYER":[
"bet","stake",
"kelly","bankroll"
],

"RUNTIME_LAYER":[
"engine","runtime",
"executor",
"pipeline",
"router",
"service"
]

}


function_registry=[]
module_registry=[]
keyword_registry=[]


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


            tree=ast.parse(code)


            classes=[]
            functions=[]


            for node in ast.walk(tree):

                if isinstance(node,ast.ClassDef):
                    classes.append(node.name)


                if isinstance(node,ast.FunctionDef):
                    functions.append(node.name)


            lower=code.lower()

            layers=[]


            for layer,words in keywords.items():

                for word in words:

                    c=lower.count(word)

                    if c:

                        layers.append(layer)

                        keyword_registry.append({

                        "keyword":word,
                        "file":fp,
                        "count":c

                        })


            function_registry.append({

            "file":fp,
            "layers":"|".join(set(layers)),
            "classes":"|".join(classes),
            "functions":"|".join(functions)

            })


            module_registry.append({

            "module":file,
            "path":fp,
            "capability":"|".join(set(layers))

            })


        except Exception as e:

            function_registry.append({

            "file":fp,
            "error":str(e)

            })



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
"Function_Capability_Registry_V1.0.csv",
function_registry
)

save(
"Module_Capability_Map_V1.0.csv",
module_registry
)

save(
"Keyword_Discovery_Map_V1.0.csv",
keyword_registry
)


print("="*60)
print("Phase 2 Function Capability Scan Complete")
print("="*60)

print("Files:",len(function_registry))
print("Modules:",len(module_registry))
print("Keywords:",len(keyword_registry))

print("")
print("Output:")
print(OUT)

