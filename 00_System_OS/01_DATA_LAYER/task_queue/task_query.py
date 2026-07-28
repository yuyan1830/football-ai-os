from core.db_connection import get_connection



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
        error_message

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

        "task_id": result[0],

        "task_type": result[1],

        "source": result[2],

        "target": result[3],

        "status": result[4],

        "priority": result[5],

        "error_message": result[6]

    }