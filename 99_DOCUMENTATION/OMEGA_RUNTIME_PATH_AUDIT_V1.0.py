import os
import json

root=r"E:\football_v"

targets=[
"04_Data_Processing_AI",
"05_MODEL_AI",
"06_PREDICTION_ENGINE",
"07_BACKTEST_AI",
"08_DECISION_ENGINE",
"17_MODEL_STORE_LAYER",
"18_MODEL_EXECUTION_ENGINE"
]

result={
    "project":"Football AI OS",
    "architecture":"Omega V3.2",
    "audit":"Runtime Path Alignment",
    "modules":{}
}

for t in targets:

    p=os.path.join(root,t)

    result["modules"][t]={
        "exists":os.path.exists(p),
        "python_files":0,
        "json_files":0,
        "md_files":0
    }

    if os.path.exists(p):

        for path,dirs,files in os.walk(p):

            for f in files:

                if f.endswith(".py"):
                    result["modules"][t]["python_files"]+=1

                elif f.endswith(".json"):
                    result["modules"][t]["json_files"]+=1

                elif f.endswith(".md"):
                    result["modules"][t]["md_files"]+=1


report=r"E:\football_v\99_DOCUMENTATION\reports\OMEGA_RUNTIME_PATH_AUDIT_V1.0.json"

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
