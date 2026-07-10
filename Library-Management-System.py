# Book class represents a single book 
class Book:
    # Initialize book details
    def __init__(self,title,author,available):
        self.title=title
        self.author=author
        self.available=available
    # Display the book information
    def display(self):
        print("Title :", self.title)
        print("Author :",self.author)
        print("Available :",self.available)
# Library class manages all books
class Library:
    # Initialize an empty list of books
    def __init__(self):
        self.books=[]
    # Add a new book to the library
    def add_books(self):
        title=input("Enter the title:")
        author=input("Enter the author name:")
        book=Book(title,author,True)
        self.books.append(book)
        print("Books added successfully")
    # Display all available books
    def view_books(self):
        if len(self.books)==0:
            print("no record found")
        else:
            print("\n All Books")
            for book in self.books:
                book.display()
    # Borrow a book if it is available
    def borrow_book(self):
        search_title=input("Enter the title:")
        for book in self.books:
            if search_title==book.title:
                if book.available:
                    book.available=False
                    print("book is successfully borrowed")
                else:
                    print("Book is already borrowed")
                return
            print("book not found")
    # Return a borrowed book
    def return_books(self):
       return_title=input("enter the title:")
       for book in self.books:
            if return_title==book.title:
                if not book.available:
                    book.available=True
                print("book returned successfully")
            else:
                print("book is already in library")
            return
       print("book not found")
# Create a library object
library=Library()
# Main Menu
while True:
    print("=== Library Mnanagement System ===")
    print("1. Add Books")
    print("2. View Books")
    print("3. Borrow Books")
    print("4. return Books")
    print("5. Exit")
    # Take input from user
    choice=int(input("Enter the choice:"))
    if(choice==1):
        library.add_books()
    elif(choice==2):
        library.view_books()
    elif(choice==3):
        library.borrow_book()
    elif(choice==4):
        library.return_books()
    elif(choice==5):
        print("Good Bye!")
        break
    else:
        print("Invalid Choice")
              
        


