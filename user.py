import mysql.connector


class UserSQL:

    def __init__(self, cursor_param):
        self.cursor = cursor_param

    def create_table_user(self):
        query = """
        CREATE TABLE IF NOT EXISTS user (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
        );
        """
        self.cursor.execute(query)

    def add_new_user(self, name, email, password):
        query = f"INSERT INTO user(name, email, password)" \
                f"VALUES" \
                f"('{name}', '{email}', '{password}');"
        self.cursor.execute(query)

    def get_user_by_id(self, id):
        query = f"SELECT * FROM user WHERE id = {id};"
        self.cursor.execute(query)
        print(self.cursor.fetchone())

    def get_all_users(self):
        query = f"SELECT * FROM user;"
        self.cursor.execute(query)
        print(self.cursor.fetchall())

    def delete_user_by_id(self, id):
        query = f"DELETE FROM user WHERE id = {id};"
        self.cursor.execute(query)
        print(f" User with id: {id} has been deleted!")

    def update_user_name(self, id, new_value):
        query = f"UPDATE user SET name = '{new_value}' WHERE id = {id}"
        self.cursor.execute(query)
        print(f" User name with id: {id} has been updated!")

    def update_user_email(self, id, new_value):
        query = f"UPDATE user SET email = '{new_value}' WHERE id = {id}"
        self.cursor.execute(query)
        print(f" User email with id: {id} has been updated!")

    def update_user_password(self, id, new_value):
        query = f"UPDATE user SET password = '{new_value}' WHERE id = {id}"
        self.cursor.execute(query)
        print(f" User password with id: {id} has been updated!")


