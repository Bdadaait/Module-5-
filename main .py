
# main.py
from book import uook
from user import User
from author import author

def display_main_menu():
    print("\nWelcome to the Library Management System with Database Integration!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            isbn = input("Enter ISBN: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            new_book = book(title, author_id, isbn, publication_date)
            new_book.save()
            print("Book added successfully!")

        elif choice == "2":
            # Implement borrow book logic
            pass

        elif choice == "3":
            # Implement return book logic
            pass

        elif choice == "4":
            title = input("Enter the title of the book to search: ")
            book = book.search_by_title(title)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == "5":
            books = book.get_all()
            for book in books:
                print(book)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            book_operations()
        elif choice == "2":
            # Implement user operations
            pass
        elif choice == "3":
            # Implement author operations
            pass
        elif choice == "4":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()