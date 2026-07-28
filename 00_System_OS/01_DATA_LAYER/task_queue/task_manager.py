import os
import sys
import uuid
from datetime import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)



from core.db_connection import get_connection


from task_queue.task_history import add_history





def generate_task_id():

    return (
        "TASK_"
        +
        uuid.uuid4()
        .hex[:8]
    )







def create_task(

        task_type,

        source,

        target,

        priority=5

):


    task_id = generate_task_id()


    now = datetime.now().isoformat()



    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        INSERT INTO data_tasks

        (

            task_id,

            task_type,

            source,

            target,

            status,

            priority,

            error_message,

            retry_count,

            updated_time,

            created_time


        )


        VALUES

        (?,?,?,?,?,?,?,?,?,?)

        """,

        (

            task_id,

            task_type,

            source,

            target,

            "pending",

            priority,

            None,

            0,

            now,

            now

        )

    )



    conn.commit()

    conn.close()



    # 创建历史记录

    add_history(

        task_id,

        None,

        "pending",

        "Task Created"

    )



    return task_id







def get_task(task_id):


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

        priority,

        error_message,

        retry_count,

        updated_time


        FROM data_tasks


        WHERE task_id=?


        """,

        (

            task_id,

        )

    )


    result = cursor.fetchone()


    conn.close()



    if not result:

        return None



    return {


        "task_id":result[0],

        "task_type":result[1],

        "source":result[2],

        "target":result[3],

        "status":result[4],

        "priority":result[5],

        "error_message":result[6],

        "retry_count":result[7],

        "updated_time":result[8]

    }








def update_task_error(

        task_id,

        error_message

):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        UPDATE data_tasks


        SET

        error_message=?,

        updated_time=?


        WHERE task_id=?


        """,

        (

            error_message,

            datetime.now().isoformat(),

            task_id

        )

    )


    conn.commit()

    conn.close()



    return True





if __name__ == "__main__":


    print(
        "Task Manager Reliability Ready"
    )