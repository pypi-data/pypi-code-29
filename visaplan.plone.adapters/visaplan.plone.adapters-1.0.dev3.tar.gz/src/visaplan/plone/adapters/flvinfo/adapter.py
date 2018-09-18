from visaplan.plone.base import Base, Interface

import sys
import logging
from optparse import OptionParser

from flvlib import __versionstr__
from flvlib import tags
from flvlib import helpers

from App.config import getConfiguration
import os


class IFlvInfo(Interface):
    pass


class Adapter(Base):

    def _storage_path(self):
        """ """
        return getConfiguration().product_config.get('flv', {})['flv_dir'] + os.sep

    def __call__(self, uid, prefix='_flash_file'):
        """Extract metadata form flv file """
        context = self.context
        path = self._storage_path() + uid + prefix

        if os.path.exists(path):
            fp = open(path, 'rb')
            flv = tags.FLV(fp)
            tag_generator = flv.iter_tags()
            for i, tag in enumerate(tag_generator):
                if tag.name == 'onMetaData':
                    return tag.variable
        return {'width': 0, 'height': 0}
