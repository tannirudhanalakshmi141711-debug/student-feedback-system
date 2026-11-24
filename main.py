from database import create_database
from feedback import add_feedback
from admin import admin_login

create_database()

while True:

    print("\n===== STUDENT FEEDBACK MANAGEMENT SYSTEM =====")
    print("1. Submit Feedback")
    print("2. Admin Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_feedback()

    elif choice == "2":
        admin_login()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")