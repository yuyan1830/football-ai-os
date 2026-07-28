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



from task_queue.task_manager import create_task


from task_queue.scheduler import (

    get_next_task,

    start_task,

    finish_task,

    fail_task,

    scheduler_status

)



from task_queue.task_query import get_task





def run_test():


    print("======================")

    print(
        "Task Scheduler Test"
    )

    print("======================")


    print()



    # 创建三个任务


    task1 = create_task(

        task_type="odds_download",

        source="Pinnacle",

        target="odds.csv",

        priority=1

    )



    task2 = create_task(

        task_type="match_download",

        source="API",

        target="match.json",

        priority=5

    )



    task3 = create_task(

        task_type="player_download",

        source="API",

        target="player.json",

        priority=3

    )



    print(
        "Created Tasks:"
    )


    print(task1)

    print(task2)

    print(task3)



    print()



    # Scheduler 获取最高优先级任务


    task = get_next_task()



    print(
        "Next Task:"
    )


    print(task)



    print()



    if task:


        start_task(

            task["task_id"]

        )


        print(
            "After Start:"
        )


        print(

            get_task(

                task["task_id"]

            )

        )



        print()



        if task["task_type"] == "odds_download":


            fail_task(

                task["task_id"],

                "Source unavailable"

            )


        else:


            finish_task(

                task["task_id"]

            )



        print(
            "After Finish:"
        )


        print(

            get_task(

                task["task_id"]

            )

        )



    print()



    print(
        "Scheduler Status:"
    )


    print(

        scheduler_status()

    )





if __name__ == "__main__":

    run_test()