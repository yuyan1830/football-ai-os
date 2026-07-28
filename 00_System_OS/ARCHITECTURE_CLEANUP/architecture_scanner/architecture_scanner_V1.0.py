
# -*- coding:utf-8 -*-

import os
import json


BASE=r"E:\football_v"


def scan():

    data=[]

    for x in os.listdir(BASE):

        if os.path.isdir(
            os.path.join(BASE,x)
        ):
            data.append(x)

    print(json.dumps(
    {
    "module":"Architecture Scanner",
    "count":len(data),
    "directories":data
    },
    indent=4,
    ensure_ascii=False
    ))


if __name__=="__main__":
    scan()
