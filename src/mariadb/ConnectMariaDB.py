# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, MySQL Connector e MariaDB."""

from mysql.connector import connect


class ConnectDB:
    """Classe."""

    def __init__(self):
        """Construtor.

        O construtor é executado sempre que a classe é instanciada
        (iniciada).
        """

        # self.con é responsável por manter uma conexão aberta com o
        # banco (commit, rollback, close, etc).
        self.con = connect(
            user='dbuser',
            password='123456',
            host='localhost',
            port='3306',
            database='database_name'
        )

        # Outra forma é passar um dicionário para a conexão.
        # config = {
        #     'user': 'dbuser',
        #     'password': '123456',
        #     'host': 'localhost',
        #     'port': '3306',
        #     'database': 'database_name'
        # }
        # self.con = connect(**config)

        # Criando o cursor que irá executar os
        # comandos SQL (instruções DML, DDL, etc).
        self.cur = self.con.cursor()

        # Remover tabela.
        self.drop_table(table='table_name')

        # Criando a tabela.
        self.create_table()

    def create_table(self):
        """Cria a tabela caso a mesma não exista."""
        query = '''CREATE TABLE IF NOT EXISTS `table_name` (
        `user_id`   INT             NOT NULL AUTO_INCREMENT,
        `name`      VARCHAR(100)    NOT NULL,
        `age`       INT(3)          NOT NULL,
        `gender`    VARCHAR(10)     NOT NULL,
        PRIMARY KEY(user_id)
        );'''
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao criar a tabela [x]: {e}')
        else:
            print('\n[!] Tabela criada com sucesso [!]')

    def drop_table(self, table):
        """Remove uma tabela.

        :param table: (str) Nome da tabela que se deseja remover.
        """
        query = f'DROP TABLE IF EXISTS {table};'
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao remover a tabela [x]: {e}')
        else:
            # Commit para registrar a operação/transação no banco.
            self.con.commit()
            print('\n[!] Tabela removida com sucesso [!]')

    def insert_row(self, data):
        """Adiciona uma nova linha na tabela.

        :param data: (tuple) Tupla contendo os dados.
        """
        query = '''INSERT INTO table_name
        (name, age, gender) 
        VALUES (%s, %s, %s);'''
        try:
            self.cur.execute(query, data)
        except Exception as e:
            # rollback reverte/desfaz a operação.
            self.con.rollback()
            print('\n[x] Falha ao inserir registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]')

    def insert_rows(self, data):
        """Adiciona varias linhas na tabela.

        Desta forma não se faz necessário um laço de repetição com
        vários ``inserts``.

        :param data: (list or tuple) Lista de tuplas contendo os dados
        ou uma tupla de tuplas contendo os dados.
        """
        query = '''INSERT INTO table_name 
        (name, age, gender) 
        VALUES (%s, %s, %s);'''
        try:
            self.cur.executemany(query, data)
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha ao inserir os registros [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registros inseridos com sucesso [!]')

    def find_row_by_id(self, rowid):
        """Consulta registro pela id.

        :param rowid: (int) id do usuário que se deseja consultar.
        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        query = 'SELECT * FROM table_name WHERE user_id = %s;'
        self.cur.execute(query, (rowid,))
        return self.cur.fetchone()

    def find_rows(self, limit=5):
        """Consulta todos os registros da tabela.

        Utilizando ``limit`` para evitar consultas longas de mais.

        :param limit: (int) Parâmetro que limita a quantidade de
        registros que serão exibidos.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Caso não sejam localizados dados é retornada uma lista vazia
        ``[]``.
        """
        query = 'SELECT * FROM table_name LIMIT %s;'
        self.cur.execute(query, (limit,))
        return self.cur.fetchall()

    def change_row(self, rowid, name, age, gender):
        """Alterar uma linha da tabela com base na id.

        :param rowid: (int) id da linha que se deseja alterar.
        :param name: (str) String com o novo valor.
        :param age: (int) Numero inteiro com o novo valor.
        :param gender: (str) String com o novo valor.
        """
        query = '''UPDATE table_name 
        SET name = %s, age = %s, gender = %s 
        WHERE user_id = %s;'''
        try:
            self.cur.execute(query, (name, age, gender, rowid))
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha na alteração do registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]')

    def remove_row(self, rowid):
        """Remove uma linha da tabela com base na id.

        :param rowid: (id) id da linha que se deseja remover.
        """
        query = 'DELETE FROM table_name WHERE user_id = %s;'
        try:
            self.cur.execute(query, (rowid,))
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha ao remover registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]')


if __name__ == '__main__':
    # Criando a conexão com o banco.
    database = ConnectDB()

    user = ('Felipe', 35, 'Masculino')
    # Inserindo um registro tabela.
    database.insert_row(data=user)

    users_list = [
        ('Fernanda', 20, 'Feminino'),
        ('João', 50, 'Masculino'),
    ]
    # Inserindo vários registros na tabela.
    database.insert_rows(data=users_list)

    users_tuple = (
        ('Augusto', 18, 'Masculino'),
        ('Helena', 40, 'Feminino'),
    )
    # Inserindo vários registros na tabela.
    database.insert_rows(data=users_tuple)

    # Consultando com filtro.
    print('\n')
    print(database.find_row_by_id(rowid=1))

    # Consultando todos (limit=10).
    print(database.find_rows(limit=5))
    print('----')

    # Alterando registro da tabela.
    print('\nANTES da alteração:')
    print(database.find_row_by_id(rowid=1))
    database.change_row(rowid=1, name='Rafaela', age=50, gender='Feminino')
    print('\nDEPOIS da alteração:')
    print(database.find_row_by_id(rowid=1))
    print('----')

    # Removendo registro da tabela.
    print('\nANTES da remoção:')
    print(database.find_rows())
    database.remove_row(rowid=2)
    print('\nDEPOIS da remoção:')
    print(database.find_rows())
    print('----')

    # Fechando conexão com o banco.
    database.con.close()
