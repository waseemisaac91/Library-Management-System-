"""
Models Package Initializer
Exposes all model classes.
Waseem Isaac
"""

from library_app.models.book import Book, Novel, Magazine
from library_app.models.user import User
from library_app.models.library import Library

__all__ = [
    "Book",
    "Novel",
    "Magazine",
    "User",
    "Library",
]