import mysql.connector
# from user import UserSQL
from author import  Author

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    db='simple_lirary',
    autocommit = True
)
cursor = DB.cursor()

# manager_of_table_user = UserSQL(cursor)
# create_table_user = manager_of_table_user.create_table_user()
# add_user_akinay = manager_of_table_user.add_new_user('Aiganysh', 'aiganysh@mail.com', '888hhh')
# get_user_by_id_1 = manager_of_table_user.get_user_by_id(2)
# delete_user = manager_of_table_user.delete_user_by_id(4)
# users = manager_of_table_user.get_all_users()
# manager_of_table_user.update_user_name(6, 'Aidanochka')
# manager_of_table_user.update_user_email(6, 'aidanochka@email.com')
# manager_of_table_user.update_user_password(7, 'kazieva2706')
new_author = Author(cursor)
# create_table = new_author.create_table_author()
# new_values = new_author.add_new_author("Jane", "Austen")
get_values = new_author.get_all_authors()
