import sys

import twisted.internet.endpoints
import twisted.internet.protocol
import twisted.protocols.amp
import twisted.python.log
import twisted.internet.defer

import altwistendpy.examples.amp.commands


def connect(reactor):
    endpoint = twisted.internet.endpoints.TCP4ClientEndpoint(
        reactor,
        "127.0.0.1",
        8750,
    )
    return endpoint.connect(
        twisted.internet.protocol.Factory.forProtocol(
            twisted.protocols.amp.AMP,
        ),
    )


@twisted.internet.defer.inlineCallbacks
def client(reactor, text):
    twisted.python.log.startLogging(sys.stdout)

    protocol = yield connect(reactor)
    result = yield protocol.callRemote(
        altwistendpy.examples.amp.commands.Print,
        text=text,
    )
    print('result: {}'.format(repr(result)))
