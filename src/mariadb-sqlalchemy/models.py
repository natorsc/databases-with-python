# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, SQLAlchemy, MySQL Connector e MariaDB."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Parametros da conexão.
dialect = 'mysql+mysqlconnector'
user = 'dbuser'
pwd = '123456'
server = 'localhost'
port = '3306'
db = 'database_name'

# Conexão. Para debug utilizar echo=True
engine = create_engine(f'{dialect}://{user}:{pwd}@{server}:{port}/{db}')

# Criando uma classe "Session" já configurada.
# Session é instanciado posteriormente para interação com a tabela.
Session = sessionmaker(bind=engine)

Base = declarative_base()


class TableName(Base):
    """Classe representa uma tabela do banco"""
    # ``__tablename__`` - Define o nome da tabela.
    # Se o nome da tabela não for definido é utilizado o nome da classe.
    __tablename__ = 'table_name'

    # Colunas da tabela.
    user_id = Column('user_id', Integer, primary_key=True)
    name = Column('name', String(32))
    age = Column('age', Integer)
    gender = Column('gender', String(10))

    def __init__(self, name=None, age=None, gender=None):
        """Construtor.

        Utilizando o construtor para passar os valores
        no momento em que a classe é instanciada.

        :param nome: (str) String com o valor que será salvo.
        :param idade: (int) Numero inteiro com o valor que será salvo.
        :param sexo: (str) String com o valor que será salvo.
        """
        self.name = name
        self.age = age
        self.gender = gender


if __name__ == "__main__":
    # Removendo todas as tabelas do banco.
    Base.metadata.drop_all(engine)

    # Criando todas as tabelas.
    Base.metadata.create_all(engine)

    # Criando uma sessão (add, commit, query, etc).
    session = Session()

    # Criando os dados que serão inseridos na tabela.
    # Classe com o construtor.
    user = TableName(name='Felipe', age=35, gender='Masculino')
    # Inserindo registro na tabela.
    session.add(user)

    users = [
        TableName(name='Helena', age=20, gender='Feminino'),
        TableName(name='João', age=50, gender='Masculino'),
    ]
    # Inserindo vários registros na tabela.
    session.add_all(users)

    # Caso não seja utilizado um construtor na classe
    # os dados são passados depois de se criar a instancia.
    another_user = TableName()
    another_user.name = 'Camila'
    another_user.age = 50
    another_user.gender = 'Feminino'
    session.add(another_user)

    # Persistindo os dados.
    session.commit()

    # Consultar todos os registros.
    records = session.query(TableName).all()
    for row in records:
        print(f'ID: {row.user_id} - Nome: {row.name} - Idade: {row.age} - Sexo: {row.gender}')
    print('---\n')

    # Consulta com filtro.
    records = session.query(TableName).filter(TableName.age > 40).all()
    for row in records:
        print(f'ID: {row.user_id} - Nome: {row.name} - Idade: {row.age} - Sexo: {row.gender}')
    print('---\n')

    # Alterar registro.
    print('ANTES da alteração:')
    record = session.query(TableName).filter(TableName.user_id == 1).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - Sexo: {record.gender}')

    new_data = {'name': 'Rafaela', 'age': 50, 'gender': 'Feminino'}
    session.query(TableName).filter(TableName.user_id == 1).update(new_data)
    session.commit()

    print('DEPOIS da alteração:')
    record = session.query(TableName).filter(TableName.user_id == 1).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - Sexo: {record.gender}')
    print('---\n')

    # Remover um registro da tabela.
    print('ANTES da remoção:')
    record = session.query(TableName).filter(TableName.user_id == 2).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - Sexo: {record.gender}')

    session.query(TableName).filter(TableName.user_id == 2).delete()
    session.commit()

    print('DEPOIS da remoção:')
    record = session.query(TableName).filter(TableName.user_id == 2).first()
    print(record)
    print('---\n')

    # Fechando a sessão.
    session.close()
