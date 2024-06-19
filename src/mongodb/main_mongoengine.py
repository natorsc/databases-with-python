# -*- coding: utf-8 -*-
"""CRUD - Python - MongoEngine - MongoDB."""

from mongoengine import Document, IntField, StringField, connect

db = connect(
    username='dbuser',
    password='123456',
    host='localhost',
    port=27017,
    db='database_name',
    authentication_source='admin',
)

# username = 'dbuser'
# password = '123456'
# host = 'localhost'
# port = 27017
# db = 'database_name'
# authentication_source = 'admin'
# URI = f'mongodb://{username}:{password}@{host}:{port}/{db}?authSource={authentication_source}'
# db = connect(host=URI)


class CollectionName(Document):
    name = StringField(max_length=32)
    age = IntField(min_value=0, max_value=150)
    meta = {'collection': 'collection_name'}

    def __str__(self):
        return f'name={self.name}, age={self.age}'


if __name__ == '__main__':
    CollectionName.drop_collection()

    # Create.
    print('[!] Create [!]')
    user = CollectionName(name='renato', age=35).save()
    obj_id = user.id

    # Bulk create.
    CollectionName.objects.insert(
        [
            CollectionName(name='Helena', age=20),
            CollectionName(name='João', age=50),
        ],
    )

    # Read.
    print('\n[!] Read [!]')
    print(CollectionName.objects)
    print(CollectionName.objects(id=obj_id))
    print(CollectionName.objects(age__gt=20))

    # Update.
    print('\n[!] Update [!]')
    print(CollectionName.objects(id=obj_id))
    CollectionName.objects(id=obj_id).update_one(
        name='joão',
    )
    print(CollectionName.objects(id=obj_id))

    # Delete.
    print('\n[!] Delete [!]')
    print(CollectionName.objects(id=obj_id))

    CollectionName.objects(id=obj_id).first().delete()
    print(CollectionName.objects(id=obj_id))

    db.close()
