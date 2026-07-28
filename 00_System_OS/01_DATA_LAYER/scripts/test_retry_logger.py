import os
import sys


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)



from task_queue.retry_logger import (

    add_retry_record,

    get_retry_records,

    get_failed_retry_count

)





def run_test():


    print(
        "======================"
    )

    print(
        "Retry Logger Test"
    )

    print(
        "======================"
    )


    task_id="TASK_RETRY_TEST_001"



    add_retry_record(

        task_id,

        1,

        "failed",

        "Connection Timeout",

        15

    )



    add_retry_record(

        task_id,

        2,

        "failed",

        "API Error",

        8

    )



    add_retry_record(

        task_id,

        3,

        "success",

        None,

        4

    )



    print()


    print(
        "Retry Records:"
    )


    for row in get_retry_records(task_id):

        print(row)



    print()


    print(
        "Failed Count:"
    )


    print(
        get_failed_retry_count(task_id)
    )





if __name__ == "__main__":

    run_test()