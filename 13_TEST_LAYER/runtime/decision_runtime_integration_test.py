from AI_RUNTIME.decision_service_bridge import run_decision


def test_decision_runtime_bridge():


    models={

        "elo":{
            "home":0.5,
            "draw":0.2,
            "away":0.3
        },

        "dixon":{
            "home":0.45,
            "draw":0.25,
            "away":0.3
        },

        "poisson":{
            "home":0.4,
            "draw":0.3,
            "away":0.3
        },

        "xgb":{
            "home":0.42,
            "draw":0.22,
            "away":0.36
        }

    }


    fusion={

        "home_win_probability":0.42,

        "draw_probability":0.2225,

        "away_win_probability":0.3575

    }


    result=run_decision(
        models,
        fusion
    )


    print(result)


    assert "final_decision" in result

    assert "decision_layer" in result
