import student

def pay_fees(student_id):
    """Handles fee payments"""
    if student_id in student.student_fees:
        amount = int(input("Enter amount to pay: "))
        student.student_fees[student_id]["Paid"] += amount
        student.student_fees[student_id]["Due"] -= amount
        print(f"✅ Payment successful. Remaining due: ₹{student.student_fees[student_id]['Due']}")
    else:
        print("\n❌ No fee details found.")

def finance_menu(role, username):
    """Finance menu"""
    while True:
        print("\n--- Finance Management ---")
        print("1. Pay Fees (Students Only)")
        print("2. Back to Dashboard")

        choice = input("Enter your choice: ")

        if choice == "1" and role == "student":
            pay_fees(username)
        elif choice == "2":
            break
        else:
            print("❌ Invalid choice or insufficient permissions.")
