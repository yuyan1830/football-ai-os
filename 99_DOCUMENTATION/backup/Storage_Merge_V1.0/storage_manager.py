# -*- coding:utf-8 -*-

"""
Football AI OS
Data Platform Storage Manager V1.0
"""

import os
import hashlib
import datetime


class StorageManager:


    def __init__(self, base_path):

        self.base_path = base_path



    def scan_files(self):

        files=[]


        for root,dirs,names in os.walk(
            self.base_path
        ):

            for name in names:

                path=os.path.join(
                    root,
                    name
                )

                files.append(path)


        return files



    def calculate_hash(self,file):

        sha256=hashlib.sha256()


        with open(
            file,
            "rb"
        ) as f:

            for block in iter(
                lambda:f.read(4096),
                b""
            ):

                sha256.update(block)


        return sha256.hexdigest()



    def create_inventory(self):


        result=[]


        for file in self.scan_files():

            result.append(

                {
                    "file":file,

                    "hash":
                    self.calculate_hash(file),

                    "time":
                    str(datetime.datetime.now())

                }

            )


        return result



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Storage Manager V1.0"
    )

    print("="*50)


    manager=StorageManager(
        "./raw"
    )


    print(
        manager.create_inventory()
    )