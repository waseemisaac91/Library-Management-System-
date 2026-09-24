"""
Library Management System - Entry Point
Login screen, main menu, and program loop.
Waseem Isaac
"""

from library_app.models.book import Book, Novel, Magazine
from library_app.models.user import User
from library_app.models.library import Library

DATA_FILE = "data/library.json"


def login_screen(library):
    """Display login or signup options. Returns logged-in User or None."""
    while True:
        print("\n" + "=" * 45)
        print("📖 Welcome to the Library Management System")
        print("=" * 45)
        print("1. Login")
        print("2. Create a new account")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        # ---------- Login ----------
        if choice == "1":
            name = input("Enter your name: ").strip()
            password = input("Enter your password: ").strip()
            user = library.login(name, password)
            if user:
                print(f"\n✅ Welcome back, {user.name}!")
                return user
            else:
                print("❌ Invalid name or password.")

        # ---------- Create Account ----------
        elif choice == "2":
            name = input("Choose a username: ").strip()
            if library.find_user(name):
                print("❌ That username is already taken.")
                continue
            password = input("Choose a password: ").strip()
            user = User(name, password)
            library.add_user(user)
            library.save(DATA_FILE)
            print(f"✅ Account created! Welcome, {name}!")

        # ---------- Exit ----------
        elif choice == "3":
            return None

        else:
            print("❌ Invalid option. Try again.")


def main_menu(library, user):
    """Display the main menu and handle user actions."""
    while True:
        print("\n" + "=" * 45)
        print(f"📚 Main Menu — Logged in as: {user.name}")
        print("=" * 45)
        print("1. List all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show my borrowed books")
        print("5. Add a new book")
        print("6. Save and exit")

        choice = input("\nChoose an option: ").strip()

        # ---------- 1. List all books ----------
        if choice == "1":
            library.show_all_books()

        # ---------- 2. Borrow a book ----------
        elif choice == "2":
            title = input("Enter the book title to borrow: ").strip()
            book = library.find_book(title)
            if not book:
                print("❌ Book not found.")
            elif book.borrow(user):
                user.borrow_book(book)
                print(f"✅ You borrowed '{book.title}'.")
            else:
                print("❌ Sorry, that book is already borrowed.")

        # ---------- 3. Return a book ----------
        elif choice == "3":
            title = input("Enter the book title to return: ").strip()
            book = library.find_book(title)
            if not book:
                print("❌ Book not found.")
            elif book.return_book():
                user.return_book(book)
                print(f"✅ You returned '{book.title}'.")
            else:
                print("❌ That book wasn't borrowed.")

        # ---------- 4. Show my borrowed books ----------
        elif choice == "4":
            books = user.list_borrowed_books()
            if not books:
                print("📭 You haven't borrowed any books yet.")
            else:
                print("\n📖 Your borrowed books:")
                for b in books:
                    print(f"  - {b}")

        # ---------- 5. Add a new book ----------
        elif choice == "5":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            year = input("Enter publication year: ").strip()
            kind = input("Type (Book/Novel/Magazine): ").strip().lower()

            if kind == "novel":
                genre = input("Enter genre: ").strip()
                book = Novel(title, author, year, genre)
            elif kind == "magazine":
                issue = input("Enter issue: ").strip()
                book = Magazine(title, author, year, issue)
            else:
                book = Book(title, author, year)

            library.add_book(book)

        # ---------- 6. Save and exit ----------
        elif choice == "6":
            library.save(DATA_FILE)
            print("👋 Goodbye!")
            return

        else:
            print("❌ Invalid option. Try again.")


def main():
    """Program entry point."""
    library = Library.load(DATA_FILE)

    # Seed sample books if the library is empty (first run)
    if not library.books:
        library.add_book(Novel("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"))
        library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
        library.add_book(Magazine("National Geographic", "NatGeo", 2023, "Vol. 243"))
        library.save(DATA_FILE)

    # Main program loop
    while True:
        user = login_screen(library)
        if user is None:
            print("👋 Goodbye!")
            break
        main_menu(library, user)


if __name__ == "__main__":
    main()