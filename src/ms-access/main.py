# -*- coding: utf-8 -*-
"""CRUD - pyodbc - Microsoft Access."""

import pathlib

import pyodbc

BASE_DIR = pathlib.Path(__file__).resolve().parent
DB_FILE = BASE_DIR.joinpath('example.accdb')

con = pyodbc.connect(
    'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' f'DBQ={DB_FILE};'
)

# Cursor (DML, DDL, etc).
cur = con.cursor()

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
    ),
)

# Read.
print('\n[!] Read [!]')
cur.execute('SELECT * FROM table_name;')
print(cur.fetchall())

# Where.
query = 'SELECT * FROM table_name WHERE user_id = ?;'
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
query = 'SELECT * FROM table_name WHERE user_id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'UPDATE table_name SET name = ? WHERE user_id = ?;'
cur.execute(
    query,
    ('joão', 1),
)

query = 'SELECT * FROM table_name WHERE user_id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

# Delete.
print('\n[!] Delete [!]')
query = 'SELECT * FROM table_name WHERE user_id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

query = 'DELETE FROM table_name WHERE user_id = ?;'
cur.execute(
    query,
    (1,),
)

query = 'SELECT * FROM table_name WHERE user_id = ?;'
cur.execute(
    query,
    (1,),
)
print(cur.fetchone())

con.close()
