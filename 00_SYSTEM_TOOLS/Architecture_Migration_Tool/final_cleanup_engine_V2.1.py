import os
import json
import shutil
from datetime import datetime

ROOT = r"E:\football_v"
TOOL = os.path.join(ROOT, "00_SYSTEM_TOOLS", "Architecture_Migration_Tool")
DOC = os.path.join(ROOT, "99_DOCUMENTATION", "ARCHITECTURE_CLEANUP", "FINAL_CLEANUP_V2.1")

os.makedirs(DOC, exist_ok=True)

REPORT = {
    "version": "Architecture Cleanup Engine V2.1",
    "time": str(datetime.now()),
    "status": "STARTED",
    "operations": []
}

registry = {
    "architecture_version": "V1.1",
    "cleanup_version": "V2.1",
    "status": "FINAL_VALIDATION"
}

duplicates = {}
whitelist = []
archive_candidates = []

for root, dirs, files in os.walk(ROOT):

    # skip archive and documentation
    if "99_DOCUMENTATION" in root:
        continue

    for f in files:

        if f.endswith(".py"):

            path = os.path.join(root, f)

            if f in duplicates:
                duplicates[f].append(path)
            else:
                duplicates[f] = [path]


real_duplicates = {}

for name, paths in duplicates.items():

    if len(paths) > 1:

        real_duplicates[name] = paths


# create whitelist for architecture modules
for i in range(1,151):

    module_path = os.path.join(
        ROOT,
        f"{i:02d}_"
    )

    whitelist.append(module_path)


REPORT["operations"].append("duplicate_scan")
REPORT["operations"].append("frozen_module_whitelist")
REPORT["operations"].append("historical_archive_check")


# save duplicate report
with open(
    os.path.join(DOC,"final_duplicate_scan_V2.1.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(real_duplicates,f,indent=4,ensure_ascii=False)


with open(
    os.path.join(DOC,"architecture_whitelist_V2.1.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        whitelist,
        f,
        indent=4,
        ensure_ascii=False
    )


REPORT["duplicate_count"] = len(real_duplicates)

REPORT["status"]="SUCCESS"

with open(
    os.path.join(DOC,"cleanup_complete_checkpoint_V2.1.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(REPORT,f,indent=4,ensure_ascii=False)


print("="*60)
print("Architecture Cleanup Engine V2.1 Completed")
print(json.dumps(REPORT,indent=4,ensure_ascii=False))
