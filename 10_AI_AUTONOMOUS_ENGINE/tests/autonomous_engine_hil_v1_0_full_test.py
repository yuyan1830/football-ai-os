# -*- coding: utf-8 -*-

import os
import json
import sys


BASE_PATH = r"E:\football_v\10_AI_AUTONOMOUS_ENGINE"


def check_file(path):

    return os.path.exists(
        os.path.join(
            BASE_PATH,
            path
        )
    )


def run_test():


    result={

        "framework":
        "Football AI OS",


        "module":
        "AI Autonomous Evolution Engine HIL V1.0",


        "status":
        "PASS",


        "checks":{

            "error_rate_calculator.py":
            check_file(
                "error_rate_calculator.py"
            ),


            "time_window_analyzer.py":
            check_file(
                "time_window_analyzer.py"
            ),


            "error_trend_detector.py":
            check_file(
                "error_trend_detector.py"
            ),


            "error_analysis_engine.py":
            check_file(
                "error_analysis_engine.py"
            ),


            "config/autonomous_config.json":
            check_file(
                "config/autonomous_config.json"
            )

        }

    }



    for value in result["checks"].values():

        if value is False:

            result["status"]="FAIL"



    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )



if __name__=="__main__":

    run_test()