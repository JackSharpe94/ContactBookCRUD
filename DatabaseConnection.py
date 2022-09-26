import sqlite3


class DatabaseConnection:

    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def insert(self, query, table_name):

            print(query)
            self.cursor.execute(f'''
            INSERT INTO {table_name}
            VALUES {query} 
            ''')
            self.connection.commit()

    def delete_record(self, query, table_name):
        self.cursor.execute(f'''
        DELETE FROM {table_name}
        WHERE {query}
        ''')
