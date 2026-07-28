import os
import sys
from datetime import datetime


# 项目根目录加入路径
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from core.db_connection import get_connection





POLICIES = [

    {
        "task_type": "odds_download",

        "max_retry": 5,

        "retry_interval": 60,

        "priority": 1,

        "description":
        "Real time bookmaker odds download"
    },


    {
        "task_type": "odds_monitor",

        "max_retry": 10,

        "retry_interval": 30,

        "priority": 1,

        "description":
        "High frequency odds movement monitoring"
    },


    {
        "task_type": "match_download",

        "max_retry": 5,

        "retry_interval": 300,

        "priority": 2,

        "description":
        "Match basic information download"
    },


    {
        "task_type": "team_download",

        "max_retry": 3,

        "retry_interval": 1800,

        "priority": 3,

        "description":
        "Team data download"
    },


    {
        "task_type": "player_download",

        "max_retry": 3,

        "retry_interval": 1800,

        "priority": 3,

        "description":
        "Player data download"
    },


    {
        "task_type": "news_download",

        "max_retry": 2,

        "retry_interval": 3600,

        "priority": 4,

        "description":
        "News data download"
    }

]





def init_retry_policy():


    print(
        "======================"
    )

    print(
        "Retry Policy Init"
    )

    print(
        "======================"
    )


    conn = get_connection()

    cursor = conn.cursor()



    for policy in POLICIES:


        cursor.execute(

            """

            INSERT OR REPLACE INTO retry_policy

            (

                task_type,

                max_retry,

                retry_interval,

                priority,

                description,

                created_time

            )

            VALUES

            (?,?,?,?,?,?)

            """,

            (

                policy["task_type"],

                policy["max_retry"],

                policy["retry_interval"],

                policy["priority"],

                policy["description"],

                datetime.now().isoformat()

            )

        )


        print(
            "Registered:",
            policy["task_type"]
        )



    conn.commit()

    conn.close()



    print()

    print(
        "Retry Policy Ready"
    )





if __name__ == "__main__":

    init_retry_policy()