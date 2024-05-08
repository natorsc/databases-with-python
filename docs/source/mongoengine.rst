MongoEngine
===========

`MongoEngine`_ é uma biblioteca de mapeamento objeto-documento (ODM) para o `MongoDB`_, um banco de dados NoSQL orientado a documentos.

O MongoEngine permite que os desenvolvedores usem classes de modelo em `Python`_ para interagir com documentos no MongoDB, proporcionando uma maneira mais simples e orientada a objetos de trabalhar com dados em comparação com a API padrão do MongoDB.

Ele fornece recursos como validação de dados, consultas avançadas e gerenciamento de relacionamentos entre documentos, tornando mais fácil para os desenvolvedores criar aplicativos Python escaláveis e robustos que utilizam o MongoDB como backend de dados.

.. code-block:: bash

    pip install mongoengine

Depois de instalado, você pode importar o MongoEngine em seus scripts Python e usá-lo para interagir com o MongoDB de forma fácil e eficiente.

Vamos ver um exemplo simples de como usar o MongoEngine para criar uma coleção e inserir um documento.

Contêiner
---------

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/mongodb/docker-compose.yml

Exemplo prático
---------------

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/mongodb/main_mongoengine.py

Conclusão
---------

O MongoDB é uma poderosa ferramenta de banco de dados NoSQL que oferece flexibilidade, escalabilidade e desempenho para uma variedade de aplicações.

Compreender os conceitos básicos, como documentos, coleções, consultas e índices, pode ajudá-lo a utilizar o MongoDB de forma eficaz em seus projetos de desenvolvimento.

.. _MongoDB: https://www.mongodb.com/
.. _MongoEngine: http://mongoengine.org/
.. _Python: https://www.python.org/
