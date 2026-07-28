# -*- coding:utf-8 -*-

"""
Football AI OS
Raw Data Scanner V1.0
"""


import os



class RawScanner:


    def __init__(self,path):

        self.path=path



    def scan(self):

        result=[]


        for root,dirs,files in os.walk(
            self.path
        ):

            for file in files:


                result.append(

                    {
                        "name":file,

                        "path":
                        os.path.join(
                            root,
                            file
                        )
                    }

                )


        return result



if __name__=="__main__":


    scanner=RawScanner(".")


    data=scanner.scan()


    print(
        "Raw Files:",
        len(data)
    )