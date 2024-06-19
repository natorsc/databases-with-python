# -*- coding: utf-8 -*-
"""CRUD - SQLAlchemy - SQLite3."""

import pathlib

from sqlalchemy import (
    SmallInteger,
    String,
    create_engine,
    delete,
    insert,
    select,
    update,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

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
    print('[!] Create [!]')
    session.execute(
        insert(TableName).values(
            name='renato',
            age=35,
        ),
    )

    # Returning the object that will be created.
    result = session.scalar(
        insert(TableName)
        .values(
            name='josé',
            age=29,
        )
        .returning(TableName),
    )
    session.commit()
    print(result)

    # Bulk create.
    session.execute(
        insert(TableName),
        [
            {'name': 'maria', 'age': 25},
            {'name': 'sandy', 'age': 19},
        ],
    )

    result = session.scalars(
        insert(TableName).returning(TableName),
        [
            {'name': 'patrick', 'age': 33},
            {'name': 'gisele', 'age': 21},
        ],
    )
    session.commit()
    print(result.all())

    # Read.
    print('\n[!] Read [!]')
    result = session.scalars(
        select(TableName),
    )
    print(result.all())

    # Get by id.
    result = session.get(TableName, 1)
    print(result)

    # Limit.
    result = session.scalars(
        select(TableName).limit(3),
    )
    print(result.all())

    # Where.
    result = session.scalars(
        select(TableName).where(TableName.age > 30),
    )
    print(result.all())

    result = session.scalar(
        select(TableName).where(TableName.id == 1),
    )
    print(result)

    # Filter.
    result = session.scalars(
        select(TableName).filter_by(name='renato'),
    )
    print(result.all())

    # Update.
    print('\n[!] Update [!]')
    print(session.get(TableName, 1))
    session.execute(
        update(TableName).where(TableName.id == 1).values(name='joão'),
    )
    print(session.get(TableName, 1))

    print(session.get(TableName, 2))
    result = session.scalar(
        select(TableName).where(TableName.id == 2),
    )
    result.name = 'antônio'
    session.commit()
    print(session.get(TableName, 2))

    # Delete.
    print('\n[!] Delete [!]')
    print(session.get(TableName, 1))
    session.execute(
        delete(TableName).where(TableName.id == 1),
    )
    print(session.get(TableName, 1))

    print(session.get(TableName, 2))
    result = session.scalar(
        select(TableName).where(TableName.id == 2),
    )
    session.delete(result)
    session.commit()
    print(session.get(TableName, 2))

    session.close()
