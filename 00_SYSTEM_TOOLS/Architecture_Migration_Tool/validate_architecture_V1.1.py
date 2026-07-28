import os
import json
from datetime import datetime
from collections import defaultdict


BASE=r"E:\football_v"

TOOL_DIR=os.path.join(
    BASE,
    "00_SYSTEM_TOOLS",
    "Architecture_Migration_Tool"
)

REPORT_DIR=os.path.join(
    TOOL_DIR,
    "reports"
)

REPORT=os.path.join(
    REPORT_DIR,
    "ARCHITECTURE_VALIDATION_REPORT_V1.1.json"
)

CHECKPOINT=os.path.join(
    REPORT_DIR,
    "ARCHITECTURE_VALIDATION_CHECKPOINT_V1.1.json"
)

REGISTRY=os.path.join(
    TOOL_DIR,
    "architecture_registry.json"
)



def save_json(path,data):

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



def scan_python_files():

    files=[]

    for root,dirs,names in os.walk(BASE):

        for name in names:

            if name.endswith(".py"):

                files.append(
                    os.path.join(root,name)
                )

    return files



def duplicate_function_scan(files):

    groups=defaultdict(list)


    for f in files:

        name=os.path.basename(f)

        key=name.lower()


        groups[key].append(f)


    duplicates={}


    for k,v in groups.items():

        if len(v)>1:

            duplicates[k]=v


    return duplicates



def layer_scan(files):

    layers=defaultdict(int)


    for f in files:

        rel=os.path.relpath(
            f,
            BASE
        )


        first=rel.split(os.sep)[0]


        layers[first]+=1


    return dict(layers)



def registry_check():

    if not os.path.exists(REGISTRY):

        return {
            "status":"MISSING"
        }


    with open(
        REGISTRY,
        "r",
        encoding="utf-8"
    ) as f:

        data=json.load(f)


    return {

        "status":"OK",

        "version":
        data.get(
            "version",
            "unknown"
        ),

        "module_count":
        len(
            data.get(
                "modules",
                []
            )
        )

    }



def validate():

    print("="*60)

    print(
        "Architecture Validation Engine V1.1"
    )

    print(
        "Validation Only Mode"
    )

    print("="*60)


    files=scan_python_files()


    duplicates=duplicate_function_scan(
        files
    )


    result={

        "version":
        "Architecture Validation Engine V1.1",

        "time":
        str(datetime.now()),

        "status":
        "VALIDATION_COMPLETE",

        "python_files":
        len(files),

        "duplicate_groups":
        len(duplicates),

        "duplicates":
        duplicates,

        "layers":
        layer_scan(files),

        "registry":
        registry_check(),

        "recommendation":
        "review_before_cleanup"

    }


    save_json(
        REPORT,
        result
    )


    checkpoint={

        "checkpoint":
        "ARCHITECTURE_VALIDATION_V1.1",

        "time":
        str(datetime.now()),

        "status":
        "COMPLETED",

        "next_step":
        "cleanup_decision"

    }


    save_json(
        CHECKPOINT,
        checkpoint
    )


    print()

    print(
        "Architecture Validation Completed"
    )

    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )



if __name__=="__main__":

    validate()

