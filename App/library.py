import data
import exceptions
from datetime import datetime, timedelta

FINE_PER_DAY = 10
BORROW_PERIOD = 7

def display_library_menu():
    print("\nLibrary Management")
    print("1. View Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. View Borrowed Books")
    print("5. Back to Main Menu")

def view_available_books():
    available_books = [book_id for book_id, details in data.books.items() if details["available"]]
    if not available_books:
        print("No books available in the library.")
        return

    print("\nAvailable Books:")
    for book_id in available_books:
        details = data.books[book_id]
        print(f"{book_id}: {details['title']} by {details['author']}")

def borrow_book():
    user_id = input("Enter your Student/Staff ID: ").strip()
    if not exceptions.is_valid_user_id(user_id):
        print("Invalid ID! Only students and staff can borrow books.")
        return

    book_id = input("Enter Book ID to borrow: ").strip()
    if not exceptions.is_valid_book_id(book_id):
        print("Invalid Book ID.")
        return

    if not exceptions.is_book_available(book_id):
        print("This book is not available.")
        return

    due_date = datetime.now() + timedelta(days=BORROW_PERIOD)
    data.books[book_id]["available"] = False

    data.borrowed_books.setdefault(user_id, []).append({
        "book_id": book_id,
        "borrow_date": datetime.now().strftime('%Y-%m-%d'),
        "due_date": due_date.strftime('%Y-%m-%d')
    })

    print(f"Book '{data.books[book_id]['title']}' has been borrowed successfully.")
    print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")

def generate_fine_bill(user_id, book_id, due_date, return_date, fine):
    bill_content = f"""
    ===== Library Fine Bill =====
    User ID: {user_id}
    Book ID: {book_id}
    Book Title: {data.books[book_id]['title']}
    Due Date: {due_date}
    Return Date: {return_date}
    Days Overdue: {(datetime.strptime(return_date, '%Y-%m-%d') - datetime.strptime(due_date, '%Y-%m-%d')).days}
    Fine Amount: ₹{fine}
    =============================
    """
    file_name = f"fine_{user_id}_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(file_name, "w") as file:
        file.write(bill_content.strip())
    print(f"Fine bill generated: {file_name}")

def return_book():
    user_id = input("Enter your Student/Staff ID: ").strip()
    if not exceptions.is_valid_user_id(user_id):
        print("Invalid ID.")
        return

    if user_id not in data.borrowed_books or not data.borrowed_books[user_id]:
        print("No borrowed books found for this ID.")
        return

    print("\nBorrowed Books:")
    for record in data.borrowed_books[user_id]:
        book_id = record["book_id"]
        print(f"{book_id}: {data.books[book_id]['title']} (Due Date: {record['due_date']})")

    book_id = input("Enter Book ID to return: ").strip()
    if not exceptions.has_borrowed_book(user_id, book_id):
        print("You did not borrow this book.")
        return

    record_to_return = next(record for record in data.borrowed_books[user_id] if record["book_id"] == book_id)

    due_date = datetime.strptime(record_to_return["due_date"], '%Y-%m-%d')
    return_date = datetime.now().strftime('%Y-%m-%d')
    days_late = (datetime.now() - due_date).days
    fine = max(0, days_late * FINE_PER_DAY)

    data.books[book_id]["available"] = True
    data.borrowed_books[user_id].remove(record_to_return)

    if not data.borrowed_books[user_id]:
        del data.borrowed_books[user_id]

    print(f"Book '{data.books[book_id]['title']}' has been returned successfully.")
    if fine > 0:
        print(f"Late return! You have a fine of ₹{fine}.")
        generate_fine_bill(user_id, book_id, record_to_return['due_date'], return_date, fine)
    else:
        print("Returned on time! No fine.")

def view_borrowed_books():
    user_id = input("Enter your Student/Staff ID: ").strip()
    if not exceptions.is_valid_user_id(user_id):
        print("Invalid ID.")
        return

    if user_id not in data.borrowed_books or not data.borrowed_books[user_id]:
        print("No borrowed books found for this ID.")
        return

    print("\nBorrowed Books:")
    for record in data.borrowed_books[user_id]:
        book_id = record["book_id"]
        due_date = record["due_date"]
        print(f"{book_id}: {data.books[book_id]['title']} (Due Date: {due_date})")

def library_menu():
    while True:
        display_library_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_available_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            view_borrowed_books()
        elif choice == '5':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
