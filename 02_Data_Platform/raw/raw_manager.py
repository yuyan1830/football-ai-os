# -*- coding:utf-8 -*-

"""
Football AI OS
Raw Data Manager V1.0
"""


import json

from raw_scanner import RawScanner

from raw_registry import RawRegistry



class RawManager:



    def __init__(self):

        self.scanner=RawScanner(
            "."
        )

        self.registry=RawRegistry()



    def execute(self):


        files=self.scanner.scan()


        return self.registry.register(
            files
        )



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Raw Data Manager V1.0"
    )

    print("="*50)



    manager=RawManager()


    result=manager.execute()


    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )