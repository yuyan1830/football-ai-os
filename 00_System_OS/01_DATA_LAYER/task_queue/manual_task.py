import datetime


from core.db_connection import get_connection



def require_manual(

    task_id,

    reason

):


    conn=get_connection()

    cursor=conn.cursor()



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

    "manual_required",

    reason,

    datetime.datetime.now().isoformat(),

    task_id

    )

    )


    conn.commit()

    conn.close()