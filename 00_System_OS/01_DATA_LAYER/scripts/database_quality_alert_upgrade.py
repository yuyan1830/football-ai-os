import os
import sys
import sqlite3


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from config.database_config import SQLITE_DB




def upgrade():


    conn = sqlite3.connect(
        SQLITE_DB
    )

    cursor = conn.cursor()



    cursor.execute(
        "PRAGMA table_info(quality_alerts)"
    )


    columns = [

        r[1]

        for r in cursor.fetchall()

    ]



    if "alert_key" not in columns:

        cursor.execute(

            """

            ALTER TABLE quality_alerts

            ADD COLUMN alert_key TEXT

            """

        )


        print(
            "Added alert_key"
        )



    if "details" not in columns:

        cursor.execute(

            """

            ALTER TABLE quality_alerts

            ADD COLUMN details TEXT

            """

        )


        print(
            "Added details"
        )



    if "count" not in columns:

        cursor.execute(

            """

            ALTER TABLE quality_alerts

            ADD COLUMN count INTEGER DEFAULT 1

            """

        )


        print(
            "Added count"
        )



    conn.commit()

    conn.close()



    print(
        "Quality Alert Upgrade Complete"
    )




if __name__=="__main__":

    upgrade()