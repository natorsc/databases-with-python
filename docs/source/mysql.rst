MySQL
=====

O `MySQL`_ é um dos sistemas de gerenciamento de banco de dados mais populares do mundo. Ele é amplamente utilizado em aplicativos da web e em muitos outros tipos de projetos de software devido à sua confiabilidade, desempenho e facilidade de uso. Neste artigo, vamos explorar os conceitos fundamentais do MySQL de uma maneira acessível para quem está começando.

O que é o MySQL?
----------------

O MySQL é um sistema de gerenciamento de banco de dados relacional (RDBMS) que permite armazenar, organizar e recuperar dados de forma eficiente. Ele utiliza a linguagem SQL (Structured Query Language) para realizar operações de manipulação e consulta de dados.

Principais Conceitos do MySQL
-----------------------------

1. **Banco de Dados**: Um banco de dados no MySQL é um conjunto de tabelas que armazenam dados relacionados. Cada banco de dados possui um nome único e pode conter várias tabelas e outros objetos de banco de dados.
2. **Tabelas**: As tabelas são estruturas fundamentais do MySQL que armazenam dados de forma organizada. Cada tabela é composta por colunas (campos) e linhas (registros). As colunas representam os diferentes tipos de informações que serão armazenadas, enquanto as linhas representam as entradas individuais de dados.
3. **Consultas SQL**: A linguagem SQL é usada para interagir com o banco de dados MySQL. Com SQL, você pode realizar consultas para recuperar dados de uma tabela, inserir novos dados, atualizar registros existentes e excluir dados.
4. **Chaves Primárias e Estrangeiras**: As chaves primárias são colunas em uma tabela que identificam exclusivamente cada registro na tabela. As chaves estrangeiras são usadas para estabelecer relacionamentos entre tabelas, permitindo consultas complexas que envolvem dados de várias tabelas.
5. **Índices**: Os índices são estruturas de dados usadas para acelerar a recuperação de dados de uma tabela. Eles são criados em colunas específicas e ajudam o MySQL a encontrar registros com base em critérios de pesquisa de maneira mais eficiente.

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

.. literalinclude:: ../../src/mysql/docker-compose.yml

Exemplo prático
```````````````

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/mysql/main.py

Exemplo prático com SQLAlchemy
``````````````````````````````

.. literalinclude:: ../../src/mysql/main_sqlalchemy.py

Conclusão
---------

O MySQL é uma ferramenta poderosa para armazenar e gerenciar dados de forma eficiente. Compreender os conceitos básicos, como bancos de dados, tabelas, consultas SQL e chaves, pode ajudá-lo a utilizar o MySQL de forma eficaz em seus projetos de desenvolvimento.

.. _MySQL: https://www.mysql.com/
