"""
Book Models
Defines Book (base), Novel, and Magazine classes.
Mohammed
"""


class Book:
    """Base class representing a book in the library."""

    def __init__(self, title, author, publication_year):
        pass

    def show_info(self):
        """Display book details in a readable format."""
        pass

    def borrow(self, user):
        """Borrow the book. Returns True if successful, False otherwise."""
        pass

    def return_book(self):
        """Return the book. Returns True if successful, False otherwise."""
        pass

    def to_dict(self):
        """Convert book to a dictionary for JSON serialization."""
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Book instance from a dictionary."""
        pass

    def __repr__(self):
        pass


class Novel(Book):
    """Novel class - inherits from Book and adds a genre attribute."""

    def __init__(self, title, author, publication_year, genre):
        pass

    def show_info(self):
        """Override to include genre."""
        pass

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        pass

    def __repr__(self):
        pass


class Magazine(Book):
    """Magazine class - inherits from Book and adds an issue attribute."""

    def __init__(self, title, author, publication_year, issue):
        pass

    def show_info(self):
        """Override to include issue."""
        pass

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        pass

    def __repr__(self):
        pass