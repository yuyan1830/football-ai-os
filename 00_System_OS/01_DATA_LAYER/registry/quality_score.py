from core.db_connection import get_connection



def save_quality(

    data_id,

    completeness,

    accuracy

):


    status="good"


    if completeness < 0.8:

        status="warning"



    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(

    """

    INSERT INTO data_quality

    VALUES

    (NULL,?,?,?,?)

    """,

    (

    data_id,

    completeness,

    accuracy,

    status

    )

    )


    conn.commit()

    conn.close()