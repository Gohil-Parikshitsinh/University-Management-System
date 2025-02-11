# Dictionary storing user credentials and roles
users = {
    "student1": {"password": "pass123", "role": "student"},
    "faculty1": {"password": "teach123", "role": "faculty"},
    "staff1": {"password": "admin123", "role": "staff"},
}


def login(username):
    """Handles user login."""
    if username in users:
        password = input("Enter password: ")
        if password == users[username]["password"]:
            role = users[username]["role"]
            print(f"\n✅ Login successful! Welcome, {username} ({role.capitalize()})")
            return role
        else:
            print("\n❌ Incorrect password. Please try again.")
    else:
        print("\n❌ Username not found. Please try again.")

    return None  # Return None if login fails

# Test the login system (Only for standalone execution)
if __name__ == "__main__":
    user_role = login()
    if user_role:
        print(f"Redirecting to {user_role} dashboard...")
