import sys
import os

# 添加项目根目录
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import sqlite3
from api.statsapi_client import StatsAPI
from config import DATABASE_PATH


def save_competitions(items):

    conn = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = conn.cursor()


    for item in items:

        cursor.execute(
            """
            INSERT OR REPLACE INTO competitions
            (
            id,
            name,
            country
            )
            VALUES
            (?,?,?)
            """,
            (
                item.get("id"),
                item.get("name"),
                item.get("country")
            )
        )


    conn.commit()
    conn.close()



def load_competitions():

    print(
        "开始获取联赛数据..."
    )


    api = StatsAPI()


    data = api.get(
        "/api/football/competitions"
    )


    print(data[:500])


    # 根据API返回结构调整
    if isinstance(data,dict):

        items = data.get(
            "data",
            []
        )

    else:

        items=[]


    if items:

        save_competitions(items)

        print(
            "联赛数据保存完成:",
            len(items)
        )

    else:

        print(
            "没有发现联赛数据"
        )



if __name__=="__main__":

    load_competitions()