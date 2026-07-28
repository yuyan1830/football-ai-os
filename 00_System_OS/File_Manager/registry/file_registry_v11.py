import json
from datetime import datetime


INPUT_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry.json"
)


OUTPUT_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry_v11.json"
)



def load_registry():

    with open(
        INPUT_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def upgrade_asset(record, index):


    now = datetime.now().isoformat()


    new_record = {


        "Asset_ID":
            record.get(
                "Asset_ID",
                f"FA-{index:06d}"
            ),


        "File_Name":
            record.get(
                "File_Name"
            ),


        "Full_Path":
            record.get(
                "Full_Path"
            ),


        "Source":
            "Unknown",


        "Data_Period":
            "Unknown",


        "Version":
            "1.0",


        "Category":
            record.get(
                "Category",
                "UNKNOWN"
            ),


        "SHA256":
            record.get(
                "SHA256"
            ),


        "Size":
            record.get(
                "Size",
                0
            ),


        "Create_Time":
            record.get(
                "Create_Time"
            ),


        "Modify_Time":
            record.get(
                "Modify_Time"
            ),


        "Owner_Module":
            "Unknown",


        "Lifecycle_Status":
            "REGISTERED",


        "Last_Access_Time":
            now

    }


    return new_record



def upgrade():


    old_records = load_registry()


    new_records = []


    for index, record in enumerate(
        old_records,
        start=1
    ):

        new_records.append(
            upgrade_asset(
                record,
                index
            )
        )


    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            new_records,
            f,
            indent=4
        )


    print(
        "Registry upgrade completed:",
        len(new_records),
        "assets"
    )



if __name__ == "__main__":

    print(
        "Football AI OS Registry Upgrade V1.1"
    )

    upgrade()