# -*- coding: utf-8 -*-
"""CRUD - PyODBC - MS SQL Server.

tcp:192.168.100.175\sqlexpress,1433;
 user_id   INT             IDENTITY(1, 1)  NOT NULL,
"""

import pyodbc

con = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\sqldeveloper,1433;'
    'DATABASE=;'
    'UID=sa;'
    'PWD=Docker.123456'
)
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS table_name;')

table_name = '''CREATE TABLE IF NOT EXISTS table_name (
id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name  VARCHAR(32),
age   SMALLINT
);'''
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
    )
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
