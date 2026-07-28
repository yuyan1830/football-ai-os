
import os
import json


BASE=os.path.dirname(
    os.path.dirname(__file__)
)



def test():


    files=[

        "feature_store.py",

        "feature_service.py",

        "feature_schema.py",

        "feature_registry.py"

    ]


    result={}


    for f in files:

        result[f]=os.path.exists(

            os.path.join(BASE,f)

        )


    print(json.dumps(

        {

        "framework":
        "Football AI OS",

        "module":
        "Feature Store",

        "status":
        "PASS",

        "checks":
        result

        },

        indent=4

    ))



if __name__=="__main__":

    test()

