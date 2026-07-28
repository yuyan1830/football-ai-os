import os
import sys
import hashlib


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)



from core.db_connection import get_connection





def check_required_fields(data):


    alerts=[]


    for key,value in data.items():


        if value is None or value=="":


            alerts.append(

                {

                "rule":

                "missing_required_field",

                "message":

                f"{key} is empty"

                }

            )


    return alerts





def calculate_hash(content):


    return hashlib.sha256(

        content.encode("utf-8")

    ).hexdigest()





def check_duplicate_hash(file_hash):


    conn=get_connection()

    cursor=conn.cursor()



    cursor.execute(

        """

        SELECT data_id

        FROM data_registry

        WHERE hash=?

        """,

        (

            file_hash,

        )

    )


    result=cursor.fetchone()


    conn.close()



    if result:


        return {


            "duplicate":True,

            "data_id":result[0]

        }


    return {


        "duplicate":False

    }







def run_basic_check(data):


    result=[]


    result.extend(

        check_required_fields(data)

    )


    return result