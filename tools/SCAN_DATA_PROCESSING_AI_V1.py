from pathlib import Path
import json
import sqlite3
import importlib.util

root=Path(r"E:\football_v")

report={
    "module":"04_DATA_PROCESSING_AI",
    "version":"V1.0",
    "checks":{}
}


module=root/"04_DATA_PROCESSING_AI"


files=list(module.rglob("*.py"))

report["python_files"]=len(files)


failed=[]


for f in files:

    try:

        spec=importlib.util.spec_from_file_location(
            f.stem,
            f
        )

        if spec:

            module_obj=importlib.util.module_from_spec(spec)

        report["checks"][str(f.relative_to(root))]="PASS"


    except Exception as e:

        failed.append(
            {
                "file":str(f),
                "error":str(e)
            }
        )


report["import_failed"]=failed

report["checks"]["import_check"]=len(failed)==0


db=root/"02_FEATURE_LAYER/database/feature_store.db"


if db.exists():

    conn=sqlite3.connect(db)

    cur=conn.cursor()

    tables=cur.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()

    report["feature_store_tables"]=len(tables)

    report["checks"]["feature_store"]="PASS"

else:

    report["checks"]["feature_store"]="FAIL"


adapter=list(
    (root/"04_DATA_PROCESSING_AI/feature_store/adapters").glob("*.py")
)

report["adapter_files"]=len(adapter)


out=root/"99_DOCUMENTATION/validation/DATA_PROCESSING_AI_V1.0_SCAN.json"


out.write_text(
    json.dumps(
        report,
        indent=4,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


print("SCAN_COMPLETE")

print(json.dumps(report,indent=4))
