import json
import os
from datetime import datetime

ROOT = r"E:\football_v"

INPUT = os.path.join(
    ROOT,
    "reports",
    "CODE_LOGIC_DUPLICATE_AUDIT_V2.0.json"
)

OUTPUT = os.path.join(
    ROOT,
    "reports",
    "CODE_LOGIC_DUPLICATE_IMPACT_ANALYSIS_V1.0.json"
)


def classify(name, files):

    paths = " ".join(files).lower()

    if "archive" in paths or "legacy" in paths or "backup" in paths:
        return {
            "classification":"ARCHIVE_DUPLICATE",
            "risk":"LOW",
            "action":"KEEP"
        }


    if name in [
        "predict",
        "run",
        "execute"
    ]:
        return {
            "classification":"ARCHITECTURE_DUPLICATE",
            "risk":"LOW",
            "action":"KEEP"
        }


    if name in [
        "connect",
        "database",
        "session"
    ]:
        return {
            "classification":"TRUE_DUPLICATE_POSSIBLE",
            "risk":"HIGH",
            "action":"REVIEW"
        }


    if name in [
        "score",
        "calculate",
        "confidence"
    ]:
        return {
            "classification":"FUNCTIONAL_LOGIC_OVERLAP",
            "risk":"MEDIUM",
            "action":"REVIEW"
        }


    return {
        "classification":"UNKNOWN_DUPLICATE",
        "risk":"MEDIUM",
        "action":"REVIEW"
    }



with open(INPUT,"r",encoding="utf-8") as f:
    data=json.load(f)



result={

    "version":
    "CODE_LOGIC_DUPLICATE_IMPACT_ANALYSIS_V1.0",

    "time":
    datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),

    "source":
    INPUT,

    "summary":{

        "function_groups":
        data.get(
            "summary",
            {}
        ).get(
            "function_duplicate_groups",
            0
        ),

        "class_groups":
        data.get(
            "summary",
            {}
        ).get(
            "class_duplicate_groups",
            0
        ),

        "delete_candidates":0,

        "merge_candidates":0
    },

    "analysis":[]

}



for item in data.get(
    "duplicate_groups",
    []
):

    name=item.get(
        "function",
        item.get(
            "class",
            "unknown"
        )
    )


    files=item.get(
        "files",
        []
    )


    c=classify(
        str(name).lower(),
        files
    )


    result["analysis"].append({

        "name":name,

        "files":files,

        **c
    })



with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print("="*60)
print("CODE LOGIC DUPLICATE IMPACT ANALYSIS")
print("="*60)
print("输出:")
print(OUTPUT)
print("分析数量:")
print(len(result["analysis"]))

