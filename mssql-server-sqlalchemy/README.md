# Python, PyODBC e MS SQL Server


Em caso de problemas na instalação com a instalação do `pyodbc` (pip install pyodbc):
 
- No Windows pode-se utilizar o pacote do site [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyodbc](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyodbc).
- No Linux pode ser necessário instalar o pacote `unixodbc-dev` (`sudo apt install unixodbc-dev`).

Além do conector é necessária a instalação do **driver** do SQL Server.

Para verificar se o driver está instalado pode utilizar `print(drivers())`.

Caso não seja listado o driver:

- [Windows](https://docs.microsoft.com/pt-br/sql/connect/odbc/windows/system-requirements-installation-and-driver-files?view=sql-server-2017#installing-microsoft-odbc-driver-for-sql-server).
- [Linux/macOS](https://docs.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017).

Vale notar que cada versão do Microsoft SQL Server pode utilizar uma versão especifica do driver:

- {SQL Server} = released with SQL Server 2000.
- {SQL Native Client} = released with SQL Server 2005 (also known as version 9.0).
- {SQL Server Native Client 10.0} = released with SQL Server 2008.
- {SQL Server Native Client 11.0} = released with SQL Server 2012.
- {ODBC Driver 11 for SQL Server} = supports SQL Server 2005 through 2014.
- {ODBC Driver 13 for SQL Server} = supports SQL Server 2005 through 2016.
- {ODBC Driver 13.1 for SQL Server} = supports SQL Server 2008 through 2016.
- {ODBC Driver 17 for SQL Server} = supports SQL Server 2008 through 2017.

Ao utilizar o Windows Serve configurar:

- Login dos usuário com o SQL Server Management Studio.
- Banco de dados e permissões com o SQL Server Management Studio.
- Acesso ao SQL Server e portas com o SQL Server 2017 Configuration Manager.
- Configurar firewall do Windows Serve para permitir conexão da porta desejada.

Ao utilizar Docker não são necessárias configurações adicionais.
