import datetime
import uuid


from core.db_connection import get_connection



def create_data_id():

    return (

        "DATA_"

        +

        datetime.datetime.now()
        .strftime("%Y%m%d")

        +

        "_"

        +

        uuid.uuid4()
        .hex[:8]

    )



def register_data(

    file_name,

    file_hash,

    data_type,

    source,

    version="v001"

):


    data_id = create_data_id()


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

    """

    INSERT INTO data_registry

    (

    data_id,

    file_name,

    file_hash,

    data_type,

    source,

    version,

    status,

    created_time

    )

    VALUES

    (?,?,?,?,?,?,?,?)

    """,

    (

    data_id,

    file_name,

    file_hash,

    data_type,

    source,

    version,

    "verified",

    datetime.datetime.now().isoformat()

    )

    )


    conn.commit()

    conn.close()


    return data_id



if __name__=="__main__":

    print(
        "Registry Manager V1.0 Ready"
    )