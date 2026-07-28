import os
import sys
import json
from datetime import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from core.db_connection import get_connection


from quality.quality_checker import run_basic_check





# ======================
# Quality Level
# ======================

def calculate_level(score):


    if score >= 90:

        return "A"


    elif score >= 75:

        return "B"


    elif score >= 60:

        return "C"


    else:

        return "D"







# ======================
# Save Quality Score
# ======================

def save_quality_score(

        data_id,

        scores

):


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(

        """

        INSERT INTO quality_scores

        (

        data_id,

        completeness_score,

        accuracy_score,

        freshness_score,

        source_score,

        total_score,

        quality_level,

        created_time

        )


        VALUES

        (?,?,?,?,?,?,?,?)

        """,

        (

            data_id,

            scores["completeness"],

            scores["accuracy"],

            scores["freshness"],

            scores["source"],

            scores["total"],

            scores["level"],

            datetime.now().isoformat()

        )

    )


    conn.commit()

    conn.close()







# ======================
# Alert Aggregation
# ======================

def save_alert(

        data_id,

        alerts

):


    conn = get_connection()

    cursor = conn.cursor()



    if not alerts:


        conn.close()

        return




    #
    # 当前规则聚合
    #

    rule_name = "missing_required_field"


    alert_key = "missing_required_field"



    messages = []


    for alert in alerts:


        messages.append(

            alert["message"]

        )



    details = json.dumps(

        messages,

        ensure_ascii=False

    )



    count = len(messages)



    now = datetime.now().isoformat()



    #
    # 查询已有告警
    #

    cursor.execute(

        """

        SELECT count

        FROM quality_alerts

        WHERE

        data_id=?

        AND rule_name=?

        AND alert_key=?


        """,

        (

            data_id,

            rule_name,

            alert_key

        )

    )


    existing = cursor.fetchone()




    if existing:



        new_count = existing[0] + count



        cursor.execute(

            """

            UPDATE quality_alerts


            SET

            details=?,

            count=?,

            updated_time=?


            WHERE

            data_id=?

            AND rule_name=?

            AND alert_key=?


            """,

            (

                details,

                new_count,

                now,

                data_id,

                rule_name,

                alert_key

            )

        )



    else:



        cursor.execute(

            """

            INSERT INTO quality_alerts

            (

            data_id,

            rule_name,

            severity,

            message,

            status,

            details,

            count,

            alert_key,

            created_time,

            updated_time

            )


            VALUES

            (?,?,?,?,?,?,?,?,?,?)

            """,

            (

                data_id,

                rule_name,

                "high",

                "Required fields missing",

                "open",

                details,

                count,

                alert_key,

                now,

                now

            )

        )



    conn.commit()

    conn.close()







# ======================
# Quality Evaluation
# ======================

def evaluate_data(

        data_id,

        data

):


    alerts = run_basic_check(data)



    #
    # Completeness
    #

    completeness = 100



    if alerts:


        completeness -= (

            len(alerts) * 20

        )


        if completeness < 0:

            completeness = 0




    #
    # 当前阶段占位评分
    #

    accuracy = 100


    freshness = 100


    source = 100




    total = (

        completeness * 0.4

        +

        accuracy * 0.3

        +

        freshness * 0.2

        +

        source * 0.1

    )




    level = calculate_level(total)




    scores = {


        "completeness":

        completeness,


        "accuracy":

        accuracy,


        "freshness":

        freshness,


        "source":

        source,


        "total":

        round(total,2),


        "level":

        level

    }




    save_quality_score(

        data_id,

        scores

    )



    if alerts:


        save_alert(

            data_id,

            alerts

        )




    return {


        "data_id":

        data_id,


        "score":

        scores,


        "alerts":

        alerts

    }