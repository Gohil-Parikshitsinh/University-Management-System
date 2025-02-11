import matplotlib.pyplot as plt
import numpy as np
import student
import exams
import finance
import courses

def plot_student_performance(username):
    """Generates a bar chart of student grades"""
    if username in exams.exam_results:
        subjects = list(exams.exam_results[username].keys())
        grades = list(exams.exam_results[username].values())

        plt.figure(figsize=(8, 5))
        plt.bar(subjects, grades, color="blue")
        plt.xlabel("Subjects")
        plt.ylabel("Grades")
        plt.title(f"📊 {username}'s Performance Report")
        plt.ylim(0, 100)
        plt.show()
    else:
        print("\n❌ No grades available.")

def plot_attendance_distribution(username):
    """Generates a pie chart of student attendance"""
    if username in student.student_attendance:
        attendance_record = student.student_attendance[username]
        present_days = np.sum(attendance_record)
        absent_days = len(attendance_record) - present_days

        labels = ["Present", "Absent"]
        sizes = [present_days, absent_days]
        colors = ["green", "red"]

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
        plt.title(f"📅 {username}'s Attendance Distribution")
        plt.show()
    else:
        print("\n❌ No attendance data available.")

def plot_fee_collection():
    """Generates a line graph of fee payments across students"""
    students = list(finance.student_fees.keys())
    paid_fees = [finance.student_fees[stu]["Paid"] for stu in students]
    due_fees = [finance.student_fees[stu]["Due"] for stu in students]

    plt.figure(figsize=(8, 5))
    plt.plot(students, paid_fees, marker="o", label="Paid Fees", color="green")
    plt.plot(students, due_fees, marker="s", label="Due Fees", color="red")
    plt.xlabel("Students")
    plt.ylabel("Amount (₹)")
    plt.title("💰 Fee Collection Report")
    plt.legend()
    plt.show()

def plot_exam_distribution():
    """Generates a histogram of exam scores"""
    all_scores = []
    for student_id in exams.exam_results:
        all_scores.extend(exams.exam_results[student_id].values())

    plt.figure(figsize=(8, 5))
    plt.hist(all_scores, bins=5, color="purple", edgecolor="black")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.title("📊 Exam Score Distribution")
    plt.show()

def plot_course_enrollment():
    """Generates a bar chart for student enrollments in courses"""
    course_codes = list(courses.courses.keys())
    student_counts = [len(courses.courses[code]["students"]) for code in course_codes]

    plt.figure(figsize=(8, 5))
    plt.bar(course_codes, student_counts, color="orange")
    plt.xlabel("Courses")
    plt.ylabel("Number of Students")
    plt.title("📖 Course Enrollment Report")
    plt.show()

def analytics_menu(username):
    """Analytics menu for visualization options"""
    while True:
        print("\n--- Analytics Dashboard ---")
        print("1. View Performance Report")
        print("2. View Attendance Trends")
        print("3. View Fee Collection (For Staff)")
        print("4. View Exam Score Distribution")
        print("5. View Course Enrollment Report")
        print("6. Back to Dashboard")

        choice = input("Enter your choice: ")

        if choice == "1":
            plot_student_performance(username)
        elif choice == "2":
            plot_attendance_distribution(username)
        elif choice == "3":
            if username.startswith("staff"):
                plot_fee_collection()
            else:
                print("❌ Only staff can access fee collection data.")
        elif choice == "4":
            plot_exam_distribution()
        elif choice == "5":
            plot_course_enrollment()
        elif choice == "6":
            print("🔙 Returning to Dashboard...")
            break
        else:
            print("❌ Invalid choice. Please try again.")
