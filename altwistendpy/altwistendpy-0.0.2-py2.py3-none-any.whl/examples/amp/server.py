import twisted.protocols.amp
import twisted.internet.protocol
import twisted.internet.endpoints

import altwistendpy.examples.amp.commands


def serve(reactor):
    endpoint = twisted.internet.endpoints.TCP4ServerEndpoint(reactor, 8750)
    factory = twisted.internet.protocol.Factory()
    factory.protocol = lambda: twisted.protocols.amp.AMP(
        locator=altwistendpy.examples.amp.commands.Commands(),
    )

    endpoint.listen(factory)
