
# user.py
from database import database

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def save(self):
        db = database()
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        params = (self.name, self.library_id)
        db.execute_query(query, params)
        db.close()

    @staticmethod
    def get_all():
        db = database()
        query = "SELECT * FROM users"
        users = db.fetch_all(query)
        db.close()
        return users