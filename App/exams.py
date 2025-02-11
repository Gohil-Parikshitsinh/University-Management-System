import student

exam_results = {
    "student1": {"CSE101": 85, "CSE102": 90},
    "student2": {"CSE101": 78, "CSE102": 88},
}

def enter_exam_results(faculty_id):
    """Allows faculty to enter exam results"""
    print("\n✏ Enter Exam Results")
    for student_id in student.student_grades.keys():
        for course in student.student_grades[student_id].keys():
            score = input(f"Enter score for {student_id} in {course} (or press Enter to skip): ")
            if score.isdigit():
                exam_results[student_id][course] = int(score)
                print(f"✅ Score updated for {student_id} in {course}.")

def view_exam_results(student_id):
    """Allows students to view their exam results"""
    if student_id in exam_results:
        print("\n📜 Exam Results:")
        for course, score in exam_results[student_id].items():
            print(f"{course}: {score}")
    else:
        print("\n❌ No exam results available.")

def exams_menu(role, username):
    """Exams menu"""
    while True:
        print("\n--- Exams & Grading System ---")
        print("1. Enter Exam Results (Faculty Only)")
        print("2. View Exam Results (Students Only)")
        print("3. Back to Dashboard")

        choice = input("Enter your choice: ")

        if choice == "1" and role == "faculty":
            enter_exam_results(username)
        elif choice == "2" and role == "student":
            view_exam_results(username)
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice or insufficient permissions.")
