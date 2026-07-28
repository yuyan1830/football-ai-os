import datetime


from core.db_connection import get_connection



def record_import(

    data_id,

    import_type,

    operator,

    result

):


    conn=get_connection()

    cursor=conn.cursor()



    cursor.execute(

    """

    INSERT INTO import_history

    (

    data_id,

    import_type,

    operator,

    import_time,

    result

    )

    VALUES

    (?,?,?,?,?)

    """,

    (

    data_id,

    import_type,

    operator,

    datetime.datetime.now().isoformat(),

    result

    )

    )



    conn.commit()

    conn.close()