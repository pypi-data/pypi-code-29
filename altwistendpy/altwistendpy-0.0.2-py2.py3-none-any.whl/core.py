import twisted.internet.defer


# TODO: CAMPid copied from epyqlib, roughly
def sleep(seconds, reactor=None):
    if reactor is None:
        import twisted.internet.reactor
        reactor = twisted.internet.reactor

    d = twisted.internet.defer.Deferred()

    reactor.callLater(seconds, d.callback, None)

    return d
