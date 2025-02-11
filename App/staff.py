import student  # Import student data for management
import courses  # Import courses module
import attendance  # Import attendance module
import exams  # Import exams module
import finance  # Import finance module
import analytics  # Import analytics for reports


def add_student():
    """Allows staff to add a new student"""
    student_id = input("\nEnter new student ID: ")
    if student_id in student.student_grades:
        print("❌ Student ID already exists.")
        return

    student_name = input("Enter student name: ")
    subjects = input("Enter subjects (comma separated): ").split(",")

    # Initialize student records
    student.student_grades[student_id] = {sub.strip(): 0 for sub in subjects}
    student.student_attendance[student_id] = []
    student.student_fees[student_id] = {"Total": 50000, "Paid": 0, "Due": 50000}

    print(f"✅ Student '{student_name}' added successfully!")


def remove_student():
    """Allows staff to remove a student"""
    student_id = input("\nEnter student ID to remove: ")
    if student_id in student.student_grades:
        del student.student_grades[student_id]
        del student.student_attendance[student_id]
        del student.student_fees[student_id]
        print(f"✅ Student {student_id} removed successfully.")
    else:
        print("❌ Student not found.")


def update_fee_payment():
    """Allows staff to update fee payments"""
    student_id = input("\nEnter student ID: ")
    if student_id in student.student_fees:
        amount = int(input("Enter amount paid: "))
        student.student_fees[student_id]["Paid"] += amount
        student.student_fees[student_id]["Due"] -= amount
        print(f"✅ Fee payment updated for {student_id}. Remaining Due: ₹{student.student_fees[student_id]['Due']}")
    else:
        print("❌ Student not found.")


def generate_reports():
    """Generates student reports (grades & attendance summary)"""
    print("\n📊 Generating Reports...")

    for student_id in student.student_grades:
        grades = student.student_grades[student_id]
        avg_grade = sum(grades.values()) / len(grades) if grades else 0

        attendance = student.student_attendance[student_id]
        attendance_percentage = (np.sum(attendance) / len(attendance)) * 100 if len(attendance) > 0 else 0

        print(f"\n📝 Student: {student_id}")
        print(f"📚 Average Grade: {avg_grade:.2f}")
        print(f"📅 Attendance: {attendance_percentage:.2f}%")
        print("────────────────────────────")


def staff_menu():
    """Staff menu options"""
    while True:
        print("\n--- Staff Dashboard ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Fee Payment")
        print("4. Manage Course Enrollments")
        print("5. View Attendance Reports")
        print("6. Generate Student Performance Reports")
        print("7. View University Analytics 📊")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_fee_payment()
        elif choice == "4":
            courses.list_courses()
        elif choice == "5":
            print("\n📅 Attendance Reports:")
            for student_id in student.student_attendance:
                attendance.view_attendance(student_id)
        elif choice == "6":
            print("\n📜 Student Performance Reports:")
            for student_id in exams.exam_results:
                exams.view_exam_results(student_id)
        elif choice == "7":
            analytics.analytics_menu("staff")
        elif choice == "8":
            print("🔒 Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")
