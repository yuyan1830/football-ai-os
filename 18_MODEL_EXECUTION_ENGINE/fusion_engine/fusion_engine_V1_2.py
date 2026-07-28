# -*- coding:utf-8 -*-


def fusion_predict(
    elo,
    dixon,
    poisson,
    xgb
):


    weights={

        "elo":0.25,

        "dixon":0.25,

        "poisson":0.25,

        "xgb":0.25

    }


    home=(

        elo["home"]*weights["elo"]

        +

        dixon["home"]*weights["dixon"]

        +

        poisson["home"]*weights["poisson"]

        +

        xgb["home"]*weights["xgb"]

    )


    draw=(

        elo["draw"]*weights["elo"]

        +

        dixon["draw"]*weights["dixon"]

        +

        poisson["draw"]*weights["poisson"]

        +

        xgb["draw"]*weights["xgb"]

    )


    away=(

        elo["away"]*weights["elo"]

        +

        dixon["away"]*weights["dixon"]

        +

        poisson["away"]*weights["poisson"]

        +

        xgb["away"]*weights["xgb"]

    )


    return {


        "home_win_probability":
        round(home,4),


        "draw_probability":
        round(draw,4),


        "away_win_probability":
        round(away,4),


        "status":
        "FUSION_V1.2_COMPLETED"

    }



if __name__=="__main__":


    result=fusion_predict(

        {
        "home":0.4,
        "draw":0.3,
        "away":0.3
        },

        {
        "home":0.45,
        "draw":0.25,
        "away":0.30
        },

        {
        "home":0.5,
        "draw":0.25,
        "away":0.25
        },

        {
        "home":0.35,
        "draw":0.35,
        "away":0.30
        }

    )


    print(result)

