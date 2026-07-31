
# -*- coding: utf-8 -*-


import sys


sys.path.insert(
    0,
    r"E:\football_v\08_DECISION_LAYER"
)


from service.decision_service_v32 import DecisionServiceV32


from .final_decision import final_decision



def run_decision(models,fusion):


    try:

        service=DecisionServiceV32()


        result=service.run(

            {

                "models":models,

                "fusion":fusion

            }

        )


        return {

            "final_decision":
            result.get(
                "decision",
                {}
            ),

            "decision_layer":
            result,

            "fallback":False

        }


    except Exception as e:


        return {

            "final_decision":
            final_decision(
                fusion
            ),

            "decision_layer":{},

            "fallback":True,

            "error":str(e)

        }
