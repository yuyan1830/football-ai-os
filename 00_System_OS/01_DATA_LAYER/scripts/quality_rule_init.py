import os
import sys
from datetime import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from core.db_connection import get_connection





QUALITY_RULES = [

    {

        "rule_name":
        "missing_required_field",

        "rule_type":
        "completeness",

        "weight":
        40,

        "threshold":
        0,

        "severity":
        "high",

        "description":
        "Required field cannot be empty"

    },


    {

        "rule_name":
        "duplicate_hash",

        "rule_type":
        "duplicate",

        "weight":
        20,

        "threshold":
        1,

        "severity":
        "medium",

        "description":
        "Duplicate data detected by hash"

    },


    {

        "rule_name":
        "data_delay",

        "rule_type":
        "freshness",

        "weight":
        20,

        "threshold":
        300,

        "severity":
        "medium",

        "description":
        "Data update delay exceeds threshold"

    },


    {

        "rule_name":
        "source_failure_rate",

        "rule_type":
        "source",

        "weight":
        10,

        "threshold":
        0.2,

        "severity":
        "high",

        "description":
        "Source reliability below standard"

    },


    {

        "rule_name":
        "odds_abnormal_change",

        "rule_type":
        "market",

        "weight":
        10,

        "threshold":
        0.3,

        "severity":
        "high",

        "description":
        "Abnormal odds movement detected"

    }

]







def init_quality_rules():


    print(
        "======================"
    )

    print(
        "Quality Rule Init"
    )

    print(
        "======================"
    )


    conn = get_connection()

    cursor = conn.cursor()



    for rule in QUALITY_RULES:


        cursor.execute(

            """

            INSERT OR REPLACE INTO quality_rules

            (

                rule_name,

                rule_type,

                weight,

                threshold,

                severity,

                description,

                created_time

            )


            VALUES

            (?,?,?,?,?,?,?)

            """,

            (

                rule["rule_name"],

                rule["rule_type"],

                rule["weight"],

                rule["threshold"],

                rule["severity"],

                rule["description"],

                datetime.now().isoformat()

            )

        )



        print(
            "Registered:",
            rule["rule_name"]
        )



    conn.commit()

    conn.close()



    print()

    print(
        "Quality Rules Ready"
    )







if __name__ == "__main__":

    init_quality_rules()