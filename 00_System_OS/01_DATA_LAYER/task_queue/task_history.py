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





def add_history(
        task_id,
        old_status,
        new_status,
        message=None
):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        INSERT INTO task_history

        (

            task_id,

            old_status,

            new_status,

            message,

            created_time

        )

        VALUES

        (?,?,?,?,?)

        """,

        (

            task_id,

            old_status,

            new_status,

            message,

            datetime.now().isoformat()

        )

    )



    conn.commit()

    conn.close()



    return True





def get_history(task_id):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT

        task_id,

        old_status,

        new_status,

        message,

        created_time


        FROM task_history


        WHERE task_id=?


        ORDER BY id ASC


        """,

        (

            task_id,

        )

    )


    result = cursor.fetchall()


    conn.close()


    return result





def get_all_history(limit=50):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT

        task_id,

        old_status,

        new_status,

        message,

        created_time


        FROM task_history


        ORDER BY id DESC


        LIMIT ?

        """,

        (

            limit,

        )

    )


    result = cursor.fetchall()


    conn.close()


    return result





if __name__ == "__main__":


    print(
        "Task History Module Ready"
    )