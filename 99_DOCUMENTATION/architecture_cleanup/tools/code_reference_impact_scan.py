import os
import json
import re
from datetime import datetime


ROOT = r"E:\football_v"

OUTPUT = (
    r"E:\football_v\99_DOCUMENTATION\architecture_cleanup\reports"
    r"\CODE_REFERENCE_IMPACT_SCAN_V1.0.json"
)


TARGETS = [
    r"04_Data_Processing_AI\feature_store\feature_database_connector.py",
    r"04_Data_Processing_AI\feature_store\database_connector.py",

    r"03_MODEL_LAYER",
    r"24_PREDICTION_INTELLIGENCE_LAYER",
    r"44_PRODUCTION_PREDICTION_RUNTIME",

    r"archive\V4_CLEANUP_ARCHIVE",
    r"deployment_scripts",

    r"feature_pipeline",
    r"processing_pipeline",
    r"backtest_pipeline",
    r"prediction_pipeline"
]


def collect_files():

    files=[]

    for root,dirs,names in os.walk(ROOT):

        for name in names:

            if name.endswith(
                (
                    ".py",
                    ".ps1",
                    ".json",
                    ".yaml",
                    ".yml"
                )
            ):
                files.append(
                    os.path.join(root,name)
                )

    return files



def scan_reference(target, files):

    result={

        "target":target,
        "python_refs":[],
        "powershell_refs":[],
        "json_refs":[]

    }


    keyword=os.path.splitext(
        os.path.basename(target)
    )[0]


    for file in files:

        try:

            with open(
                file,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                lines=f.readlines()


        except:
            continue


        for i,line in enumerate(lines,1):

            text=line.lower()


            if keyword.lower() in text:


                item={

                    "file":file,
                    "line":i,
                    "content":line.strip()

                }


                if file.endswith(".py"):

                    result["python_refs"].append(item)


                elif file.endswith(".ps1"):

                    result["powershell_refs"].append(item)


                elif file.endswith(".json"):

                    result["json_refs"].append(item)



    return result



def decision(item):

    refs=sum(
        len(v)
        for k,v in item.items()
        if isinstance(v,list)
    )


    target=item["target"]


    if "archive" in target.lower():

        return "KEEP_ARCHIVE"


    if refs==0:

        return "DELETE_READY"


    return "MIGRATE_FIRST"



def main():

    files=collect_files()

    results=[]


    for target in TARGETS:

        path=os.path.join(
            ROOT,
            target
        )


        if not os.path.exists(path):

            continue


        result=scan_reference(
            target,
            files
        )


        result["decision"]=decision(result)

        results.append(result)



    report={

        "version":
        "CODE_REFERENCE_IMPACT_SCAN_V1.0",

        "time":
        str(datetime.now()),

        "scan_root":
        ROOT,

        "targets":
        results

    }


    os.makedirs(
        os.path.dirname(OUTPUT),
        exist_ok=True
    )


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("==============================")
    print("CODE REFERENCE IMPACT SCAN")
    print("==============================")
    print("Targets:",len(results))
    print("Report:")
    print(OUTPUT)



if __name__=="__main__":

    main()
