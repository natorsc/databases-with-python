# -*- coding: utf-8 -*-
'''Exemplo de CRUD com Python 3 e SQLite3.'''

import sqlite3


con = sqlite3.connect(':memory:')
# con = sqlite3.connect('db.sqlite3')

cur = con.cursor()

# cur.execute('DROP TABLE IF EXISTS ?;', 'table_name')

table_name = '''CREATE TABLE IF NOT EXISTS `table_name` (
`user_id`   INTEGER         NOT NULL,
`name`      VARCHAR(100)    NOT NULL,
`age`       INTEGER(3)      NOT NULL,
PRIMARY KEY(user_id)
);'''
cur.execute(table_name)

insert_user = 'INSERT INTO table_name (name, age) VALUES (?, ?);'

user = ('Felipe', 35)
cur.execute(insert_user, user)

users = (
        ('Augusto', 18),
        ('Helena', 40,),
)
cur.executemany(insert_user, users)

select_user = 'SELECT * FROM table_name WHERE user_id = ?;'
cur.execute(select_user, (1,))
print(cur.fetchone())

cur.execute('SELECT * FROM table_name LIMIT ?;', (3,))
print(cur.fetchall())


update_user = '''UPDATE table_name 
SET name = ?, age = ?
WHERE user_id = ?;'''
cur.execute(update_user, ('New name', 80, 1))

cur.execute('DELETE FROM table_name WHERE user_id = ?;', (3,))
cur.execute('SELECT * FROM table_name')
print(cur.fetchall())


con.close()
