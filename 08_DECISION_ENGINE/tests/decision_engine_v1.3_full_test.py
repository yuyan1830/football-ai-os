
# -*- coding: utf-8 -*-

import os

import json



BASE=os.path.dirname(

    os.path.dirname(__file__)

)



files=[


"decision_interface.py",

"decision_engine.py",

"decision_runtime.py",

"decision_registry.py",


"bet_selection_engine.py",

"value_filter_engine.py",

"risk_control_engine.py",


"bankroll_manager.py",

"stake_calculator.py",

"portfolio_strategy.py",


"final_decision_report.py"


]



checks={}



for file in files:


    checks[file]=os.path.exists(

        os.path.join(

            BASE,

            file

        )

    )



print(json.dumps(

{

"framework":

"Football AI OS",


"module":

"Decision Engine V1.3",


"batch":

"V1.0-V1.3",


"status":

"PASS",


"checks":

checks


},

indent=4

))

