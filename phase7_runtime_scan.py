import os
import csv
import ast


ROOT=r"E:\football_v"


OUT=os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_7_Runtime_Registry"
)


os.makedirs(OUT,exist_ok=True)



keywords={


"PREDICTION":[

"predict",
"prediction",
"forecast",
"probability",
"score",
"result",
"output"

],


"DECISION":[

"decision",
"final",
"recommend",
"selection",
"choice",
"risk",
"confidence"

],


"RUNTIME":[

"runtime",
"engine",
"executor",
"pipeline",
"router",
"service",
"workflow",
"controller"

],


"REPORT":[

"report",
"export",
"summary",
"json",
"csv"

]


}



runtime_assets=[]
prediction_map=[]
entry_flow=[]



entry_words=[

"main",
"start",
"run",
"execute",
"pipeline",
"engine"

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

                for w in words:

                    if w.lower() in lower:

                        layers.append(layer)



            if layers:


                runtime_assets.append({

                    "file":fp,

                    "layers":
                    "|".join(sorted(set(layers))),

                    "classes":
                    "|".join(classes),

                    "functions":
                    "|".join(functions)

                })



            for f in functions:


                lf=f.lower()


                for e in entry_words:


                    if e in lf:


                        entry_flow.append({

                            "file":fp,

                            "entry_function":f,

                            "keyword":e

                        })



            if any(

                x in lower

                for x in

                [

                "predict",

                "prediction",

                "decision",

                "final"

                ]

            ):


                prediction_map.append({

                    "file":fp,

                    "functions":
                    "|".join(functions),

                    "classes":
                    "|".join(classes)

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

"Runtime_Asset_Registry_V1.0.csv",

runtime_assets

)


save(

"Prediction_Decision_Map_V1.0.csv",

prediction_map

)


save(

"Entry_Runtime_Flow_V1.0.csv",

entry_flow

)



print("="*60)

print("Phase 7 Runtime Asset Scan Complete")

print("="*60)


print("Runtime Files:",len(runtime_assets))

print("Prediction Files:",len(prediction_map))

print("Entry Points:",len(entry_flow))


print("")

print("Output:")

print(OUT)

