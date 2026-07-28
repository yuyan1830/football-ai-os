# -*- coding: utf-8 -*-

"""
Football AI OS Dependency Engine V1.2
"""

import json
import os



BASE_PATH = (
    r"E:\football_v\00_SYSTEM_OS\Registry"
)


DEPENDENCY_FILE = os.path.join(
    BASE_PATH,
    "dependency_map.json"
)



def load():

    with open(
        DEPENDENCY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def resolve():


    print(
        "Football AI OS Dependency Engine V1.2"
    )


    data = load()


    deps = data["Dependencies"]


    order=[]



    def visit(node):

        if node in order:

            return


        for dep in deps.get(
            node,
            []
        ):

            visit(dep)


        order.append(node)



    for module in deps:

        visit(module)



    print("")

    print(
        "Startup Order:"
    )


    for i,m in enumerate(
        order,
        1
    ):

        print(
            str(i)
            +
            ".",
            m
        )



    return order



if __name__=="__main__":

    resolve()