MariaDB
=======

O `MariaDB`_ é um sistema de gerenciamento de banco de dados relacional de código aberto e uma bifurcação do MySQL.

Ele foi desenvolvido para manter a compatibilidade com o MySQL, enquanto oferece melhorias e novos recursos. Neste artigo, vamos explorar os conceitos fundamentais do MariaDB de uma maneira acessível para quem está começando.

O que é o MariaDB?
------------------

O MariaDB é um sistema de gerenciamento de banco de dados relacional (RDBMS) que utiliza a linguagem SQL (Structured Query Language) para manipular dados.

Ele oferece uma variedade de recursos, incluindo suporte a transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade), replicação de dados, e uma ampla gama de tipos de dados.

Principais conceitos do MariaDB
-------------------------------

1. **Banco de Dados**: Um banco de dados no MariaDB é um conjunto de tabelas que armazenam dados relacionados. Cada banco de dados tem um nome único e pode conter várias tabelas, índices e outros objetos de banco de dados.
2. **Tabelas**: As tabelas são estruturas fundamentais do MariaDB que armazenam dados em linhas e colunas. Cada tabela é composta por colunas que representam os diferentes tipos de dados que podem ser armazenados e por linhas que representam os registros individuais.
3. **Consultas SQL**: A linguagem SQL é usada para interagir com o MariaDB. Com SQL, você pode realizar consultas para recuperar dados de uma tabela, inserir novos dados, atualizar registros existentes e excluir dados.
4. **Chaves Primárias e Estrangeiras**: As chaves primárias são colunas em uma tabela que identificam exclusivamente cada registro na tabela. As chaves estrangeiras são usadas para estabelecer relacionamentos entre tabelas, permitindo consultas complexas que envolvem dados de várias tabelas.
5. **Índices**: Os índices no MariaDB são estruturas de dados usadas para acelerar a recuperação de dados de uma tabela. Eles são criados em colunas específicas e ajudam o MariaDB a encontrar registros com base em critérios de pesquisa de maneira mais eficiente.

mysql-connector-python
----------------------

O `mysql-connector-python`_ é um conector Python oficial fornecido pela `Oracle`_  para conectar aplicativos Python ao MySQL. Ele permite que os desenvolvedores escrevam código Python para interagir com um banco de dados MySQL, executando consultas, inserindo dados, atualizando registros e muito mais.

Este conector é uma biblioteca Python que implementa o protocolo de comunicação MySQL nativo, permitindo que o Python se comunique diretamente com o servidor MySQL. Ele fornece uma maneira fácil e eficaz de trabalhar com bancos de dados MySQL em aplicativos Python.

O `mysql-connector-python` pode ser instalado usando o `pip`, que é o gerenciador de pacotes padrão do Python. Por exemplo, para instalar o `mysql-connector-python`, você pode usar o seguinte comando:

.. code-block:: bash

    pip install mysql-connector-python

Depois de instalado, você pode importar o conector em seus scripts Python e usá-lo para se conectar a um servidor MySQL e executar operações de banco de dados.

Contêiner
`````````

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/mariadb/docker-compose.yml

Exemplo prático
```````````````

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/mariadb/main.py

Exemplo prático com SQLAlchemy
``````````````````````````````

.. literalinclude:: ../../src/mariadb/main_sqlalchemy.py

mariadb
-------

.. code-block:: bash

    pip install mariadb

Dependencias
------------

macOS

.. code-block:: bash
    
    brew install \
    mariadb-connector-c

Linux

Arch Linux

.. code-block:: bash

    sudo pacman -S \
    openssl

Fedora

.. code-block:: bash

    sudo dnf install \
    openssl

Ubuntu

.. code-block:: bash

    sudo apt install \
    openssl


Conclusão
---------

O MariaDB é uma poderosa ferramenta de banco de dados relacional que oferece compatibilidade com o MySQL e uma variedade de recursos avançados.

Compreender os conceitos básicos, como banco de dados, tabelas, consultas SQL e índices, pode ajudá-lo a utilizar o MariaDB de forma eficaz em seus projetos de desenvolvimento.

.. _MariaDB: https://mariadb.org/
.. _mysql-connector-python: https://pypi.org/project/mysql-connector-python/
.. _Oracle: https://www.oracle.com/br/
