repi-client
===========

Remote control your PyPi-packages via Redis PubSub. If you have a lot of virtual environments on different machines, install repi-client in each of them and only run one script. After that you can publish events like INSTALL to, you guessed it, install python packages on all connected systems.

Installation
------------

repi-client requires a running Redis server. See `Redis' quickstart <http://redis.io/topics/quickstart>`_ for installation instructions. repi-client is compatible with Redis clusters (which is an experimental feature at this point).

.. code-block:: bash

    $ pip install repi-client

or from source:

.. code-block:: bash

    $ python setup.py install

Getting started
---------------

After installation, you can run the 'repi-client' script.

.. code-block:: bash

    $ repi-client my_client_name

That's all!

To connect to a Redis host different from 'localhost', you can see a list of all the available options by running:

.. code-block:: bash
    $ repi-client my_client_name

Commands
--------
The default channels are using the 'repi' namespace. To talk to all connected repi-clients, publish a command to 'repi:cluster' (you can change those names). To talk to a specific repi-client, publish to 'repi:client-name'.

Exchange a simple PING/PONG:

.. code-block:: json

    {
        "command": "PING",
        "client": "master",
        "data": null
    }

Get a list of all installed packages:

.. code-block:: json

    {
        "command": "PACKAGE_LIST",
        "client": "master",
        "data": null
    }

Install a package:

.. code-block:: json

    {
        "command": "INSTALL",
        "client": "master",
        "data": {
            "package": "BeautifulSoup",
            "version": null
        }
    }

Install a certain package version:

.. code-block:: json

    {
        "command": "INSTALL",
        "client": "master",
        "data": {
            "package": "BeautifulSoup",
            "version": "3.2.1"
        }
    }
