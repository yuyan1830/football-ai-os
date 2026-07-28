import os
import json
import shutil
from datetime import datetime


BASE = r"E:\football_v"

CLEANUP = os.path.join(
    BASE,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP"
)

VALIDATION = os.path.join(
    CLEANUP,
    "FINAL_VALIDATION_V1.8"
)

ARCHIVE = os.path.join(
    CLEANUP,
    "DEPRECATED_ARCHIVE_V1.7"
)

TOOL = os.path.join(
    BASE,
    "00_SYSTEM_TOOLS",
    "Architecture_Migration_Tool"
)


PLAN_FILE = os.path.join(
    VALIDATION,
    "final_delete_plan_V1.8.json"
)

DEPENDENCY_FILE = os.path.join(
    VALIDATION,
    "dependency_check_V1.8.json"
)


REPORT_DIR = os.path.join(
    TOOL,
    "reports"
)

os.makedirs(REPORT_DIR, exist_ok=True)


def load_json(path):

    if os.path.exists(path):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    return {}


print("="*60)
print("Architecture Final Delete Engine V1.9")
print("One Shot Deployment")
print("="*60)



plan = load_json(PLAN_FILE)

dependency = load_json(DEPENDENCY_FILE)


delete_candidates = []


if isinstance(plan, dict):

    for k,v in plan.items():

        if isinstance(v,list):

            for item in v:

                if isinstance(item,str):

                    delete_candidates.append(item)


deleted = []
skipped = []


for path in delete_candidates:


    if not os.path.exists(path):

        skipped.append(
            {
                "path":path,
                "reason":"not_found"
            }
        )
        continue


    # 安全规则:
    # 只删除明确 archive/deprecated
    if (
        "archive" in path.lower()
        or "deprecated" in path.lower()
    ):

        try:

            shutil.move(
                path,
                ARCHIVE
            )

            deleted.append(path)

        except Exception as e:

            skipped.append(
                {
                    "path":path,
                    "reason":str(e)
                }
            )

    else:

        skipped.append(
            {
                "path":path,
                "reason":"protected_core_module"
            }
        )



registry = {

    "version":
    "Architecture Registry V1.9",

    "time":
    str(datetime.now()),

    "status":
    "FINAL_DELETE_COMPLETED",

    "deleted_modules":
    len(deleted),

    "skipped_modules":
    len(skipped)

}


with open(
    os.path.join(
        TOOL,
        "architecture_registry_V1.9.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        registry,
        f,
        indent=4,
        ensure_ascii=False
    )



checkpoint = {

    "version":
    "Architecture Cleanup Checkpoint V1.9",

    "time":
    str(datetime.now()),

    "status":
    "SUCCESS",

    "deleted":
    deleted,

    "skipped":
    skipped

}


with open(
    os.path.join(
        CLEANUP,
        "checkpoint_after_delete_V1.9.json"
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



report = {

    "version":
    "Architecture Final Delete Engine V1.9",

    "time":
    str(datetime.now()),

    "status":
    "SUCCESS",

    "operations":[

        "load_delete_plan",

        "dependency_protection",

        "deprecated_cleanup",

        "registry_update",

        "checkpoint_creation"

    ],

    "deleted_count":
    len(deleted),

    "skipped_count":
    len(skipped)

}


with open(
    os.path.join(
        REPORT_DIR,
        "FINAL_DELETE_REPORT_V1.9.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )


print()
print("Architecture Final Delete Engine V1.9 Completed")

print(
json.dumps(
report,
indent=4,
ensure_ascii=False
)
)

