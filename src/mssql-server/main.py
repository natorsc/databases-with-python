# -*- coding: utf-8 -*-
'''CRUD - Python - PyODBC - SQL Server.'''

import pyodbc

con = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost;'
    'port=1433;'
    'DATABASE=master;'
    'UID=sa;'
    'PWD=Docker.123456;'
    'TrustServerCertificate=yes'
)
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS table_name;')

table_name = '''IF OBJECT_ID(N'table_name', N'U') IS NULL
CREATE TABLE table_name (
id      INT PRIMARY KEY IDENTITY,
name    VARCHAR(32),
age     SMALLINT
);'''
cur.execute(table_name)

# Create.
print('[!] Create [!]')
query = 'INSERT INTO table_name (name, age) VALUES (?, ?);'
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
query = 'SELECT TOP (?) * FROM table_name;'
cur.execute(
    query,
    (3,),
)
print(cur.fetchall())

# Where.
query = 'SELECT * FROM table_name WHERE id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'SELECT * FROM table_name WHERE age > ?;'
cur.execute(
    query,
    (20,),
)
print(cur.fetchall())

# Update.
print('\n[!] Update [!]')
query = 'SELECT * FROM table_name WHERE id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'UPDATE table_name SET name = ? WHERE id = ?;'
cur.execute(
    query,
    ('joão', 1),
)

query = 'SELECT * FROM table_name WHERE id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

# Delete.
print('\n[!] Delete [!]')
query = 'SELECT * FROM table_name WHERE id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'DELETE FROM table_name WHERE id = ?;'
cur.execute(
    query,
    (1,),
)

query = 'SELECT * FROM table_name WHERE id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

con.close()
