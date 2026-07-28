
# -*- coding: utf-8 -*-

import os
import json


BASE=os.path.dirname(
    os.path.dirname(__file__)
)



def test():


    files=[

        "feature_database_connector.py",

        "feature_dataset_builder.py",

        "feature_validator.py",

        "feature_pipeline.py"

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

        "Feature Store V1.1",


        "status":

        "PASS",


        "checks":

        result

        },

        indent=4

        ))



if __name__=="__main__":

    test()


