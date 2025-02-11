import numpy as np
import analytics  # Import analytics for data visualization
import courses  # Import courses for enrollment
import attendance  # Import attendance system
import exams  # Import exams module
import finance  # Import finance module

# Sample student data
student_grades = {
    "student1": {"CSE101": 85, "CSE102": 90},
    "student2": {"CSE101": 75, "CSE102": 80},
}

student_attendance = {
    "student1": np.array([1, 1, 0, 1, 1, 1, 0, 1, 1, 1]),  # 1 = Present, 0 = Absent
    "student2": np.array([1, 0, 1, 1, 1, 0, 1, 1, 1, 1]),
}

student_fees = {
    "student1": {"Total": 50000, "Paid": 30000, "Due": 20000},
    "student2": {"Total": 50000, "Paid": 50000, "Due": 0},
}


def view_grades(username):
    """Displays grades for the logged-in student"""
    if username in student_grades:
        print("\n📚 Your Grades:")
        for subject, grade in student_grades[username].items():
            print(f"{subject}: {grade}")
    else:
        print("\n❌ No grades found for this student.")

def view_attendance(username):
    """Displays attendance percentage for the student"""
    if username in student_attendance:
        attendance_record = student_attendance[username]
        total_classes = len(attendance_record)
        attended_classes = np.sum(attendance_record)
        attendance_percentage = (attended_classes / total_classes) * 100
        print(f"\n📅 Your Attendance: {attendance_percentage:.2f}% ({attended_classes}/{total_classes} classes attended)")
    else:
        print("\n❌ No attendance record found.")

def view_fee_status(username):
    """Displays the fee payment status for the student"""
    if username in student_fees:
        fee_info = student_fees[username]
        print("\n💰 Fee Status:")
        print(f"Total Fee: ₹{fee_info['Total']}")
        print(f"Paid: ₹{fee_info['Paid']}")
        print(f"Due: ₹{fee_info['Due']}")
    else:
        print("\n❌ No fee details found.")

def student_menu(username):
    """Student menu options"""
    while True:
        print("\n--- Student Dashboard ---")
        print("1. View Enrolled Courses")
        print("2. Enroll in a Course")
        print("3. View Attendance")
        print("4. View Exam Results")
        print("5. View & Pay Fees")
        print("6. View Performance Reports 📊")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n📖 Your Enrolled Courses:")
            for code, details in courses.courses.items():
                if username in details["students"]:
                    print(f"{code}: {details['name']} (Instructor: {details['faculty']})")
        elif choice == "2":
            courses.list_courses()
            course_code = input("Enter course code to enroll: ").upper()
            courses.enroll_student(username, course_code)
        elif choice == "3":
            attendance.view_attendance(username)
        elif choice == "4":
            exams.view_exam_results(username)
        elif choice == "5":
            finance.pay_fees(username)
        elif choice == "6":
            analytics.analytics_menu(username)
        elif choice == "7":
            print("🔒 Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")