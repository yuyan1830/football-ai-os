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
        """
        PRAGMA table_info(quality_alerts)
        """
    )


    columns = [
        r[1]
        for r in cursor.fetchall()
    ]


    if "updated_time" not in columns:

        cursor.execute(
            """
            ALTER TABLE quality_alerts
            ADD COLUMN updated_time TEXT
            """
        )

        print(
            "Added updated_time"
        )


    conn.commit()


    #
    # 创建唯一索引
    #

    cursor.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS
        idx_quality_alert_unique

        ON quality_alerts
        (
            data_id,
            rule_name,
            alert_key
        )
        """
    )


    conn.commit()


    conn.close()


    print(
        "Alert Final Upgrade Completed"
    )



if __name__=="__main__":

    upgrade()