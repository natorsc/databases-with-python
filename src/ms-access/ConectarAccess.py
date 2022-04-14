#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, pyodbc e Microsoft Access.


"""

from os.path import dirname, join, abspath

from pyodbc import connect


class ConnectDB:
    """Classe."""
    path = dirname(abspath(__file__))
    access_file = 'exemplo.accdb'

    def __init__(self):
        """Construtor.

        O construtor é executado sempre que a classe é instanciada.
        """
        self.con = connect(
            'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            # Deve ser utilizado o path/caminho absoluto até o arquivo.
            f'DBQ={join(self.path, self.access_file)};'
        )

        # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
        self.cur = self.con.cursor()

        # Remover tabela.
        self.drop_table(table='table_name')

        # Criando a tabela.
        self.create_table()

        # Listando as tabelas existentes.
        self.list_tables()

    def create_table(self):
        """Cria a tabela caso a mesma não exista."""
        # Verificando se a tabela já existe.
        # Isso porque o MSSQL não tem o `CREATE TABLE IF NOT EXISTS`.
        if not self.cur.tables(table='table_name').fetchone():
            query = f'''CREATE TABLE table_name (
                user_id   AUTOINCREMENT PRIMARY KEY,
                name      TEXT,
                age       NUMBER,
                gender    TEXT
                );'''
            try:
                self.cur.execute(query)
            except Exception as e:
                print(f'[x] Falha ao criar tabela [x]: {e}')
            else:
                # Commit para criar a tabela.
                self.con.commit()
                print('\n[!] Tabela criada com sucesso [!]')
        else:
            print('\n[!] Tabela já existe [!]')

    def drop_table(self, table):
        """Remove uma tabela.

        :param table: (str) Nome da tabela que se deseja remover.
        """
        query = f'DROP TABLE {table};'
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao remover a tabela [x]: {e}')
        else:
            # Commit para registrar a operação/transação no banco.
            self.con.commit()
            print('\n[!] Tabela removida com sucesso [!]')

    def reset_table_index(self, table):
        """Reincia o indice da tabela.

        :param table_name: (str) Nome da tabela.
        """
        query = f'ALTER TABLE {table} ALTER COLUMN id COUNTER(1,1);'
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'[x] Falha ao resetar o indice da tabela [x]: {e}')
        else:
            self.con.commit()
            print('\n[!] Indice resetado com sucesso [!]')

    def list_tables(self):
        for table_info in self.cur.tables(tableType='TABLE'):
            print('Tabelas disponíveis:\n', table_info.table_name)

    def insert_row(self, data):
        """Adiciona uma nova linha na tabela.

        :param data: (tuple) Tupla contendo os dados.
        """
        query = '''INSERT INTO table_name
                (name, age, gender) 
                VALUES (?, ?, ?);'''
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
                VALUES (?, ?, ?);'''
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
        """Função consulta o registro pela id.

        :param rowid: (int) id do usuário que se deseja consultar.
        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        query = 'SELECT * FROM table_name WHERE user_id = ?;'
        self.cur.execute(query, rowid)
        return self.cur.fetchone()

    def find_rows(self, limit=10.0):
        """Função consulta todos os registros da tabela.

        Utilizando ``limit`` para evitar consultas longas de mais.

        :param limit: (int) Parâmetro que limita a quantidade de
        registros que serão exibidos.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia ``[]``.
        """
        query = f'SELECT TOP {limit} * FROM table_name;'
        self.cur.execute(query)
        return self.cur.fetchall()

    def change_row(self, rowid, name, age, gender):
        """Método alterar uma linha da tabela com base na id.

        :param rowid: (int) id da linha que se deseja alterar.
        :param name: (str) String com o novo valor.
        :param age: (int) Numero inteiro com o novo valor.
        :param gender: (str) String com o novo valor.
        """
        query = '''UPDATE table_name 
                SET name = ?, age = ?, gender = ? 
                WHERE user_id = ?;'''
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
        """Método remove uma linha da tabela com base na id.

        :param rowid: (id) id da linha que se deseja remover.
        """
        query = 'DELETE FROM table_name WHERE user_id = ?;'
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
    # print('Driver(s) localizado(s):', drivers())
    # Criando a conexão com o banco.
    database = ConnectDB()

    user = ('Felipe', 35.0, 'Masculino')
    # Inserindo um registro tabela.
    database.insert_row(data=user)

    users_list = [
        ('Fernanda', 20.0, 'Feminino'),
        ('João', 50.0, 'Masculino'),
    ]
    # Inserindo vários registros na tabela.
    database.insert_rows(data=users_list)

    users_tuple = (
        ('Augusto', 18.0, 'Masculino'),
        ('Helena', 40.0, 'Feminino'),
    )
    # Inserindo vários registros na tabela.
    database.insert_rows(data=users_tuple)

    # Consultando com filtro.
    print('\n')
    print(database.find_row_by_id(rowid=1.0))

    # Consultando todos.
    print(database.find_rows(limit=5.0))
    print('----')

    # Alterando registro da tabela.
    print('\nANTES da alteração:')
    print(database.find_row_by_id(rowid=1.0))
    database.change_row(rowid=1.0, name='Rafaela', age=50.0, gender='Feminino')
    print('\nDEPOIS da alteração:')
    print(database.find_row_by_id(rowid=1.0))
    print('----')

    # Removendo registro da tabela.
    print('\nANTES da remoção:')
    print(database.find_rows())
    database.remove_row(rowid=2.0)
    print('\nDEPOIS da remoção:')
    print(database.find_rows())
    print('----')

    # # Fechando conexão com o banco.
    database.con.close()
