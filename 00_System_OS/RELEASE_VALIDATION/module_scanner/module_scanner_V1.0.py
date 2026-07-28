
# -*- coding: utf-8 -*-

import os


BASE=r"E:\football_v"


def scan():

    modules=[]

    for x in os.listdir(BASE):

        if x[:2].isdigit():
            modules.append(x)

    print(
        {
        "module":"Module Scanner",
        "count":len(modules),
        "modules":modules
        }
    )


if __name__=="__main__":
    scan()
