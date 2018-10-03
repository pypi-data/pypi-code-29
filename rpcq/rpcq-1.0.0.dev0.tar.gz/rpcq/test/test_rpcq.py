#!/usr/bin/env python

# ########################################################################
# Copyright (C) Rigetti & Co. Inc. - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# September, 2017
# ########################################################################

from __future__ import print_function


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import logging

import pytest
from rpcq.base import (Message)

log = logging.getLogger(__file__)


def test_messages():

    class RPCError(Message):
        """A error message for JSONRPC requests."""

        # fix slots
        __slots__ = (
            'jsonrpc',
            'error',
            'id',
        )

        def asdict(self):
            """Generate dictionary representation of self."""
            return {
                'jsonrpc': self.jsonrpc,
                'error': self.error,
                'id': self.id
            }

        def astuple(self):
            """Generate tuple representation of self."""
            return (
                self.jsonrpc,
                self.error,
                self.id
            )

        def __init__(self,
                     error,
                     id,
                     jsonrpc="2.0"):
            # type: (str, str, str) -> None

            # check presence of required fields
            if jsonrpc is None:
                raise ValueError("The field 'jsonrpc' cannot be None")
            if error is None:
                raise ValueError("The field 'error' cannot be None")
            if id is None:
                raise ValueError("The field 'id' cannot be None")

            # verify types
            if not isinstance(jsonrpc, str):
                raise TypeError("Parameter jsonrpc must be of type str, "
                                + "but object of type {} given".format(type(jsonrpc)))
            if not isinstance(error, str):
                raise TypeError("Parameter error must be of type str, "
                                + "but object of type {} given".format(type(error)))
            if not isinstance(id, str):
                raise TypeError("Parameter id must be of type str, "
                                + "but object of type {} given".format(type(id)))

            self.jsonrpc = jsonrpc  # type: str
            """The JSONRPC version."""

            self.error = error  # type: str
            """The error message."""

            self.id = id  # type: str
            """The RPC request id."""

    e = "Error"
    i = "asefa32423"
    m = RPCError(e, id=i)
    assert m.error == e
    assert m.id == i
    assert m.jsonrpc == "2.0"

    assert m['error'] == e
    assert m.get('error', 1) == e

    assert m.asdict() == {"error": e,
                        "id": i,
                        "jsonrpc": "2.0"}
    assert m.astuple() == ("2.0", e, i)

    with pytest.raises(TypeError):
        RPCError(bad_field=1)
