"""
Book Models
Defines Book (base), Novel, and Magazine classes.
Mohammed
"""


class Book:
    """Base class representing a book in the library."""

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self. publication_year = publication_year
        self.is_borrowed = False
        self.borrowed_by = None

    def show_info(self):
        """Display book details in a readable format."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        if self.is_borrowed:
            print(f"Status: Borrowed by {self.borrowed_by}")
        else:
            print("Status: Available")

    def borrow(self, user):
        """Borrow the book. Returns True if successful, False otherwise."""
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user
            return True

        return False

    def return_book(self):
        """Return the book. Returns True if successful, False otherwise."""
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrowed_by = None
            return True

        return False

    def to_dict(self):
        """Convert book to a dictionary for JSON serialization."""
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Book instance from a dictionary."""
        return cls(
            data["title"],
            data["author"],
            data["publication_year"]
        )

        book.is_borrowed = data.get("is_borrowed", False)
        book.borrowed_by = data.get("borrowed_by", None)


    def __repr__(self):
        return (
            f"Book(title={self.title!r}, "
            f"author={self.author!r}, "
            f"publication_year={self.publication_year!r})")


class Novel(Book):
    """Novel class - inherits from Book and adds a genre attribute."""

    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre


    def show_info(self):
        """Override to include genre."""
        super().show_info()
        print(f"Genre: {self.genre}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Novel"
        data["genre"] = self.genre
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["publication_year"],
            data["genre"]
        )

        novel.is_borrowed = data.get("is_borrowed", False)
        novel.borrowed_by = data.get("borrowed_by", None)


    def __repr__(self):
        return (
            f"Novel(title={self.title!r}, "
            f"author={self.author!r}, "
            f"publication_year={self.publication_year!r}, "
            f"genre={self.genre!r})"
        )



class Magazine(Book):
    """Magazine class - inherits from Book and adds an issue attribute."""

    def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue

    def show_info(self):
        """Override to include issue."""
        super().show_info()
        print(f"Issue: {self.issue}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Magazine"
        data["issue"] = self.issue
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["publication_year"],
            data["issue"]
        )

        magazine.is_borrowed = data.get("is_borrowed", False)
        magazine.borrowed_by = data.get("borrowed_by", None)


    def __repr__(self):
        return (
            f"Magazine(title={self.title!r}, "
            f"author={self.author!r}, "
            f"publication_year={self.publication_year!r}, "
            f"issue={self.issue!r})"
        )