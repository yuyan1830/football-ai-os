import os
import json


from core.db_connection import test_connection

from core.logger import write_log

from import_pipeline.importer import import_file



SYSTEM_NAME = "Football AI OS"

VERSION = "Data Layer V1.3.1"



def startup_check():

    print("======================")
    print(SYSTEM_NAME)
    print(VERSION)
    print("======================")

    print()


    print("Database Check:")

    db_status = test_connection()

    print(db_status)


    print()


    try:

        write_log(
            "INFO",
            "Core Service Started"
        )


        print(
            "Logger: OK"
        )


    except Exception as e:


        print(
            "Logger Error:",
            e
        )



    print(
        "Core Service Layer Ready"
    )





def import_test():


    print()

    print("======================")

    print(
        "Import Pipeline Test"
    )

    print("======================")


    test_file = os.path.join(

        "test_data",

        "test_odds.csv"

    )



    if not os.path.exists(test_file):


        result = {


            "status":
            "failed",


            "message":
            "Test file missing",


            "file":
            test_file

        }


        print(
            json.dumps(
                result,
                indent=4,
                ensure_ascii=False
            )
        )


        return result





    result = import_file(

        file_path=test_file,

        data_type="market_odds",

        source="manual_test"

    )



    print()


    print(
        json.dumps(

            result,

            indent=4,

            ensure_ascii=False

        )
    )


    return result





def system_status():


    status = {


        "system":
        SYSTEM_NAME,


        "version":
        VERSION,


        "database":
        "ready",


        "core_service":
        "ready",


        "import_pipeline":
        "ready"

    }


    return status





def main():


    startup_check()


    result = import_test()



    print()


    print("======================")

    print(
        "System Status"
    )

    print("======================")


    print(

        json.dumps(

            system_status(),

            indent=4,

            ensure_ascii=False

        )

    )





if __name__ == "__main__":

    main()