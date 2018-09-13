"""Sysmonitor models ORM"""

import datetime
import peewee
from playhouse.db_url import connect

from sysmonitor.configuration import Configuration

CONFIG = Configuration()

class BaseModel(peewee.Model):
    """
    SysMonitor base model
    """

    class Meta:
        """
        Peewee Meta class
        """
        # pylint: disable=too-few-public-methods
        database = connect(CONFIG.get("database", "url"))
        legacy_table_names = False

    create_date = peewee.DateTimeField()
    write_date = peewee.DateTimeField()

    def save(self, force_insert=False, only=None):
        if force_insert:
            self.create_date = datetime.datetime.now()
        self.write_date = datetime.datetime.now()
        return super(BaseModel, self).save(force_insert=force_insert, only=only)
