import sqlite3

DB_PATH = "data/football.db"


def audit_database():

    print("==============================")
    print("Football AI Data Audit Engine")
    print("==============================")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    tables = cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table'
    """).fetchall()

    result = []

    for item in tables:

        table = item[0]

        count = cursor.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]

        columns = cursor.execute(
            f"PRAGMA table_info({table})"
        ).fetchall()

        col_names = [c[1] for c in columns]

        if table in [
            "team_form",
            "home_away_rating",
            "fatigue_rating"
        ]:
            risk = "高"
            suggestion = "禁止直接用于历史回测，需要改造成时间序列版本"

        elif table == "elo_history":
            risk = "低"
            suggestion = "可用于时间序列预测"

        elif table in [
            "matches_clean",
            "matches_full"
        ]:
            risk = "低"
            suggestion = "基础历史数据"

        else:
            risk = "待评估"
            suggestion = "需要进一步检查"

        result.append(
            (
                table,
                count,
                ",".join(col_names),
                risk,
                suggestion
            )
        )

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_audit_report(
        table_name TEXT,
        row_count INTEGER,
        columns TEXT,
        risk_level TEXT,
        suggestion TEXT
    )
    """)

    cursor.execute(
        "DELETE FROM data_audit_report"
    )

    cursor.executemany(
        """
        INSERT INTO data_audit_report VALUES
        (?,?,?,?,?)
        """,
        result
    )

    conn.commit()

    print("==============================")
    print("数据检查完成")
    print("==============================")

    for row in result:
        print(
            row[0],
            "|",
            row[1],
            "|风险:",
            row[3]
        )

    conn.close()


if __name__ == "__main__":
    audit_database()
