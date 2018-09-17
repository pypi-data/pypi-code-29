# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
Berechtigungen
"""

__author__ = "Tobias Herp <tobias.herp@visaplan.com>"
VERSION = (0,
           4,   # weitere Konstanten, vorrangig: importiert
           )
__version__ = '.'.join(map(str, VERSION))

from Products.CMFCore.permissions import (
        AccessInactivePortalContent,
        AddPortalContent,     # 'Add portal content'
        ModifyPortalContent,  # 'Modify portal content'
        )
# 'Access contents information':
from Products.Sessions.SessionPermissions import ACCESS_CONTENTS_PERM as Access_contents_information

# Gruppenberechtigungen:
from Products.PlonePAS.permissions import (ManageGroups, ViewGroups,
        AddGroups, DeleteGroups, SetGroupOwnership,
        )
# Benutzer:
ManageUsers = intern('Manage users')
# Die Berechtigungen 'Manage users', 'Manage Groups' (siehe Import oben)
# und 'unitracc: Manage courses' werden in einer vereinheitlichten
# Variablen-Konvention bereitgestellt

# Kurse (Module):
ManageCourses = intern('unitracc: Manage courses')
Access_course_documents = 'unitracc: Access course documents'

# Werbung:
Manage_Ads = 'unitracc: Manage ads'  # in @@advertisement als PERM_MANAGE

Manage_Subportals = 'unitracc: Manage subportals'
# Informationen des aktuellen Subportals auslesen:
Get_Subportal_Info = 'unitracc: Get subportal info'
# creator setzen; Plone-Berechtigungen mit 'ownership': 'Take ownership', 'Set Group Ownership'
Modify_Ownership_Settings = 'unitracc: Modify ownership settings'
# -------------------------------------- [ aus .config ... [
MANAGE_TANS = 'unitracc: Manage TANs'
CREATE_TAN = 'unitracc: Create TAN'
VIEW_TANS = 'unitracc: View TANs'
MODIFY_EXPIRES='unitracc: Modify expires'
# mutmaßlich: Veröffentlichungsdatum ändern
MODIFY_EFFECTIVE='unitracc: Modify effective'
ADD_LEXICON='unitracc: Add lexicon'
ADD_COMMENT = 'unitracc: Add UnitraccComment'
EDIT_SOURCE = 'unitracc: Edit HTML Source'
EDIT_PUBLISHED_SIMPLE = 'unitracc: Edit published simple content'
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
# -------------------------------------- ] ... aus .config ]

# Entwicklung:
View_Development_Information = 'unitracc: View Development Information'
