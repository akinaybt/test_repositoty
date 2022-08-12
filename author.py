import mysql.connector


class Author:

    def __init__(self, cursor_param):
        self.cursor = cursor_param

    def create_table_author(self):
        query = """
        CREATE TABLE IF NOT EXISTS authors (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        surname VARCHAR(100) NOT NULL
        );
        """
        self.cursor.execute(query)
        print('table has been created')

    def add_new_author(self, name, surname):
        query = f"INSERT INTO authors(name, surname)" \
                f"VALUES" \
                f"('{name}', '{surname}');"
        self.cursor.execute(query)

    def get_author_by_id(self, id):
        query = f"SELECT * FROM authors WHERE id = {id};"
        self.cursor.execute(query)
        print(self.cursor.fetchone())

    def get_all_authors(self):
        query = f"SELECT * FROM authors;"
        self.cursor.execute(query)
        print(self.cursor.fetchall())

    def get_author_by_name(self, name):
        query = f"SELECT name FROM authors WHERE name = '{name}';"
        self.cursor.execute(query)
        print(self.cursor.fetchone())



