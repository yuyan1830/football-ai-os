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





def add_retry_record(

        task_id,

        attempt,

        result,

        error_message=None,

        duration=0

):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        INSERT INTO retry_records

        (

            task_id,

            attempt,

            result,

            error_message,

            duration,

            created_time

        )

        VALUES

        (?,?,?,?,?,?)

        """,

        (

            task_id,

            attempt,

            result,

            error_message,

            duration,

            datetime.now().isoformat()

        )

    )



    conn.commit()

    conn.close()



    return True





def get_retry_records(task_id):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT

        task_id,

        attempt,

        result,

        error_message,

        duration,

        created_time


        FROM retry_records


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





def get_failed_retry_count(task_id):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT COUNT(*)

        FROM retry_records


        WHERE task_id=?

        AND result='failed'


        """,

        (

            task_id,

        )

    )


    result = cursor.fetchone()


    conn.close()



    return result[0]





if __name__ == "__main__":


    print(
        "Retry Logger Module Ready"
    )