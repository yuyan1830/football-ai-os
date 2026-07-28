import os
import sys
from datetime import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from core.db_connection import get_connection


from task_queue.task_history import add_history


from task_queue.retry_logger import add_retry_record





def get_retry_policy(task_type):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT

        max_retry,

        retry_interval,

        priority


        FROM retry_policy


        WHERE task_type=?


        """,

        (

            task_type,

        )

    )


    result = cursor.fetchone()


    conn.close()



    if not result:


        return {


            "max_retry":3,

            "retry_interval":300,

            "priority":5

        }



    return {


        "max_retry":result[0],

        "retry_interval":result[1],

        "priority":result[2]

    }





def get_task_info(task_id):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT

        task_type,

        status,

        retry_count


        FROM data_tasks


        WHERE task_id=?


        """,

        (

            task_id,

        )

    )


    result = cursor.fetchone()


    conn.close()



    return result





def update_task_status(

        task_id,

        status,

        message=None

):


    conn = get_connection()

    cursor = conn.cursor()



    old = get_task_info(task_id)



    old_status = None


    if old:

        old_status = old[1]



    cursor.execute(

        """

        UPDATE data_tasks


        SET

        status=?,

        updated_time=?


        WHERE task_id=?


        """,

        (

            status,

            datetime.now().isoformat(),

            task_id

        )

    )



    conn.commit()

    conn.close()



    add_history(

        task_id,

        old_status,

        status,

        message

    )





def retry_task(task_id):


    task = get_task_info(task_id)



    if not task:


        return {


            "status":"error",

            "message":"Task not found"

        }



    task_type = task[0]

    current_retry = task[2]



    policy = get_retry_policy(

        task_type

    )



    max_retry = policy["max_retry"]





    if current_retry >= max_retry:


        update_task_status(

            task_id,

            "manual_required",

            "Maximum retry reached"

        )


        return {


            "status":

            "manual_required",


            "retry_count":

            current_retry

        }





    update_task_status(

        task_id,

        "retrying",

        "Preparing retry"

    )



    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        UPDATE data_tasks


        SET

        retry_count=retry_count+1,

        status='pending',

        updated_time=?


        WHERE task_id=?


        """,

        (

            datetime.now().isoformat(),

            task_id

        )

    )



    conn.commit()

    conn.close()



    add_retry_record(

        task_id,

        current_retry + 1,

        "retry_pending",

        None,

        0

    )



    add_history(

        task_id,

        "retrying",

        "pending",

        "Retry queued"

    )



    return {


        "status":

        "retry_pending",


        "retry_count":

        current_retry + 1,


        "next_interval":

        policy["retry_interval"]

    }





if __name__ == "__main__":


    print(

        "Retry Engine V1.3.4 Ready"

    )