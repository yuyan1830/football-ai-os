# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime


BASE = r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER\migration_engine"


def run():

    report = {

        "module": "Migration Engine",

        "version": "V1.0",

        "status": "READY",

        "time": str(datetime.now())

    }


    report_path = os.path.join(
        BASE,
        "reports",
        "migration_status.json"
    )


    os.makedirs(
        os.path.dirname(report_path),
        exist_ok=True
    )


    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


    print(
        json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        )
    )


if __name__ == "__main__":

    run()

