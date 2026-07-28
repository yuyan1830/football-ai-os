# -*- coding: utf-8 -*-

import os
import json
import importlib.util
from datetime import datetime


BASE = r"E:\football_v\04_Data_Processing_AI\data_intelligence_engine"


TEST_DIR = os.path.join(
    BASE,
    "tests"
)


REPORT = os.path.join(
    BASE,
    "reports",
    "data_intelligence_test_report.json"
)


results=[]


def add_test(name,status,message):

    results.append({

        "test":name,

        "status":status,

        "message":message

    })


# ==========================
# Engine Test
# ==========================

try:

    file=os.path.join(
        BASE,
        "data_intelligence_engine.py"
    )


    spec=importlib.util.spec_from_file_location(
        "engine",
        file
    )


    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    obj=module.DataIntelligenceEngine()


    result=obj.analyze(
        [
            "team_strength",
            "recent_form"
        ]
    )


    if result["status"]=="analyzed":

        add_test(
            "engine_test",
            "PASS",
            "engine ready"
        )

    else:

        add_test(
            "engine_test",
            "FAIL",
            str(result)
        )


except Exception as e:

    add_test(
        "engine_test",
        "FAIL",
        str(e)
    )


# ==========================
# Router Test
# ==========================

try:

    file=os.path.join(
        BASE,
        "data_router.py"
    )


    spec=importlib.util.spec_from_file_location(
        "router",
        file
    )


    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    router=module.DataRouter()


    models=[

        "Elo",

        "Dixon-Coles",

        "Poisson",

        "XGBoost",

        "Fusion"

    ]


    success=True


    for m in models:

        if len(router.route(m))==0:

            success=False


    if success:

        add_test(
            "model_router_test",
            "PASS",
            "5 models connected"
        )

    else:

        add_test(
            "model_router_test",
            "FAIL",
            "routing error"
        )


except Exception as e:

    add_test(
        "model_router_test",
        "FAIL",
        str(e)
    )


# ==========================
# Model Interface Test
# ==========================

try:

    file=os.path.join(
        BASE,
        "model_interface.py"
    )


    spec=importlib.util.spec_from_file_location(
        "interface",
        file
    )


    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    interface=module.ModelInterface()


    models=interface.available_models()


    if len(models)==5:


        add_test(
            "model_interface_test",
            "PASS",
            str(models)
        )

    else:

        add_test(
            "model_interface_test",
            "FAIL",
            str(models)
        )


except Exception as e:

    add_test(
        "model_interface_test",
        "FAIL",
        str(e)
    )


# ==========================
# Config Test
# ==========================

try:

    with open(

        BASE+r"\config\data_intelligence_config.json",

        "r",

        encoding="utf-8"

    ) as f:

        config=json.load(f)


    if len(config["supported_models"])==5:


        add_test(
            "config_test",
            "PASS",
            "config valid"
        )


    else:

        add_test(
            "config_test",
            "FAIL",
            "model count error"
        )


except Exception as e:

    add_test(
        "config_test",
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

    "data_intelligence_engine_test",


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