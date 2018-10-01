class ResourceDoesNotExistLocally(Exception):
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return "Resource {0} does not exist locally.".format(self.value)


class ResourceDoesNotExistRemotelly(Exception):
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return "Resource {0} does not exist remotelly.".format(self.value)


class CapabilityDoesNotExist(Exception):
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return "Capability {0} does not exist.".format(self.value)
