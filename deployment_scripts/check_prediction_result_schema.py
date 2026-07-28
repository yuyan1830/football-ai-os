import json
from datetime import datetime

file=r"E:\football_v\14_OPERATION_LAYER\output\prediction_result.json"

with open(file,"r",encoding="utf-8") as f:
    data=json.load(f)

result={
    "version":"FOOTBALL_AI_OS_V4.0_PREDICTION_SCHEMA_AUDIT",
    "time":str(datetime.now()),
    "file":file,
    "top_keys":list(data.keys()),
    "match_keys":list(data.get("match",{}).keys()),
    "model_keys":list(data.get("models",{}).keys()),
    "prediction_keys":list(data.get("prediction",{}).keys()),
    "market_keys":list(data.get("market",{}).keys()),
    "risk_keys":list(data.get("risk",{}).keys()),
    "decision":data.get("decision"),
    "status":data.get("status")
}

print(json.dumps(result,indent=4,ensure_ascii=False))
