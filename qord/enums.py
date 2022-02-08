# MIT License

# Copyright (c) 2022 Izhar Ahmad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations


class GatewayEvent:
    r"""An enumeration that details names of various events sent over gateway.

    These events names are commonly passed in :class:`Client.event` decorator for
    registering a listener for relevant event.
    """

    GATEWAY_DISPATCH = "gateway_dispatch"
    r"""Called whenever gateway sends a dispatch event. See :class:`events.GatewayDispatch`."""

    SHARD_READY = "shard_ready"
    r"""Called whenever a shard successfully connects to Discord gateway."""


class PremiumType:
    r"""An enumeration that details values for a user's premium aka nitro subscription.

    Most common place where this enumeration is useful is when working with the
    :attr:`User.premium_type` attribute.
    """

    NONE = 0
    r"""User has no nitro subcription."""

    NITRO_CLASSIC = 1
    r"""User has nitro classic subscription."""

    NITRO = 2
    r"""User has nitro subscription."""

class DefaultAvatar:
    r"""An enumeration that details values for a user's default avatar.

    A user's default avatar value is calculated on the basis of user's
    four digits discriminator. It can be generated by::

        default_avatar = int(user.discriminator) % DefaultAvatar.INDEX

    To get a user's default avatar value, You should use :attr:`User.default_avatar`
    attribute.
    """

    BLURPLE = 0
    r"""Blurple coloured default avatar."""

    GRAY = 1
    r"""Gray coloured default avatar."""

    GREEN = 2
    r"""Green coloured default avatar."""

    YELLOW = 3
    r"""Yellow coloured default avatar."""

    RED = 4
    r"""Red coloured default avatar."""

    PINK = 5
    r"""Pink coloured default avatar."""

    INDEX = 5
    r"""The zero based index integer used for generating the user's default avatar.

    This is based of number of colours available for default avatars.
    As such, If Discord adds a new avatar colour, This index will increment.
    """

class ImageExtension:
    r"""An enumeration that details values for a various image extensions supported
    on the Discord CDN URLs.
    """

    PNG = "png"
    r"""PNG extension."""

    JPG = "jpg"
    r"""An alias of :attr:`.JPEG`."""

    JPEG = "jpeg"
    r"""JPEG extension."""

    WEBP = "webp"
    r"""WEBP extension."""

    GIF = "gif"
    r"""GIF extension. This is only supported for animated image resources."""
