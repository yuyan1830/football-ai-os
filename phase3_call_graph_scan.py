import os
import ast
import csv


ROOT=r"E:\football_v"


OUT=os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_3_Call_Graph"
)


os.makedirs(OUT,exist_ok=True)


call_graph=[]
class_map=[]
entry_map=[]


entry_keywords=[
    "main",
    "run",
    "start",
    "execute",
    "pipeline",
    "engine"
]


python_files=[]


for path,dirs,files in os.walk(ROOT):

    for file in files:

        if file.endswith(".py"):

            python_files.append(
                os.path.join(path,file)
            )



for fp in python_files:

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
        calls=[]


        for node in ast.walk(tree):


            if isinstance(node,ast.ClassDef):

                classes.append(node.name)

                class_map.append({

                "file":fp,
                "class":node.name

                })


            if isinstance(node,ast.FunctionDef):

                functions.append(node.name)


                for child in ast.walk(node):

                    if isinstance(child,ast.Call):

                        if isinstance(child.func,ast.Name):

                            calls.append(
                                child.func.id
                            )


        for c in calls:

            call_graph.append({

            "file":fp,
            "called_function":c

            })


        for f in functions:

            low=f.lower()

            for key in entry_keywords:

                if key in low:

                    entry_map.append({

                    "file":fp,
                    "entry_function":f,
                    "keyword":key

                    })



    except Exception as e:

        call_graph.append({

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
"Call_Graph_Registry_V1.0.csv",
call_graph
)


save(
"Class_Function_Map_V1.0.csv",
class_map
)


save(
"Entry_Point_Map_V1.0.csv",
entry_map
)



print("="*60)
print("Phase 3 Call Graph Scan Complete")
print("="*60)

print("Calls:",len(call_graph))
print("Classes:",len(class_map))
print("Entry:",len(entry_map))

print("")
print("Output:")
print(OUT)

