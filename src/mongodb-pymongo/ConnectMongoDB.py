# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, pymongo e MongoDB."""

from bson.objectid import ObjectId
from pymongo import MongoClient, ReturnDocument


class ConnectDB:
    """Classe."""

    def __init__(self):
        """Construtor.

        O construtor é executado sempre que a classe é instanciada
        (iniciada).
        """
        # Conexão em outro host.
        # self.client = MongoClient(
        #     username='dbuser',
        #     password='123456',
        #     host='localhost',
        #     port=27017,
        #     authSource='admin',
        # )

        # Conexão utilizando URI.
        username = 'dbuser'
        password = '123456'
        host = 'localhost'
        port = '27017'
        db = 'database_name'
        authSource = 'admin'
        URI = f'mongodb://{username}:{password}@{host}:{port}/{db}?authSource={authSource}'
        self.client = MongoClient(host=URI)

        # Acessando o banco.
        db = self.client['database_name']

        # Removendo a collection.
        db.drop_collection('collection_name')

        # Criando a collection.
        self.collection = db['collection_name']

    def insert_document(self, data):
        """Adiciona um novo documento na collection.

        :param data: (dict) Dicionário contendo os dados.
        :return: O ObjectId do documento que foi criado.
        """
        try:
            doc = self.collection.insert_one(data)
        except Exception as e:
            print(f'\n[x] Falha ao inserir documento [x]: {e}')
        else:
            print('\n[!] Documento inserido com sucesso [!]')
            return doc.inserted_id

    def insert_documents(self, many_data):
        """Adiciona varios documentos na collection.

        :param many_data: (list) Lista de dicionarios (dict) ou tupla
        (tuple) de dicionarios (dict) contendo os dados que serão
        inseridos.
        :return: Retornada uma lista com os ObjectId dos documentos que
        foram criados.
        """
        try:
            docs = self.collection.insert_many(many_data)
        except Exception as e:
            print(f'\n[x] Falha ao inserir os documentos [x]: {e}')
        else:
            print('\n[!] Documentos inseridos com sucesso [!]')
            return docs.inserted_ids

    def find_document_by_id(self, doc_id):
        """Consulta documento pelo ObjectId.

        :param doc_id: (str) ObjectId do usuário que se deseja consultar.
        :return: É retornado um dicionário (dict) com os dados.
        Caso o documento não seja localizado é retornado ``None``.
        """
        return self.collection.find_one({'_id': ObjectId(doc_id)})

    def find_documents(self, limit=5):
        """Consulta todos os documentos da collection.

        Utilizando ``limit`` para evitar consultas longas.

        :param limit: (int) Numero de documentos que se deseja localizar.
        :return: É retornada uma lista (list) de dicionários (dict)
        contendo os dados.
        """
        return self.collection.find().limit(limit)

    def change_record(self, doc_id, name, age, gender):
        """Altera um documento com base no ObjectId.

        :param doc_id: (str) ObjectId da linha que se deseja alterar.
        :param name: (str) String com o novo nome.
        :param age: (int) Numero inteiro com a nova idade.
        :param gender: (str) String com o novo genero.
        """
        try:
            self.collection.find_one_and_update(
                {'_id': ObjectId(doc_id)},
                {'$set': {'name': name, 'age': age, 'gender': gender}},
                return_document=ReturnDocument.AFTER,
            )
        except Exception as e:
            print(f'\n[x] Falha na alteração do documento [x]: {e}')
        else:
            print('\n[!] Documento alterado com sucesso [!]')

    def remove_document(self, doc_id):
        """Remove um documento com base no ObjectId.

        :param doc_id: (str) ObjectId do documento que se deseja remover.
        """
        try:
            self.collection.delete_one(
                {'_id': ObjectId(doc_id)}
            )
        except Exception as e:
            print('\n[x] Falha ao remover documento [x]: {e}')
        else:
            print('\n[!] documento removido com sucesso [!]')


if __name__ == '__main__':
    # Criando a conexão com o banco.
    database = ConnectDB()

    user = {'name': 'Felipe', 'age': 35, 'gender': 'Masculino'}
    # Inserindo documento.
    pk_doc = database.insert_document(data=user)

    users_list = [
        {'name': 'Fernanda', 'age': 20, 'gender': 'Feminino'},
        {'name': 'João', 'age': 50, 'gender': 'Masculino'},
    ]
    # Inserindo vários registros na tabela.
    pk_docs = database.insert_documents(many_data=users_list)

    users_tuple = (
        {'name': 'Augusto', 'age': 18, 'gender': 'Masculino'},
        {'name': 'Helena', 'age': 40, 'gender': 'Feminino'},
    )
    # Inserindo vários registros na tabela.
    database.insert_documents(many_data=users_tuple)

    # Consultar documento pelo ObjectId.
    print('\nConsulta pelo ObjectId:')
    print(database.find_document_by_id(doc_id=pk_doc))

    # Consultar documentos.
    print('\nConsulta com limit:')
    for doc in database.find_documents():
        print(doc)
    print('----')

    # Alterando registro da tabela.
    print('\nANTES da alteração:')
    print(database.find_document_by_id(doc_id=pk_doc))

    database.change_record(doc_id=pk_doc, name='Rafaela', age=50,
                           gender='Feminino')

    print('\nDEPOIS da alteração:')
    print(database.find_document_by_id(doc_id=pk_doc))
    print('----')

    # Removendo registro da tabela.
    print('\nANTES da remoção:')
    for doc in database.find_documents():
        print(doc)

    database.remove_document(doc_id=pk_docs[0])

    print('\nDEPOIS da remoção:')
    for doc in database.find_documents():
        print(doc)
    print('----')

    # Fechando conexão com o banco.
    database.client.close()
