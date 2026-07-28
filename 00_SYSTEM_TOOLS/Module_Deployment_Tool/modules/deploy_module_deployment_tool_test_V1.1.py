# -*- coding: utf-8 -*-

import os
import json
import importlib.util
from datetime import datetime


BASE = r"E:/football_v/00_SYSTEM_TOOLS/Module_Deployment_Tool"

REPORT = os.path.join(
    BASE,
    "reports",
    "deployment_tool_test_report.json"
)


tests = []


def add_test(name,status,message):

    tests.append({

        "test": name,

        "status": status,

        "message": message

    })


def load_module(name,path):

    spec = importlib.util.spec_from_file_location(
        name,
        path
    )

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module



# ==========================
# Syntax Validator
# ==========================

try:

    module = load_module(

        "syntax_validator",

        BASE + "/core/syntax_validator.py"

    )

    obj = module.SyntaxValidator()


    result = obj.check(

        BASE + "/core/syntax_validator.py"

    )


    if result:

        add_test(
            "syntax_validator",
            "PASS",
            "syntax check ready"
        )

    else:

        add_test(
            "syntax_validator",
            "FAIL",
            "syntax failed"
        )


except Exception as e:

    add_test(
        "syntax_validator",
        "FAIL",
        str(e)
    )



# ==========================
# Encoding Validator
# ==========================

try:

    module = load_module(

        "encoding_validator",

        BASE + "/core/encoding_validator.py"

    )


    obj = module.EncodingValidator()


    result = obj.check(

        BASE + "/core/encoding_validator.py"

    )


    if result:

        add_test(
            "encoding_validator",
            "PASS",
            "UTF-8 ready"
        )


except Exception as e:

    add_test(
        "encoding_validator",
        "FAIL",
        str(e)
    )



# ==========================
# JSON Validator
# ==========================

try:

    module = load_module(

        "json_validator",

        BASE + "/core/json_validator.py"

    )


    obj = module.JsonValidator()


    result = obj.check(

        BASE + "/config/deployment_tool_config.json"

    )


    if result:

        add_test(
            "json_validator",
            "PASS",
            "json format ready"
        )


except Exception as e:

    add_test(
        "json_validator",
        "FAIL",
        str(e)
    )



# ==========================
# Path Validator
# ==========================

try:

    module = load_module(

        "path_validator",

        BASE + "/core/path_validator.py"

    )


    obj = module.PathValidator()


    result = obj.check(

        BASE + "/modules"

    )


    if result:

        add_test(
            "path_validator",
            "PASS",
            "path structure ready"
        )


except Exception as e:

    add_test(
        "path_validator",
        "FAIL",
        str(e)
    )



# ==========================
# Deployment Engine
# ==========================

try:

    module = load_module(

        "deployment_engine",

        BASE + "/core/deployment_engine.py"

    )


    obj = module.DeploymentEngine()


    result = obj.run()


    if result["status"]=="ready":

        add_test(
            "deployment_engine",
            "PASS",
            "engine ready"
        )


except Exception as e:

    add_test(
        "deployment_engine",
        "FAIL",
        str(e)
    )



failed = [

x for x in tests

if x["status"]=="FAIL"

]



report = {


"framework":

"Football AI OS Ultimate Fusion Framework V1.5",


"tool":

"Module Deployment Tool",


"version":

"V1.1",


"service":

"deployment_tool_self_test",


"status":

"PASS" if len(failed)==0 else "FAIL",


"total_tests":

len(tests),


"failed":

len(failed),


"tests":

tests,


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