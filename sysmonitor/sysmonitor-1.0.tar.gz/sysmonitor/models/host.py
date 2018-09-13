"""Sysmonitor HOSTS"""

import logging
import threading
import math
import peewee
import requests


from sysmonitor.orm import models
from sysmonitor.configuration import Configuration


LOGGER = logging.getLogger(__name__)

CONFIG = Configuration()


HOST_AUTH_CONSTRAINT = peewee.Check("""
requires_authentication = false OR 
(requires_authentication = true AND authentication_api IS NOT NULL)
""")


class Host(models.BaseModel):
    """
    sysmonitor hosts. It saves all hosts
    """

    name = peewee.CharField(unique=True)
    address = peewee.CharField()
    authentication_api = peewee.CharField(null=True,
                                          constraints=[HOST_AUTH_CONSTRAINT])
    requires_authentication = peewee.BooleanField(default=True)
    hostname = peewee.CharField(null=True)
    operating_system = peewee.CharField(null=True)
    active = peewee.BooleanField(default=True)


    def _parse_resources(self, json_result):
        json_resources = json_result.get("resources", False)
        if json_resources:
            resource = Resource.create(host_id=self,
                                       load=json_resources.get("load", 0),
                                       memory=json_resources.get("memory", 0),
                                       swap=json_resources.get("swap", 0))
            json_disk = json_resources.get("disk", False)
            if json_disk:
                for mountpoint, usage in json_disk.items():
                    Disk.create(resource_id=resource, mountpoint=mountpoint,
                                usage=usage)

    def _parse_services(self, json_result):
        json_services = json_result.get("services", False)
        if json_services:
            for name, state in json_services.items():
                service, created = Service.get_or_create(host_id=self,
                                                         name=name,
                                                         defaults={
                                                             "state": state})
                if not created:
                    service.state = state
                    service.save()

    def query(self):
        """Query the host for information"""
        url = "%s/report" % self.address
        headers = {}
        if self.requires_authentication:
            headers["Authorization"] = self.authentication_api
        LOGGER.info("Querying host %s", self.name)
        req = requests.get(url, headers=headers)
        json_result = req.json()
        if req.status_code != 200:
            error = json_result.get("error", {})
            message = error.get("message", "Unknown error")
            LOGGER.error("Unable to query host %s: %s", self.name, message)
            return False
        self.hostname = json_result.get("hostname", self.hostname)
        self.operating_system = json_result.get("os", self.operating_system)
        self.save()
        self._parse_services(json_result)
        self._parse_resources(json_result)
        return True


    @staticmethod
    def query_hosts():
        """Query all active hosts

        It calls the query method
        """

        def _do_query(group):
            """Function used in threads. It calls query method for each host"""
            for host in group:
                host.query()

        # Get all active hosts
        hosts = Host.select().where(Host.active)
        count = hosts.count()
        if count == 0:
            LOGGER.warning("No hosts to query")
            return
        LOGGER.debug("Querying %d hosts", count)

        # Split hosts by n threads
        host_groups = [[]]
        i = 0
        thread_num = int(CONFIG.get("hosts", "query_threads"))
        for host in hosts:
            host_groups[-1].append(host)
            i += 1
            if i > math.ceil(count/thread_num) - 1:
                host_groups.append([])
                i = 0

        # Remove empty groups
        host_groups = [x for x in host_groups if x]

        # Run n threads to query hosts
        threads = []
        for group in host_groups:
            thread = threading.Thread(target=_do_query, args=(group,))
            thread.start()
            threads.append(thread)

        # Lets wait for all threads to finish
        for thread in threads:
            thread.join()


class Resource(models.BaseModel):
    """
    Host resources
    """

    host_id = peewee.ForeignKeyField(Host, backref="resource_ids",
                                     on_delete="CASCADE")
    load = peewee.FloatField(default=0)
    memory = peewee.FloatField(default=0)
    swap = peewee.FloatField(null=True)


class Disk(models.BaseModel):
    """
    Stores disks resources
    """

    resource_id = peewee.ForeignKeyField(Resource, backref="disk_ids",
                                         on_delete="CASCADE")
    mountpoint = peewee.CharField()
    usage = peewee.FloatField(default=0)


class Service(models.BaseModel):
    """
    Host services
    """

    host_id = peewee.ForeignKeyField(Host, backref="service_ids",
                                     on_delete="CASCADE")

    name = peewee.CharField()
    state = peewee.CharField(default="invalid")

    def save(self, force_insert=False, only=None):
        try:
            old_state = self.get(id=self.id).state
        except peewee.DoesNotExist:
            old_state = None
        res = super(Service, self).save(force_insert=force_insert, only=only)
        if old_state != self.state:
            LOGGER.warning("Service %s changed state to %s on host %s",
                           self.name, self.state, self.host_id.name)
            ServiceHistory.create(service_id=self, old_state=old_state,
                                  new_state=self.state)
        return res


class ServiceHistory(models.BaseModel):
    """
    Service history. It saves the history of a service
    """

    service_id = peewee.ForeignKeyField(Service, backref="history_ids",
                                        on_delete="CASCADE")
    old_state = peewee.CharField(null=True)
    new_state = peewee.CharField()

    def save(self, force_insert=False, only=None):
        if force_insert:
            return super(ServiceHistory, self).save(force_insert=force_insert,
                                                    only=only)
        raise Exception("Service history can't be updated")
