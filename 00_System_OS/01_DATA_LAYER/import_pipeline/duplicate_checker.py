from core.db_connection import get_connection



def check_duplicate(file_hash):


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT 
    data_id,
    file_name,
    version

    FROM data_registry

    WHERE file_hash=?

    """,
    (
        file_hash,
    )
    )


    result=cursor.fetchone()


    conn.close()


    if result:

        return {

            "duplicate": True,

            "data_id": result[0],

            "file_name": result[1],

            "version": result[2]

        }


    return {

        "duplicate": False

    }