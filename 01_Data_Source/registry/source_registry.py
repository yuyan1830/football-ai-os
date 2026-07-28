# -*- coding: utf-8 -*-

"""
Football AI OS
Source Registry Engine V1.1
"""


import json
import os
import datetime



BASE_DIR = os.path.dirname(__file__)


REGISTRY_FILE = os.path.join(
    BASE_DIR,
    "source_registry.json"
)



def load_registry():

    with open(
        REGISTRY_FILE,
        "r",
        encoding="utf-8-sig"
    ) as f:

        return json.load(f)



def list_sources():

    return load_registry()



def get_source(source_id):

    data = load_registry()


    for source in data["sources"]:

        if source["id"] == source_id:

            return source


    return None



def source_summary():

    data = load_registry()


    result = {

        "framework":
        data["framework"],

        "module":
        data["module"],

        "version":
        data["version"],

        "count":
        len(data["sources"]),

        "time":
        str(datetime.datetime.now())

    }


    return result



if __name__ == "__main__":


    print("="*50)

    print(
        "Football AI OS Source Registry Engine V1.1"
    )

    print("="*50)



    print(
        json.dumps(
            source_summary(),
            indent=4,
            ensure_ascii=False
        )
    )


    print()


    print(
        "Sources:"
    )


    print(
        json.dumps(
            list_sources()["sources"],
            indent=4,
            ensure_ascii=False
        )
    )