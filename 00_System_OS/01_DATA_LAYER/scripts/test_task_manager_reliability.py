import os
import sys


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


from task_queue.task_history import (

    get_history

)





def run_test():


    print(
        "======================"
    )

    print(
        "Task Manager Reliability Test"
    )

    print(
        "======================"
    )



    task_id=create_task(

        task_type="odds_download",

        source="Pinnacle",

        target="odds.csv",

        priority=1

    )



    print()

    print(
        "Created:"
    )

    print(task_id)



    print()

    print(
        "Task:"
    )

    print(
        get_task(task_id)
    )



    print()

    print(
        "History:"
    )


    for row in get_history(task_id):

        print(row)






if __name__ == "__main__":

    run_test()