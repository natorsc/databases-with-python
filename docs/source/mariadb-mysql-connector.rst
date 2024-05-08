mysql-connector-python
======================

O `mysql-connector-python`_ é um conector Python oficial fornecido pela `Oracle`_  para conectar aplicativos Python ao `MySQL`_.

Ele permite que os desenvolvedores escrevam código Python para interagir com um banco de dados MySQL, executando consultas, inserindo dados, atualizando registros e muito mais.

Este conector é uma biblioteca `Python`_ que implementa o protocolo de comunicação MySQL nativo, permitindo que o Python se comunique diretamente com o servidor MySQL. Ele fornece uma maneira fácil e eficaz de trabalhar com bancos de dados MySQL em aplicativos Python.

O `mysql-connector-python` pode ser instalado usando o `pip`, que é o gerenciador de pacotes padrão do Python. Por exemplo, para instalar o `mysql-connector-python`, você pode usar o seguinte comando:

.. code-block:: bash

    pip install mysql-connector-python

Depois de instalado, você pode importar o conector em seus scripts Python e usá-lo para se conectar a um servidor MySQL e executar operações de banco de dados.

Contêiner
---------

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/mariadb/docker-compose.yml

Exemplo prático
---------------

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/mariadb/mariadb_mysql_connector.py

Exemplo prático com SQLAlchemy
------------------------------

.. literalinclude:: ../../src/mariadb/mariadb_mysql_connector_sqlalchemy.py

.. _MySQL: https://www.mysql.com/
.. _mysql-connector-python: https://pypi.org/project/mysql-connector-python/
.. _Oracle: https://www.oracle.com/br/
.. _Python: https://www.python.org/
