SQLite
======

O `SQLite`_ é um banco de dados leve, autônomo e de código aberto que não requer um servidor para funcionar.

Ele é amplamente utilizado em aplicativos móveis, navegadores da web e outros sistemas de software devido à sua simplicidade, portabilidade e facilidade de uso.

Neste artigo, vamos explorar os conceitos fundamentais do SQLite de uma maneira acessível para quem está começando.

O que é o SQLite?
-----------------

O SQLite é um banco de dados relacional que armazena dados em um arquivo de banco de dados, em vez de em um servidor de banco de dados separado.

Isso o torna uma escolha popular para aplicativos que precisam de um banco de dados embutido, como aplicativos móveis, navegadores da web e software de desktop.

Principais Conceitos do SQLite
------------------------------

1. **Arquivo de Banco de Dados**: No SQLite, os dados são armazenados em um único arquivo de banco de dados. Esse arquivo contém todas as tabelas, índices, visões e outros objetos de banco de dados.
2. **Tabelas**: As tabelas são estruturas fundamentais do SQLite que armazenam dados de forma organizada. Cada tabela é composta por colunas (campos) e linhas (registros). As colunas representam os diferentes tipos de informações que serão armazenadas, enquanto as linhas representam os registros individuais.
3. **Consultas SQL**: O SQLite suporta a linguagem SQL (Structured Query Language) para realizar operações de consulta e manipulação de dados. Com SQL, você pode realizar consultas para recuperar dados de uma tabela, inserir novos dados, atualizar registros existentes e excluir dados.
4. **Transações**: O SQLite suporta transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade), o que significa que as operações de banco de dados são executadas de forma segura e confiável, mesmo em casos de falha.
5. **Índices**: Os índices no SQLite são estruturas de dados usadas para acelerar a recuperação de dados de uma tabela. Eles são criados em colunas específicas e ajudam o SQLite a encontrar registros com base em critérios de pesquisa de maneira mais eficiente.

Vamos ver um exemplo simples de criação de uma tabela e inserção de dados usando o SQLite:

Contêiner
---------

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/sqlite-3/docker-compose.yml

Exemplo prático
---------------

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/sqlite-3/main.py

Exemplo prático com SQLAlchemy
------------------------------

.. literalinclude:: ../../src/sqlite-3/main_sqlalchemy.py

    
Conclusão
---------

O SQLite é uma excelente escolha para projetos que precisam de um banco de dados leve e embutido.

Compreender os conceitos básicos, como arquivo de banco de dados, tabelas, consultas SQL e transações, pode ajudá-lo a utilizar o SQLite de forma eficaz em seus projetos de desenvolvimento.

.. _sqlite: https://www.sqlite.org/
