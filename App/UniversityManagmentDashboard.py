users = {
    "admin1": {
        "password": "admin123",
        "acc_type": "Admin"
    },
    "faculty1": {
        "password": "faculty123",
        "acc_type": "Faculty"
    },
    "parent1": {
        "password": "parent123",
        "acc_type": "Parent"
    },
    "student1": {
        "password": "stu123",
        "acc_type": "Student"
    },
}


class UserManagement:
    def login(self):
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        print("Choose the role: ")
        print("1. Admin")
        print("2. Faculty")
        print("3. Parent")
        print("4. Student")

        user_choose = int(input("Enter the Choice: "))
        accountType = ""

        if user_choose == 1:
            accountType = "Admin"
        elif user_choose == 2:
            accountType = "Faculty"
        elif user_choose == 3:
            accountType = "Parent"
        elif user_choose == 4:
            accountType = "Student"
        else:
            print("Invalid Choice")
            return

        if username in users:
            if users[username]["password"] == password:
                if accountType == users[username]["acc_type"]:
                    print(f"Login successful! Welcome {username}, you are logged in as {accountType}.")
                    if accountType == "Admin":
                        AdminManagement().manage()
                    elif accountType == "Faculty":
                        TeacherManagement().manage()
                    elif accountType == "Parent":
                        ParentManagement().manage()
                    elif accountType == "Student":
                        StudentManagement().manage()
                else:
                    print("Incorrect account type selected!")
            else:
                print("Incorrect password!")
        else:
            print("Username not found!")


class AdminManagement:
    def manage(self):
        print("Admin management options...")


class TeacherManagement:
    def manage(self):
        print("Faculty management options...")


class ParentManagement:
    def manage(self):
        print("Parent management options...")


class StudentManagement:
    def manage(self):
        print("Student management options...")


user_management = UserManagement()
user_management.login()
