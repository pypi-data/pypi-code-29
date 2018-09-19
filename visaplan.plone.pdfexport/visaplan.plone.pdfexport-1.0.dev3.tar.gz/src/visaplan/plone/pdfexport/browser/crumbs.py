# -*- coding: utf-8 -*-

# Unitracc-Tools:
from visaplan.tools.minifuncs import translate_dummy as _

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import (BaseCrumb,
        RootedBrowserCrumb, GenericViewCrumb,
        register, registered,
        )
from ...adapters.breadcrumbs.utils import crumbdict

from ..management.crumbs import OK


# ---------------------------------------------- [ Crumb-Klassen ... [
class ExportProfileViewCrumb(BaseCrumb):
    def tweak(self, crumbs, hub, info):
        tid = self.id
        pid = info['export_profile_id']
        crumbs.append(crumbdict(
            info['export_profile_title'],
            '/@@export/%(tid)s?pid=%(pid)s'
            % locals()))

class ExportProfileEditCrumb(BaseCrumb):
    def tweak(self, crumbs, hub, info):
        tid = self.id
        pid = info['export_profile_id']
        crumbs.append(crumbdict(
            hub['translate']('Edit'),
            '/@@export/%(tid)s?pid=%(pid)s'
            % locals()))
# ---------------------------------------------- ] ... Crumb-Klassen ]


# -------------------------------------------- [ Initialisierung ... [
def register_crumbs():
    export_profiles_crumb = registered('manage_export_profiles')
    register(ExportProfileViewCrumb('viewExportProfile',
                                    [export_profiles_crumb]))
    register(ExportProfileEditCrumb('editExportProfile',
                               [registered('viewExportProfile')]))
    register(RootedBrowserCrumb('newExportProfile',
                                _('New profile'),
                                'export',
                                [export_profiles_crumb]))
    register(GenericViewCrumb(""'export_view'))

register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]

OK = True
