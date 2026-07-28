import os
import json
import hashlib
import ast
from datetime import datetime


ROOT = r"E:\football_v"

TOOL = os.path.join(
    ROOT,
    "00_SYSTEM_TOOLS",
    "Architecture_Migration_Tool"
)

DOC = os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP",
    "FINAL_FREEZE_V4.0"
)

ARCHIVE = os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP",
    "FINAL_CLEANUP_V3.0",
    "DEPRECATED_ARCHIVE"
)

os.makedirs(DOC,exist_ok=True)


def file_hash(path):

    h=hashlib.sha256()

    try:
        with open(path,"rb") as f:
            for b in iter(lambda:f.read(8192),b""):
                h.update(b)

        return h.hexdigest()

    except:
        return None



def imports(path):

    result=[]

    try:

        tree=ast.parse(
            open(path,encoding="utf8").read()
        )

        for node in ast.walk(tree):

            if isinstance(node,ast.Import):

                for n in node.names:
                    result.append(n.name)

            if isinstance(node,ast.ImportFrom):

                if node.module:
                    result.append(node.module)

    except:
        pass

    return result



modules={}

for root,dirs,files in os.walk(ROOT):

    if "DEPRECATED_ARCHIVE" in root:
        continue

    if "FINAL_CLEANUP_V3.0" in root:
        continue


    for f in files:

        if f.endswith(".py"):

            p=os.path.join(root,f)

            h=file_hash(p)

            if h:

                modules.setdefault(h,[]).append(p)



duplicates=[]

masters={}


for h,items in modules.items():

    if len(items)>1:


        # 优先选择非临时目录

        items.sort(
            key=lambda x:
            (
                "test" in x.lower(),
                "archive" in x.lower(),
                len(x)
            )
        )


        masters[h]=items[0]


        for dup in items[1:]:

            duplicates.append(
                {
                    "hash":h,
                    "master":items[0],
                    "duplicate":dup
                }
            )



dependency_map=[]


for h,master in masters.items():

    dependency_map.append(
        {
            "hash":h,
            "master":master
        }
    )


report={

    "version":
    "Architecture Cleanup Engine V4.0",

    "time":
    str(datetime.now()),

    "status":
    "FROZEN_ANALYSIS_COMPLETE",

    "module_total":
    len(modules),

    "duplicate_detected":
    len(duplicates),

    "master_modules":
    len(masters),

    "dependency_scan":
    "COMPLETED",

    "next":
    "FINAL_DELETE_AFTER_CONFIRM"

}



with open(
    os.path.join(DOC,"final_duplicate_scan_V4.0.json"),
    "w",
    encoding="utf8"
) as f:

    json.dump(
        duplicates,
        f,
        indent=4,
        ensure_ascii=False
    )



with open(
    os.path.join(DOC,"dependency_redirect_map_V4.0.json"),
    "w",
    encoding="utf8"
) as f:

    json.dump(
        dependency_map,
        f,
        indent=4,
        ensure_ascii=False
    )



with open(
    os.path.join(DOC,"FROZEN_ARCHITECTURE_CHECKPOINT_V4.0.json"),
    "w",
    encoding="utf8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )


print(
json.dumps(
report,
indent=4,
ensure_ascii=False
)
)

