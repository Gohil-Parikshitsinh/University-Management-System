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
                        StudentManagement().get_faculty_details()
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
    faculty_details = {}
    def manage(self):
        print("Faculty management options...")
        self.get_faculty_details()

    def get_faculty_details(self):
        # Creating a dictionary to store faculty details

        # Personal Information
        print("Enter Personal Information:")
        self.faculty_details["Full Name"] = input("Full Name (as per official records): ")
        self.faculty_details["Date of Birth"] = input("Date of Birth (DD/MM/YYYY): ")
        self.faculty_details["Gender"] = input("Gender (Male/Female/Other): ")
        self.faculty_details["Nationality"] = input("Nationality: ")
        self.faculty_details["Contact Information"] = {
            "Phone Number": input("Phone Number: "),
            "Email Address": input("Email Address: ")
        }
        self.faculty_details["Permanent Address"] = input("Permanent Address: ")
        self.faculty_details["Current Address"] = input("Current Address: ")

        # Educational Qualifications
        print("\nEnter Educational Qualifications:")
        self.faculty_details["Educational Qualifications"] = {
            "Bachelor's Degree": input("Bachelor's Degree: "),
            "Master's Degree": input("Master's Degree: "),
            "PhD": input("PhD (if applicable): "),
            "Other Certifications": input("Other relevant certifications (if any): ")
        }

        # Professional Details
        print("\nEnter Professional Details:")
        self.faculty_details["Position/Designation"] = input("Position/Designation (e.g., Assistant Professor): ")
        self.faculty_details["Department"] = input("Department and field of expertise: ")
        self.faculty_details["Date of Joining"] = input("Date of Joining: ")
        self.faculty_details["Previous Academic Experience"] = input("Previous academic or teaching experience (if any): ")
        self.faculty_details["Publications/Research"] = input(
            "Publications, research work, and contributions (if applicable): ")

        # Employment History
        print("\nEnter Employment History:")
        self.faculty_details["Previous Employment"] = input("Details of previous academic or professional employment: ")
        self.faculty_details["References"] = input("References from previous institutions or employers: ")

        # Government/Institutional Identification
        print("\nEnter Identification Details:")
        self.faculty_details["Identity Proof"] = input("Identity Proof (e.g., Passport, Aadhar card, etc.): ")
        self.faculty_details["Background Check"] = input("Any required background checks or clearances: ")

        # Bank Account Information
        self.faculty_details["Bank Account"] = input("\nEnter Bank Account Information for salary processing: ")

        # Photograph
        self.faculty_details["Photograph"] = input(
            "Recent Passport-Sized Photograph (provide file path or 'Yes' to confirm): ")

        # Research Interests or Teaching Interests
        self.faculty_details["Research/Teaching Interests"] = input("\nResearch/Teaching Interests and Goals: ")

        # Professional Memberships
        self.faculty_details["Professional Memberships"] = input("Professional Memberships (e.g., IEEE, ACM, etc.): ")

        # Medical/Health Certificate
        self.faculty_details["Medical Certificate"] = input(
            "Do you have a medical certificate confirming fitness to work? (Yes/No): ")

    def display_details(self):
        # Display the entered details
        print("\nFaculty Registration Completed. Here are the entered details:")
        for key, value in self.faculty_details.items():
            print(f"{key}: {value}")

        return self.faculty_details

        if __name__ == "__main__":
            details = get_faculty_details()

class ParentManagement:
    def manage(self):
        print("Parent management options...")


class StudentManagement:
    def manage(self):
        print("Student management options...")
        StudentManagement.get_faculty_details()


user_management = UserManagement()
user_management.login()
