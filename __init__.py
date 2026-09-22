"""
Library Management System - Package Initializer
Exposes all public classes for easy imports.
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

__version__ = "1.0.0"