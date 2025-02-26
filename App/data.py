from datetime import datetime
staff = {
    "S001": {"name": "John Doe", "role": "Teacher", "salary": 50000},
    "S002": {"name": "Jane Smith", "role": "Accountant", "salary": 45000},
}

students = {
    "ST001": {"name": "Parikshitsinh Gohil", "age": 20, "course": "Computer Science"},
    "ST002": {"name": "Dhariya Gandhi", "age": 22, "course": "Mathematics"},
    "ST003": {"name": "Dishant Mali", "age": 19, "course": "Physics"},
    "ST004": {"name": "Pranav Thakar", "age": 21, "course": "English Literature"},
    "ST005": {"name": "Vinay Dhamsaniya", "age": 23, "course": "History"}
}

books = {
    "B001": {"title": "Python Programming", "author": "John Doe", "available": True},
    "B002": {"title": "Data Science with Python", "author": "Jane Smith", "available": True},
    "B003": {"title": "Machine Learning Basics", "author": "Andrew Ng", "available": True},
    "B004": {"title": "History of Mathematics", "author": "David Johnson", "available": True},
    "B005": {"title": "Artificial Intelligence", "author": "Elon Gates", "available": True}
}

# Example borrowed_books structure
# "ST001": [{"book_id": "B001", "borrow_date": "2025-02-25", "due_date": "2025-03-03"}]
borrowed_books = {}

