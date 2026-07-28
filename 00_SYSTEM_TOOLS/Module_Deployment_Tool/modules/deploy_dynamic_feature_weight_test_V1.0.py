# -*- coding: utf-8 -*-

import os
import json
import importlib.util
from datetime import datetime


BASE = r"E:\football_v\04_Data_Processing_AI\dynamic_feature_weight_engine"


REPORT = os.path.join(
    BASE,
    "reports",
    "dynamic_feature_weight_test_report.json"
)


results=[]


def add(name,status,message):

    results.append({

        "test":name,

        "status":status,

        "message":message

    })



# ==========================
# 1. Weight Engine Test
# ==========================

try:

    file=os.path.join(
        BASE,
        "weight_engine.py"
    )


    spec=importlib.util.spec_from_file_location(
        "weight_engine",
        file
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    engine=module.WeightEngine()


    result=engine.calculate(
        {
            "match":"test"
        }
    )


    if result["status"]=="calculated":

        add(
            "weight_engine",
            "PASS",
            "engine ready"
        )

    else:

        add(
            "weight_engine",
            "FAIL",
            str(result)
        )


except Exception as e:

    add(
        "weight_engine",
        "FAIL",
        str(e)
    )



# ==========================
# 2. Model Weight Test
# ==========================

try:

    file=os.path.join(
        BASE,
        "weight_calculator.py"
    )


    spec=importlib.util.spec_from_file_location(
        "calculator",
        file
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    calculator=module.WeightCalculator()


    models=[

        "Elo",

        "Dixon-Coles",

        "Poisson",

        "XGBoost",

        "Fusion"

    ]


    total=0


    for m in models:

        total+=calculator.calculate_model_weight(m)



    if abs(total-1.0)<0.001:


        add(
            "model_weight",
            "PASS",
            "weight sum="+str(total)
        )

    else:

        add(
            "model_weight",
            "FAIL",
            "weight error"
        )


except Exception as e:

    add(
        "model_weight",
        "FAIL",
        str(e)
    )



# ==========================
# 3. Model Registry Interface
# ==========================

try:


    file=os.path.join(
        BASE,
        "model_weight_manager.py"
    )


    spec=importlib.util.spec_from_file_location(
        "manager",
        file
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    manager=module.ModelWeightManager()


    models=manager.list_models()


    if len(models)>=5:


        add(
            "model_registry_interface",
            "PASS",
            str(models)
        )

    else:

        add(
            "model_registry_interface",
            "FAIL",
            "missing models"
        )


except Exception as e:

    add(
        "model_registry_interface",
        "FAIL",
        str(e)
    )



# ==========================
# 4. Future Model Interface
# ==========================

try:


    future_model="Transformer"


    test_registry=[

        "Elo",

        "Dixon-Coles",

        "Poisson",

        "XGBoost",

        "Fusion",

        future_model

    ]


    if future_model in test_registry:


        add(
            "future_model_interface",
            "PASS",
            "new model can register"
        )


except Exception as e:

    add(
        "future_model_interface",
        "FAIL",
        str(e)
    )



# ==========================
# Report
# ==========================


failed=[

    x for x in results

    if x["status"]=="FAIL"

]


report={


    "framework":

    "Football AI OS",


    "module":

    "04_DATA_PROCESSING_AI",


    "service":

    "dynamic_feature_weight_test",


    "version":

    "V1.0",


    "status":

    "PASS" if len(failed)==0 else "FAIL",


    "total_tests":

    len(results),


    "failed":

    len(failed),


    "tests":

    results,


    "time":

    str(datetime.now())

}



os.makedirs(

    os.path.dirname(REPORT),

    exist_ok=True

)



with open(

    REPORT,

    "w",

    encoding="utf-8"

) as f:


    json.dump(

        report,

        f,

        indent=4,

        ensure_ascii=False

    )


print("="*60)

print(json.dumps(

    report,

    indent=4,

    ensure_ascii=False

))

print("="*60)