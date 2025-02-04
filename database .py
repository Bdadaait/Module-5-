
# database.py
import mysql.connector

class database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="library_management"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()