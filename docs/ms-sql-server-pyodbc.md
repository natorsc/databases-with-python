# Python PyODBC

## Microsoft SQL Server 

### Dependências

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

- [Windows](https://docs.microsoft.com/pt-br/sql/connect/odbc/windows/system-requirements-installation-and-driver-files?view=sql-server-2017#installing-microsoft-odbc-driver-for-sql-server).
- [Linux/macOS](https://docs.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017).

Cada versão do Microsoft SQL Server pode utilizar uma versão especifica do driver:

- {SQL Server} = Lançado com o SQL Server 2000.
- {SQL Native Client} = Lançado com o SQL Server 2005 (Também conhecido como versão 9.0).
- {SQL Server Native Client 10.0} = Lançado com o SQL Server 2008.
- {SQL Server Native Client 11.0} = Lançado com o SQL Server 2012.
- {ODBC Driver 11 for SQL Server} = Suporta o SQL Server 2005 até 2014.
- {ODBC Driver 13 for SQL Server} = Suporta o SQL Server 2005 até 2016.
- {ODBC Driver 13.1 for SQL Server} = Suporta o SQL Server 2008 Até 2016.
- {ODBC Driver 17 for SQL Server} = Suporta SQL Server 2008 Até 2017.

Ao utilizar o Windows Serve configurar:

- Login dos usuário com o SQL Server Management Studio.
- Banco de dados e permissões com o SQL Server Management Studio.
- Acesso ao SQL Server e portas com o SQL Server 2017 Configuration Manager.
- Configurar firewall do Windows Serve para permitir conexão da porta desejada.

> Ao utilizar Docker não são necessárias configurações adicionais.

## Microsoft Access

Código só funciona no Microsoft Windows, uma vez que é necessário instalar o driver de conexão do Microsoft Access ou ter o Microsoft Access instalado no computador.

Driver do MS Access:

- [Driver Access 2010](https://www.microsoft.com/en-us/download/details.aspx?id=54920).
- [Driver Access 2016](https://www.microsoft.com/en-US/download/details.aspx?id=13255).

> **OBS**:
> - `*.accdb`: Formato utilizado pelo Access 2007 em diante.
> - `*.mdb`: Formato utilizado pelo Access 97, Access 2000, Access 2002 ou Access 2003.

---
