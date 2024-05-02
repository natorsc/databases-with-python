# -*- coding: utf-8 -*-
"""CRUD - MySQL Connector - MariaDB."""

from mysql.connector import connect

con = connect(
    user='dbuser',
    password='123456',
    host='localhost',
    port='3306',
    database='database_name'
)

# config = {
#     'user': 'dbuser',
#             'password': '123456',
#             'host': 'localhost',
#             'port': '3306',
#             'database': 'database_name'
# }
# con = connect(**config)

# Cursor (DML, DDL, etc).
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS table_name;')

table_name = '''CREATE TABLE IF NOT EXISTS `table_name` (
`user_id`   INT         NOT NULL AUTO_INCREMENT,
`name`      VARCHAR(32) NOT NULL,
`age`       INT(3)      NOT NULL,
PRIMARY KEY(user_id)
);'''

cur.execute(table_name)

# Create.
insert_user = 'INSERT INTO table_name (name, age) VALUES (%s, %s);'

user = ('Felipe', 35)
cur.execute(insert_user, user)

users = (
    ('Augusto', 18),
    ('Helena', 40,),
)
cur.executemany(insert_user, users)

# Read.
select_user = 'SELECT * FROM table_name WHERE user_id = %s;'
cur.execute(select_user, (1,))
print(cur.fetchone())

cur.execute('SELECT * FROM table_name LIMIT %s;', (10,))
print(cur.fetchall())

# Update.
update_user = '''UPDATE table_name
SET name = %s, age = %s
WHERE user_id = %s;'''
cur.execute(update_user, ('New name', 80, 1))

# Delete.
cur.execute('DELETE FROM table_name WHERE user_id = %s;', (3,))
cur.execute('SELECT * FROM table_name;')
print(cur.fetchall())

con.close()
