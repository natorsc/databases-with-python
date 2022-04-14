![Bancos de dados com Python 3](./docs/images/python-databases-1600x840.webp "Bancos de dados com Python 3")

[![natorsc - databases-with-python](https://img.shields.io/static/v1?label=natorsc&message=databases-with-python&color=blue&logo=github)](https://github.com/natorsc/databases-with-python "Ir para o repositório.")
&emsp;
[![stars - databases-with-python](https://img.shields.io/github/stars/natorsc/databases-with-python?style=social)](https://github.com/natorsc/databases-with-python)
&emsp;
[![forks - databases-with-python](https://img.shields.io/github/forks/natorsc/databases-with-python?style=social)](https://github.com/natorsc/databases-with-python)

[![License MIT](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://github.com/natorsc/databases-with-python)

# Bancos de dados com Python 3

Exemplo de CRUD (Create, Read, Update e Delete) com a linguagem de programação Python e os principais bancos de dados do mercado.

<!-- START doctoc -->
<!-- END doctoc -->

---

## 🤓 Autor

Feito com 💙 por [Renato Cruz](https://github.com/natorsc) 🤜🤛 Entre em contato!

[![Blog](https://img.shields.io/static/v1?label=&message=Blog&color=orange&logoColor=white&logo=hashnode)](https://blog.justcode.com.br/ "Enviar e-mail.")
&emsp;
[![E-mail](https://img.shields.io/static/v1?label=&message=E-mail&color=blueviolet&logoColor=white&logo=gmail)](mailto:zkpcvm6dz@mozmail.com "Enviar e-mail.")
&emsp;
[![LinkedIn](https://img.shields.io/static/v1?label=&message=LinkedIn&color=blue&logoColor=white&logo=LinkedIn)](https://www.linkedin.com/in/natorsc "Entre em contato.")

Uma das playlist que costumo ouvir quando estou estudando ou "codando" 😁:

[![Spotify](https://img.shields.io/static/v1?label=&message=Spotify&color=darkgreen&logoColor=white&logo=spotify)](https://open.spotify.com/playlist/1xf3u29puXlnrWO7MsaHL5?si=A-LgwRJXSvOno_e6trpi5w&utm_source=copy-link "Acessar playlist.")

Sempre que possível escrevo tutoriais no meu blog pessoal 🚀:

[![Blog](https://img.shields.io/static/v1?label=&message=Blog&color=grey&logoColor=white&logo=hashnode)](https://blog.codigoninja.dev/ "Ir para o blog.")

---

## 💝 Doações

### Ko-Fi

[![Ko-Fi](https://img.shields.io/static/v1?label=&message=Ko-Fi&color=orange&logoColor=white&logo=ko-fi)](https://ko-fi.com/natorsc "Ajude com uma doação.")

### Pix

<img src="./docs/images/donation/pix-qr-code.jpg" alt="drawing" width="150"/>

**Chave**: `b1839493-2afe-484d-9272-82a3e402b36f`

---

## Bancos

### [MariaDB](https://mariadb.org/)

- [Python (mysql-connector-python)](./src/mariadb).
- [SQLAlchemy](./src/mariadb-sqlalchemy).

### [MongoDB](https://www.mongodb.com/pt-br)

- [Python (mongoengine)](./src/mongodb-mongoengine).
- [Python (pymongo)](./src/mongodb-pymongo).

### [Microsoft Access](https://www.microsoft.com/pt-br/microsoft-365/access)

> **OBS**: Funciona apenas no Microsoft Windows.

> Para utilizar o PyODBC são necessárias depedências e configurações, [clique aqui](./docs/ms-sql-server-pyodbc.md).

- [Python (pyodbc)](./src/ms-access).

### [SQL Server](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads)

> Para utilizar o PyODBC são necessárias depedências e configurações, [clique aqui](./docs/ms-sql-server-pyodbc.md).

- [Python (pyodbc)](./src/mssql-server).
- [SQLAlchemy](./src/mssql-server-sqlalchemy).

### [MySQL](https://www.mysql.com/)

- [Python (mysql-connector-python)](./src/mysql).
- [SQLAlchemy](./src/mysql-sqlalchemy).

### [PostgreSQL](https://www.postgresql.org/)

- [Python (psycopg2-binary)](./src/postgresql).
- [SQLAlchemy](./src/postgresql-sqlalchemy).

### [Redis](https://redis.io/)

- [Python (redis)](./src/redis).

### [SQLite3](https://www.sqlite.org/index.html)

- [Python](./src/sqlite3).
- [SQLAlchemy](./src/sqlite3-sqlalchemy).

---

## 💡 Extra

### Poetry

#### requirements.txt

Para gerar o arquivo de dependências `requirements.txt` através do [Poetry](https://python-poetry.org/) utilizar o comando:

```bash
poetry export \
--without-hashes \
-f requirements.txt \
-o requirements.txt
```

---
