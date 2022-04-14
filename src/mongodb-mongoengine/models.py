# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, MongoEngine e MongoDB."""

from mongoengine import Document, IntField, StringField, connect

# Conexão.
connect(
    username='dbuser',
    password='123456',
    host='localhost',
    port=27017,
    db='database_name',
    authentication_source='admin',
)


# Conexão utilizando URI.
# username = 'dbuser'
# password = '123456'
# host = 'localhost'
# port = 27017
# db = 'database_name'
# authentication_source = 'admin'
# URI = f'mongodb://{username}:{password}@{host}:{port}/{db}?authSource={authentication_source}'
# connect(host=URI)


class CollectionName(Document):
    """Estrutura o documento.

    Utilizando meta para definir do nome da collection.
    """
    name = StringField(max_length=200)
    age = IntField(min_value=0, max_value=120)
    gender = StringField(max_length=10)
    meta = {
        'collection': 'collection_name'
    }


if __name__ == "__main__":
    # Apagando a collection.
    CollectionName.drop_collection()

    # Inserindo os documentos.
    user = CollectionName(name='Felipe', age=35, gender='Masculino').save()

    users = [
        CollectionName(name='Helena', age=20, gender='Feminino'),
        CollectionName(name='João', age=50, gender='Masculino'),
    ]
    user_id = []
    for doc in users:
        doc.save()
        user_id.append(doc.pk)

    another_user = CollectionName()
    another_user.name = 'Camila'
    another_user.age = 50
    another_user.gender = 'Feminino'
    another_user.save()

    # Consultar todos os documentos.
    data = CollectionName.objects
    for doc in data:
        print(f'ID: {doc.pk} - Nome: {doc.name} - Idade: {doc.age} - Sexo: {doc.gender}')
    print('----\n')

    # Consulta documentos com filtro.
    data = CollectionName.objects(age__gt=40)
    for doc in data:
        print(f'ID: {doc.pk} - Nome: {doc.name} - Idade: {doc.age} - Sexo: {doc.gender}')
    print('----\n')

    # Alterar documento.
    print('ANTES da alteração:')
    data = CollectionName.objects(pk=user.pk)
    for doc in data:
        print(f'ID: {doc.pk} - Nome: {doc.name} - Idade: {doc.age} - Sexo: {doc.gender}')

    CollectionName.objects(pk=user.pk).update_one(name='Eduarda', age=25, gender='Feminino')

    # Utilizando um dicionário.
    # new_data = {'name': 'Rafaela', 'age': 50, 'gender': 'Feminino'}
    # CollectionName.objects(pk=user.pk).update_one(**new_data)
    print('\nDocumento alterado com sucesso\n')

    print('DEPOIS da alteração:')
    data = CollectionName.objects(pk=user.pk)
    for doc in data:
        print(f'ID: {doc.pk} - Nome: {doc.name} - Idade: {doc.age} - Sexo: {doc.gender}')
    print('----\n')

    # Remover documento.
    print('ANTES da remoção:')
    data = CollectionName.objects
    for doc in data:
        print(f'ID: {doc.pk} - Nome: {doc.name} - Idade: {doc.age} - Sexo: {doc.gender}')

    CollectionName.objects(pk=user_id[0]).first().delete()
    print('\nDocumento removido com sucesso\n')

    print('DEPOIS da remoção:')
    data = CollectionName.objects
    for doc in data:
        print(f'ID: {doc.pk} - Nome: {doc.name} - Idade: {doc.age} - Sexo: {doc.gender}')
    print('----\n')
