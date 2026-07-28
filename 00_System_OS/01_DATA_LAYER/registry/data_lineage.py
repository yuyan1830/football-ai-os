import datetime


from core.db_connection import get_connection




def add_lineage(

    data_id,

    parent,

    process

):


    conn=get_connection()

    cursor=conn.cursor()



    cursor.execute(

    """

    INSERT INTO data_lineage

    (

    data_id,

    parent_data,

    process,

    created_time

    )

    VALUES

    (?,?,?,?)

    """,

    (

    data_id,

    parent,

    process,

    datetime.datetime.now().isoformat()

    )

    )


    conn.commit()

    conn.close()