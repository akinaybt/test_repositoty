import mysql.connector

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    db='test_db',
    # autocommit = True
)
cursor = DB.cursor()
# cursor.execute('SELECT * FROM user;')
# cursor.execute("SELECT * FROM author;")
# print(cursor.fetchall())
# print(cursor.fetchone())

while True:
    answer_to_exit = input('do you want to exit from programm? \n'
                           'Please enter your answer Yes (y) or No (n)'
                           'Answer: ').lower()
    if answer_to_exit in ['yes', 'y']:
        break
    name = input('Name: ')
    email = input('E-mail:')
    password = input('Password: ')
    query = f" INSERT INTO user (name, email, password)" \
            f"VALUES " \
            f"('{name}', '{email}', '{password}');"
    cursor.execute(query)
    DB.commit()

cursor.execute('SELECT * FROM user;')
print(cursor.fetchall())
