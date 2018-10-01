from minty_cqs.command_and_query import CommandAndQuery
from pyramid.request import Request


class CommandAndQueryRequest:
    def command(self, **kwargs):
        # Do something with logged in user
        cqs = CommandAndQuery()

        # Do something with hostname
        # if "params" not in kwargs.keys():
        #     kwargs["params"] = {}

        # kwargs["params"]["auth"] = {"type": "subject", "id": 1}
        # kwargs["params"]["instance_hostname"] = self.host

        return cqs.command(**kwargs)

    def query(self, **kwargs):
        # Do something with logged in user
        cqs = CommandAndQuery()

        # Do something with hostname
        # if "params" not in kwargs.keys():
        #     kwargs["params"] = {}

        # kwargs["params"]["auth"] = {"type": "subject", "id": 1}
        # kwargs["params"]["instance_hostname"] = self.host

        return cqs.query(**kwargs)


# Extends the request object of pyramid, to supply instance configuration, etc
class MintyRequest(Request):
    cqs = None

    def __init__(self, *args, **kwargs):
        super(MintyRequest, self).__init__(*args, **kwargs)

        self.cqs = CommandAndQueryRequest()
