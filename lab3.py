class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_title, author):
        if book_title not in self.books:
            self.books[book_title] = author
            print(f"Book '{book_title}' added successfully.")
        else:
            print("Book already exists in the library.")

    def display_books(self):
        print("Available books in the library:")
        for book, author in self.books.items():
            print(f"Title: {book}, Author: {author}")
