
# -*- coding: utf-8 -*-

import json


def run():

    result={
    "module":"Dependency Checker",
    "status":"READY",
    "dependencies":[
        "database",
        "model_store",
        "api",
        "dashboard"
    ]
    }

    print(json.dumps(result,indent=4))


if __name__=="__main__":
    run()
