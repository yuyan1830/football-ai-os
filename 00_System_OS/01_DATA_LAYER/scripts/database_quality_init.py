import os
import sys
import sqlite3


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from config.database_config import SQLITE_DB





def create_quality_rules(cursor):


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS quality_rules
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,


            rule_name TEXT UNIQUE,


            rule_type TEXT,


            weight REAL DEFAULT 0,


            threshold REAL DEFAULT 0,


            severity TEXT,


            description TEXT,


            created_time TEXT


        )
        """
    )






def create_quality_scores(cursor):


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS quality_scores
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,


            data_id TEXT,


            completeness_score REAL,


            accuracy_score REAL,


            freshness_score REAL,


            source_score REAL,


            total_score REAL,


            quality_level TEXT,


            created_time TEXT


        )
        """
    )






def create_quality_alerts(cursor):


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS quality_alerts
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,


            data_id TEXT,


            rule_name TEXT,


            severity TEXT,


            message TEXT,


            status TEXT DEFAULT 'open',


            created_time TEXT


        )
        """
    )








def init_quality_database():


    print(
        "======================"
    )

    print(
        "Data Quality Database Init"
    )

    print(
        "======================"
    )



    conn = sqlite3.connect(
        SQLITE_DB
    )


    cursor = conn.cursor()



    create_quality_rules(
        cursor
    )


    create_quality_scores(
        cursor
    )


    create_quality_alerts(
        cursor
    )



    conn.commit()


    conn.close()



    print(
        "Quality Rules Table Ready"
    )


    print(
        "Quality Scores Table Ready"
    )


    print(
        "Quality Alerts Table Ready"
    )


    print(
        "Data Quality Database Completed"
    )






if __name__ == "__main__":

    init_quality_database()