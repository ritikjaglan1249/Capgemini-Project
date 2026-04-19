# Library Management System (Single File)

# Common Data (like utils.py)
books = ["MATH", "SCIENCE", "ENGLISH"]
issue_books = []

# Add Book
def add():
    book_name = input("Enter the Book name to add: ").upper()
    
    if book_name in books:
        print("Book already exists")
    else:
        books.append(book_name)
        print(f"Book Added: {book_name}")

# Show Books
def show():
    if len(books) == 0:
        print("No books available")
    else:
        print("\nAvailable Books:")
        for book in books:
            print(book)

# Issue Book
def issue():
    book_name = input("Enter book name: ").upper()
    
    if book_name in books:
        books.remove(book_name)
        issue_books.append(book_name)
        print("Book issued successfully")
    else:
        print("Book not available")

# Return Book
def return_book():
    book_name = input("Enter book name: ").upper()
    
    if book_name in issue_books:
        issue_books.remove(book_name)
        books.append(book_name)
        print("Book returned successfully")
    else:
        print("This book was not issued")

# Main Function
def library():
    while True:
        print("\nLIBRARY MENU")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input")
            continue
        
        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            issue()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid choice")

# Run program
library()