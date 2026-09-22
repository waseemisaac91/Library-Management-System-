"""
User Model
Defines the User class for library members.
Dana
"""


class User:
    """Represents a library user."""

    def __init__(self, name, password):
        pass

    def borrow_book(self, book):
        """Add a book to the user's borrowed list."""
        pass

    def return_book(self, book):
        """Remove a book from the user's borrowed list."""
        pass

    def list_borrowed_books(self):
        """Return a list of borrowed book titles."""
        pass

    def to_dict(self):
        """Convert user to a dictionary for JSON serialization."""
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a User instance from a dictionary."""
        pass

    def __repr__(self):
        pass