import data
import exceptions


def generate_student_id():
    if not data.students:
        return "ST001"

    existing_ids = [int(student_id[2:]) for student_id in data.students.keys()]
    new_id = max(existing_ids) + 1
    return f"ST{str(new_id).zfill(3)}"


def display_student_menu():
    print("\nStudent Management")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Remove Student")
    print("5. Back to Main Menu")


def add_student():
    student_id = generate_student_id()
    print(f"Generated Student ID: {student_id}")

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Enrolled Course: ")

    try:
        exceptions.validate_name(name)
        exceptions.validate_age(age)
        exceptions.validate_course(course)

        data.students[student_id] = {"name": name, "age": int(age), "course": course}
        print(f"Student {name} added successfully with ID {student_id}.")

    except (exceptions.InvalidNameError, exceptions.InvalidAgeError, exceptions.InvalidCourseError) as e:
        print(e)


def view_students():
    if not data.students:
        print("No student records found.")
        return
    print("\nStudent List:")
    for student_id, details in data.students.items():
        print(f"{student_id}: {details['name']} - Age: {details['age']} - Course: {details['course']}")


def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id not in data.students:
        print("Student ID not found!")
        return

    name = input("Enter new name (or press Enter to keep current): ") or data.students[student_id]['name']
    age = input("Enter new age (or press Enter to keep current): ") or data.students[student_id]['age']
    course = input("Enter new course (or press Enter to keep current): ") or data.students[student_id]['course']

    try:
        exceptions.validate_name(name)
        exceptions.validate_age(age)
        exceptions.validate_course(course)

        data.students[student_id] = {"name": name, "age": int(age), "course": course}
        print("Student record updated successfully.")

    except (exceptions.InvalidNameError, exceptions.InvalidAgeError, exceptions.InvalidCourseError) as e:
        print(e)


def remove_student():
    student_id = input("Enter Student ID to remove: ")
    if student_id in data.students:
        del data.students[student_id]
        print("Student removed successfully.")
    else:
        print("Student ID not found.")


def student_menu():
    while True:
        display_student_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
