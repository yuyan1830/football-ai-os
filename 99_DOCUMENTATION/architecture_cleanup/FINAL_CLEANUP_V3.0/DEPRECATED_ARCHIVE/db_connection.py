
import sqlite3
import sys
import os



BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)



if BASE_DIR not in sys.path:

    sys.path.insert(
        0,
        BASE_DIR
    )



from config.database_config import SQLITE_DB



# Logger integration

try:

    from core.logger import logger

except:

    logger = None



# Exception integration

try:

    from core.exception import DatabaseException

except:

    class DatabaseException(Exception):
        pass





def get_connection():


    try:


        conn = sqlite3.connect(

            SQLITE_DB,

            timeout=30

        )


        return conn



    except sqlite3.Error as e:


        if logger:

            logger.error(
                str(e)
            )


        raise DatabaseException(
            str(e)
        )






def test_connection():


    conn=None


    try:


        conn=get_connection()


        cursor=conn.cursor()


        cursor.execute(

            "SELECT sqlite_version();"

        )


        result=cursor.fetchone()


        return result



    except Exception as e:


        if logger:

            logger.error(
                str(e)
            )


        raise



    finally:


        if conn:

            conn.close()






def health_check():


    result=test_connection()


    return {


        "service":
            "Database Service",


        "status":
            "OK",


        "sqlite_version":
            result[0]

    }





if __name__=="__main__":


    print(
        health_check()
    )


