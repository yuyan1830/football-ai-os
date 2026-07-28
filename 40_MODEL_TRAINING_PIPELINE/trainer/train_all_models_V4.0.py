import os
import json
import datetime


ROOT = r"E:\FOOTBALL_V"


TRAINER_DIR = os.path.join(
    ROOT,
    "40_MODEL_TRAINING_PIPELINE",
    "TRAINER"
)


REPORT_DIR = os.path.join(
    ROOT,
    "40_MODEL_TRAINING_PIPELINE",
    "reports"
)


os.makedirs(REPORT_DIR, exist_ok=True)


training_order = [

    "elo_trainer_V4.0.py",

    "dixon_coles_trainer_V4.0.py",

    "poisson_trainer_V4.0.py",

    "xgboost_trainer_V4.0.py",

    "fusion_trainer_V4.0.py"

]


training_config = {

    "version":
    "TRAIN_ALL_MODELS_V4.0",

    "status":
    "READY",

    "execution_order":
    training_order,

    "weights":
    {

        "Fusion":0.30,

        "ELO":0.20,

        "Dixon-Coles":0.20,

        "Poisson":0.15,

        "XGBoost":0.15

    },

    "architecture_change":
    False,

    "auto_weight_change":
    False

}



def run_training():

    result = {

        "version":
        "MODEL_TRAINING_EXECUTION_V4.0",

        "time":
        str(datetime.datetime.now()),

        "status":
        "TRAINING_PIPELINE_READY",

        "modules":

        []

    }


    for module in training_order:

        result["modules"].append(

            {

            "module":module,

            "status":"WAITING"

            }

        )


    return result



if __name__ == "__main__":


    result = run_training()


    report = os.path.join(

        REPORT_DIR,

        "TRAINING_EXECUTION_STATUS_V4.0.json"

    )


    with open(

        report,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            result,

            f,

            indent=4,

            ensure_ascii=False

        )


    print("="*70)

    print("Football AI OS V4.0")

    print("TRAINING EXECUTION ENGINE READY")

    print("="*70)

    print(json.dumps(

        result,

        indent=4,

        ensure_ascii=False

    ))

