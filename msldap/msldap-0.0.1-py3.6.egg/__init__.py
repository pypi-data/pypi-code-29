
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


#from .core.msldap import *
#from .ldap_objects import *

#__all__ = ['MSLDAPUserCredential', 'MSLDAPTargetServer', 'MSLDAP', 'MSADInfo', 'MSADUser', 'MSLDAP_UAC']