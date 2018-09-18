# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
_vars-Modul für unitracc->breadcrumbs

Siehe auch Modul .honeypot (nur für Parser)
"""

__author__ = "Tobias Herp <tobias.herp@visaplan.com>"
VERSION = (0,
           2,  # Daten für Breadcrumb-Registry
           1,  # Importe geordnet
           )
__version__ = '.'.join(map(str, VERSION))

# Unitracc-Tools:
from visaplan.plone.tools.log import getLogSupport

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport(defaultFromDevMode=0)

# die folgenden Templates brechen die Breadcrumb-Generierung ab:
SHORTCUT_TEMPLATES = (
        'refresh_lock',
        'require_login',  # sonst mehrfache Startseitenkrümel
        'mainpage_view',  # wenig prakt. Nährwert; Platzverschwendung
        )
# die folgenden Templates unterdrücken die Erzeugung eines
# Schreibtischkrümels durch die BaseParentsCrumbs-Klasse:
NODESKTOP_TEMPLATES = (
        'folder_contents',
        'folder_listing',
        )
# die folgenden Templates erzeugen Krümel auch für von der Navigation
# ausgeschlossene Ordner (bzw. Objekte):
LISTING_TEMPLATES = (
        'folder_contents',
        'folder_listing',
        )

