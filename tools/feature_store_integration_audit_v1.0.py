import os
import json
from datetime import datetime

BASE=r"E:\football_v"

targets=[
r"04_Data_Processing_AI\feature_store",
r"05_MODEL_AI\MODEL_LAYER",
r"06_PREDICTION_ENGINE",
r"06_PREDICTION_INTELLIGENCE_ENGINE",
r"27_MODEL_FUSION_ENGINE",
r"50_MODEL_REGISTRY"
]

keywords=[
"feature_store",
"FeatureStore",
"feature",
"database",
"model_store",
"elo",
"dixon",
"poisson",
"xgboost",
"registry"
]


result={
    "project":"Football AI OS",
    "phase":"Phase 2 Feature Store Integration Audit",
    "time":str(datetime.now()),
    "scan":{}
}


for t in targets:

    path=os.path.join(BASE,t)

    result["scan"][t]={
        "exists":os.path.exists(path),
        "files":[],
        "matches":[]
    }

    if not os.path.exists(path):
        continue


    for root,dirs,files in os.walk(path):

        for f in files:

            if f.endswith((".py",".json",".yaml",".yml",".md",".txt")):

                fp=os.path.join(root,f)

                result["scan"][t]["files"].append(fp)

                try:
                    with open(fp,"r",encoding="utf-8",errors="ignore") as file:
                        text=file.read()

                    hit=[]

                    for k in keywords:
                        if k.lower() in text.lower():
                            hit.append(k)

                    if hit:
                        result["scan"][t]["matches"].append({
                            "file":fp,
                            "keywords":hit
                        })

                except:
                    pass



out=r"E:\football_v\99_DOCUMENTATION\reports\FEATURE_STORE_INTEGRATION_AUDIT_V1.0.json"

os.makedirs(os.path.dirname(out),exist_ok=True)

with open(out,"w",encoding="utf-8") as f:
    json.dump(result,f,indent=2,ensure_ascii=False)


print(json.dumps({
    "status":"PASS",
    "report":out
},indent=2))
