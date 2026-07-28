# -*- coding: utf-8 -*-
import os
import json
import importlib.util
from datetime import datetime


BASE = r"E:\football_v\04_Data_Processing_AI\feature_store"


REPORT_PATH = os.path.join(
    BASE,
    "reports",
    "feature_store_test_report.json"
)


results = []


def check(name, status, message):

    results.append(
        {
            "test": name,
            "status": status,
            "message": message
        }
    )


# ==========================
# 1. 文件结构测试
# ==========================

required_files = [

    "feature_store.py",
    "feature_service.py",
    "feature_loader.py",
    "feature_schema.py",
    "feature_registry.py",

    r"schema\feature_schema.json",

    r"registry\feature_registry.json",

    r"adapters\elo_adapter.py",
    r"adapters\dixon_coles_adapter.py",
    r"adapters\poisson_adapter.py",
    r"adapters\xgboost_adapter.py",
    r"adapters\fusion_adapter.py"

]


for file in required_files:

    path=os.path.join(
        BASE,
        file
    )

    if os.path.exists(path):

        check(
            "file_check",
            "PASS",
            file
        )

    else:

        check(
            "file_check",
            "FAIL",
            file
        )


# ==========================
# 2. Schema测试
# ==========================

try:

    with open(
        os.path.join(
            BASE,
            "schema",
            "feature_schema.json"
        ),
        "r",
        encoding="utf-8"
    ) as f:

        schema=json.load(f)


    if "features" in schema:

        check(
            "schema_check",
            "PASS",
            str(schema["features"])
        )

    else:

        check(
            "schema_check",
            "FAIL",
            "missing features"
        )


except Exception as e:

    check(
        "schema_check",
        "FAIL",
        str(e)
    )



# ==========================
# 3. Adapter接口测试
# ==========================


adapter_list=[

    ("elo_adapter","EloAdapter"),

    ("dixon_coles_adapter",
     "DixonColesAdapter"),

    ("poisson_adapter",
     "PoissonAdapter"),

    ("xgboost_adapter",
     "XGBoostAdapter"),

    ("fusion_adapter",
     "FusionAdapter")

]


for module_name,class_name in adapter_list:


    try:

        file=os.path.join(
            BASE,
            "adapters",
            module_name+".py"
        )


        spec=importlib.util.spec_from_file_location(
            module_name,
            file
        )

        module=importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)


        cls=getattr(
            module,
            class_name
        )


        obj=cls()


        check(
            "adapter_"+module_name,
            "PASS",
            "interface ready"
        )


    except Exception as e:

        check(
            "adapter_"+module_name,
            "FAIL",
            str(e)
        )



# ==========================
# 4. 总结
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
    "feature_store_test",


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
    os.path.dirname(REPORT_PATH),
    exist_ok=True
)


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


print("="*60)

print(json.dumps(
    report,
    indent=4,
    ensure_ascii=False
))

print("="*60)
