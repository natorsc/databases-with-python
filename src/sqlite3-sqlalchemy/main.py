# -*- coding: utf-8 -*-
'''CRUD - SQLAlchemy - SQLite3.'''

import datetime
import pathlib

from sqlalchemy import SmallInteger, String
from sqlalchemy import create_engine, func, insert, select, update, delete
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import sessionmaker, mapped_column


BASE_DIR = pathlib.Path(__file__).resolve().parent

# In-Memory Database.
# engine = sa.create_engine(url='sqlite://')
engine = create_engine(url='sqlite:///:memory:')

# Local file.
# engine = sa.create_engine(url=f'sqlite:///{BASE_DIR.joinpath('db.sqlite3')}')


Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class TableName(Base):
    __tablename__ = 'table_name'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column('name', String(32))
    age: Mapped[int] = mapped_column('age', SmallInteger)
    created_at: Mapped[datetime.datetime]

    def __repr__(self) -> str:
        return f'TableName(id={self.id}, name={self.name}, age={self.age})'


if __name__ == '__main__':
    # Removing all tables from the database.
    Base.metadata.drop_all(engine)

    # Creating all tables.
    Base.metadata.create_all(engine)

    # Creating a session (add, commit, query, etc.).
    session = Session()

    # Create.
    session.execute(
        insert(TableName)
        .values(
            name='felipe',
            age=35,
            created_at=func.now(),
        ),
    )
    # Create and return the object.
    result = session.scalar(
        insert(TableName)
        .values(
            name='josé',
            age=35,
            created_at=func.now(),
        ).returning(TableName),
    )
    if result:
        print(result)

    # Bulk create.
    session.execute(
        statement=insert(TableName).values(created_at=func.now()),
        params=[
            {'name': 'renato', 'age': 40},
            {'name': 'sandy', 'age': 19},
        ],
    )

    result = session.scalars(
        insert(TableName).values(created_at=func.now()).returning(TableName),
        [
            {'name': 'patrick', 'age': 20},
            {'name': 'gisele', 'age': 21},
        ],
    )
    if result:
        print(result.fetchall())

    # # Persisting the data.
    # session.commit()

    # Read.
    print(session.get(TableName, 1))
    result = session.scalars(select(TableName))
    if result:
        print(f'Todos: {result.all()}')
    # records = session.query(TableName).all()
    # for row in records:
    #     print(f'ID: {row.user_id} - Name: {row.name} - Age: {row.age}')
    # print('---\n')
    # https://docs.sqlalchemy.org/en/20/changelog/migration_20.html#migration-orm-usage.
    result = session.scalars(
        select(TableName)
        .where(TableName.age > 40)
    )
    print(result.all())

    # Filter.

    # result = session.query(TableName).filter(TableName.age > 40).all()
    # print(result)
    # # Scalar retorna o objeto.
    # result = session.scalar(sa.select(TableName).where(TableName.age > 40))
    # result = session.scalars(sa.select(TableName).where(TableName.age > 40))
    # print(result)
    # data = result.fetchall()
    # print(data[0].name)
    # # for row in records:
    # #     print(f'ID: {row.user_id} - Nome: {row.name} - Idade: {row.age}')
    # # print('---\n')

    # # # Update.
    # # print('BEFORE the change:')
    # # record = session.query(TableName).filter(TableName.user_id == 1).first()
    # # print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age}')
    # record = session.scalar(sa.select(TableName).where(TableName.id == 1))
    # print(record)

    # # new_data = {'name': 'Rafaela', 'age': 50}
    # # session.query(TableName).filter(TableName.user_id == 1).update(new_data)
    # # session.commit()

    # # print('AFTER the change:')
    # # record = session.query(TableName).filter(TableName.user_id == 1).first()
    # # print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age}')
    # # print('---\n')

    # # # Delete.
    # # print('ANTES da remoção:')
    # # record = session.query(TableName).filter(TableName.user_id == 2).first()
    # # print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - '
    # #       f'Sexo: {record.gender}')

    # # session.query(TableName).filter(TableName.user_id == 2).delete()
    # record = session.scalar(sa.select(TableName).where(TableName.id == 1))
    # session.delete(record)
    # session.commit()
    # record = session.scalar(sa.select(TableName))
    # print(record)

    # print('DEPOIS da remoção:')
    # record = session.query(TableName).filter(TableName.user_id == 2).first()
    # print(record)
    # print('---\n')

    # # Fechando a sessão.
    # session.close()
