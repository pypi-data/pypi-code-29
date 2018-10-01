import requests
from interscity_client.exceptions import *


SHOULD_REGISTER_REMOTELLY = True
SHOULD_NOT_REGISTER_REMOTELLY = False


class connection():
    def __init__(self, protocol="http", kong_host="localhost:8000"):
        self.protocol = protocol
        self.kong_host = kong_host


    def capability_available(self, title):
        ENDPOINT = '/catalog/capabilities'
        response = requests.get(self.protocol + "://" + self.kong_host + ENDPOINT)
        capabilities = response.json()["capabilities"]
        return any(capability["name"] == title for capability in capabilities)


    def create_capability(self, title, description, capability_type = "sensor"):
        if (not self.capability_available(title)):
            ENDPOINT = '/catalog/capabilities'
            capability_json = {
                "name": title,
                "description": description,
                "capability_type": capability_type
            }
            response = requests.post(self.protocol + "://" + self.kong_host + ENDPOINT,
                                     json=capability_json)
            if (response.status_code > 300):
                raise Exception("Couldn't create capability {0}".format(title))
            else:
                print("Capability {0} successfully created.".format(title))
        else:
            print("Capability {0} already exist.".format(title))


    def register_resource(self, resource):
        ENDPOINT = "/catalog/resources"
        response = requests.post(self.protocol + "://" + self.kong_host + ENDPOINT,
                json={"data": resource})
        if (response.status_code > 300):
            print("Couldn't register resource {0}.".format(resource["uniq_key"]))
            print("Reason: {0}".format(response.text))
            return False
        else:
            return response.json()["data"]["uuid"]


    def send_data(self, uuid, resource):
        ENDPOINT = "/adaptor/components/{0}/data".format(uuid)
        response = requests.post(self.protocol + "://" + self.kong_host + ENDPOINT,
                json={"data": resource})
        if (response.status_code > 300):
            print("Couldn't send resource {0} data.".format(resource["uniq_key"]))
            print("Reason: {0}".format(response.text))
            return False


class resource_builder():
    def __init__(self, connection, capability, uniq_key):
        self.connection = connection
        self.capability = capability
        self.uniq_key = uniq_key
        self.resources = {}


    def register_locally(self, resource):
        if (resource["uniq_key"] in self.resources.keys()):
            print("Resource {0} already exist locally.".format(resource["uniq_key"]))
            if ("uuid" in resource["uniq_key"].keys):
                return SHOULD_REGISTER_REMOTELLY
            else:
                print("Resource {0} already exist remotelly.".format(resource["uniq_key"]))
                return SHOULD_NOT_REGISTER_REMOTELLY
        else:
            self.resources[resource["uniq_key"]] = resource
            print("Resource {0} registered locally...".format(resource["uniq_key"]))
            return SHOULD_REGISTER_REMOTELLY


    def register_remotelly(self, resource):
        REQUIRED_ATTRS = ["description", "capabilities", "status", "lat", "lon"]

        for attr in REQUIRED_ATTRS:
            if (not(attr in resource.keys())):
                raise Exception("Missing {0} in resource.".format(attr))

        r = self.connection.register_resource(resource)
        if (r != False):
            self.resources[resource["uniq_key"]]["uuid"] = r
            print("Resource {0} successfully registered.".format(resource["uniq_key"]))


    def register(self, uniq_key, description, capabilities, lat=-23, lon=-46):
        if (not(self.connection.capability_available(self.capability))):
            raise CapabilityDoesNotExist(self.capability)

        resource = {
            "uniq_key": uniq_key,
            "description": description,
            "capabilities": capabilities,
            "lat": lat,
            "lon": lon,
            "status": "active"
        }
        if (self.register_locally(resource) == SHOULD_REGISTER_REMOTELLY):
            self.register_remotelly(resource)


    def send_data(self, uniq_key, measure):
        if (not uniq_key in self.resources.keys()):
            print("Resource {0} not registered.".format(uniq_key))
            raise ResourceDoesNotExistLocally(uniq_key)
        else:
            if (not "uuid" in self.resources[uniq_key].keys()):
                print("Resource {0} not registered remotelly.".format(uniq_key))
                raise ResourceDoesNotExistRemotelly(uniq_key)
            resource = {}
            resource[self.capability] = [measure]
            self.connection.send_data(self.resources[uniq_key]["uuid"], resource)
