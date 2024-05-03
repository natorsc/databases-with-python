# -*- coding: utf-8 -*-
'''CRUD - SQLAlchemy - SQLite3.'''

import pathlib

import sqlalchemy as sa

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


BASE_DIR = pathlib.Path(__file__).resolve().parent

# In-Memory Database.
# engine = sa.create_engine(url='sqlite://')
engine = sa.create_engine(url='sqlite:///:memory:')

# Local file.
# engine = sa.create_engine(url=f'sqlite:///{BASE_DIR.joinpath("db.sqlite3")}')


Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class TableName(Base):
    __tablename__ = 'table_name'

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column('name', sa.String(32))
    age: Mapped[int] = mapped_column('age', sa.SmallInteger)

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'TableName(id={self.pk!r}, name={self.name!r}, age={self.age!r})'



if __name__ == '__main__':
    # Removing all tables from the database.
    Base.metadata.drop_all(engine)

    # Creating all tables.
    Base.metadata.create_all(engine)

    # Creating a session (add, commit, query, etc.).
    session = Session()

    # Create.
    user = TableName(name='Felipe', age=35)
    session.add(user)

    users = [
        TableName(name='Helena', age=20),
        TableName(name='João', age=50),
    ]
    # Bulk create.
    session.add_all(users)

    # If a constructor is not used in the class,
    # the data is passed after creating the instance.
    another_user = TableName()
    another_user.name = 'Camila'
    another_user.age = 50
    session.add(another_user)

    # Persisting the data.
    session.commit()

    # Read.
    records = session.query(TableName).all()
    for row in records:
        print(f'ID: {row.user_id} - Name: {row.name} - Age: {row.age}')
    print('---\n')

    # Filter.
    records = session.query(TableName).filter(TableName.age > 40).all()
    for row in records:
        print(f'ID: {row.user_id} - Nome: {row.name} - Idade: {row.age}')
    print('---\n')

    # Update.
    print('BEFORE the change:')
    record = session.query(TableName).filter(TableName.user_id == 1).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age}')

    new_data = {'name': 'Rafaela', 'age': 50}
    session.query(TableName).filter(TableName.user_id == 1).update(new_data)
    session.commit()

    print('AFTER the change:')
    record = session.query(TableName).filter(TableName.user_id == 1).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age}')
    print('---\n')

    # Delete.
    print('ANTES da remoção:')
    record = session.query(TableName).filter(TableName.user_id == 2).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - '
          f'Sexo: {record.gender}')

    session.query(TableName).filter(TableName.user_id == 2).delete()
    session.commit()

    print('DEPOIS da remoção:')
    record = session.query(TableName).filter(TableName.user_id == 2).first()
    print(record)
    print('---\n')

    # Fechando a sessão.
    session.close()
