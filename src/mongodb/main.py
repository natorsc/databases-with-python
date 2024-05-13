# -*- coding: utf-8 -*-
'''CRUD - Python - PyMongo - MongoDB.'''

from bson import ObjectId
from pymongo import MongoClient, ReturnDocument

client = MongoClient(
    username='dbuser',
    password='123456',
    host='localhost',
    port=27017,
    authSource='admin',
)

# Conexão utilizando URI.
# username = 'dbuser'
# password = '123456'
# host = 'localhost'
# port = '27017'
# db = 'database_name'
# authSource = 'admin'
# URI = f'mongodb://{username}:{password}@{host}:{port}/{db}?authSource={authSource}'
# client = MongoClient(host=URI)

db = client['database_name']

# Remove collection.
db.drop_collection('collection_name')

# Create collection.
collection = db['collection_name']

# Create.
print('[!] Create [!]')
result = collection.insert_one(
    {
        'name': 'renato',
        'age': 35,
    },
)
obj_id = result.inserted_id
print(obj_id)

result = collection.insert_many(
    [
        {'name': 'maria', 'age': 25},
        {'name': 'sandy', 'age': 19},

    ],
)
print(result.inserted_ids)

# Read.
print('\n[!] Read [!]')
print(collection.find_one({'_id': ObjectId(obj_id)}))

# Limit.
for document in collection.find().limit(3):
    print(document)

# Update.
print('\n[!] Update [!]')
print(collection.find_one({'_id': ObjectId(obj_id)}))
result = collection.find_one_and_update(
    {'_id': ObjectId(obj_id)},
    {'$set': {'name': 'joão'}},
    return_document=ReturnDocument.AFTER,
)
print(collection.find_one({'_id': ObjectId(obj_id)}))

# Delete.
print('\n[!] Delete [!]')
print(collection.find_one({'_id': ObjectId(obj_id)}))
result = collection.delete_one(
    {'_id': ObjectId(obj_id)},
)
print(collection.find_one({'_id': ObjectId(obj_id)}))

client.close()
