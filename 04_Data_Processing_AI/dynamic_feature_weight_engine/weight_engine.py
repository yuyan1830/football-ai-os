
# -*- coding:utf-8 -*-

class WeightEngine:


    def calculate(self, context):

        return {

            "status":"calculated",

            "weights":context

        }


if __name__=="__main__":

    print(
        WeightEngine().calculate({})
    )
