import attendance  # Import attendance module
import courses  # Import courses module
import exams  # Import exams module
import analytics  # Import analytics for faculty insights
# Faculty-specific data
faculty_courses = {
    "faculty1": ["Math", "Science"],
    "faculty2": ["History", "English"],
}

notices = []  # List to store posted notices


def mark_attendance():
    """Allows faculty to mark attendance for students"""
    print("\n📅 Mark Attendance")

    for student_id, attendance in student.student_attendance.items():
        print(f"\nStudent: {student_id} (Previous Attendance: {attendance.tolist()})")
        new_attendance = input("Enter attendance for today's class (1 for Present, 0 for Absent): ")

        if new_attendance in ["0", "1"]:
            student.student_attendance[student_id] = np.append(attendance, int(new_attendance))
            print(f"✅ Attendance updated for {student_id}.")
        else:
            print("❌ Invalid input. Attendance not updated.")


def enter_grades():
    """Allows faculty to enter grades for students"""
    print("\n✏ Enter Grades")

    for student_id, grades in student.student_grades.items():
        print(f"\nStudent: {student_id} (Current Grades: {grades})")
        for subject in grades.keys():
            new_grade = input(f"Enter new grade for {subject} (or press Enter to skip): ")
            if new_grade.isdigit():
                student.student_grades[student_id][subject] = int(new_grade)
                print(f"✅ Grade updated for {student_id} in {subject}.")

    print("✅ Grades updated successfully.")


def post_notice():
    """Allows faculty to post announcements"""
    print("\n📢 Post a Notice")
    notice_text = input("Enter the notice: ")
    if notice_text.strip():
        notices.append(notice_text)
        print("✅ Notice posted successfully.")
    else:
        print("❌ Notice cannot be empty.")



def faculty_menu(username):
    """Faculty menu options"""
    while True:
        print("\n--- Faculty Dashboard ---")
        print("1. View Assigned Courses")
        print("2. Mark Attendance")
        print("3. Enter Exam Results")
        print("4. Post Notices")
        print("5. View Student Analytics 📊")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            courses.faculty_courses(username)
        elif choice == "2":
            attendance.mark_attendance(username)
        elif choice == "3":
            exams.enter_exam_results(username)
        elif choice == "4":
            post_notice()
        elif choice == "5":
            analytics.analytics_menu(username)
        elif choice == "6":
            print("🔒 Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

