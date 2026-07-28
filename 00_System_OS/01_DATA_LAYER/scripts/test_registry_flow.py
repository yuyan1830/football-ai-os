import os
import sys


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    BASE_DIR
)


from core.hash_service import calculate_hash

from registry.registry_manager import register_data

from registry.data_lineage import add_lineage

from registry.import_tracker import record_import

from registry.quality_score import save_quality



TEST_FILE = os.path.join(

    BASE_DIR,

    "test_data",

    "test_odds.csv"

)



def run_test():


    print("======================")

    print("Registry Flow Test")

    print("======================")


    # 1 Hash

    file_hash = calculate_hash(
        TEST_FILE
    )


    print()

    print(
        "HASH:"
    )

    print(
        file_hash
    )



    # 2 Registry


    data_id = register_data(

        file_name="test_odds.csv",

        file_hash=file_hash,

        data_type="market_odds",

        source="manual_test",

        version="v001"

    )


    print()

    print(
        "DATA ID:"
    )

    print(
        data_id
    )



    # 3 Lineage


    add_lineage(

        data_id,

        "external_source",

        "manual_import"

    )



    # 4 Import


    record_import(

        data_id,

        "csv",

        "system_test",

        "success"

    )



    # 5 Quality


    save_quality(

        data_id,

        1.0,

        1.0

    )



    print()

    print(
        "Registry Flow Completed"
    )



if __name__=="__main__":

    run_test()