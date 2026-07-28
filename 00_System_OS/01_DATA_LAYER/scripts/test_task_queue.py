import os
import sys


BASE_DIR=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    BASE_DIR
)



from task_queue.task_manager import create_task, update_task_status

from task_queue.task_query import get_task



def test():



    task_id=create_task(

        task_type="odds_download",

        source="Pinnacle",

        target="match_odds.csv",

        priority=1

    )


    print(
        "Created Task:"
    )

    print(task_id)



    update_task_status(

        task_id,

        "fetching"

    )


    print(
        get_task(task_id)
    )



    update_task_status(

        task_id,

        "manual_required",

        "Download failed"

    )


    print(
        get_task(task_id)
    )



    update_task_status(

        task_id,

        "completed"

    )


    print(
        get_task(task_id)
    )




if __name__=="__main__":

    test()