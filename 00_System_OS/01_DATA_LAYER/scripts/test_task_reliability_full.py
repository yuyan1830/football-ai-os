import os
import sys
import time


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)



from task_queue.task_manager import (
    create_task,
    get_task
)


from task_queue.scheduler import (
    start_task,
    finish_task
)


from task_queue.retry_engine import (
    retry_task
)


from task_queue.task_history import (
    get_history
)


from task_queue.retry_logger import (
    get_retry_records
)





def run_test():


    print(
        "======================"
    )

    print(
        "Full Reliability Flow Test"
    )

    print(
        "======================"
    )



    task_id = create_task(

        task_type="odds_download",

        source="Pinnacle",

        target="odds.csv",

        priority=1

    )


    print()

    print(
        "Created Task:"
    )

    print(task_id)



    print()

    print(
        "Start Task"
    )


    start_task(task_id)



    print(
        get_task(task_id)
    )



    print()

    print(
        "Simulate Download Failure"
    )



    finish_task(

        task_id,

        success=False,

        error="API timeout"

    )



    print(
        get_task(task_id)
    )



    print()

    print(
        "Retry Engine"
    )



    result = retry_task(task_id)


    print(result)



    print()

    print(
        "After Retry:"
    )


    print(
        get_task(task_id)
    )



    print()

    print(
        "Task History:"
    )


    for row in get_history(task_id):

        print(row)



    print()

    print(
        "Retry Records:"
    )


    for row in get_retry_records(task_id):

        print(row)





if __name__ == "__main__":

    run_test()