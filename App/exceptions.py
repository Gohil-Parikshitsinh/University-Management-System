import data
# staff
class InvalidSalaryError(Exception):
    pass

class StaffIDExistsError(Exception):
    pass

class StaffNotFoundError(Exception):
    pass

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Salary must be a positive number.")

def check_staff_id_exists(staff_id, staff_data):
    if staff_id in staff_data:
        raise StaffIDExistsError(f"Staff ID {staff_id} already exists.")

def check_staff_id_not_found(staff_id, staff_data):
    if staff_id not in staff_data:
        raise StaffNotFoundError(f"Staff ID {staff_id} not found.")

# students
class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidCourseError(Exception):
    pass

def validate_name(name):
    if not name.strip():
        raise InvalidNameError("Student name cannot be empty.")
    if any(char.isdigit() for char in name):
        raise InvalidNameError("Student name cannot contain numbers.")

def validate_age(age):
    if not age.isdigit() or int(age) <= 0:
        raise InvalidAgeError("Student age must be a positive integer.")

def validate_course(course):
    if not course.strip():
        raise InvalidCourseError("Course name cannot be empty.")


#library

def is_valid_user_id(user_id):
    return user_id in data.students or user_id in data.staff

def is_valid_book_id(book_id):
    return book_id in data.books

def is_book_available(book_id):
    return data.books.get(book_id, {}).get("available", False)

def is_not_empty(input_str):
    return bool(input_str.strip())

def has_borrowed_book(user_id, book_id):
    return any(record["book_id"] == book_id for record in data.borrowed_books.get(user_id, []))
