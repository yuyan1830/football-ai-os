# -*- coding:utf-8 -*-

from model_adapter_V1.2 import load_models


def run_models():


    models=load_models()


    output={}


    for name,func in models.items():

        try:

            result=func()

            output[name]=result


        except Exception as e:

            output[name]={
                "error":str(e)
            }


    return output



if __name__=="__main__":


    result=run_models()


    print(result)

