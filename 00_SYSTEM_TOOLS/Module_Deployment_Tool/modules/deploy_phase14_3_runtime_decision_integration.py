# -*- coding: utf-8 -*-

"""
Football AI OS Ω+

Phase14.3 Runtime Decision Integration Deployment

"""

import os
import shutil
from datetime import datetime


ROOT = r"E:\football_v"


BACKUP_DIR = os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "checkpoints",
    "backup_phase14_3"
)


def backup(path):

    src = os.path.join(ROOT, path)

    if os.path.exists(src):

        os.makedirs(
            BACKUP_DIR,
            exist_ok=True
        )

        shutil.copy2(
            src,
            os.path.join(
                BACKUP_DIR,
                os.path.basename(src) + ".bak"
            )
        )

        print("Backup:", path)



def write(path, content):

    full = os.path.join(ROOT, path)

    os.makedirs(
        os.path.dirname(full),
        exist_ok=True
    )

    with open(
        full,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)

    print("Create:", path)



def replace(path, content):

    full = os.path.join(ROOT, path)

    with open(
        full,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)

    print("Update:", path)



print("="*60)
print("Phase14.3 Runtime Decision Integration")
print("="*60)



# ==========================
# Backup
# ==========================


for f in [

    r"AI_RUNTIME\prediction_executor.py",

    r"AI_RUNTIME\ai_report.py",

    r"08_DECISION_LAYER\test\decision_service_test.py"

]:

    backup(f)



# ==========================
# decision_engine_v32
# ==========================


write(
r"08_DECISION_LAYER\engine\decision_engine_v32.py",

r'''
# -*- coding: utf-8 -*-


class DecisionEngineV32:


    def evaluate(self,fusion):


        probabilities={

            "主胜":
            fusion.get("home_win_probability",0),

            "平局":
            fusion.get("draw_probability",0),

            "客胜":
            fusion.get("away_win_probability",0)

        }


        decision=max(
            probabilities,
            key=probabilities.get
        )


        return {

            "decision":decision,

            "confidence":
            round(
                probabilities[decision],
                4
            ),

            "probabilities":
            probabilities,

            "status":
            "DECISION_V32_READY"

        }
'''
)



# ==========================
# decision_service_v32
# ==========================


write(
r"08_DECISION_LAYER\service\decision_service_v32.py",

r'''
# -*- coding: utf-8 -*-


from engine.decision_engine_v32 import DecisionEngineV32

from engine.consensus_engine import ConsensusEngine

from engine.risk_engine import RiskEngine



class DecisionServiceV32:


    def __init__(self):

        self.decision_engine = DecisionEngineV32()

        self.consensus_engine = ConsensusEngine()

        self.risk_engine = RiskEngine()



    def run(self,data):


        fusion=data.get(
            "fusion",
            {}
        )


        models=data.get(
            "models",
            {}
        )


        decision=self.decision_engine.evaluate(
            fusion
        )


        consensus=self.consensus_engine.analyze(
            models
        )


        risk=self.risk_engine.analyze(
            decision
        )


        return {

            "decision":decision,

            "consensus":consensus,

            "risk":risk,

            "status":
            "DECISION_SERVICE_V32_READY"

        }
'''
)



# ==========================
# Bridge
# ==========================


write(
r"AI_RUNTIME\decision_service_bridge.py",

r'''
# -*- coding: utf-8 -*-


import sys


sys.path.insert(
    0,
    r"E:\football_v\08_DECISION_LAYER"
)


from service.decision_service_v32 import DecisionServiceV32





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


    
'''
)



# ==========================
# Runtime Test
# ==========================


write(
r"13_TEST_LAYER\runtime\decision_runtime_integration_test.py",

r'''
from AI_RUNTIME.decision_service_bridge import run_decision


models={

"elo":{"home":0.5,"draw":0.2,"away":0.3},

"dixon":{"home":0.45,"draw":0.25,"away":0.3},

"poisson":{"home":0.4,"draw":0.3,"away":0.3},

"xgb":{"home":0.42,"draw":0.22,"away":0.36}

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
'''
)



print("="*60)
print("Phase14.3 Deployment Base Created")
print("="*60)


# ==========================
# Update Runtime Prediction Executor
# ==========================

replace(
r"AI_RUNTIME\prediction_executor.py",
r'''# -*- coding: utf-8 -*-

from .model_runtime_connector import model_runtime_check
from .model_outputs import run_models
from .model_fusion import fusion_predict
from .decision_service_bridge import run_decision
from .ai_report import generate_report


def run_prediction(home, away):

    models = run_models(
        home,
        away
    )

    fusion = fusion_predict(
        models["elo"],
        models["dixon"],
        models["poisson"],
        models["xgb"]
    )

    decision = run_decision(
        models,
        fusion
    )


    prediction = {

        "match":{
            "home":home,
            "away":away
        },

        "models":models,

        "fusion":fusion,

        "runtime":model_runtime_check(),

        "prediction_status":
            "PREDICTION_COMPLETED"

    }


    return generate_report(
        prediction,
        decision
    )
''')


# ==========================
# Update AI Report
# ==========================

replace(
r"AI_RUNTIME\ai_report.py",
r'''def generate_report(prediction,decision):


    return {

        "system":
            "Football AI OS",

        "match":
            prediction["match"],

        "model_result":
            prediction["fusion"],

        "final_decision":
            decision.get(
                "final_decision",
                {}
            ),

        "decision_layer":
            decision.get(
                "decision_layer",
                {}
            ),

        "fallback":
            decision.get(
                "fallback",
                False
            ),

        "status":
            "REPORT_READY"

    }
''')


# ==========================
# Update Decision Test Import
# ==========================

test_file=os.path.join(
    ROOT,
    r"08_DECISION_LAYER\test\decision_service_test.py"
)


if os.path.exists(test_file):

    with open(
        test_file,
        encoding="utf-8"
    ) as f:

        content=f.read()


    content=content.replace(
        "service.decision_service_v32"
    )


    with open(
        test_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)


    print(
        "Update:",
        test_file
    )




