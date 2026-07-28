import os
import json
from datetime import datetime


BASE = r"E:\football_v"

SRC = os.path.join(
    BASE,
    "00_SYSTEM_TOOLS",
    "Architecture_Migration_Tool",
    "reports",
    "MERGE_ANALYSIS_REPORT_V1.0.json"
)

OUT_DIR = os.path.join(
    BASE,
    "99_DOCUMENTATION",
    "architecture_cleanup"
)


os.makedirs(OUT_DIR, exist_ok=True)


def load_report():

    if not os.path.exists(SRC):

        return {}

    with open(
        SRC,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def classify(report):

    result = {

        "KEEP":[],
        "MERGE":[],
        "DEPRECATED":[],
        "ARCHIVE":[]

    }


    duplicate = report.get(
        "duplicates",
        {}
    )


    for name, paths in duplicate.items():

        if len(paths) <= 1:
            continue


        keep = paths[0]

        result["KEEP"].append(
            keep
        )


        for p in paths[1:]:

            result["MERGE"].append(
                {
                    "source":p,
                    "target":keep
                }
            )


            result["DEPRECATED"].append(
                p
            )



    return result



def generate():

    report = load_report()

    plan = classify(report)


    output={

        "version":
        "Architecture Cleanup Planner V1.2",

        "time":
        str(datetime.now()),


        "status":
        "CLEANUP_PLAN_CREATED",


        "summary":{

            "keep":
            len(plan["KEEP"]),

            "merge":
            len(plan["MERGE"]),

            "deprecated":
            len(plan["DEPRECATED"])

        },


        "plan":
        plan

    }


    with open(

        os.path.join(
            OUT_DIR,
            "cleanup_plan_V1.2.json"
        ),

        "w",
        encoding="utf-8"

    ) as f:

        json.dump(
            output,
            f,
            indent=4,
            ensure_ascii=False
        )


    migration={

        "version":
        "Migration Map V1.2",

        "time":
        str(datetime.now()),

        "migration_targets":
        plan["MERGE"]

    }


    with open(

        os.path.join(
            OUT_DIR,
            "migration_map_V1.2.json"
        ),

        "w",
        encoding="utf-8"

    ) as f:

        json.dump(
            migration,
            f,
            indent=4,
            ensure_ascii=False
        )



    deprecated={

        "version":
        "Deprecated Registry V1.2",

        "count":
        len(plan["DEPRECATED"]),

        "items":
        plan["DEPRECATED"]

    }


    with open(

        os.path.join(
            OUT_DIR,
            "deprecated_list_V1.2.json"
        ),

        "w",
        encoding="utf-8"

    ) as f:

        json.dump(
            deprecated,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("="*60)
    print("Architecture Cleanup Planner V1.2")
    print("="*60)

    print(
        json.dumps(
            output["summary"],
            indent=4
        )
    )

    print(
        "Cleanup Plan Generated"
    )



if __name__=="__main__":

    generate()

