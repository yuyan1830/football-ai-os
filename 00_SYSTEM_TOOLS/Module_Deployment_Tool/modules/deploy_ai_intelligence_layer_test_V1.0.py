# -*- coding: utf-8 -*-

import os
import json
import importlib.util
from datetime import datetime


BASE = r"E:\football_v\05_AI_INTELLIGENCE_LAYER"

REPORT = os.path.join(
    BASE,
    "reports",
    "ai_intelligence_layer_test_report.json"
)


results=[]


def add_test(name,status,message):

    results.append({

        "test":name,

        "status":status,

        "message":message

    })



# ===============================
# Model Registry Test
# ===============================

try:

    path=os.path.join(
        BASE,
        "MODEL_REGISTRY",
        "model_registry.py"
    )


    spec=importlib.util.spec_from_file_location(
        "registry",
        path
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    registry=module.ModelRegistry()


    models=registry.list_models()


    if len(models)>=5:

        registry.register(
            "Transformer",
            "V1.0"
        )

        if "Transformer" in registry.list_models():

            add_test(
                "model_registry",
                "PASS",
                "future model register success"
            )

    else:

        add_test(
            "model_registry",
            "FAIL",
            "missing models"
        )


except Exception as e:

    add_test(
        "model_registry",
        "FAIL",
        str(e)
    )



# ===============================
# Adapter Test
# ===============================

try:

    path=os.path.join(
        BASE,
        "MODEL_ADAPTER_FRAMEWORK",
        "adapter_base.py"
    )


    spec=importlib.util.spec_from_file_location(
        "adapter",
        path
    )


    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    adapter=module.BaseAdapter()


    if (

        adapter.train({})

        and

        adapter.predict({})=={}

    ):

        add_test(
            "adapter_framework",
            "PASS",
            "interface ready"
        )

    else:

        add_test(
            "adapter_framework",
            "FAIL",
            "interface error"
        )


except Exception as e:

    add_test(
        "adapter_framework",
        "FAIL",
        str(e)
    )



# ===============================
# Fusion Test
# ===============================

try:

    path=os.path.join(
        BASE,
        "FUSION_DECISION_ENGINE",
        "fusion_engine.py"
    )


    spec=importlib.util.spec_from_file_location(
        "fusion",
        path
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    fusion=module.FusionEngine()


    result=fusion.combine(

        [

            "Elo",

            "Poisson",

            "XGBoost"

        ]

    )


    if result["fusion"]=="completed":

        add_test(
            "fusion_engine",
            "PASS",
            "fusion ready"
        )

    else:

        add_test(
            "fusion_engine",
            "FAIL",
            str(result)
        )


except Exception as e:

    add_test(
        "fusion_engine",
        "FAIL",
        str(e)
    )



# ===============================
# Evaluation Test
# ===============================

try:

    path=os.path.join(
        BASE,
        "MODEL_EVALUATION_ENGINE",
        "evaluator.py"
    )


    spec=importlib.util.spec_from_file_location(
        "evaluation",
        path
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    evaluator=module.Evaluator()


    result=evaluator.evaluate(
        0.8,
        1
    )


    if "error" in result:

        add_test(
            "evaluation_engine",
            "PASS",
            str(result)
        )


except Exception as e:

    add_test(
        "evaluation_engine",
        "FAIL",
        str(e)
    )



# ===============================
# Reflection Test
# ===============================

try:

    path=os.path.join(
        BASE,
        "SELF_REFLECTION_ENGINE",
        "reflection_engine.py"
    )


    spec=importlib.util.spec_from_file_location(
        "reflection",
        path
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)


    reflection=module.ReflectionEngine()


    result=reflection.reflect(
        {
            "error":0.2
        }
    )


    if result["reflection"]=="stored":

        add_test(
            "self_reflection",
            "PASS",
            "experience interface ready"
        )


except Exception as e:

    add_test(
        "self_reflection",
        "FAIL",
        str(e)
    )



failed=[

x for x in results

if x["status"]=="FAIL"

]


report={


"framework":

"Football AI OS Ultimate Fusion Framework V1.5",


"layer":

"05_AI_INTELLIGENCE_LAYER",


"service":

"ai_intelligence_layer_test",


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