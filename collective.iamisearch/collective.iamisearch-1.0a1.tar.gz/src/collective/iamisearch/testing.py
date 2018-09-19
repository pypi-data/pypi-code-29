# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.iamisearch


class CollectiveIamisearchLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.iamisearch)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.iamisearch:default')


COLLECTIVE_IAMISEARCH_FIXTURE = CollectiveIamisearchLayer()


COLLECTIVE_IAMISEARCH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_IAMISEARCH_FIXTURE,),
    name='CollectiveIamisearchLayer:IntegrationTesting'
)


COLLECTIVE_IAMISEARCH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_IAMISEARCH_FIXTURE,),
    name='CollectiveIamisearchLayer:FunctionalTesting'
)


COLLECTIVE_IAMISEARCH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_IAMISEARCH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveIamisearchLayer:AcceptanceTesting'
)
