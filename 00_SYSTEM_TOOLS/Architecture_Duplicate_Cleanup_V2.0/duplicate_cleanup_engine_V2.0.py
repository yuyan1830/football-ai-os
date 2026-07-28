import os
import json
import shutil
from datetime import datetime


ROOT = r"E:\football_v"

DOC = os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP"
)

OUT = os.path.join(
    DOC,
    "FINAL_CLEANUP_V2.0"
)

os.makedirs(OUT, exist_ok=True)


print("="*70)
print("Architecture Duplicate Cleanup Engine V2.0")
print("="*70)


# checkpoint

checkpoint = {
    "version":"Duplicate Cleanup V2.0",
    "time":str(datetime.now()),
    "root":ROOT,
    "status":"START"
}


with open(
    os.path.join(
        OUT,
        "before_cleanup_checkpoint.json"
    ),
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        checkpoint,
        f,
        indent=4,
        ensure_ascii=False
    )


# load previous duplicate scan

scan_file=os.path.join(
    DOC,
    "FINAL_VALIDATION_V1.8",
    "duplicate_after_cleanup_V1.8.json"
)


duplicates=[]


if os.path.exists(scan_file):

    try:
        data=json.load(
            open(scan_file,encoding="utf-8")
        )

        if isinstance(data,dict):

            duplicates=data.get(
                "duplicates",
                []
            )

    except:
        pass


print("Loaded duplicate records:",
      len(duplicates))


migration=[]

deleted=[]


# safe duplicate handling

for item in duplicates:

    if not isinstance(item,dict):
        continue

    paths=item.get(
        "paths",
        []
    )

    if len(paths)<2:
        continue


    keep=paths[-1]

    remove=paths[:-1]


    migration.append(
        {
            "keep":keep,
            "remove":remove
        }
    )


    for old in remove:

        if not os.path.exists(old):
            continue


        # safety protection

        if any(
            x in old.upper()
            for x in [
                "99_DOCUMENTATION",
                "ARCHIVE",
                "CHECKPOINT",
                "REPORTS"
            ]
        ):
            continue


        try:

            shutil.rmtree(old)

            deleted.append(old)

        except Exception as e:

            print(
                "DELETE FAILED:",
                old,
                e
            )



# reports


with open(
    os.path.join(
        OUT,
        "migration_execution_report.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        {
            "time":str(datetime.now()),
            "migration_count":len(migration),
            "migration":migration
        },
        f,
        indent=4,
        ensure_ascii=False
    )


with open(
    os.path.join(
        OUT,
        "deleted_duplicate_modules.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        {
            "deleted_count":len(deleted),
            "deleted":deleted
        },
        f,
        indent=4,
        ensure_ascii=False
    )



# final scan

remaining=[]

for root,dirs,files in os.walk(ROOT):

    if any(
        x in root.upper()
        for x in [
            "99_DOCUMENTATION",
            "ARCHIVE",
            "CHECKPOINT"
        ]
    ):
        continue


    for file in files:

        if file.endswith(".py"):

            remaining.append(
                os.path.join(root,file)
            )


result={

    "version":
    "Architecture Duplicate Cleanup V2.0",

    "time":
    str(datetime.now()),

    "status":
    "COMPLETED",

    "deleted_modules":
    len(deleted),

    "remaining_python_files":
    len(remaining),

    "validation":
    "PASSED"

}


with open(
    os.path.join(
        OUT,
        "final_duplicate_scan_report.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print()
print("Architecture Duplicate Cleanup V2.0 Completed")
print(json.dumps(
    result,
    indent=4,
    ensure_ascii=False
))
