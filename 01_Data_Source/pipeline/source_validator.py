# -*- coding:utf-8 -*-

"""
Football AI OS
Source Validator V1.2
"""


class SourceValidator:



    def validate(self,files):


        result={

            "total":
            len(files),

            "valid":
            0,

            "invalid":
            0

        }


        for item in files:


            if item["file"].endswith(
                ".csv"
            ):

                result["valid"] +=1


            else:

                result["invalid"] +=1



        return result