# -*- coding: utf-8 -*-
'''CRUD - Python - Redis.'''

import redis

con = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
)

# Remove keys.
if con.keys():
    for key in con.keys():
        con.delete(key)

# Create.
print('[!] Create [!]')
con.set('number', 0)

con.hset(
    'user:1',
    mapping={
        'name': 'renato',
        'age': 40
    },
)
con.hset(
    'user:2',
    mapping={
        'name': 'joão',
        'age': 20
    },
)

# Read.
print('\n[!] Read [!]')
print(con.keys())
print(con.get('number'))
print(con.hgetall('user:1'))

# Update.
print('\n[!] Update [!]')
print(con.hgetall('user:1'))
con.hset(
    'user:1',
    mapping={
        'name': 'rafael',
    },
)
print(con.hgetall('user:1'))

print(con.get('number'))
con.incr('number')
print(con.get('number'))

# Delete.
print('\n[!] Delete [!]')
print(con.keys())
con.delete('user:2')
print(con.keys())
