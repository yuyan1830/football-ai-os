import csv
from datetime import datetime


out=r"E:\football_v\10_GOVERNANCE_LAYER\audit\DATA_LAYER_Governance_Summary_V1.0.csv"


data=[

{
"Asset":"match_data.db",
"Layer":"01_DATA_LAYER",
"Decision":"KEEP_CURRENT",
"Legacy_Action":"RETAIN",
"Risk":"LOW",
"Status":"APPROVED"
},

{
"Asset":"feature_store.db",
"Layer":"02_FEATURE_LAYER",
"Decision":"KEEP_CURRENT",
"Legacy_Action":"ARCHIVE_REFERENCE",
"Risk":"MEDIUM",
"Status":"APPROVED"
},

{
"Asset":"model_store.db",
"Layer":"03_MODEL_LAYER",
"Decision":"HOLD",
"Legacy_Action":"REVIEW_REQUIRED",
"Risk":"HIGH",
"Status":"PENDING_MODEL_GOVERNANCE"
}

]


with open(out,"w",newline="",encoding="utf-8") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=[
        "Asset",
        "Layer",
        "Decision",
        "Legacy_Action",
        "Risk",
        "Status"
        ])

    writer.writeheader()
    writer.writerows(data)


print(out)

