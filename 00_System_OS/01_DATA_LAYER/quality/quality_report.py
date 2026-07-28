from core.db_connection import get_connection




def get_quality_report(data_id):


    conn=get_connection()

    cursor=conn.cursor()



    cursor.execute(

        """

        SELECT *

        FROM quality_scores

        WHERE data_id=?

        ORDER BY id DESC

        LIMIT 1

        """,

        (

            data_id,

        )

    )


    score=cursor.fetchone()



    cursor.execute(

        """

        SELECT *

        FROM quality_alerts

        WHERE data_id=?

        """,

        (

            data_id,

        )

    )


    alerts=cursor.fetchall()



    conn.close()



    return {


        "score":score,

        "alerts":alerts

    }