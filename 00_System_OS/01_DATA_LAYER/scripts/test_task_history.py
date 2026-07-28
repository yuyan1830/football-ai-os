import os
import sys


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)



from task_queue.task_history import (
    add_history,
    get_history
)





def run_test():


    print(
        "======================"
    )

    print(
        "Task History Test"
    )

    print(
        "======================"
    )


    task_id="TASK_TEST_001"



    add_history(

        task_id,

        None,

        "pending",

        "Task Created"

    )



    add_history(

        task_id,

        "pending",

        "fetching",

        "Download Started"

    )



    add_history(

        task_id,

        "fetching",

        "failed",

        "Network Timeout"

    )



    add_history(

        task_id,

        "failed",

        "retrying",

        "Retry Attempt 1"

    )



    add_history(

        task_id,

        "retrying",

        "completed",

        "Download Success"

    )



    print()

    print(
        "History:"
    )


    for row in get_history(task_id):

        print(row)





if __name__ == "__main__":

    run_test()