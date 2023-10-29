class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        if isinstance(book,str):
            parts = book.strip("\n").split(" by ", 1)
            self.books.append(Book(parts[0],parts[1]))
        elif isinstance(book,Book):
            self.books.append(book)
        else: raise ValueError("book Type should be str or Book")
    def get_authors(self):
        authors = list(set(book.author for book in self.books))
        return authors
    def get_books_per_author(self):
        books_per_author = {}
        
        for book in self.books:
            author = book.author
            if author in books_per_author:
                books_per_author[author] += 1
            else:
                books_per_author[author] = 1

        return books_per_author
    def __str__(self):
        sorted_books = sorted(self.books, key=lambda book: book.author)
        book_list = [f"{book.title} by {book.author}" for book in sorted_books]
        return "\n".join(book_list)

