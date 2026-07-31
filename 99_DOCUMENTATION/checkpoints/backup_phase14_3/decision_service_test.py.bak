# -*- coding: utf-8 -*-

import sys

sys.path.insert(
    0,
    r"E:\football_v\08_DECISION_LAYER"
)


from service.decision_service_V3.2 import DecisionServiceV32


service = DecisionServiceV32()


result = service.run(

    {

        "fusion":{

            "home_win_probability":0.42,

            "draw_probability":0.2225,

            "away_win_probability":0.3575

        },


        "models":{


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

    }

)


print(result)
