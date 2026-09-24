"""
Library Model
Manages books, users, and JSON persistence.
Waseeem Isaac
"""

import json
import os
from library_app.models.book import Book, Novel, Magazine
from library_app.models.user import User


class Library:
    """Represents the library system."""

    def __init__(self, name="Personal Library"):
        self.name = name
        self.books = []  # list of Book objects
        self.users = []  # list of User objects

    # ---------- Book Management ----------
    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"✅ Book '{book.title}' added to the library.")

    def show_all_books(self):
        """Display all books in the library."""
        if not self.books:
            print("📭 No books in the library yet.")
            return
        print(f"\n📚 Books in '{self.name}':")
        print("-" * 50)
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.show_info()}")
            print("-" * 50)

    def find_book(self, title):
        """Find a book by title (case-insensitive)."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    # ---------- User Management ----------
    def add_user(self, user):
        """Add a user to the library."""
        self.users.append(user)

    def find_user(self, name):
        """Find a user by name (case-insensitive)."""
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None

    def login(self, name, password):
        """Authenticate a user. Returns User object if successful, None otherwise."""
        user = self.find_user(name)
        if user and user.password == password:
            return user
        return None

    # ---------- Persistence ----------
    def save(self, filepath):
        """Save all data to a JSON file."""
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)

        data = {
            "name": self.name,
            "books": [book.to_dict() for book in self.books],
            "users": [user.to_dict() for user in self.users],
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"💾 Saved to {filepath}")

    @classmethod
    def load(cls, filepath):
        """Load library data from a JSON file."""
        if not os.path.exists(filepath):
            print(f"⚠️ File '{filepath}' not found. Starting fresh.")
            return cls()

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        library = cls(name=data.get("name", "Personal Library"))

        # Restore books
        for book_data in data.get("books", []):
            book_type = book_data.get("type", "Book")
            if book_type == "Novel":
                book = Novel.from_dict(book_data)
            elif book_type == "Magazine":
                book = Magazine.from_dict(book_data)
            else:
                book = Book.from_dict(book_data)
            library.books.append(book)

        # Restore users
        for user_data in data.get("users", []):
            user = User.from_dict(user_data)
            library.users.append(user)

        print(f"📂 Loaded from {filepath}")
        return library

    def __repr__(self):
        return f"Library({self.name!r}, books={len(self.books)}, users={len(self.users)})"