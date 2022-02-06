.. currentmodule:: qord

API Reference
=============

Welcome to API Reference of Qord. This section details every single aspect of the
core API.

The Starter Point
-----------------

Client
~~~~~~

.. autoclass:: Client
    :members:

Data classes
------------

Shard
~~~~~

.. autoclass:: Shard()
    :members:

Flags
-----

Flags
~~~~~

.. autoclass:: Flags()
    :members:

Intents
~~~~~~~

.. autoclass:: Intents()
    :members:

Exceptions
----------

These are the exceptions raised by the library. All of these exceptions inherit a common
class :exc:`QordException`.

.. autoexception:: QordException()
.. autoexception:: ClientSetupRequired()
.. autoexception:: HTTPException()
.. autoexception:: HTTPBadRequest()
.. autoexception:: HTTPForbidden()
.. autoexception:: HTTPNotFound()
.. autoexception:: HTTPServerError()
.. autoexception:: ShardException()
.. autoexception:: ShardCloseException()
.. autoexception:: MissingPrivilegedIntents()
