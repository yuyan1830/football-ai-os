import os
import json


root=r"E:\football_v"


checks={}


targets={

"feedback_modules":[
"07_BACKTEST_AI\feature_feedback.py",
"07_BACKTEST_AI\model_feedback.py",
"07_BACKTEST_AI\optimization_scheduler.py"
],

"model_modules":[
"05_MODEL_AI\MODEL_LAYER\models\elo_model.py",
"05_MODEL_AI\MODEL_LAYER\fusion\fusion_engine.py",
"05_MODEL_AI\MODEL_LAYER\model_registry.py"
],

"model_store":[
"17_MODEL_STORE_LAYER\model_registry",
"17_MODEL_STORE_LAYER\model_validator",
"17_MODEL_STORE_LAYER\model_version_manager.py"
],

"runtime":[
"18_MODEL_EXECUTION_ENGINE\model_loader",
"18_MODEL_EXECUTION_ENGINE\prediction_pipeline",
"18_MODEL_EXECUTION_ENGINE\fusion_engine"
]

}


for group,items in targets.items():

    checks[group]=[]

    for item in items:

        path=os.path.join(root,item)

        checks[group].append({

            "path":item,

            "exists":os.path.exists(path)

        })


result={

"project":"Football AI OS",

"architecture":"Omega V3.2",

"phase":"Phase5 Learning Core Precheck",

"status":"AUDIT_COMPLETED",

"checks":checks

}


report=r"E:\football_v\99_DOCUMENTATION\reports\PHASE5_LEARNING_CORE_PRECHECK_V1.0.json"


with open(report,"w",encoding="utf-8") as f:

    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )


print(json.dumps(result,indent=2,ensure_ascii=False))

print("")
print("REPORT:")
print(report)

