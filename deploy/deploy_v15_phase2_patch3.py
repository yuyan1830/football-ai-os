from pathlib import Path


ROOT = Path(r"E:\football_v\10_AI_AUTONOMOUS_ENGINE\tests")


mapping = {
    "autonomous_engine_hil_v1": "autonomous_engine_v3",
    "autonomous_engine_v1": "autonomous_engine_v3",
    "autonomous_engine_v2": "autonomous_engine_v3",
}


count = 0


for file in ROOT.glob("*.py"):

    text = file.read_text(encoding="utf-8")

    old = text

    for k, v in mapping.items():
        text = text.replace(
            f"from {k} import",
            f"from {v} import"
        )

        text = text.replace(
            f"import {k}",
            f"import {v}"
        )

    if text != old:
        file.write_text(text, encoding="utf-8")
        print("[PATCH]", file)
        count += 1


print("")
print("==============================")
print("Football AI OS V1.5 Phase2 Patch3 Complete")
print("Modified:", count)
print("==============================")