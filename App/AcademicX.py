import staff
import student
import library

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            staff.staff_menu()
        elif choice == '2':
            library.library_menu()
        elif choice == '3':
            student.student_menu()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    print("\n-----------------------------------------------------")
    print("\nAcademicX: Academic Institute Management System")
    print("1. Staff Management")
    print("2. Library Management")
    print("3. Student Management")
    print("4. Exit")


if __name__ == "__main__":
    main()
