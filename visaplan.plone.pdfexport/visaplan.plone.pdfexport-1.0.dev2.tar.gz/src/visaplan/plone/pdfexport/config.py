# -*- coding: utf-8 -*- äöü
"""
Konfiguration für PDF-Generierung
"""
# Standardmodule:
from collections import defaultdict
from os.path import abspath, join, dirname, pardir

# Plone/Zope:
from App.config import getConfiguration
from Globals import DevelopmentMode

# Unitracc-Tools:
from visaplan.plone.tools.cfg import get_config
from visaplan.tools.minifuncs import (NoneOrString, NoneOrInt, NoneOrBool,
        gimme_None,
        )
from visaplan.tools.dicts import subdict
from visaplan.tools.debug import pp

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport()

__all__ = ['pdfreactor_kwargs',
           'pdfreactor_options',
           'LICENSE_DATA',
           'CREATE_THREAD',
           'DevelopmentMode',
           ]

logger.info('Lese Konfiguration fuer "Produkt" pdfreactor ...')

_factories = {'host': NoneOrString,
              'port': NoneOrInt,
              'debug': NoneOrBool,
              'license_file': NoneOrString,
              'create_thread': NoneOrBool,
              }
_defaults = defaultdict(gimme_None)
env = getConfiguration().environment
# hier noch incl. der Initialisierungs-Argumente:
pdfreactor_options = get_config(product='pdfreactor',
                                defaults=_defaults,
                                factories=_factories)

# TODO: ersetzen durch Integration optionaler Umgebungsvariablen in get_config!
def _refine(key, oldenv, default):
    val = pdfreactor_options.get(key)
    if val is None:
        logger.warn('pdfreactor[%(key)r] ist undefiniert!', locals())
        if oldenv is not None and env.get(oldenv, None):
            logger.info('verwende Umgebungsvariable %(oldenv)r (veraltend!)', locals())
            pdfreactor_options[key] = val = _factories[key](env[oldenv])
        else:
            logger.info('verwende Vorgabewert %(default)r', locals())
            pdfreactor_options[key] = val = default

    logger.info('pdfreactor[%(key)r]=%(val)r', locals())


_refine('host', 'pdfreactor_host', 'pdfreactor.visaplan.com')
_refine('port', 'pdfreactor_port', 9423)
_refine('debug', None, True)
_refine('create_thread', None, not DevelopmentMode)
# alter (fixer) Ablageort (gf): ../../browser/export/licensekey.txt
_refine('license_file', None, abspath(join(dirname(__file__),
                                           pardir, pardir,
                                           'browser/export/',
                                           'licensekey.txt',
                                           )))

# das Ergebnis wird als kwargs-Dict. an den Konstruktor übergeben;
pdfreactor_kwargs = subdict(pdfreactor_options,
                            ['host', 'port', 'debug'],
                            do_pop=True)
pp(pdfreactor_options=pdfreactor_options, pdfreactor_kwargs=pdfreactor_kwargs)

CREATE_THREAD = pdfreactor_options['create_thread']

LICENSE_DATA = None
def read_license_data(filename=pdfreactor_options['license_file']):
    global LICENSE_DATA
    try:
        with open(filename, 'r') as f:
            LICENSE_DATA = f.read()
        logger.info("PDFReactor license read from '%s'",
                    filename)
        return True
    except OSError as e:
        logger.error("Error reading PDFReactor license from '%s'",
                     filename)
        logger.exception(e)
    except Exception as e:
        logger.error("%s Exception reading PDFReactor license from '%s'",
                     e.__class__.__name__,
                     filename)
        logger.exception(e)
read_license_data()

