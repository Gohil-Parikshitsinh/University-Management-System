import user_management
import student
import faculty
import staff
import courses
import attendance
import exams
import finance
import analytics


def student_dashboard():
    """Student Menu"""
    while True:
        print("\n--- Student Dashboard ---")
        print("1. View Grades")
        print("2. View Attendance")
        print("3. View Fee Status")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Displaying Grades...")
        elif choice == "2":
            print("Showing Attendance...")
        elif choice == "3":
            print("Checking Fee Status...")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def faculty_dashboard():
    """Faculty Menu"""
    while True:
        print("\n--- Faculty Dashboard ---")
        print("1. Mark Attendance")
        print("2. Enter Grades")
        print("3. Post Notices")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Marking Attendance...")
        elif choice == "2":
            print("Entering Grades...")
        elif choice == "3":
            print(" Posting Notices...")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def staff_dashboard():
    """Staff Menu"""
    while True:
        print("\n--- Staff Dashboard ---")
        print("1. Manage Students")
        print("2. Handle Fee Payments")
        print("3. Generate Reports")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("👥 Managing Student Records...")
        elif choice == "2":
            print("Handling Fee Payments...")
        elif choice == "3":
            print("Generating Reports...")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    """Main function to start the system"""
    print("\n🎓 Welcome to the University Management System 🎓")

    while True:
        username = input("Enter username: ")
        role = user_management.login(username)

        if role:
            while True:
                print("\n--- Dashboard ---")

                # Show different menus based on role
                if role == "student":
                    print("1. Student Dashboard")
                    print("2. Courses")
                    print("3. Attendance")
                    print("4. Exams & Results")
                    print("5. Finance")
                    print("6. Analytics")
                    print("7. Logout")

                elif role == "faculty":
                    print("1. Faculty Dashboard")
                    print("2. Courses")
                    print("3. Attendance")
                    print("4. Exams & Grading")
                    print("5. Analytics")
                    print("6. Logout")

                elif role == "staff":
                    print("1. Staff Dashboard")
                    print("2. Finance")
                    print("3. Analytics")
                    print("4. Logout")

                choice = input("Enter your choice: ")

                if role == "student":
                    if choice == "1":
                        student.student_menu(username)
                    elif choice == "2":
                        courses.courses_menu(role, username)
                    elif choice == "3":
                        attendance.attendance_menu(role, username)
                    elif choice == "4":
                        exams.exams_menu(role, username)
                    elif choice == "5":
                        finance.finance_menu(role, username)
                    elif choice == "6":
                        analytics.analytics_menu(username)
                    elif choice == "7":
                        break

                elif role == "faculty":
                    if choice == "1":
                        faculty.faculty_menu(username)
                    elif choice == "2":
                        courses.courses_menu(role, username)
                    elif choice == "3":
                        attendance.attendance_menu(role, username)
                    elif choice == "4":
                        exams.exams_menu(role, username)
                    elif choice == "5":
                        analytics.analytics_menu(username)
                    elif choice == "6":
                        break

                elif role == "staff":
                    if choice == "1":
                        staff.staff_menu()
                    elif choice == "2":
                        finance.finance_menu(role, username)
                    elif choice == "3":
                        analytics.analytics_menu("staff")
                    elif choice == "4":
                        break

                else:
                    print("❌ Invalid choice. Please try again.")

        else:
            print("\n❌ Login failed. Please try again.")


if __name__ == "__main__":
    main()

