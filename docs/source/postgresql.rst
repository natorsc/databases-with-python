PostgreSQL
==========

O `PostgreSQL`_ é um sistema de gerenciamento de banco de dados relacional (RDBMS) de código aberto conhecido por sua confiabilidade, robustez e conformidade com os padrões SQL. É uma escolha popular para uma variedade de aplicativos, desde pequenos projetos até grandes sistemas corporativos. Neste artigo, vamos explorar os conceitos fundamentais do PostgreSQL de uma maneira acessível para quem está começando.

O que é o PostgreSQL?
---------------------

O PostgreSQL, também conhecido como Postgres, é um sistema de gerenciamento de banco de dados relacional baseado no modelo de dados relacional, o que significa que ele organiza os dados em tabelas com linhas e colunas. Ele suporta consultas SQL complexas, transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade) e uma variedade de recursos avançados, como índices, visões e gatilhos.

Principais Conceitos do PostgreSQL
----------------------------------

1. **Banco de Dados**: No PostgreSQL, um banco de dados é um contêiner para um conjunto de objetos, como tabelas, índices e funções. Cada banco de dados tem seu próprio conjunto de objetos e pode ser acessado por vários usuários.
2. **Tabelas**: As tabelas são estruturas fundamentais do PostgreSQL que armazenam dados em linhas e colunas. Cada tabela é composta por colunas que representam os diferentes tipos de dados que podem ser armazenados e por linhas que representam os registros individuais.
3. **Consultas SQL**: A linguagem SQL é usada para interagir com o PostgreSQL. Com SQL, você pode realizar consultas para recuperar dados de uma tabela, inserir novos dados, atualizar registros existentes e excluir dados.
4. **Chaves Primárias e Estrangeiras**: As chaves primárias são colunas em uma tabela que identificam exclusivamente cada registro na tabela. As chaves estrangeiras são usadas para estabelecer relacionamentos entre tabelas, permitindo consultas complexas que envolvem dados de várias tabelas.
5. **Índices**: Os índices são estruturas de dados usadas para acelerar a recuperação de dados de uma tabela. Eles são criados em colunas específicas e ajudam o PostgreSQL a encontrar registros com base em critérios de pesquisa de maneira mais eficiente.

Psycopg
-------

Psycopg é um adaptador de banco de dados PostgreSQL para a linguagem de programação Python. Ele permite que os programas Python se conectem a um banco de dados PostgreSQL, enviem consultas SQL e manipulem os resultados dessas consultas.

O Psycopg é amplamente utilizado devido à sua facilidade de uso e eficiência, sendo uma escolha popular para desenvolvedores que trabalham com Python e PostgreSQL.

Contêiner
`````````

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/postgresql/docker-compose.yml

Exemplo prático
```````````````

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/postgresql/main.py

Exemplo prático com SQLAlchemy
``````````````````````````````

.. literalinclude:: ../../src/postgresql/main_sqlalchemy.py

Conclusão
---------

O PostgreSQL é um sistema de gerenciamento de banco de dados poderoso e versátil, adequado para uma ampla gama de aplicações. Compreender os conceitos básicos, como bancos de dados, tabelas, consultas SQL e chaves, pode ajudá-lo a utilizar o PostgreSQL de forma eficaz em seus projetos de desenvolvimento.

.. _PostgreSQL: https://www.postgresql.org/
