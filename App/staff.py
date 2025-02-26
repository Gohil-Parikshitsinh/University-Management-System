import data
import exceptions

def display_staff_menu():
    print("\nStaff Management")
    print("1. Add Staff")
    print("2. View All Staff")
    print("3. Update Staff")
    print("4. Remove Staff")
    print("5. Back to Main Menu")


def generate_staff_id():
    if not data.staff:
        return "S001"

    # Extract the numeric part, find the highest, and increment by 1
    existing_ids = [int(staff_id[1:]) for staff_id in data.staff.keys()]
    new_id = max(existing_ids) + 1
    return f"S{str(new_id).zfill(3)}"


def add_staff():
    staff_id = generate_staff_id()
    print(f"Generated Staff ID: {staff_id}")

    name = input("Enter Staff Name: ")
    role = input("Enter Staff Role: ")

    try:
        salary = float(input("Enter Staff Salary: "))
        exceptions.validate_salary(salary)

        exceptions.check_staff_id_exists(staff_id, data.staff)

        data.staff[staff_id] = {"name": name, "role": role, "salary": salary}
        print(f"Staff {name} added successfully with ID {staff_id}.")

    except exceptions.StaffIDExistsError as e:
        print(e)
    except exceptions.InvalidSalaryError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a numeric value for salary.")


def view_staff():
    if not data.staff:
        print("No staff records found.")
        return
    print("\nStaff List:")
    for staff_id, details in data.staff.items():
        print(f"{staff_id}: {details['name']} - {details['role']} - ${details['salary']}")


def update_staff():
    staff_id = input("Enter Staff ID to update: ")
    if staff_id not in data.staff:
        print("Staff ID not found!")
        return

    print(f"Updating record for {data.staff[staff_id]['name']}")
    name = input("Enter new name (or press Enter to keep current): ") or data.staff[staff_id]['name']
    role = input("Enter new role (or press Enter to keep current): ") or data.staff[staff_id]['role']
    try:
        salary = input("Enter new salary (or press Enter to keep current): ")
        salary = float(salary) if salary else data.staff[staff_id]['salary']
        data.staff[staff_id] = {"name": name, "role": role, "salary": salary}
        print("Staff record updated successfully.")
    except ValueError:
        print("Invalid salary input.")


def remove_staff():
    staff_id = input("Enter Staff ID to remove: ")
    if staff_id in data.staff:
        del data.staff[staff_id]
        print("Staff removed successfully.")
    else:
        print("Staff ID not found.")


def staff_menu():
    while True:
        display_staff_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_staff()
        elif choice == '2':
            view_staff()
        elif choice == '3':
            update_staff()
        elif choice == '4':
            remove_staff()
        elif choice == '5':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
