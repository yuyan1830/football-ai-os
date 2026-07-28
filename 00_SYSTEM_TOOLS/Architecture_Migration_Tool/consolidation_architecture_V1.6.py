import os
import json
from datetime import datetime


BASE = r"E:\football_v"

OUT = os.path.join(
    BASE,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP",
    "CONSOLIDATION_V1.6"
)


def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path,"r",encoding="utf-8") as f:
                return json.load(f)
        except:
            return default
    return default


def save(name,data):
    path=os.path.join(OUT,name)
    with open(path,"w",encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


print("="*60)
print("Architecture Consolidation Engine V1.6")
print("One Shot Deployment")
print("="*60)


cleanup_dir=os.path.join(
    BASE,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP"
)


migration=load_json(
    os.path.join(
        cleanup_dir,
        "migration_map_V1.2.json"
    ),
    {}
)


deprecated=load_json(
    os.path.join(
        cleanup_dir,
        "deprecated_list_V1.2.json"
    ),
    {}
)


dependency=load_json(
    os.path.join(
        cleanup_dir,
        "DEPENDENCY_MIGRATION_V1.5",
        "dependency_graph_V1.5.json"
    ),
    {}
)


checkpoint={
    "version":"Consolidation Checkpoint V1.6 BEFORE",
    "time":str(datetime.now()),
    "status":"CREATED",
    "source_modules":len(migration),
}


save(
    "checkpoint_before_consolidation_V1.6.json",
    checkpoint
)


plan={
    "version":"Architecture Consolidation Plan V1.6",
    "time":str(datetime.now()),
    "mode":"SAFE_CONSOLIDATION",

    "rules":[
        "one_function_one_location",
        "keep_primary_module",
        "archive_duplicate_module",
        "redirect_dependency"
    ],

    "migration_items":len(migration),

    "dependency_items":len(dependency),

    "deprecated_items":len(deprecated),

    "operations":[
        "duplicate_resolution",
        "dependency_redirect",
        "registry_prepare",
        "archive_prepare",
        "checkpoint"
    ]
}


save(
    "consolidation_plan_V1.6.json",
    plan
)


redirect={
    "version":"Dependency Redirect Map V1.6",
    "time":str(datetime.now()),
    "status":"READY",

    "redirect_rules":migration
}


save(
    "dependency_redirect_map_V1.6.json",
    redirect
)


report={
    "version":"Architecture Consolidation Engine V1.6",
    "time":str(datetime.now()),
    "status":"ANALYSIS_COMPLETE",

    "mode":"NO_DELETE",

    "created":[
        "checkpoint_before_consolidation_V1.6.json",
        "consolidation_plan_V1.6.json",
        "dependency_redirect_map_V1.6.json"
    ],

    "next_step":
    "V1.7_CONSOLIDATION_EXECUTION"
}


save(
    "consolidation_execution_report_V1.6.json",
    report
)


print("Architecture Consolidation Engine V1.6 Completed")

print(json.dumps(
    report,
    indent=4,
    ensure_ascii=False
))

