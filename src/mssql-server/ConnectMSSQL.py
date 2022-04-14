# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, PyODBC e MS SQL Server.

Código testado com:

- Windows Server 2016 + SQL Server 2016.
- Ubuntu server 18.04 + Docker.
"""

# Conector recomendado na documentação oficial.
from pyodbc import connect, drivers


class ConnectDB:
    """Classe."""

    def __init__(self):
        """Construtor.

        O construtor é executado sempre que a classe é instanciada
        (iniciada).
        """
        # self.con é responsável por manter uma conexão
        # aberta com o banco (commit, rollback, close, etc).

        # Windows Server.
        # self.con = connect(
        #     # Driver que será utilizado na conexão
        #     r'DRIVER={ODBC Driver 17 for SQL Server};'
        #     # IP ou nome do servidor + porta.
        #     r'SERVER=tcp:192.168.100.175\sqlexpress,1433;'
        #     # Banco que será utilizado.
        #     r'DATABASE=database_name;'
        #     # Nome de usuário.
        #     r'UID=dbuser;'
        #     # Senha.
        #     r'PWD=Python.123456'
        # )

        # Docker.
        self.con = connect(
            # Driver que será utilizado na conexão
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            # IP ou nome do servidor + porta.
            r'SERVER=tcp:localhost\sqlexpress,1433;'
            # Banco que será utilizado (Criar banco).
            r'DATABASE=tempdb;'
            # Nome de usuário (Usuário default da imagem).
            r'UID=SA;'
            # Senha.
            r'PWD=Python.123456'
        )

        # Criando o cursor que irá executar os
        # comandos SQL (instruções DML, DDL, etc).
        self.cur = self.con.cursor()

        # Remover tabela.
        self.drop_table(table='table_name')

        # Criando a tabela.
        self.create_table()

    def create_table(self):
        """Cria a tabela caso a mesma não exista."""
        # Verificando se a tabela já existe.
        # Isso porque o MSSQL não tem o `CREATE TABLE IF NOT EXISTS`.
        if not self.cur.tables(table='table_name').fetchone():
            query = '''CREATE TABLE table_name (
                    user_id   INT             IDENTITY(1, 1)  NOT NULL,
                    name      VARCHAR(100)    NOT NULL,
                    age       INT             NOT NULL,
                    gender    VARCHAR(10)     NOT NULL,
                    PRIMARY KEY(user_id)
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
        self.cur.execute(query, (rowid,))
        return self.cur.fetchone()

    def find_rows(self, limit=5):
        """Função consulta todos os registros da tabela.

        Utilizando ``limit`` para evitar consultas longas de mais.

        :param limit: (int) Parâmetro que limita a quantidade de
        registros que serão exibidos.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia ``[]``.
        """
        query = 'SELECT TOP (?) * FROM table_name;'
        self.cur.execute(query, (limit,))
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
    print('Driver(s) localizado(s):', drivers())
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
