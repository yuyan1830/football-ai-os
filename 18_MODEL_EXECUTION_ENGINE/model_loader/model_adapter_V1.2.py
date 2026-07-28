# -*- coding:utf-8 -*-

import sys


MODEL_PATH=r"E:\football_v\00_System_OS\03_MODEL_LAYER\Model_Pool"

sys.path.append(MODEL_PATH)


def load_elo():

    from Elo.elo_engine import calculate_elo

    return calculate_elo



def load_dixon_coles():

    from Dixon_Coles.dixon_coles import calculate_dixon_coles

    return calculate_dixon_coles



def load_poisson():

    from Poisson.poisson_engine import calculate_poisson

    return calculate_poisson



def load_models():


    return {

        "ELO":
        load_elo(),

        "DIXON_COLES":
        load_dixon_coles(),

        "POISSON":
        load_poisson()

    }



if __name__=="__main__":

    models=load_models()

    print(
    {
        "status":"READY",
        "models":list(models.keys())
    }
    )
