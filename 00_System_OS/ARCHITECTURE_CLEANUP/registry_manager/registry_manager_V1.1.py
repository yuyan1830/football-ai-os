# -*- coding:utf-8 -*-

import json
from datetime import datetime


REPORT_PATH=r"E:\football_v\00_SYSTEM_OS\ARCHITECTURE_CLEANUP\registry\architecture_registry.json"


report={

"system":"Football AI OS",

"framework":"Ultimate Fusion Framework V1.5",

"version":"V1.1",

"ACTIVE":[

"00_SYSTEM_OS",
"01_DATA_LAYER",
"02_FEATURE_LAYER",
"03_MODEL_LAYER",
"16_DATABASE_GOVERNANCE_LAYER",
"17_MODEL_STORE_LAYER",
"18_MODEL_EXECUTION_ENGINE",
"19_API_LAYER",
"20_DASHBOARD_LAYER",
"21_PRODUCT_PACKAGE"

],

"LEGACY":[

"07_BACKTEST_AI",
"07_BACKTEST_SYSTEM",
"08_DECISION_ENGINE",
"10_Dashboard"

],

"MIGRATION_REQUIRED":[],

"DEPRECATED":[],

"time":str(datetime.now())

}


with open(
REPORT_PATH,
"w",
encoding="utf-8"
) as f:

    json.dump(
    report,
    f,
    indent=4,
    ensure_ascii=False
    )


print(report)

