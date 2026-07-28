import json
import os


registry={
    "module":"feature_store",
    "version":"V1.0",
    "status":"active",
    "models":[
        "Elo",
        "Dixon-Coles",
        "Poisson",
        "XGBoost",
        "Fusion"
    ],
    "time":str(datetime.now())
}


path=os.path.join(
    os.path.dirname(__file__),
    "registry",
    "feature_registry.json"
)


with open(
    path,
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        registry,
        f,
        indent=4,
        ensure_ascii=False
    )


print(registry)
