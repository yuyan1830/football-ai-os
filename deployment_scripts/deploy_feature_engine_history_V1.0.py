import sqlite3
import os
import json
from datetime import datetime


BASE=r"E:\football_v"

MATCH_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"01_DATA_LAYER",
"database",
"match_data.db"
)

FEATURE_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"02_FEATURE_LAYER",
"database",
"feature_store.db"
)

REPORT=os.path.join(
BASE,
"99_Documentation",
"reports",
"FEATURE_ENGINE_HISTORY_V1.0_REPORT.json"
)


def create_tables():

    conn=sqlite3.connect(FEATURE_DB)
    cur=conn.cursor()

    tables={

    "elo_history":
    """
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    team TEXT,
    elo REAL
    """,

    "dixon_coles_history":
    """
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    team TEXT,
    attack REAL,
    defense REAL
    """,

    "poisson_history":
    """
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    team TEXT,
    lambda REAL
    """,

    "team_form_history":
    """
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    team TEXT,
    form REAL
    """,

    "home_away_history":
    """
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    team TEXT,
    home_rating REAL,
    away_rating REAL
    """,

    "fatigue_rating":
    """
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    team TEXT,
    fatigue REAL
    """,

    "feature_vector":
    """
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    feature TEXT
    """

    }


    for name,schema in tables.items():

        cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {name}
        ({schema})
        """
        )


    conn.commit()
    conn.close()



def generate_features():

    src=sqlite3.connect(MATCH_DB)

    dst=sqlite3.connect(FEATURE_DB)


    sc=src.cursor()
    dc=dst.cursor()


    sc.execute(
    """
    SELECT id
    FROM matches_clean
    ORDER BY id
    """
    )


    rows=sc.fetchall()


    count=0


    for r in rows:

        mid=r[0]


        dc.execute(
        """
        INSERT INTO elo_history
        (match_id,team,elo)
        VALUES(?,?,?)
        """,
        (mid,"UNKNOWN",1500)
        )


        dc.execute(
        """
        INSERT INTO dixon_coles_history
        (match_id,team,attack,defense)
        VALUES(?,?,?,?)
        """,
        (mid,"UNKNOWN",1,1)
        )


        dc.execute(
        """
        INSERT INTO poisson_history
        (match_id,team,lambda)
        VALUES(?,?,?)
        """,
        (mid,"UNKNOWN",1)
        )


        dc.execute(
        """
        INSERT INTO team_form_history
        (match_id,team,form)
        VALUES(?,?,?)
        """,
        (mid,"UNKNOWN",0)
        )


        dc.execute(
        """
        INSERT INTO home_away_history
        (match_id,team,home_rating,away_rating)
        VALUES(?,?,?,?)
        """,
        (mid,"UNKNOWN",0,0)
        )


        dc.execute(
        """
        INSERT INTO fatigue_rating
        (match_id,team,fatigue)
        VALUES(?,?,?)
        """,
        (mid,"UNKNOWN",0)
        )


        dc.execute(
        """
        INSERT INTO feature_vector
        (match_id,feature)
        VALUES(?,?)
        """,
        (mid,"INITIAL")


        )

        count+=1


        if count%5000==0:
            dst.commit()


    dst.commit()


    src.close()
    dst.close()


    return count



def check():

    conn=sqlite3.connect(FEATURE_DB)

    cur=conn.cursor()


    tables=[
    "elo_history",
    "dixon_coles_history",
    "poisson_history",
    "team_form_history",
    "home_away_history",
    "fatigue_rating",
    "feature_vector"
    ]


    result={}


    for t in tables:

        cur.execute(
        f"SELECT COUNT(*) FROM {t}"
        )

        result[t]=cur.fetchone()[0]


    conn.close()

    return result



def main():

    print("="*60)
    print("Football AI OS Feature Engine History V1.0")
    print("="*60)


    create_tables()

    total=generate_features()

    result=check()


    report={

    "version":
    "FEATURE_ENGINE_HISTORY_V1.0",

    "time":
    datetime.now().isoformat(),

    "source":

    MATCH_DB,

    "matches_processed":
    total,

    "feature_tables":
    result

    }


    os.makedirs(
    os.path.dirname(REPORT),
    exist_ok=True
    )


    with open(
    REPORT,
    "w",
    encoding="utf8"
    ) as f:

        json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
        )


    print(
    json.dumps(
    report,
    indent=4,
    ensure_ascii=False
    )
    )


    print("FEATURE ENGINE COMPLETE")


if __name__=="__main__":
    main()

