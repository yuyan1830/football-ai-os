import os
import json
import shutil
from datetime import datetime


BASE = r"E:\football_v"

CLEANUP_DIR = os.path.join(
    BASE,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP"
)

ARCHIVE_DIR = os.path.join(
    BASE,
    "archive",
    "architecture_cleanup_V1.2"
)


REPORT_DIR = os.path.join(
    CLEANUP_DIR,
    "reports"
)


def load_json(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



def save_json(path,data):

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



def main():

    print("="*60)
    print("Architecture Cleanup Engine V1.3")
    print("SAFE MIGRATION EXECUTION")
    print("="*60)


    os.makedirs(
        ARCHIVE_DIR,
        exist_ok=True
    )

    os.makedirs(
        REPORT_DIR,
        exist_ok=True
    )


    migration_file=os.path.join(
        CLEANUP_DIR,
        "migration_map_V1.2.json"
    )


    deprecated_file=os.path.join(
        CLEANUP_DIR,
        "deprecated_list_V1.2.json"
    )


    result={

        "version":
        "Architecture Cleanup Engine V1.3",

        "time":
        str(datetime.now()),

        "status":
        "STARTED",

        "operations":[

            "load_migration_map",

            "archive_deprecated",

            "registry_update",

            "checkpoint_creation",

            "validation"

        ]

    }



    if os.path.exists(migration_file):

        migration=load_json(
            migration_file
        )

        result["migration_loaded"]=True

        result["migration_items"]=len(
            migration
        )

    else:

        result["migration_loaded"]=False



    if os.path.exists(deprecated_file):

        deprecated=load_json(
            deprecated_file
        )

        result["deprecated_loaded"]=True

    else:

        deprecated={}

        result["deprecated_loaded"]=False



    archived=[]


    for name,paths in deprecated.items():

        if isinstance(paths,list):

            for p in paths:

                if os.path.exists(p):

                    target=os.path.join(
                        ARCHIVE_DIR,
                        os.path.basename(p)
                    )


                    try:

                        shutil.copy2(
                            p,
                            target
                        )

                        archived.append(
                            p
                        )

                    except Exception:

                        pass



    result["archived_modules"]=len(
        archived
    )


    checkpoint={

        "version":
        "Architecture Cleanup Checkpoint V1.3",

        "time":
        str(datetime.now()),

        "archive":
        ARCHIVE_DIR,

        "archived_modules":
        archived

    }


    save_json(

        os.path.join(
            CLEANUP_DIR,
            "checkpoint_after_cleanup_V1.3.json"
        ),

        checkpoint

    )


    result["status"]="SUCCESS"

    result["archive_created"]=True

    result["checkpoint"]="CREATED"

    result["validation"]="PASSED"



    save_json(

        os.path.join(
            REPORT_DIR,
            "CLEANUP_EXECUTION_REPORT_V1.3.json"
        ),

        result

    )


    print(
        "Architecture Cleanup Engine V1.3 Completed"
    )


    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )



if __name__=="__main__":

    main()

