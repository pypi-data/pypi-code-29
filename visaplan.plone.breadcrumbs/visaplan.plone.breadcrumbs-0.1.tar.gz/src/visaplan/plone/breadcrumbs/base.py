# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
base-Modul für visaplan.plone.breadcrumbs

Instantiierbare Klassen, Exception-Klassen;
register, registered
"""
# TODO: unnötige Breadcrumb-Klassen eliminieren
#       (möglichst auf Grundtypen zurückführen)

__author__ = "Tobias Herp <tobias.herp@visaplan.com>"
VERSION = (0,
           3,  # Klassen aus .tree
           1,  # Verwendung von print_indented entfernt
           )
__version__ = '.'.join(map(str, VERSION))

# Zope:
import zope.component.hooks

# Standardmodule:
from urllib import urlencode

# Unitracc-Tools:
from visaplan.plone.base.typestr import pt_string
from visaplan.tools.minifuncs import translate_dummy as _
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.debug import arginfo
from visaplan.tools.debug import pp, log_or_trace

# Andere Browser:
from visaplan.plone.unitracctool.unitraccfeature.utils import (
        MYUNITRACC_UID, TEMP_UID,
        )
# from ...browser.groupdesktop.crumbs import OK

# Dieser Adapter:
from .utils import (crumbdict, title_or_caged_id__tup,
        LAST_NONFOLDERISH_BASECRUMB_KEY,
        )
from ._vars import LISTING_TEMPLATES

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport(defaultFromDevMode=1)
from visaplan.tools.dicts import subdict_forquery
from visaplan.tools.minifuncs import gimme_None


__all__ = (# Brotkrümel-Basis:
           'BaseCrumb',
           # Vielseitig verwendbare Krümel:
           'RootedCrumb',
           'ContextCrumb',
           # für dynamische Registrierung:
           'RootedDefaultCrumb',
           # Exception-Klassen:
           'BreadcrumbsException',
           'NoCrumbsException',
           'SkipCrumbException',
           # Registry:
           'register', 'registered',
           # Entwickungsunterstützung:
           'tellabout_call',
           )

# ---------------- [ Brotkrümel-Registry: Exception-Klassen ... [
class BreadcrumbsException(Exception):
    pass


class NoCrumbsException(BreadcrumbsException):
    """
    Keine Breadcrumbs für diesen Request
    """
    def __init__(self, cls, id):
        self.cls = cls
        self._id = id

    def __str__(self):
        return '%s(%s, %r)' % (
                self.__class__.__name__,
                self.cls,
                self._id,
                )


class SkipCrumbException(BreadcrumbsException):
    """
    Diesen Krümel nicht erzeugen
    (noch nicht verwendet)

    Die Krümelklasse --> SkipCrumb verwenden, um für bekannte Requests keinen
    Krümel für die Aufrufmethode zu erzeugen (wohl aber ggf. für den Kontext)
    """
# ---------------- ] ... Brotkrümel-Registry: Exception-Klassen ]


# --------- [ Brotkrümel-Registry: Entwickungsunterstützung ... [
def tellabout_call(f, tail=0):
    # chunks = [f.__class__.__name__]
    chunks = []
    if f.func_name != '__call__':
        chunks.extend(('.', f.func_name))
    if 0:
        # print dir(f)
        args = ((f.__class__, f.__class__.__name__), (f, chunks))
        kwargs = dict([(key, getattr(f, key))
                       for key in dir(f)
                       if key.startswith('func')
                          and key != 'func_globals'
                       ])
        pp(*args, **kwargs)
    nesting_string = '  '
    mask_before = '%(np)s<<< %(self)s%(funcname)s(%(context)s) ... <<<'
    mask_after = '%(np)s>>> ... %(self)s%(funcname)s(%(context)s) >>>'
    np = ''

    def inner(self, crumbs, hub, info, *args, **kwargs):
        funcname = ''.join(chunks)
        if not info['_context_printed']:
            context = info['context']
            info['_context_printed'] = True
            # print self, self.__class__, self.__class__.__name__
        else:
            context = '...'
        print mask_before % locals()
        res = f(self, crumbs, hub, info, *args, **kwargs)
        if tail:
            pp('Letzte %d Breadcrumbs:' % tail, crumbs[-tail:])
        print mask_after % locals()
        return res
    return inner
# --------- ] ... Brotkrümel-Registry: Entwickungsunterstützung ]


# -------------------- [ Brotkrümel-Basisklasse "BaseCrumb" ... [
class BaseCrumb:
    """
    Virtuelle Basisklasse für alle Brotkrümelklassen.
    Bei der Generierung der Brotkrümel für einen konkreten Request werden
    Instanzen dieser Klassen verwendet (Brotkrümelfunktionen), die zu Beginn
    (bei Import des Moduls) erzeugt werden.
    """

    def __init__(self, id, parents=[]):
        """
        id -- entspricht meist der ID des aufrufenden Seitentemplates
              und wird in vielen Brotkrümelklassen entsprechend für den
              erzeugten Krümel verwendet
        parents -- eine Sequenz von Brotkrümelfunktionen, zumeist mit einem
                   einzigen Element
        """
        self.id = id
        self.parents = list(parents)
        if debug_active >= 2:
            self.tell()

    # @tellabout_call
    def __call__(self, crumbs, hub, info):
        """
        Es wird kein Wert zurückgegeben; die Liste "crumbs" wird
        in-place geändert, ebenso wie hub und info.
        """
        # es ist eigentlich immer genau *ein* parent:
        for parent in self.parents:
            parent(crumbs, hub, info)
        self.tweak(crumbs, hub, info)
        if debug_active:
            pp('Breadcrumbs-Klasse: %r' % self.__class__,
               'info (Auszug):',
               subdict_forquery(info,
                                ['is_view_template',
                                 'view_url',
                                 'view_template_id',
                                 'view_template_done',
                                 ],
                                defaults_factory=gimme_None,
                                strict=False),
               'crumbs am Ende von __call__:',
               crumbs)

    def getParent(self):
        """
        Verwendet zum Bauen eines Strukturbaums.
        Bislang haben alle Instanzen maximal ein Elternelement,
        was für die Brotkrümelgenerierung ohne Bedeutung ist.
        Diese Methode erzwingt es jedoch.
        """
        if not self.parents:
            return None
        elif self.parents[1:]:
            raise ValueError('%s: Zu viele Eltern! (%s)'
                             % (self, self.parents))
        else:
            return self.parents[0]

    def tweak(self, crumbs, hub, info):
        """
        Diese Methode muß in abgeleiteten Klassen überschrieben werden;
        sie nimmt die spezifischen Änderungen vor.
        """
        raise NotImplementedError

    def __str__(self):
        if self.parents:
            return '%s[%r, parents: %s]' % (
                    self.__class__.__name__,
                    self.id,
                    self.parents,
                    )
        return '%s[%r]' % (
                self.__class__.__name__,
                self.id,
                )

    def __repr__(self):
        return '<%s(%r)>' % (self.__class__.__name__, self.id)

    def _brain_id_and_gid(self, brain, gid, tid=None):
        """
        Da sehr oft gebraucht ...
        """
        url = brain.getURL()
        if tid is None:
            tid = self.id
        return '%(url)s/%(tid)s?gid=%(gid)s' % locals()

    def _context_url(self, info, tid):
        """
        URL des Objekts aus dem Kontext
        """
        url = info['context_url']
        gid = info['gid']
        if gid is not None:
            return '%(url)s/%(tid)s?gid=%(gid)s' % locals()
        else:
            return '%(url)s/%(tid)s' % locals()

    def _desktop_subpage_url(self, info, tid=None):
        """
        URL einer Unterseite des Schreibtischs
        """
        if tid is None:
            tid = self.id
        url = info['desktop_url']
        gid = info['gid']
        if gid is not None:
            return '%(url)s/%(tid)s?gid=%(gid)s' % locals()
        else:
            return '%(url)s/%(tid)s' % locals()

    def _desktop_url(self, info):
        """
        URL des Schreibtischs
        """
        if info['gid'] is not None:
            return '%(desktop_url)s?gid=%(gid)s' % info
        else:
            return '%(desktop_url)s' % info

    def _rooted_url(self, info, tid):
        """
        URL einer direkten Unterseite des Portals
        """
        url = info['portal_url']
        return '%(url)s/%(tid)s' % locals()

    def tell(self, verbose=0):
        """
        Für Debugging: Selbstauskunft
        """
        args = ['%s(%r):' % (
                self.__class__.__name__,
                self.id,
                )]
        if verbose:
            args.append(('*** parents:', self.parents))
        else:
            args.append('%d parents' % len(self.parents))
        pp(*args)
# -------------------- ] ... Brotkrümel-Basisklasse "BaseCrumb" ]


# -------------------------- [ generische Brotkrümelklassen ... [
class BaseParentsCrumbs(BaseCrumb):

    """
    Keine Registrierung, keine ID; wird IMMER zuerst ausgeführt.
    Erzeugt Krümel für alle akquirierten Container,
    incl. der virtuellen Container "persönlicher" und "Gruppenschreibtisch"
    (durch Aufruf der DesktopCrumbs-Instanz registered('group-desktop')).
    """

    # @log_or_trace(debug_active, trace_key='base_crumbs', trace=0)
    def tweak(self, crumbs, hub, info):
        list_ = list(hub['parents']())
        list_.reverse()
        lnf_idx = None
        desktop_found = False
        boring_template = info['template_id'] not in LISTING_TEMPLATES

        for object_ in list_[1:]:  # Zope-Root ignorieren
            try:
                ouid = object_.UID()
                if object_.portal_type == 'Plone Site':
                    crumbs.append(
                            crumbdict(hub['translate']('Home'),
                                      info['portal_url']))
                    continue
                elif object_.getExcludeFromNav():
                    if boring_template:
                        if ouid == TEMP_UID:
                            desktop_found = True
                            break
                        else:
                            continue
                    # Listing-Template gefunden - normal fortfahren
            except AttributeError as e:
                continue
            else:
                if ouid == MYUNITRACC_UID:
                    registered('group-desktop')(crumbs, hub, info)
                    break
                # falls der temp-Ordner nicht von
                # der Navigation ausgeschlossen ist:
                elif ouid == TEMP_UID:
                    desktop_found = True
                    # hier liegen die unveröffentlichten Objekte,
                    # incl. derer auf dem persönlichen Schreibtisch
                    if boring_template:
                        break
                elif (ouid == TEMP_UID
                      and info['template_id'] not in NODESKTOP_TEMPLATES
                      ):
                    # Temp-Ordner --> Schreibtisch:
                    registered('group-desktop')(crumbs, hub, info)
                    break
                else:
                    title, do_translate = title_or_caged_id__tup(object_)
                    if do_translate:
                        title = hub['translate'](title)
                    crumbs.append(
                            crumbdict(title,
                                      object_.absolute_url()))
                    if object_.isPrincipiaFolderish:
                        lnf_idx = None
                    else:
                        lnf_idx = len(crumbs) - 1
        # wenn temp-Ordner nicht im Pfad, keinen Schreibtisch erzeugen:
        if not info['skip_desktop_crumbs'] and not desktop_found:
            info['skip_desktop_crumbs'] = True

        info[LAST_NONFOLDERISH_BASECRUMB_KEY] = lnf_idx
        if not info['skip_desktop_crumbs']:
            registered('group-desktop')(crumbs, hub, info)


class RootedCrumb(BaseCrumb):
    """
    Generischer Krümel für in der Portalwurzel angesiedelte Seiten

    Das Label wird bei Instantiierung angegeben.
    """
    def __init__(self, id, label, parents=[]):
        """
        eingeschobenes Pflichtargument: die Beschriftung
        """
        self._raw_label = label
        BaseCrumb.__init__(self, id, parents)

    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            hub['translate'](self._raw_label),
            self._rooted_url(info, self.id)))


class RootedUidCrumb(BaseCrumb):
    """
    Generischer Krümel für Seiten mit einer Request-Variablen 'uid'

    Das Label ist der Title des Objekts mit der angegebenen UID.
    """
    def tweak(self, crumbs, hub, info):
        uid = info['uid']
        if uid is not None:
            o = hub['getbrain'](uid)
            if o is not None:
                tid = self.id
                crumbs.append(crumbdict(
                    o.Title,
                    '/%(tid)s?uid=%(uid)s' % locals()))


class DesktopBrowserCrumb(RootedCrumb):
    """
    Generischer Krümel für Unterseiten des Schreibtischs, die zusätzlich die
    Angabe eines Browsers benötigen.

    Das Label und der Browser werden bei Instantiierung angegeben.
    """
    def __init__(self, id, label, browser, parents=[]):
        """
        eingeschobene Pflichtargumente:
        - die Beschriftung (wie RootedCrumb)
        - der Browser
        """
        assert id is not None
        if browser is None:
            self._virtual_id = '@@%(id)s' % locals()
        elif browser:
            self._virtual_id = '@@%(browser)s/%(id)s' % locals()
        else:
            self._virtual_id = '@@%(id)s' % locals()
        RootedCrumb.__init__(self, id, label, parents)

    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            hub['translate'](self._raw_label),
            self._desktop_subpage_url(info, self._virtual_id)))


class RootedBrowserCrumb(DesktopBrowserCrumb):
    """
    Dieselbe Initialisierungslogik wie DesktopBrowserCrumb, aber nicht für den
    Schreibtisch, sondern relativ zur Portalwurzel.

    Mit leerem Browser z. B. '@@syndication-settings'

    Das Label und der Browser werden bei Instantiierung angegeben.

    Wenn das Präfix '@@' stört (bzw. nicht funktionieren würde), stattdessen
    einfach --> RootedCrumb verwenden!
    """
    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            hub['translate'](self._raw_label),
            self._rooted_url(info, self._virtual_id)))


class RootedRequestvarCrumb(BaseCrumb):
    """
    Das Label wird einer Request-Variablen entnommen.

    Siehe auch --> RootedUidCrumb.
    """
    def __init__(self, id, key, parents=[]):
        """
        key -- der Name der Request-Variablen
        """
        self._key = key
        BaseCrumb.__init__(self, id, parents)

    def tweak(self, crumbs, hub, info):
        key = self._key
        val = info['request_var'].get(key)
        if val:
            query_s = urlencode([(key, val)])
            crumbs.append(crumbdict(
                val,
                self._rooted_url(info, '?'.join((self.id, query_s)))))
        elif val is not None:
            info['request_var'][key] = None


class RootedCrumbWithChild(RootedCrumb, RootedRequestvarCrumb):
    """
    Ein fixer Krümel, und einer, der von einer Request-Variablen abhängt;
    der Wert dieser Variablen ist das Label des variablen Krümels
    """
    def __init__(self, id, label, key, parents=[]):
        """
        eingeschobenes Pflichtargument: die Beschriftung
        """
        self._key = key
        RootedCrumb.__init__(self, id, label, parents)

    def tweak(self, crumbs, hub, info):
        RootedCrumb.tweak(self, crumbs, hub, info)
        RootedRequestvarCrumb.tweak(self, crumbs, hub, info)


class RootedInfokeyCrumb(RootedRequestvarCrumb):
    """
    Das Label wird einem Schlüssel des info-Dictionarys entnommen.
    Die URL wird von einer übergebenen Funktion erzeugt.
    """
    # XXX: am 28.1.2015 keine weiteren Vorkommen gefunden
    def __init__(self, id, key, urlfunc, parents=[]):
        """
        key -- der Name der Request-Variablen (aus RootedRequestvarCrumb)
        urlfunc -- Funktion, um die URL zu erzeugen
        """
        self._urlfunc = urlfunc
        RootedRequestvarCrumb.__init__(self, id, key, parents)

    def tweak(self, crumbs, hub, info):
        key = self._key
        val = info[key]
        if val:
            func = self._urlfunc
            crumbs.append(crumbdict(
                val,
                func(crumbs, hub, info)))


class RootedDefaultCrumb(BaseCrumb):
    """
    Generischer Krümel für vergessene Managementseiten.
    Nicht schön, aber vorhanden, und etwaige parents werden verarbeitet
    (i.e. insbesondere die Management-Zentrale).
    """
    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            self.id,  # nicht schön genug? Was schöneres explizit registrieren!
            self._rooted_url(info, self.id)))


class GenericContainerCrumb(BaseCrumb):
    """
    Als Elternkrümel, z. B. für "view"
    """
    def tweak(self, crumbs, hub, info):
        if info['skip_desktop_crumbs']:
            return
        has_group = info['gid'] is not None
        try:
            tup = pt2tup[info['portal_type']][has_group]
        except KeyError as e:
            logger.error('%(self)s: kein Template für %(pt)r (%(context)s)',
                         locals())
        else:
            crumbs.append(crumbdict(
                hub['translate'](tup[0]),
                self._desktop_subpage_url(info, tup[1])))


class ViewCrumb(BaseCrumb):
    """
    Spezifischer View-Krümel, z. B. für "unitraccnews_view";
    die Beschriftung wird dem Kontext entnommen.
    Es wird die übergebene id verwendet.

    Allgemeine View-Krümel werden aus der Struktur erzeugt,
    siehe --> BaseParentsCrumbs;  diese Klasse erzeugt Krümel nur noch,
    wenn das verwendete Template nicht das Standard-Template des Objekts ist,
    oder wenn dieser Krümel durch den (Gruppen-) Schreibtisch gelöscht wurde.

    Der Titel ist entsprechend nicht mehr der Objekttitel (der ja schon in
    Verwendung sein sollte), sondern eine "Übersetzung" des Template-Titels.

    Siehe auch -> GenericViewCrumb; zusammenführen?
    """
    # @log_or_trace(debug_active, trace_key='viewcrumb', trace=0)
    def tweak(self, crumbs, hub, info):
        info['view_url'], info['view_template_id'], info['is_view_template']
        # pp(self.__class__, info)
        if info['personal_desktop_done']:
            # Der Krümel wurde vom Schreibtisch gelöscht und nun hier neu
            # erzeugt:
            crumbs.append(crumbdict(
                info['context_title'],
                info['view_url']))
            info['view_template_done'] = True
            return
        elif info['is_view_template']:
            # Der Krümel für die Standardansicht (mit Objekttitel) wird von
            # BaseParentsCrumbs aus der Objektstruktur erzeugt ...
            return

        tid = self.id
        crumbs.append(crumbdict(
            hub['translate'](tid),
            self._context_url(info, tid)))
        return  # pep 20.2


class GenericViewCrumb(BaseCrumb):
    """
    Allgemeine View-Krümel werden aus der Struktur erzeugt,
    siehe --> BaseParentsCrumbs;  diese Klasse erzeugt Krümel nur noch,
    wenn das verwendete Template nicht das Standard-Template des Objekts ist,
    oder wenn dieser Krümel durch den (Gruppen-) Schreibtisch gelöscht wurde.

    Der Titel ist entsprechend nicht mehr der Objekttitel (der ja schon in
    Verwendung sein sollte), sondern eine "Übersetzung" des Template-Titels.

    Siehe auch -> ViewCrumb; zusammenführen?
    """
    @tellabout_call #(2)
    def tweak(self, crumbs, hub, info):
        is_new = not info['context_title']
        info['view_url'], info['view_template_id'], info['is_view_template']
        # pp(self.__class__, info)
        # XXX ??? Dokumentieren? (evtl. obsolet)
        is_published = len(crumbs) >= 3
        if not is_published:
            # generic_container_crumb(crumbs, hub, info)
            registered('--generic container--')(crumbs, hub, info)

        # wenn das Objekt noch keinen Titel hat, wird es gerade erst erzeugt
        # und kann noch nicht beguckt werden:
        if is_new:
            return
        if info['personal_desktop_done']:
            # Der Krümel wurde vom Schreibtisch gelöscht und nun hier neu
            # erzeugt:
            crumbs.append(crumbdict(
                info['context_title'],
                info['view_url']))
            info['view_template_done'] = True
            return
        elif info['is_view_template']:
            # Der Krümel für die Standardansicht (mit Objekttitel) wird von
            # BaseParentsCrumbs aus der Objektstruktur erzeugt ...
            return

        tid = self.id
        crumbs.append(crumbdict(
            hub['translate'](tid),
            self._context_url(info, tid)))


class BaseEditCrumb(BaseCrumb):
    """
    Bearbeiten: wenn neues Objekt, dann kein href-Attribut erzeugen

    Das Label ist der Titel des bearbeiteten Objekts; wird dies gerade erst
    erzeugt, hängt es vom Typ ab.
    """

    @tellabout_call #(2)
    def tweak(self, crumbs, hub, info):
        # set_trace()
        if info['context_title']:
            raw_title = 'Edit'
            url = self._context_url(info, self.id)
        else:
            try:
                raw_title = pt_string[info['portal_type']]['New thingy']
            except KeyError as e:
                pt = info['portal_type']
                context = info['context']
                logger.error('%(self)s: KeyError %(e)r (%(pt)r, %(context)s)',
                             locals())
                raw_title = 'Edit'
            url = None
        crumbs.append(crumbdict(
            hub['translate'](raw_title),
            url))


class ContextCrumb(BaseCrumb):
    """
    Das Label wird bei Instantiierung übergeben
    und bei Ausführung übersetzt
    """
    def __init__(self, id, label, parents):
        self.label = label
        BaseCrumb.__init__(self, id, parents)

    def tweak(self, crumbs, hub, info):
        _ = hub['translate']
        crumbs.append(crumbdict(
            _(self.label),
            self.id))
# -------------------------- ] ... generische Brotkrümelklassen ]


# --------- [ spezielle Brotkrümel- (Nicht-Krümel-) Klassen ... [
class NoCrumbs(BaseCrumb):
    """
    Kurzschluß: Es liegt ein Request vor, für den *keinerlei*
    Breadcrumbs erzeugt werden sollen.
    """
    def tweak(self, crumbs, hub, info):
        raise NoCrumbsException(self.__class__.__name__, self.id)


class SkipCrumb(BaseCrumb):
    """
    Für dieses Template soll kein Krümel erzeugt werden
    (etwaige Parents werden aber ausgeführt).

    Siehe auch --> SkipCrumbException
    """
    def tweak(self, crumbs, hub, info):
        pass
# --------- ] ... spezielle Brotkrümel- (Nicht-Krümel-) Klassen ]


# ---------------------------------------- [ Brotkrümel-Registry ... [
if debug_active:
    REGISTRY = {}

def make_registry():
    if debug_active:
        global REGISTRY
    else:
        REGISTRY = {}
    def set(handler, id=None):
        if id is None:
            id = handler.id
        if REGISTRY.has_key(id):
            old_handler = REGISTRY[id]
            logger.warning('There is an existing crumb adapter with id %(id)r'
                           ' (%(old_handler)r; replaced by'
                           ' %(handler)r)',
                           locals())
        if id is not None:
            REGISTRY[id] = handler
        return handler

    def get(id):
        try:
            return REGISTRY[id]
        except KeyError:
            logger.error('registry: no breadcrumb handler %(id)r found',
                    locals())
            raise

    return set, get

register, registered = make_registry()

def show_registry():
    if debug_active:
        pp(REGISTRY)
# ---------------------------------------- ] ... Brotkrümel-Registry ]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
