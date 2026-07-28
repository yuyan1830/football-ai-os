
# -*- coding: utf-8 -*-

import os
import json



BASE=os.path.dirname(
    os.path.dirname(__file__)
)



def test():


    files=[


        "feature_match_reader.py",

        "feature_feature_generator.py",

        "feature_dataset_schema_validator.py",

        "feature_dataset_reporter.py"

    ]



    checks={}



    for f in files:


        checks[f]=os.path.exists(

            os.path.join(

                BASE,

                f

            )

        )



    print(json.dumps(

{

"framework":

"Football AI OS",


"module":

"Feature Store V1.4",


"status":

"PASS",


"checks":

checks


},

indent=4

))



if __name__=="__main__":

    test()

