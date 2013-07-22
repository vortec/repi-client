RePi
===========

RePi manages your virtual environments, whether they're are all
on the same machine or not. You can remotely list installed PyPi
packages or install new ones. RePi does not, unlike Chef or Puppet,
require a SSH connection. All you need is a Redis server your machines
can connect to. If you want to go crazy, you can also use the nightly
Redis build which supports clustering. RePi will still work.

repi-client
===========

You need to install this module in each of your virtual environments.
After that, you need to install
`repi-server <http://github.com/vortec/repi-server>`_ to manage them.

Installation
------------

repi-client requires a running Redis server. See
`Redis' quickstart <http://redis.io/topics/quickstart>`_ for
installation instructions. repi-client is compatible with Redis clusters
(which is an experimental feature at this point).

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

To connect to a Redis host different from 'localhost', you can see a
list of all the available options by running:

.. code-block:: bash

    $ repi-client -h

