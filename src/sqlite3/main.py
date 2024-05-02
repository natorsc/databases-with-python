# -*- coding: utf-8 -*-
'''CRUD - SQLite3.'''

import pathlib
import sqlite3

BASE_DIR = pathlib.Path(__file__).resolve().parent

# Conexão (commit, rollback, close, etc).
con = sqlite3.connect(':memory:')
# con = sqlite3.connect(BASE_DIR.joinpath('db.sqlite3'))

# Cursor (DML, DDL, etc).
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS table_name;')

table_name = '''CREATE TABLE IF NOT EXISTS `table_name` (
`user_id`   INTEGER     NOT NULL, AUTO_INCREMENT,
`name`      VARCHAR(32) NOT NULL,
`age`       INTEGER(3)  NOT NULL,
PRIMARY KEY(user_id)
);'''
cur.execute(table_name)

# Create.
insert_user = 'INSERT INTO table_name (name, age) VALUES (?, ?);'

user = ('Felipe', 35)
cur.execute(insert_user, user)

users = (
    ('Augusto', 18),
    ('Helena', 40),
)
cur.executemany(insert_user, users)

# Read.
select_user = 'SELECT * FROM table_name WHERE user_id = ?;'
cur.execute(select_user, (1,))
print(cur.fetchone())

cur.execute('SELECT * FROM table_name LIMIT ?;', (10,))
print(cur.fetchall())

# Update.
update_user = '''UPDATE table_name
SET name = ?, age = ?
WHERE user_id = ?;'''
cur.execute(update_user, ('New name', 80, 1))

# Delete.
cur.execute('DELETE FROM table_name WHERE user_id = ?;', (3,))
cur.execute('SELECT * FROM table_name;')
print(cur.fetchall())

con.close()
