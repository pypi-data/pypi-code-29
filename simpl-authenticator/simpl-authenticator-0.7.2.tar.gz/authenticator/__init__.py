from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.wamp import ApplicationSession

_version = "0.7.2"
__version__ = VERSION = tuple(map(int, _version.split('.')))


class AuthenticatorComponent(ApplicationSession):
    def authenticate(self, realm, authid, details):
        self.log.debug(
            "authenticate called: realm = '{realm!r}', authid = '{authid!r}', details = '{details!r}'",
            realm=realm, authid=authid, details=details,
        )
        # We dont need to check the password, as the user has already been
        # authenticated upstream by PennKey. We just need to know who they are
        # TODO: Authenticate against the Simpl's API
        return {
            'secret': 'nopassword',
            'role': 'browser',
        }

    @inlineCallbacks
    def onJoin(self, details):
        self.log.info("session joined by authenticator")
        try:
            yield self.register(self.authenticate, 'world.simpl.authenticate')
            self.log.info("custom WAMP-CRA authenticator registered")
        except Exception as e:
            self.log.error(
                "could not register custom WAMP-CRA authenticator: {error!r}",
                error=e)
