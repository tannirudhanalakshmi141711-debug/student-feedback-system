import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        subject TEXT,
        rating INTEGER,
        comments TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()