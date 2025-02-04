
# author.py
from database import database

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def save(self):
        db = database()
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        params = (self.name, self.biography)
        db.execute_query(query, params)
        db.close()

    @staticmethod
    def get_all():
        db = database()
        query = "SELECT * FROM authors"
        authors = db.fetch_all(query)
        db.close()
        return authors