# -*- coding: utf-8 -*-
"""CRUD - Python - MySQL Connector - MariaDB."""

from mysql.connector import connect

# Conexão (commit, rollback, close, etc).
con = connect(
    user='dbuser',
    password='123456',
    host='localhost',
    port='3306',
    database='database_name',
)

# config = {
#    'user': 'dbuser',
#    'password': '123456',
#    'host': 'localhost',
#    'port': '3306',
#    'database': 'database_name'
# }
# con = connect(**config)

# Cursor (DML, DDL, etc).
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS table_name;')

table_name = """CREATE TABLE IF NOT EXISTS table_name (
id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name  VARCHAR(32),
age   SMALLINT
);"""
cur.execute(table_name)

# Create.
print('[!] Create [!]')
query = 'INSERT INTO table_name (name, age) VALUES (%s, %s);'
cur.execute(
    query,
    ('renato', 35),
)

# Bulk create.
cur.executemany(
    query,
    (
        ('maria', 25),
        ('sandy', 19),
    ),
)

# Read.
print('\n[!] Read [!]')
cur.execute('SELECT * FROM table_name;')
print(cur.fetchall())

# Limit.
query = 'SELECT * FROM table_name LIMIT %s;'
cur.execute(
    query,
    (3,),
)
print(cur.fetchall())

# Where.
query = 'SELECT * FROM table_name WHERE id = %s;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'SELECT * FROM table_name WHERE age > %s;'
cur.execute(
    query,
    (20,),
)
print(cur.fetchall())

# Update.
print('\n[!] Update [!]')
query = 'SELECT * FROM table_name WHERE id = %s;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'UPDATE table_name SET name = %s WHERE id = %s;'
cur.execute(
    query,
    ('joão', 1),
)

query = 'SELECT * FROM table_name WHERE id = %s;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

# Delete.
print('\n[!] Delete [!]')
query = 'SELECT * FROM table_name WHERE id = %s;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'DELETE FROM table_name WHERE id = %s;'
cur.execute(
    query,
    (1,),
)

query = 'SELECT * FROM table_name WHERE id = %s;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

con.close()
