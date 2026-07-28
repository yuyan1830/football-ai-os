import os
import json
from datetime import datetime


BASE = r"E:\football_v\04_Data_Processing_AI\feature_store\adapters"


ADAPTERS = {

"elo_adapter.py":
'''
class EloAdapter:

    def transform(self, features):

        return {
            "model":"Elo",
            "features":[
                "team_strength",
                "league_strength"
            ],
            "input":features
        }


if __name__=="__main__":
    print(EloAdapter().transform({}))
''',


"dixon_coles_adapter.py":
'''
class DixonColesAdapter:

    def transform(self, features):

        return {
            "model":"Dixon-Coles",
            "features":[
                "attack",
                "defense",
                "goal_pattern"
            ],
            "input":features
        }


if __name__=="__main__":
    print(DixonColesAdapter().transform({}))
''',


"poisson_adapter.py":
'''
class PoissonAdapter:

    def transform(self, features):

        return {
            "model":"Poisson",
            "features":[
                "goal_rate",
                "attack_rate",
                "defense_rate"
            ],
            "input":features
        }


if __name__=="__main__":
    print(PoissonAdapter().transform({}))
''',


"xgboost_adapter.py":
'''
class XGBoostAdapter:

    def transform(self, features):

        return {
            "model":"XGBoost",
            "features":[
                "all_features"
            ],
            "input":features
        }


if __name__=="__main__":
    print(XGBoostAdapter().transform({}))
''',


"fusion_adapter.py":
'''
class FusionAdapter:

    def transform(self, model_outputs):

        return {
            "model":"Fusion",
            "models":[
                "Elo",
                "Dixon-Coles",
                "Poisson",
                "XGBoost"
            ],
            "input":model_outputs
        }


if __name__=="__main__":
    print(FusionAdapter().transform({}))
'''
}


for filename,code in ADAPTERS.items():

    path=os.path.join(BASE,filename)

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)


registry={

    "module":
    "Feature Store Adapter Layer",

    "version":
    "V1.0",

    "status":
    "active",

    "adapters":[
        "Elo",
        "Dixon-Coles",
        "Poisson",
        "XGBoost",
        "Fusion"
    ],

    "time":
    str(datetime.now())

}


registry_path=os.path.join(
    os.path.dirname(BASE),
    "registry",
    "adapter_registry.json"
)


os.makedirs(
    os.path.dirname(registry_path),
    exist_ok=True
)


with open(
    registry_path,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        registry,
        f,
        indent=4,
        ensure_ascii=False
    )


print("="*60)

print(registry)

print("="*60)