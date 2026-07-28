import sqlite3
import json
import os
import datetime


ROOT=r"E:\FOOTBALL_V"

DB_PATH=os.path.join(
    ROOT,
    "data",
    "football.db"
)


MODEL_DIR=os.path.join(
    ROOT,
    "50_MODEL_REGISTRY",
    "models"
)


os.makedirs(
    MODEL_DIR,
    exist_ok=True
)



K=20

HOME_ADVANTAGE=60



teams={}



def get_rating(team):

    if team not in teams:

        teams[team]=1500

    return teams[team]



if os.path.exists(DB_PATH):

    conn=sqlite3.connect(DB_PATH)

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT 
    home_team,
    away_team,
    home_score,
    away_score
    FROM matches_clean
    ORDER BY date ASC
    """
    )


    matches=cursor.fetchall()


    for home,away,hg,ag in matches:


        home_rating=get_rating(home)+HOME_ADVANTAGE

        away_rating=get_rating(away)


        expected_home=1/(1+10**((away_rating-home_rating)/400))


        if hg>ag:

            result=1

        elif hg==ag:

            result=0.5

        else:

            result=0



        teams[home]+=K*(result-expected_home)

        teams[away]+=K*((1-result)-(1-expected_home))



    conn.close()



model={


"version":
"ELO_MODEL_V4.0",


"time":
str(datetime.datetime.now()),


"teams":
teams,


"team_count":
len(teams),


"status":
"TRAINED"

}



out=os.path.join(

MODEL_DIR,

"elo_model_V4.0.json"

)



with open(

out,

"w",

encoding="utf-8"

) as f:

    json.dump(

        model,

        f,

        indent=4,

        ensure_ascii=False

    )



print("="*60)

print("ELO TRAINING V4.0 COMPLETE")

print("Teams:",len(teams))

print(out)

print("="*60)

