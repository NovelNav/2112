from datetime import datetime, timedelta

class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies
        self.borrowed_by = []

    def available_copies(self):
        return self.copies - len(self.borrowed_by)

    def borrow(self, student):
        if self.available_copies() > 0 and student.can_borrow():
            self.borrowed_by.append(student)
            student.borrowed_books.append(self)
            return True
        return False

    def return_book(self, student):
        if student in self.borrowed_by:
            self.borrowed_by.remove(student)
            student.borrowed_books.remove(self)
            return True
        return False

class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.borrowed_dates = {}

    def can_borrow(self):
        return len(self.borrowed_books) < 10

    def borrow(self, book):
        if book.borrow(self):
            self.borrowed_dates[book.title] = datetime.now()
            return True
        return False

    def renew(self, book):
        if book.title in self.borrowed_dates and book.title in [b.title for b in self.borrowed_books]:
            if (datetime.now() - self.borrowed_dates[book.title]).days <= 30 and book.renewable():
                self.borrowed_dates[book.title] += timedelta(days=30)
                return True
        return False

    def return_book(self, book):
        if book.return_book(self):
            del self.borrowed_dates[book.title]
            return True
        return False

    def get_due_date(self, book):
        if book.title in self.borrowed_dates:
            return self.borrowed_dates[book.title] + timedelta(days=30)
        return None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

def main():
    books = [Book("Book A", 3), Book("Book B", 5), Book("Book C", 2)]
    students = [Student("Student 1"), Student("Student 2")]

    
    student = students[0]
    book = books[0]

    if student.borrow(book):
        print(f"{student} borrowed {book.title}")
        print(f"Due date: {student.get_due_date(book)}")

    if student.renew(book):
        print(f"{student} renewed {book.title}")
        print(f"Due date after renewal: {student.get_due_date(book)}")

    if student.return_book(book):
        print(f"{student} returned {book.title}")

if __name__ == "__main__":
    main()
