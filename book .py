
# book.py
from database import database

class Book:
    def __init__(self, title, author_id, isbn, publication_date, availability=True):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability

    def save(self):
        db = database()
        query = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
        params = (self.title, self.author_id, self.isbn, self.publication_date, self.availability)
        db.execute_query(query, params)
        db.close()

    @staticmethod
    def get_all():
        db = database()
        query = "SELECT * FROM books"
        books = db.fetch_all(query)
        db.close()
        return books

    @staticmethod
    def search_by_title(title):
        db = database()
        query = "SELECT * FROM books WHERE title = %s"
        book = db.fetch_one(query, (title,))
        db.close()
        return book