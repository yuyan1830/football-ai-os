import os
import json
from pathlib import Path


ROOT = Path(r"E:\football_v")

OUTPUT = ROOT / "99_DOCUMENTATION" / "MODEL_LAYER_FULL_AUDIT"


OUTPUT.mkdir(parents=True, exist_ok=True)


keywords = [
    "MODEL_LAYER",
    "elo",
    "dixon",
    "poisson",
    "xgboost",
    "model_registry",
    "model_runtime",
    "model_loader",
    "fusion_engine",
    "prediction_engine"
]


results = {
    "scan_root": str(ROOT),
    "files": [],
    "keyword_hits": {},
    "model_files": [],
    "config_files": [],
    "registry_files": []
}


extensions = [
    ".py",
    ".json",
    ".md",
    ".txt",
    ".yaml",
    ".yml"
]


for path in ROOT.rglob("*"):

    if not path.is_file():
        continue

    if path.suffix.lower() not in extensions:
        continue


    try:
        text = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except:
        continue


    record = {
        "file": str(path),
        "size": path.stat().st_size
    }


    results["files"].append(record)


    lower = text.lower()


    for key in keywords:

        if key.lower() in lower:

            results["keyword_hits"].setdefault(
                key,
                []
            ).append(
                str(path)
            )


    name = path.name.lower()


    if "model" in name:
        results["model_files"].append(
            str(path)
        )


    if "config" in name:
        results["config_files"].append(
            str(path)
        )


    if "registry" in name:
        results["registry_files"].append(
            str(path)
        )



with open(
    OUTPUT / "MODEL_LAYER_FULL_AUDIT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results,
        f,
        indent=2,
        ensure_ascii=False
    )



with open(
    OUTPUT / "MODEL_LAYER_FULL_AUDIT.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "Football AI OS MODEL LAYER FULL AUDIT\n"
    )

    f.write("="*60+"\n\n")


    for k,v in results["keyword_hits"].items():

        f.write(
            "\n### "+k+"\n"
        )

        for item in v:

            f.write(
                item+"\n"
            )


    f.write("\n\nMODEL FILES\n")
    f.write("="*60+"\n")

    for x in results["model_files"]:

        f.write(x+"\n")


    f.write("\n\nREGISTRY FILES\n")
    f.write("="*60+"\n")

    for x in results["registry_files"]:

        f.write(x+"\n")



print("SCAN COMPLETE")
print(
    OUTPUT / "MODEL_LAYER_FULL_AUDIT.json"
)
print(
    OUTPUT / "MODEL_LAYER_FULL_AUDIT.txt"
)
