import os
import csv
import json
from datetime import datetime

base=r"E:\football_v"

layers=[
"11_SIMULATION_LAYER",
"12_API_LAYER",
"13_TEST_LAYER"
]

assets=[]

for layer in layers:
    path=os.path.join(base,layer)

    if os.path.exists(path):
        for root,dirs,files in os.walk(path):
            for f in files:
                fp=os.path.join(root,f)

                assets.append([
                    f,
                    fp,
                    layer,
                    os.path.splitext(f)[1],
                    True,
                    "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",
                    "Football_AI_OS_Legacy_Asset_Index_V1.0",
                    "DISCOVERED",
                    datetime.now()
                ])


out=r"E:\football_v\10_GOVERNANCE_LAYER\audit\Phase6_Asset_Inventory_V1.0.csv"

with open(out,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow([
        "Asset",
        "Path",
        "Layer",
        "Type",
        "Exists",
        "Architecture_Source",
        "Legacy_Source",
        "Status",
        "Validation_Time"
    ])
    w.writerows(assets)


checkpoint={
"Checkpoint":"PHASE6_DISCOVERY_V1.0",
"Architecture":"Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",
"Legacy_Source":"Football_AI_OS_Legacy_Asset_Index_V1.0",
"Rule_Source":"CLAUDE.md",
"Status":"DISCOVERY_COMPLETED",
"Assets":len(assets),
"Modification":{
"Database_Content":False,
"Business_Logic":False,
"Model_Code":False
}
}

with open(
r"E:\football_v\10_GOVERNANCE_LAYER\checkpoint\Checkpoint_PHASE6_DISCOVERY_V1.0.json",
"w",
encoding="utf-8"
) as f:
    json.dump(checkpoint,f,indent=4)

print("PHASE6 DISCOVERY COMPLETED")
print("Assets:",len(assets))
