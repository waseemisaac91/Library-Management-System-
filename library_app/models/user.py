"""
User Model
Defines the User class for library members.
Dana
"""


class User:
    """Represents a library user."""

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.borrowed_books = []  # list of book title

    def borrow_book(self, book):
        """Add a book to the user's borrowed list."""
        self.borrowed_books.append(book.title)

    def return_book(self, book):
        """Remove a book from the user's borrowed list."""
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            return True
        return False


    def list_borrowed_books(self):
        """Return a list of borrowed book titles."""
        return self.borrowed_books

    def to_dict(self):
        """Convert user to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": self.borrowed_books,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a User instance from a dictionary."""
        user = cls(data["name"], data["password"])
        user.borrowed_books = data.get("borrowed_books", [])
        return user

    def __repr__(self):
        return f"User(name={self.name!r}, borrowed={len(self.borrowed_books)})"