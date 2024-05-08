Pymongo
=======

O `pymongo`_ é uma biblioteca Python oficial que permite interagir com o MongoDB, um banco de dados NoSQL de código aberto. O `pymongo` fornece uma API simples e intuitiva para trabalhar com o MongoDB, permitindo que os desenvolvedores criem, atualizem, consultem e excluam dados de maneira eficiente.

Com o `pymongo`, os desenvolvedores podem se conectar a um servidor MongoDB, acessar bancos de dados e coleções, executar consultas complexas, inserir e atualizar documentos e muito mais. Ele é amplamente utilizado em aplicativos Python que utilizam o MongoDB como seu sistema de armazenamento de dados.

O `pymongo` pode ser instalado usando o `pip`, que é o gerenciador de pacotes padrão do Python. Por exemplo, para instalar o `mysql-connector-python`, você pode usar o seguinte comando:

.. code-block:: bash

    pip install pymongo

Depois de instalado, você pode importar o `pymongo` em seus scripts Python e usá-lo para interagir com o MongoDB de forma fácil e eficiente.

Vamos ver um exemplo simples de como usar o MongoDB para criar uma coleção e inserir um documento.

Contêiner
---------

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/mongodb/docker-compose.yml

Exemplo prático
---------------

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/mongodb/main.py

Conclusão
---------

O MongoDB é uma poderosa ferramenta de banco de dados NoSQL que oferece flexibilidade, escalabilidade e desempenho para uma variedade de aplicações. Compreender os conceitos básicos, como documentos, coleções, consultas e índices, pode ajudá-lo a utilizar o MongoDB de forma eficaz em seus projetos de desenvolvimento.

.. _MongoDB: https://www.mongodb.com/
.. _pymongo: https://pypi.org/project/pymongo/
