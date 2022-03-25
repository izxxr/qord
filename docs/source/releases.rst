.. currentmodule:: qord

Releases
========

This page details the changelog containing every notable change of every releases.

- The release with "Unreleased" in title indicates that the release is not yet released and is under development.
- The releases with "Pre-release" in title or if the version ends with an identifier, It indicates that the release was a pre-release.

v0.3.0 (Unreleased)
-------------------

Additions
~~~~~~~~~

- Added handling of HTTP ratelimits.
- Added support for channel permission overwrites.
- Added :attr:`Message.referenced_message` attribute.

Fixes
~~~~~

- Fixed cache not cleaning up on client closure.
- Fixed typing issues across the library.
    - Passing ``None`` is not supported in various places especially ``x_url()`` methods.
    - ``None`` is now allowed in ``reason`` parameters in REST methods.
    - Other minor improvements and fixes.


v0.3.0a1 (Pre-release)
----------------------

Breaking Changes
~~~~~~~~~~~~~~~~~

- Event system restructure

    - Custom events are now created using BaseEvent
    - :meth:`Client.invoke_event()` now takes single BaseEvent instance.
    - BaseEvent is no longer a protocol, all custom events must inherit it.
    - New protocol class BaseGatewayEvent has been added for gateway related events.
    - MessagesSupport was renamed to BaseMessageChannel for consistency.

Additions
~~~~~~~~~

- Added :class:`MessageType` enumeration.
- Added support for message embeds.
- Added support for message allowed mentions.
- Added support for message flags.
- Added support for message references.
- Added :meth:`Message.edit()` and :meth:`Message.delete()` methods.
- Added :meth:`Shard.disconnect()` and :meth:`~Shard.reconnect()` methods.
- Added :meth:`PrivateChannel.close()` method.
- Added :attr:`Intents.message_content` privileged intent flag.
- Added support for embeds, files and other options in :meth:`~BaseMessageChannel.send()`

Fixes
~~~~~

- Fix various crashes on startup.
- Fix minor bugs.

Improvements
~~~~~~~~~~~~

- Startup time has minor improvements.
- Library is now completely typed, there may be breaking type changes.

v0.2.0
------

Additions
~~~~~~~~~

- Added support for guild roles.
- Added support for guild members.
- Added support for permissions.
- Added support for guild channels.
- Added support for messages.
- Added :attr:`User.proper_name` property.
- Added :attr:`User.mention` property.

Improvements
~~~~~~~~~~~~

- :attr:`Guild.cache` is no longer optional.
- Startup time has been significantly improved.

Fixes
~~~~~

- Fixed :meth:`GuildCache.clear()` not getting called upon guild evictions.
- Fixed extension parameter incorrectly behaving for various URL methods.
- Fixed shards closing on receiving unhandleable OP code.
- Fixed client not properly handling graceful closure in some cases.
- Fixed :meth:`Client.launch()` raising RuntimeError upon relaunching the client after closing.


v0.2.0a1 (Pre-release)
----------------------

Additions
~~~~~~~~~

Add support for users.
Add support for guilds.
Add support for caching.

Improvements
~~~~~~~~~~~~

- Event listeners tasks now have proper exception handling.
- Various performance improvements.

Fixes
~~~~~

- Fixed wrong instance check on manually passing a client session.

v0.1.0
------

- Initial release.