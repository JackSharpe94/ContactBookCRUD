import sqlite3


class DatabaseConnection:

    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def insert(self, contact):

            self.cursor.execute(f'''
            INSERT INTO contacts (ContactID,FirstName,LastName,Telephone)
            VALUES (NULL, '{contact.first_name}', '{contact.last_name}', '{contact.telephone_number}'); 
            ''')
            self.connection.commit()


