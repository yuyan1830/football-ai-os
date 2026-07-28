import json
import os
from datetime import datetime


REGISTRY_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry_v11.json"
)


VERSION_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\version\version_registry.json"
)



def load_json(path):

    if not os.path.exists(path):

        return []

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



def create_version(asset,index):


    return {


        "Version_ID":
            f"VER-{index:06d}",


        "Asset_ID":
            asset.get(
                "Asset_ID"
            ),


        "Version_Number":
            "1.0",


        "Parent_Version":
            None,


        "Create_Time":
            datetime.now().isoformat(),


        "Source":
            asset.get(
                "Source",
                "Unknown"
            ),


        "Data_Period":
            asset.get(
                "Data_Period",
                "Unknown"
            ),


        "SHA256":
            asset.get(
                "SHA256"
            ),


        "Status":
            "CURRENT",


        "Change_Reason":
            "Initial registration"

    }



def run():


    assets = load_json(
        REGISTRY_PATH
    )


    versions = load_json(
        VERSION_PATH
    )


    if versions:

        print(
            "Version registry already exists"
        )

        return



    for i,asset in enumerate(
        assets,
        start=1
    ):


        versions.append(
            create_version(
                asset,
                i
            )
        )



    save_json(
        VERSION_PATH,
        versions
    )


    print(
        "Version Manager completed:",
        len(versions),
        "versions"
    )



if __name__=="__main__":

    print(
        "Football AI OS Version Manager V1.1"
    )

    run()