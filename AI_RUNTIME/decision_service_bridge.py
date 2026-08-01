# -*- coding: utf-8 -*-

"""
Football AI OS Ω+

Decision Service Bridge V3.2


职责:

AI_RUNTIME



08_DECISION_LAYER

连接桥
"""


import os
import sys



PROJECT_ROOT = os.path.dirname(
    os.path.dirname(__file__)
)


DECISION_LAYER_PATH = os.path.join(
    PROJECT_ROOT,
    "08_DECISION_LAYER"
)


if DECISION_LAYER_PATH not in sys.path:

    sys.path.insert(
        0,
        DECISION_LAYER_PATH
    )



from service.decision_service_v32 import DecisionServiceV32




def run_decision(models, fusion):


    try:


        service = DecisionServiceV32()


        result = service.run(

            {

                "models": models,

                "fusion": fusion

            }

        )


        return {


            "decision_layer":

                result,


            "status":

                "DECISION_SERVICE_V32_SUCCESS",


            "fallback":

                False

        }



    except Exception as e:


        return {


            "decision_layer":

                {

                    "error":

                        str(e),


                    "status":

                        "DECISION_SERVICE_V32_FAILED"

                },


            "status":

                "DECISION_SERVICE_FAILED",


            "fallback":

                True

        }

