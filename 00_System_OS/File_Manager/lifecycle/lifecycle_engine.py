import json
from datetime import datetime


RULE_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\lifecycle\lifecycle_rules.json"
)


REGISTRY_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry_v11.json"
)


HISTORY_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\lifecycle\lifecycle_history.json"
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
            indent=4
        )



def process_asset(asset):


    old_status = (
        asset.get(
            "Lifecycle_Status"
        )
    )


    new_status = old_status


    if old_status == "REGISTERED":

        if asset.get("SHA256"):

            new_status="VALIDATED"



    if old_status=="VALIDATED":

        new_status="ACTIVE"



    if new_status != old_status:


        asset["Lifecycle_Status"] = new_status


        return {

            "Asset_ID":
                asset["Asset_ID"],

            "Old_Status":
                old_status,

            "New_Status":
                new_status,

            "Time":
                datetime.now().isoformat()

        }



    return None



def run():


    assets = load_json(
        REGISTRY_PATH
    )


    history=[]


    for asset in assets:


        result = process_asset(
            asset
        )


        if result:

            history.append(
                result
            )



    save_json(
        REGISTRY_PATH,
        assets
    )


    save_json(
        HISTORY_PATH,
        history
    )


    print(
        "Lifecycle Engine completed:",
        len(history),
        "changes"
    )



if __name__=="__main__":

    print(
        "Football AI OS Lifecycle Rule Engine V1.1"
    )

    run()