class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("Available Books:", self.books)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("You borrowed:", book)
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print("You returned:", book)


# Main Program
lib = Library(["Python", "Java", "C++", "Data Structures"])
lib.display_books()

b_book = input("Enter book name to borrow: ")
lib.borrow_book(b_book)
lib.display_books()

r_book = input("Enter book name to return: ")
lib.return_book(r_book)
lib.display_books()