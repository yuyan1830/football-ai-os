# -*- coding: utf-8 -*-

"""
Football AI OS
Source Scanner V1.2
"""

import os


class SourceScanner:


    def __init__(self,path):

        self.path = path



    def scan(self):

        result=[]


        for root,dirs,files in os.walk(self.path):

            for file in files:

                result.append(
                    {
                        "file":file,
                        "path":
                        os.path.join(root,file)
                    }
                )


        return result



if __name__=="__main__":


    scanner=SourceScanner(
        "../download"
    )


    print(
        scanner.scan()
    )