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


    total=home+draw+away


    return {

        "home_win_probability":
            round(home/total,4),

        "draw_probability":
            round(draw/total,4),

        "away_win_probability":
            round(away/total,4),

        "status":
            "FUSION_COMPLETED"

    }
