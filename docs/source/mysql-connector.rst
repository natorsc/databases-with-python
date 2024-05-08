mysql-connector-python
======================

O `mysql-connector-python`_ é um conector Python oficial fornecido pela `Oracle`_  para conectar aplicativos `Python`_ ao `MySQL`_.

Ele permite que os desenvolvedores escrevam código Python para interagir com um banco de dados MySQL, executando consultas, inserindo dados, atualizando registros e muito mais.

Este conector é uma biblioteca Python que implementa o protocolo de comunicação MySQL nativo, permitindo que o Python se comunique diretamente com o servidor MySQL. Ele fornece uma maneira fácil e eficaz de trabalhar com bancos de dados MySQL em aplicativos Python.

O `mysql-connector-python` pode ser instalado usando o `pip`, que é o gerenciador de pacotes padrão do Python. Por exemplo, para instalar o `mysql-connector-python`, você pode usar o seguinte comando:

.. code-block:: bash

    pip install mysql-connector-python

Depois de instalado, você pode importar o conector em seus scripts Python e usá-lo para se conectar a um servidor MySQL e executar operações de banco de dados.

Contêiner
---------

Os códigos de exemplo foram testados no contêiner:

.. literalinclude:: ../../src/mysql/docker-compose.yml

Exemplo prático
---------------

Vamos ver um exemplo simples de como usar o MariaDB para criar uma tabela e inserir alguns dados.

.. literalinclude:: ../../src/mysql/main.py

Exemplo prático com SQLAlchemy
------------------------------

.. literalinclude:: ../../src/mysql/main_sqlalchemy.py

Conclusão
---------

O MySQL é uma ferramenta poderosa para armazenar e gerenciar dados de forma eficiente.

Compreender os conceitos básicos, como bancos de dados, tabelas, consultas SQL e chaves, pode ajudá-lo a utilizar o MySQL de forma eficaz em seus projetos de desenvolvimento.

.. _MySQL: https://www.mysql.com/
.. _mysql-connector: https://pypi.org/project/mysql-connector-python/
.. _Python: https://www.python.org/
.. _Oracle: https://www.oracle.com/br/
