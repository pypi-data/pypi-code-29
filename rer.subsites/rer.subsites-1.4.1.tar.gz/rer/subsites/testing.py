# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rer.subsites


class RERSubsitesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=rer.subsites)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rer.subsites:default')


RER_SUBSITES_FIXTURE = RERSubsitesLayer()


RER_SUBSITES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RER_SUBSITES_FIXTURE,),
    name='RERSubsitesLayer:IntegrationTesting'
)


RER_SUBSITES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RER_SUBSITES_FIXTURE,),
    name='RERSubsitesLayer:FunctionalTesting'
)


RER_SUBSITES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RER_SUBSITES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RERSubsitesLayer:AcceptanceTesting'
)
