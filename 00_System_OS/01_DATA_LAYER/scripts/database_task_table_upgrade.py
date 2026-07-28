import os
import sys
import sqlite3
from datetime import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from config.database_config import SQLITE_DB





def upgrade_data_tasks():


    print(
        "======================"
    )

    print(
        "Data Tasks Upgrade"
    )

    print(
        "======================"
    )


    conn = sqlite3.connect(
        SQLITE_DB
    )

    cursor = conn.cursor()



    cursor.execute(
        """
        PRAGMA table_info(data_tasks)
        """
    )


    columns = [

        row[1]

        for row in cursor.fetchall()

    ]



    print(
        "Current Columns:"
    )

    print(columns)



    if "retry_count" not in columns:


        cursor.execute(

            """

            ALTER TABLE data_tasks

            ADD COLUMN retry_count INTEGER DEFAULT 0

            """

        )


        print(
            "Added retry_count"
        )



    if "updated_time" not in columns:


        cursor.execute(

            """

            ALTER TABLE data_tasks

            ADD COLUMN updated_time TEXT

            """

        )


        print(
            "Added updated_time"
        )



    conn.commit()

    conn.close()



    print()

    print(
        "Data Tasks Upgrade Completed"
    )





if __name__ == "__main__":

    upgrade_data_tasks()