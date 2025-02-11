# Course Management System

courses = {
    "CSE101": {"name": "Data Structures", "faculty": "faculty1", "students": []},
    "CSE102": {"name": "Algorithms", "faculty": "faculty2", "students": []},
}

def list_courses():
    """Lists available courses"""
    print("\n📚 Available Courses:")
    for code, details in courses.items():
        print(f"{code}: {details['name']} (Instructor: {details['faculty']})")

def enroll_student(student_id, course_code):
    """Enrolls a student in a course"""
    if course_code in courses:
        if student_id not in courses[course_code]["students"]:
            courses[course_code]["students"].append(student_id)
            print(f"✅ {student_id} enrolled in {course_code}.")
        else:
            print(f"❌ {student_id} is already enrolled in {course_code}.")
    else:
        print("❌ Invalid course code.")

def faculty_courses(faculty_id):
    """Shows courses assigned to a faculty"""
    print(f"\n📖 Courses taught by {faculty_id}:")
    for code, details in courses.items():
        if details["faculty"] == faculty_id:
            print(f"{code}: {details['name']}")

def courses_menu(role, username):
    """Course management menu"""
    while True:
        print("\n--- Course Management ---")
        print("1. List Courses")
        print("2. Enroll in a Course (Students Only)")
        print("3. View Assigned Courses (Faculty Only)")
        print("4. Back to Dashboard")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_courses()
        elif choice == "2" and role == "student":
            course_code = input("Enter course code to enroll: ").upper()
            enroll_student(username, course_code)
        elif choice == "3" and role == "faculty":
            faculty_courses(username)
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice or insufficient permissions.")
