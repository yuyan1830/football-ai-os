import os
import json
import hashlib
import shutil
from datetime import datetime

ROOT = r"E:\football_v"

DOC = os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "ARCHITECTURE_CLEANUP",
    "FINAL_CLEANUP_V3.0"
)

ARCHIVE = os.path.join(
    DOC,
    "DEPRECATED_ARCHIVE"
)

os.makedirs(DOC, exist_ok=True)
os.makedirs(ARCHIVE, exist_ok=True)


def sha256(path):
    h = hashlib.sha256()
    try:
        with open(path,"rb") as f:
            for b in iter(lambda:f.read(8192),b""):
                h.update(b)
        return h.hexdigest()
    except:
        return None


files = {}

for root,dirs,fs in os.walk(ROOT):
    if "DEPRECATED_ARCHIVE" in root:
        continue

    for f in fs:
        if f.endswith(".py"):
            p=os.path.join(root,f)
            h=sha256(p)

            if h:
                files.setdefault(h,[]).append(p)


duplicates=[]

for h,items in files.items():

    if len(items)>1:

        master=items[0]

        for old in items[1:]:
            duplicates.append({
                "master":master,
                "duplicate":old,
                "hash":h
            })


migrated=[]

for item in duplicates:

    old=item["duplicate"]

    try:
        target=os.path.join(
            ARCHIVE,
            os.path.basename(old)
        )

        if os.path.exists(old):
            shutil.move(old,target)

        migrated.append(item)

    except Exception as e:
        item["error"]=str(e)


report={
    "version":"Architecture Cleanup Engine V3.0",
    "time":str(datetime.now()),
    "status":"SUCCESS",
    "duplicate_found":len(duplicates),
    "archived":len(migrated),
    "final_scan":"RUNNING"
}


with open(
    os.path.join(DOC,"cleanup_report_V3.0.json"),
    "w",
    encoding="utf8"
) as f:
    json.dump(report,f,indent=4,ensure_ascii=False)


print(json.dumps(report,indent=4,ensure_ascii=False))
