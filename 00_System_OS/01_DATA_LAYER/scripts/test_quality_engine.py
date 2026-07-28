import os
import sys


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)



from quality.quality_engine import evaluate_data


from quality.quality_report import get_quality_report





def run_test():


    print(
        "======================"
    )

    print(
        "Quality Engine Test"
    )

    print(
        "======================"
    )



    #
    # Test 1:
    # 正常数据
    #

    print()

    print(
        "Test 1: Normal Data"
    )



    data_id_1 = "DATA_QUALITY_TEST_001"



    normal_data = {


        "match_id":

        "MATCH_001",


        "bookmaker":

        "Pinnacle",


        "odds":

        "1.85",


        "market":

        "1X2"


    }



    result1 = evaluate_data(

        data_id_1,

        normal_data

    )



    print(result1)



    print()



    #
    # Test 2:
    # 异常数据
    #

    print(
        "Test 2: Bad Data"
    )



    data_id_2 = "DATA_QUALITY_TEST_002"



    bad_data = {


        "match_id":

        "",


        "bookmaker":

        "",


        "odds":

        None,


        "market":

        "1X2"


    }



    result2 = evaluate_data(

        data_id_2,

        bad_data

    )



    print(result2)



    print()



    #
    # 查询报告
    #

    print(
        "Quality Reports"
    )



    print(
        get_quality_report(

            data_id_1

        )

    )


    print()


    print(
        get_quality_report(

            data_id_2

        )

    )







if __name__ == "__main__":

    run_test()