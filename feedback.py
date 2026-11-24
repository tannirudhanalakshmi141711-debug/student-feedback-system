import sqlite3

def add_feedback():

    name = input("Enter Student Name: ")
    subject = input("Enter Subject: ")
    rating = int(input("Enter Rating (1-5): "))
    comments = input("Enter Comments: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO feedback
        (student_name, subject, rating, comments)
        VALUES (?, ?, ?, ?)
        """,
        (name, subject, rating, comments)
    )

    conn.commit()
    conn.close()

    print("Feedback Submitted Successfully!")

def view_feedback():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback")
    rows = cursor.fetchall()

    print("\n===== FEEDBACK RECORDS =====")

    for row in rows:
        print(row)

    conn.close()
    def delete_feedback():

    feedback_id = int(input("Enter Feedback ID to Delete: "))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM feedback WHERE id=?",
        (feedback_id,)
    )

    conn.commit()
    conn.close()

    print("Feedback Deleted Successfully!")