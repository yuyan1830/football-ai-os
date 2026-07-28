import os
import json
import shutil
from datetime import datetime


BASE = r"E:\football_v"

TOOL_DIR = os.path.join(
    BASE,
    "00_SYSTEM_TOOLS",
    "Architecture_Migration_Tool"
)

DOC_DIR = os.path.join(
    BASE,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP"
)

ARCHIVE_DIR = os.path.join(
    DOC_DIR,
    "DEPRECATED_ARCHIVE_V1.7"
)

REPORT_DIR = os.path.join(
    ARCHIVE_DIR,
    "reports"
)


os.makedirs(ARCHIVE_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


deprecated_registry = os.path.join(
    TOOL_DIR,
    "deprecated_registry.json"
)

migration_map = os.path.join(
    DOC_DIR,
    "migration_map_V1.2.json"
)


checkpoint_before = {
    "version":"Deprecated Archive Engine V1.7",
    "time":str(datetime.now()),
    "status":"BEFORE_ARCHIVE"
}


with open(
    os.path.join(
        ARCHIVE_DIR,
        "checkpoint_before_archive_V1.7.json"
    ),
    "w",
    encoding="utf8"
) as f:
    json.dump(
        checkpoint_before,
        f,
        indent=4,
        ensure_ascii=False
    )


items=[]


if os.path.exists(deprecated_registry):

    with open(
        deprecated_registry,
        encoding="utf8"
    ) as f:
        data=json.load(f)

    if isinstance(data,list):
        items=data

    elif isinstance(data,dict):
        items=list(data.values())


archive_count=0
skipped=0
errors=[]


for item in items:

    try:

        if isinstance(item,dict):
            path=item.get("path")
        else:
            path=item


        if not path:
            continue


        if os.path.exists(path):

            rel=os.path.relpath(
                path,
                BASE
            )

            target=os.path.join(
                ARCHIVE_DIR,
                rel
            )


            os.makedirs(
                os.path.dirname(target),
                exist_ok=True
            )


            shutil.move(
                path,
                target
            )

            archive_count+=1


        else:
            skipped+=1


    except Exception as e:

        errors.append(
            {
                "file":str(item),
                "error":str(e)
            }
        )



report={

    "version":
    "Architecture Cleanup Engine V1.7",

    "time":
    str(datetime.now()),

    "status":
    "SUCCESS",

    "operation":[

        "deprecated_verification",
        "archive_migration",
        "registry_update",
        "checkpoint_creation"

    ],

    "archived_modules":
    archive_count,

    "skipped":
    skipped,

    "errors":
    errors

}



with open(
    os.path.join(
        REPORT_DIR,
        "deprecated_move_report_V1.7.json"
    ),
    "w",
    encoding="utf8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )



checkpoint_after={

    "version":
    "Deprecated Archive Engine V1.7",

    "time":
    str(datetime.now()),

    "status":
    "ARCHIVE_COMPLETED",

    "archived_modules":
    archive_count

}


with open(
    os.path.join(
        ARCHIVE_DIR,
        "checkpoint_after_archive_V1.7.json"
    ),
    "w",
    encoding="utf8"
) as f:

    json.dump(
        checkpoint_after,
        f,
        indent=4,
        ensure_ascii=False
    )



print("="*60)
print("Architecture Cleanup Engine V1.7 Completed")
print(json.dumps(
    report,
    indent=4,
    ensure_ascii=False
))
print("="*60)
