import student

def mark_attendance(faculty_id):
    """Marks student attendance"""
    print("\n📅 Mark Attendance")
    for student_id in student.student_attendance.keys():
        status = input(f"Mark attendance for {student_id} (1 for Present, 0 for Absent): ")
        if status in ["0", "1"]:
            student.student_attendance[student_id] = student.student_attendance[student_id].tolist()
            student.student_attendance[student_id].append(int(status))
            print(f"✅ Attendance updated for {student_id}.")
        else:
            print("❌ Invalid input.")

def view_attendance(student_id):
    """Displays attendance for a student"""
    if student_id in student.student_attendance:
        attendance = student.student_attendance[student_id]
        print(f"\n📅 Attendance for {student_id}: {attendance}")
    else:
        print("\n❌ No attendance record found.")

def attendance_menu(role, username):
    """Attendance menu"""
    while True:
        print("\n--- Attendance System ---")
        print("1. Mark Attendance (Faculty Only)")
        print("2. View Attendance (Students Only)")
        print("3. Back to Dashboard")

        choice = input("Enter your choice: ")

        if choice == "1" and role == "faculty":
            mark_attendance(username)
        elif choice == "2" and role == "student":
            view_attendance(username)
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice or insufficient permissions.")
