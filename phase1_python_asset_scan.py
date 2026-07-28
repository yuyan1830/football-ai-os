from pathlib import Path
import ast
import csv
import os

ROOT = r"E:\football_v"

OUT = os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "Legacy_Asset_Index",
    "Phase_1_Python_Asset"
)

os.makedirs(OUT, exist_ok=True)

python_assets=[]
class_assets=[]
function_assets=[]
dependency_assets=[]


for path,dirs,files in os.walk(ROOT):

    for file in files:

        if not file.endswith(".py"):
            continue

        fp=os.path.join(path,file)

        try:

            code=Path(fp).read_text(
                encoding="utf-8",
                errors="ignore"
            )

            tree=ast.parse(code)

            classes=[]
            functions=[]
            imports=[]


            for node in ast.walk(tree):

                if isinstance(node,ast.ClassDef):
                    classes.append(node.name)

                    class_assets.append({
                        "file":fp,
                        "class":node.name
                    })


                elif isinstance(node,ast.FunctionDef):
                    functions.append(node.name)

                    function_assets.append({
                        "file":fp,
                        "function":node.name
                    })


                elif isinstance(node,ast.Import):

                    for n in node.names:

                        imports.append(n.name)

                        dependency_assets.append({
                            "file":fp,
                            "dependency":n.name
                        })


                elif isinstance(node,ast.ImportFrom):

                    if node.module:

                        imports.append(node.module)

                        dependency_assets.append({
                            "file":fp,
                            "dependency":node.module
                        })


            python_assets.append({
                "file":fp,
                "lines":len(code.splitlines()),
                "classes":len(classes),
                "functions":len(functions),
                "imports":len(imports)
            })


        except Exception as e:

            python_assets.append({
                "file":fp,
                "error":str(e)
            })


def save(name,data):

    if not data:
        return

    fields=set()

    for row in data:
        fields.update(row.keys())


    with open(
        os.path.join(OUT,name),
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer=csv.DictWriter(
            f,
            fieldnames=list(fields),
            extrasaction="ignore"
        )

        writer.writeheader()
        writer.writerows(data)



save(
    "Python_Asset_Index_V1.0.csv",
    python_assets
)

save(
    "Python_Class_Registry_V1.0.csv",
    class_assets
)

save(
    "Python_Function_Registry_V1.0.csv",
    function_assets
)

save(
    "Python_Dependency_Map_V1.0.csv",
    dependency_assets
)


print("="*60)
print("Phase 1 Python Asset Scan Complete")
print("="*60)

print("Python Files:",len(python_assets))
print("Classes:",len(class_assets))
print("Functions:",len(function_assets))

print("")
print("Output:")
print(OUT)

