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


from task_queue.retry_engine import retry_task





def get_pending_tasks(limit=10):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT

        task_id,

        task_type,

        source,

        target,

        status,

        priority


        FROM data_tasks


        WHERE status='pending'


        ORDER BY priority ASC, id ASC


        LIMIT ?


        """,

        (

            limit,

        )

    )


    result = cursor.fetchall()


    conn.close()


    return result





def start_task(task_id):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT status

        FROM data_tasks

        WHERE task_id=?

        """,

        (

            task_id,

        )

    )


    result = cursor.fetchone()



    if not result:


        conn.close()

        return False



    old_status=result[0]



    cursor.execute(

        """

        UPDATE data_tasks


        SET

        status='fetching',

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



    add_history(

        task_id,

        old_status,

        "fetching",

        "Scheduler started task"

    )


    return True





def finish_task(

        task_id,

        success=True,

        error=None

):


    conn=get_connection()

    cursor=conn.cursor()



    cursor.execute(

        """

        SELECT status

        FROM data_tasks

        WHERE task_id=?

        """,

        (

            task_id,

        )

    )


    result=cursor.fetchone()


    if not result:

        conn.close()

        return False



    old_status=result[0]



    if success:


        new_status="completed"


    else:


        new_status="failed"




    cursor.execute(

        """

        UPDATE data_tasks


        SET

        status=?,

        error_message=?,

        updated_time=?


        WHERE task_id=?


        """,

        (

            new_status,

            error,

            datetime.now().isoformat(),

            task_id

        )

    )



    conn.commit()

    conn.close()



    add_history(

        task_id,

        old_status,

        new_status,

        error

    )


    return True






def process_queue():


    tasks=get_pending_tasks()



    for task in tasks:


        task_id=task[0]


        print(

            "Processing:",

            task_id

        )



        start_task(task_id)



        # 这里以后接真实采集器
        # 当前模拟成功/失败


        finish_task(

            task_id,

            success=True

        )



    return len(tasks)





if __name__ == "__main__":


    print(

        "Scheduler Reliability V1.3.4 Ready"

    )