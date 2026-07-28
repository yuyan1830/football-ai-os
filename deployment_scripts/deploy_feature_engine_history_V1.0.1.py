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
"FEATURE_ENGINE_HISTORY_V1.0.1_REPORT.json"
)



def upgrade_schema():

    conn=sqlite3.connect(FEATURE_DB)
    cur=conn.cursor()


    schemas={

    "elo_history":
    ["match_id INTEGER",
     "team TEXT",
     "elo REAL"],


    "dixon_coles_history":
    ["match_id INTEGER",
     "team TEXT",
     "attack REAL",
     "defense REAL"],


    "poisson_history":
    ["match_id INTEGER",
     "team TEXT",
     "lambda REAL"],


    "team_form_history":
    ["match_id INTEGER",
     "team TEXT",
     "form REAL"],


    "home_away_history":
    ["match_id INTEGER",
     "team TEXT",
     "home_rating REAL",
     "away_rating REAL"],


    "fatigue_rating":
    ["match_id INTEGER",
     "team TEXT",
     "fatigue REAL"],


    "feature_vector":
    ["match_id INTEGER",
     "feature TEXT"]

    }



    for table,fields in schemas.items():

        cur.execute(
        f"PRAGMA table_info({table})"
        )

        exist=[
            x[1]
            for x in cur.fetchall()
        ]


        for field in fields:

            name=field.split()[0]

            if name not in exist:

                cur.execute(
                f"""
                ALTER TABLE {table}
                ADD COLUMN {field}
                """
                )


    conn.commit()
    conn.close()



def generate():

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


    for r in rows:

        mid=r[0]


        dc.execute(
        """
        INSERT INTO elo_history
        (match_id,team,elo)
        VALUES(?,?,?)
        """,
        (mid,"SYSTEM",1500)
        )


        dc.execute(
        """
        INSERT INTO dixon_coles_history
        (match_id,team,attack,defense)
        VALUES(?,?,?,?)
        """,
        (mid,"SYSTEM",1,1)
        )


        dc.execute(
        """
        INSERT INTO poisson_history
        (match_id,team,lambda)
        VALUES(?,?,?)
        """,
        (mid,"SYSTEM",1)
        )


        dc.execute(
        """
        INSERT INTO team_form_history
        (match_id,team,form)
        VALUES(?,?,?)
        """,
        (mid,"SYSTEM",0)
        )


        dc.execute(
        """
        INSERT INTO home_away_history
        (match_id,team,home_rating,away_rating)
        VALUES(?,?,?,?)
        """,
        (mid,"SYSTEM",0,0)
        )


        dc.execute(
        """
        INSERT INTO fatigue_rating
        (match_id,team,fatigue)
        VALUES(?,?,?)
        """,
        (mid,"SYSTEM",0)
        )


        dc.execute(
        """
        INSERT INTO feature_vector
        (match_id,feature)
        VALUES(?,?)
        """,
        (mid,"INITIAL")
        )


    dst.commit()

    src.close()
    dst.close()


def check():

    conn=sqlite3.connect(FEATURE_DB)

    cur=conn.cursor()

    result={}


    for t in [
    "elo_history",
    "dixon_coles_history",
    "poisson_history",
    "team_form_history",
    "home_away_history",
    "fatigue_rating",
    "feature_vector"
    ]:

        cur.execute(
        f"SELECT COUNT(*) FROM {t}"
        )

        result[t]=cur.fetchone()[0]


    conn.close()

    return result



def main():

    print("="*60)
    print("Feature Engine History V1.0.1")
    print("="*60)


    upgrade_schema()

    generate()

    report={

    "version":
    "FEATURE_ENGINE_HISTORY_V1.0.1",

    "time":
    datetime.now().isoformat(),

    "result":
    check()

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


    print(json.dumps(
    report,
    indent=4,
    ensure_ascii=False
    ))


    print("FEATURE ENGINE COMPLETE")



if __name__=="__main__":
    main()

