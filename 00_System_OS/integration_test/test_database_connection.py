
# -*- coding:utf-8 -*-

import os

BASE=r"E:\football_v"

targets=[

"16_DATABASE_GOVERNANCE_LAYER",

"17_MODEL_STORE_LAYER",

"18_MODEL_EXECUTION_ENGINE"

]


result=[]


for t in targets:

    result.append({

    "module":t,

    "exists":os.path.exists(

        os.path.join(BASE,t)

    )

    })


print(result)

