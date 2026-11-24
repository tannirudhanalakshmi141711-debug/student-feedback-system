import streamlit as st
import sqlite3
import matplotlib.pyplot as plt

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Student Feedback Management System",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------
# DATABASE
# ---------------------------------

conn = sqlite3.connect(
    "students.db",
    check_same_thread=False
)

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

# ---------------------------------
# TITLE
# ---------------------------------

st.markdown("""
<h1 style='text-align:center;color:#00BFFF'>
MARWADI UNIVERSITY
</h1>

<h2 style='text-align:center'>
🎓 Student Feedback Management System by dhanalakshmi
</h2>

<h4 style='text-align:center'>
A Smart Feedback Collection and Analytics Platform
</h4>

<hr>
""", unsafe_allow_html=True)
# ---------------------------------
# SIDEBAR
# ---------------------------------

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "🏠 Home",
        "📝 Submit Feedback",
        "📋 View Feedback",
        "🔍 Search Feedback",
        "✏️ Update Feedback",
        "🗑️ Delete Feedback",
        "📊 Dashboard",
        "🔐 Admin Login"
    ]
)

# ---------------------------------
# HOME
# ---------------------------------

if menu == "🏠 Home":

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        use_container_width=True
    )

    st.markdown("""
    # 🎓 Welcome

    ### Student Feedback Management System

    This platform helps students submit feedback
    about subjects and faculty members.

    ### Features

    ✅ Submit Feedback

    ✅ View Feedback Records

    ✅ Search Feedback

    ✅ Update Feedback

    ✅ Delete Feedback

    ✅ Dashboard Analytics

    ✅ Rating Statistics

    ✅ SQLite Database Storage
    """)

    st.info(
        "Project Developed Using Python, Streamlit and SQLite"
    )

    st.markdown("""
    ### 👨‍💻 Developer

    **Name:** Priya

    **Technology Stack:**
    - Python
    - Streamlit
    - SQLite
    - Matplotlib

    ### 🎯 Objective

    To provide an efficient system for collecting,
    managing and analyzing student feedback.
    """)

# ---------------------------------
# SUBMIT
# ---------------------------------

elif menu == "📝 Submit Feedback":

    st.subheader("Submit Feedback")

    name = st.text_input("Student Name")

    subject = st.text_input("Subject")

    rating = st.slider(
        "Rating",
        1,
        5,
        3
    )

    comments = st.text_area("Comments")

    if st.button("Submit Feedback"):

        cursor.execute("""
        INSERT INTO feedback
        (student_name, subject, rating, comments)
        VALUES (?,?,?,?)
        """,
        (
            name,
            subject,
            rating,
            comments
        ))

        conn.commit()

        st.success(
            "Feedback Submitted Successfully"
        )

# ---------------------------------
# VIEW
# ---------------------------------

elif menu == "📋 View Feedback":

    st.subheader("All Feedback Records")

    cursor.execute(
        "SELECT * FROM feedback"
    )

    rows = cursor.fetchall()

    if rows:
        st.table(rows)
    else:
        st.warning(
            "No Feedback Available"
        )

# ---------------------------------
# SEARCH
# ---------------------------------

elif menu == "🔍 Search Feedback":

    st.subheader("Search Feedback")

    student = st.text_input(
        "Enter Student Name"
    )

    if st.button("Search"):

        cursor.execute("""
        SELECT * FROM feedback
        WHERE student_name LIKE ?
        """,
        (
            "%" + student + "%",
        ))

        result = cursor.fetchall()

        if result:
            st.table(result)
        else:
            st.error(
                "No Record Found"
            )

# ---------------------------------
# UPDATE
# ---------------------------------

elif menu == "✏️ Update Feedback":

    st.subheader("Update Feedback")

    feedback_id = st.number_input(
        "Enter Feedback ID",
        min_value=1
    )

    new_comment = st.text_area(
        "New Comment"
    )

    if st.button("Update"):

        cursor.execute("""
        UPDATE feedback
        SET comments=?
        WHERE id=?
        """,
        (
            new_comment,
            feedback_id
        ))

        conn.commit()

        st.success(
            "Feedback Updated Successfully"
        )

# ---------------------------------
# DELETE
# ---------------------------------

elif menu == "🗑️ Delete Feedback":

    st.subheader("Delete Feedback")

    feedback_id = st.number_input(
        "Feedback ID",
        min_value=1,
        key="delete"
    )

    if st.button("Delete Record"):

        cursor.execute("""
        DELETE FROM feedback
        WHERE id=?
        """,
        (
            feedback_id,
        ))

        conn.commit()

        st.success(
            "Record Deleted Successfully"
        )

# ---------------------------------
# DASHBOARD
# ---------------------------------

elif menu == "📊 Dashboard":

    st.subheader(
        "Feedback Analytics"
    )

    cursor.execute(
        "SELECT COUNT(*) FROM feedback"
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT AVG(rating) FROM feedback"
    )

    avg_rating = cursor.fetchone()[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Feedback",
            total
        )

    with col2:
        st.metric(
            "Average Rating",
            round(avg_rating, 2)
            if avg_rating
            else 0
        )

    cursor.execute(
        "SELECT rating FROM feedback"
    )

    ratings = cursor.fetchall()

    if ratings:

        rating_list = [
            row[0]
            for row in ratings
        ]

        fig, ax = plt.subplots()

        ax.hist(
            rating_list,
            bins=5
        )

        ax.set_title(
            "Rating Distribution"
        )

        ax.set_xlabel(
            "Rating"
        )

        ax.set_ylabel(
            "Count"
        )

        st.pyplot(fig)

    # ---------------------------------
# ADMIN LOGIN
# ---------------------------------

elif menu == "🔐 Admin Login":

    st.subheader("Admin Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "1234":

            st.success("✅ Login Successful")

        else:

            st.error("❌ Invalid Username or Password")