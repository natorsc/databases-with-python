![Bancos de dados com Python 3](./docs/images/python-databases-1600x840.webp "Bancos de dados com Python 3")

[![natorsc - databases-with-python](https://img.shields.io/static/v1?label=natorsc&message=databases-with-python&color=blue&logo=github)](https://github.com/natorsc/databases-with-python "Ir para o repositório.")
&emsp;
[![stars - databases-with-python](https://img.shields.io/github/stars/natorsc/databases-with-python?style=social)](https://github.com/natorsc/databases-with-python)
&emsp;
[![forks - databases-with-python](https://img.shields.io/github/forks/natorsc/databases-with-python?style=social)](https://github.com/natorsc/databases-with-python)

[![License MIT](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://github.com/natorsc/databases-with-python)

# Bancos de dados com Python 3

Exemplo de CRUD (Create, Read, Update e Delete) com a linguagem de programação Python e os principais bancos de dados do mercado.

---

## 🤓 Autor

Feito com 💙 por [Renato Cruz](https://github.com/natorsc) 🤜🤛 Entre em contato!

[![E-mail](https://img.shields.io/static/v1?label=&message=E-mail&color=blueviolet&logoColor=white&logo=gmail)](mailto:zkpcvm6dz@mozmail.com "Enviar e-mail.")
&emsp;
[![LinkedIn](https://img.shields.io/static/v1?label=&message=LinkedIn&color=blue&logoColor=white&logo=LinkedIn)](https://www.linkedin.com/in/natorsc "Entre em contato.")

Uma das playlist que costumo ouvir quando estou estudando ou "codando" 😁:

[![Spotify](https://img.shields.io/static/v1?label=&message=Spotify&color=darkgreen&logoColor=white&logo=spotify)](https://open.spotify.com/playlist/1xf3u29puXlnrWO7MsaHL5?si=A-LgwRJXSvOno_e6trpi5w&utm_source=copy-link "Acessar playlist.")

Sempre que possível escrevo tutoriais no meu blog pessoal 🚀:

[![Blog](https://img.shields.io/static/v1?label=&message=Blog&color=gray&logoColor=blue&logo=hashnode)](https://blog.codigoninja.dev/ "Ir para o blog.")

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

---

### [MongoDB](https://www.mongodb.com/pt-br)

- [Python (mongoengine)](./src/mongodb-mongoengine).
- [Python (pymongo)](./src/mongodb-pymongo).

---

### [Microsoft Access](https://www.microsoft.com/pt-br/microsoft-365/access)

> **OBS**: Funciona apenas no Microsoft Windows.

Código só funciona no Microsoft Windows, uma vez que é necessário instalar o driver de conexão do Microsoft Access ou ter o Microsoft Access instalado no computador.

Driver do MS Access:

- [Driver Access 2010](https://www.microsoft.com/en-us/download/details.aspx?id=54920).
- [Driver Access 2016](https://www.microsoft.com/en-US/download/details.aspx?id=13255).

https://www.microsoft.com/en-us/download/details.aspx?id=54920

> **OBS**:
> - `*.accdb`: Formato utilizado pelo Access 2007 em diante.
> - `*.mdb`: Formato utilizado pelo Access 97, Access 2000, Access 2002 ou Access 2003.

- [Python (pyodbc)](./src/ms-access).

Dependência
> brew install unixodbc

---

### [SQL Server](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads)

### Dependências

#### macOS

brew install unixodbc
python -m pip install pyodbc

#### Arch Linux

```bash
sudo pacman -S unixodbc
```

#### Fedora

```bash
sudo dnf install \
python3-devel \
unixODBC-devel
```

#### Ubuntu e derivados

```bash
sudo apt install unixodbc-dev
```

#### Microsoft Windows

Pacote Wheel (`*.whl`) [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyodbc](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyodbc).

### Driver

Além do conector é necessária a instalação do **driver** do SQL Server.

Para verificar se o driver está instalado pode utilizar `print(drivers())`.

Caso não seja listado o driver:

- [Microsoft ODBC Driver for SQL Server (Windows)](https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server).
- [Microsoft ODBC Driver for SQL Server (Linux)](https://learn.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server).
- [Microsoft ODBC Driver for SQL Server (macOS)](https://learn.microsoft.com/pt-br/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos).


Cada versão do Microsoft SQL Server pode utilizar uma versão especifica do driver:

- **SQL Server**: Lançado com o SQL Server 2000.
- **SQL Native Client**: Lançado com o SQL Server 2005 (Também conhecido como versão 9.0).
- **SQL Server Native Client 10.0**: Lançado com o SQL Server 2008.
- **SQL Server Native Client 11.0**: Lançado com o SQL Server 2012.
- **ODBC Driver 11 for SQL Server**: Suporta o SQL Server 2005 até 2014.
- **ODBC Driver 13 for SQL Server**: Suporta o SQL Server 2005 até 2016.
- **ODBC Driver 13.1 for SQL Server**: Suporta o SQL Server 2008 Até 2016.
- **ODBC Driver 17 for SQL Server**: Suporta SQL Server 2008 Até 2017.
- **ODBC Driver 17 for SQL Server**: Suporta SQL Server 2008 Até 2017.
- **ODBC Driver 18 for SQL Server**: Suporta SQL Server 2019 ou superior.

Ao utilizar o Windows Serve configurar:

- Login dos usuário com o SQL Server Management Studio.
- Banco de dados e permissões com o SQL Server Management Studio.
- Acesso ao SQL Server e portas com o SQL Server 2017 Configuration Manager.
- Configurar firewall do Windows Serve para permitir conexão da porta desejada.

> Ao utilizar Docker não são necessárias configurações adicionais.

- [Python (pyodbc)](./src/mssql-server).
- [SQLAlchemy](./src/mssql-server-sqlalchemy).

---

### [MySQL](https://www.mysql.com/)

- [Python (mysql-connector-python)](./src/mysql).
- [SQLAlchemy](./src/mysql-sqlalchemy).

---

### [PostgreSQL](https://www.postgresql.org/)

- [Python (psycopg2-binary)](./src/postgresql).
- [SQLAlchemy](./src/postgresql-sqlalchemy).

---

### [Redis](https://redis.io/)

- [Python (redis)](./src/redis).

---

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

Para gerar o arquivo com as dependências de desenvolvimento (`requirements-dev.txt`):

```bash
poetry export \
--with dev \
--without-hashes \
-f requirements.txt \
-o requirements-dev.txt
```

---

# Docker

- [Site oficial](https://www.docker.com/community/).

## Docker desktop

- [Site oficial](https://www.docker.com/products/docker-desktop/).

### macOS

```bash
brew install \
--cask docker
```

sudo rm -rf /opt/homebrew/share/zsh/site-functions/_docker
sudo rm -rf /opt/homebrew/share/fish/vendor_completions.d/docker.fish

### Linux

#### Arch Linux

[Site oficial](https://docs.docker.com/desktop/install/archlinux/).

```bash
curl \
-o docker-desktop.pkg.tar.zst \
https://desktop.docker.com/linux/main/amd64/145265/docker-desktop-4.29.0-x86_64.pkg.tar.zst
```

```bash
sudo pacman \
-U ./docker-desktop.pkg.tar.zst
```

```bash
systemctl --user \
start docker-desktop
```

```bash
systemctl --user \
enable docker-desktop
```

#### Fedora

[Site oficial](https://docs.docker.com/desktop/install/fedora/).

```bash
curl \
-o docker-desktop.rpm \
https://desktop.docker.com/linux/main/amd64/145265/docker-desktop-4.29.0-x86_64.rpm
```

```bash
sudo dnf install \
./docker-desktop.rpm
```

```bash
systemctl --user \
start docker-desktop
```

```bash
systemctl --user \
enable docker-desktop
```

#### Ubuntu

[Site oficial](https://docs.docker.com/desktop/install/ubuntu/).

```bash
curl \
-o docker-desktop.deb \
https://desktop.docker.com/linux/main/amd64/145265/docker-desktop-4.29.0-amd64.deb
```

```bash
sudo apt install \
./docker-desktop.deb
```

```bash
systemctl --user \
start docker-desktop
```

```bash
systemctl --user \
enable docker-desktop
```

---

## Docker compose

### macOS

```bash
brew install \
docker-compose
```

### Linux

#### Arch Linux

```bash
sudo pacman -S \
docker-compose
```

#### Fedora

```bash
sudo dnf install \
docker-compose
```

#### Ubuntu

```bash
sudo apt install \
docker-compose
```






---

# Podman

- [Site oficial](https://podman-desktop.io/).



### macOS

```bash
brew install \
podman
```

```bash
podman machine init
```

```bash
podman machine start
```

### Linux

#### Arch Linux

```bash
sudo pacman -S \
podman
```

#### Fedora

```bash
sudo dnf install \
podman
```

#### Ubuntu

```bash
sudo apt install \
podman
```

## Podman desktop

- [Site oficial](https://podman-desktop.io/).

### Microsoft Windows

#### Winget

```ps1
winget install -e --id RedHat.Podman-Desktop
```

## Linux

### Flatpak

```bash
flatpak install \
flathub io.podman_desktop.PodmanDesktop
```

### macOS

#### Homebrew

```bash
brew install --cask \
podman-desktop
```

## Podman compose

```bash
brew install \
podman \
podman-compose
```


