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
        pass

    # ---------- Book Management ----------
    def add_book(self, book):
        """Add a book to the library."""
        pass

    def show_all_books(self):
        """Display all books in the library."""
        pass

    def find_book(self, title):
        """Find a book by title (case-insensitive)."""
        pass

    # ---------- User Management ----------
    def add_user(self, user):
        """Add a user to the library."""
        pass

    def find_user(self, name):
        """Find a user by name (case-insensitive)."""
        pass

    def login(self, name, password):
        """Authenticate a user. Returns User object if successful, None otherwise."""
        pass

    # ---------- Persistence ----------
    def save(self, filepath):
        """Save all data to a JSON file."""
        pass

    @classmethod
    def load(cls, filepath):
        """Load library data from a JSON file."""
        pass

    def __repr__(self):
        pass