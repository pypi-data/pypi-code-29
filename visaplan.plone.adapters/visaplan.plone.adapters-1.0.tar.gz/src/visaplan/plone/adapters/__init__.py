from os import listdir
from os.path import join

# import patch
# siehe (gf): ../tools/zcmlgen.py

BASE = """<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:browser="http://namespaces.zope.org/browser">
    %s

</configure>
"""

PACKAGE = """
    <include package=".%(name)s" />"""

BASE_PATH = __path__[0]

packages = list()
for name in sorted(listdir(BASE_PATH)):
    if '.' not in name:
        packages.append(PACKAGE % locals())

fp = open(join(BASE_PATH, 'configure.zcml'), 'w')
fp.write(BASE % ''.join(packages))
fp.close()
