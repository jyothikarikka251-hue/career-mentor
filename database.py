import sqlite3

def create_db():

    conn = sqlite3.connect(
        "career.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY,

        target_role TEXT,

        skills TEXT,

        ats_score INTEGER
    )
    """)

    conn.commit()

    conn.close()

def save_report(
        role,
        skills,
        ats_score):

    conn = sqlite3.connect(
        "career.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
        target_role,
        skills,
        ats_score
        )
        VALUES (?, ?, ?)
        """,
        (
            role,
            str(skills),
            ats_score
        )
    )

    conn.commit()

    conn.close()