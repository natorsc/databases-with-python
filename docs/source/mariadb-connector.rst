mariadb-connector
=================

O conector `mariadb`_ para `Python`_ é uma biblioteca que permite que programas escritos em Python se conectem a um banco de dados `MariaDB`_, que é um sistema de gerenciamento de banco de dados relacional compatível com o `MySQL`_.

Com o conector `mariadb`, os desenvolvedores podem executar consultas SQL, recuperar e atualizar dados no banco de dados MariaDB usando código Python.

Essa biblioteca facilita a integração de aplicativos Python com bancos de dados MariaDB, tornando mais fácil para os desenvolvedores criar aplicativos web, científicos, de análise de dados e muito mais.

O conector pode ser instalando utilizando-se o gerenciado de pacotes do Python:

.. code-block:: bash

    pip install mariadb

.. attention::

    Antes de instalar o pacote instale as dependências.

Dependências
============

macOS
-----

.. code-block:: bash
    
    brew install \
    mariadb-connector-c

Linux
-----

Arch Linux
^^^^^^^^^^

.. code-block:: bash

    sudo pacman -S \
    openssl

Fedora
^^^^^^

.. code-block:: bash

    sudo dnf install \
    openssl

Ubuntu
^^^^^^

.. code-block:: bash

    sudo apt install \
    openssl

Contêiner
---------

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/mariadb/docker-compose.yml

Exemplo prático
---------------

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados:

.. literalinclude:: ../../src/mariadb/mariadb_connector.py

Exemplo prático com SQLAlchemy
------------------------------

Vamos ver um exemplo simples de como usar o MariaDB e o SQLAlchemy para criar uma tabela e inserir alguns dados:

.. literalinclude:: ../../src/mariadb/main_mariadb_mariadb_connector_sqlalchemy.py

Conclusão
---------

O MariaDB é uma poderosa ferramenta de banco de dados relacional que oferece compatibilidade com o MySQL e uma variedade de recursos avançados.

Compreender os conceitos básicos, como banco de dados, tabelas, consultas SQL e índices, pode ajudá-lo a utilizar o MariaDB de forma eficaz em seus projetos de desenvolvimento.

.. _mariadb: https://github.com/mariadb-corporation/mariadb-connector-python
.. _MariaDB: https://mariadb.org/
.. _MySQL: https://www.mysql.com/
.. _Python: https://www.python.org/
