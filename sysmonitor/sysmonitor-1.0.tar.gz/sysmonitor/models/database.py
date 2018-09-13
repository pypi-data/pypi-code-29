"""Migrate sysmonitor database"""

import logging
import peewee
from sysmonitor.orm import models

LOGGER = logging.getLogger(__name__)

class DatabaseVariable(models.BaseModel):
    """Variables values to store in database"""

    name = peewee.CharField(unique=True)
    value = peewee.CharField()

    @staticmethod
    def set_variable(name, value):
        """Save/create variable

        :param string name: variable name
        :param string value: variable value
        """
        rec, created = DatabaseVariable.get_or_create(name=name,
                                                      defaults={"value": value})
        if created:
            LOGGER.info("Created variable %s", name)
        else:
            LOGGER.info("Updated variable %s", name)
            rec.value = value
            rec.save()

    @staticmethod
    def get_variable(name, default=None):
        """
        Get variable value

        :param string name: variable name
        :param string default: variable default value if can't find in database
        """
        rec = DatabaseVariable.select().where(DatabaseVariable.name == name)
        if rec.count() == 1:
            return rec[0].value
        return default
