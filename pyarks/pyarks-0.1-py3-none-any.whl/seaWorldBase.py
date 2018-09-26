import requests

from .parkBase import Park
from .rideBase import Ride
from .utility import seaworldNameToID

class SeaWorldPark(Park):
    def __init__(self, name):
        super(SeaWorldPark, self).__init__(name)
        self.rides = self.getRides()

    def getRides(self):
        rides = []
        response = self.getResponse()
        for ride in response:
            if "waitTime" in ride["status"]:
                rides.append(Ride(self, ride["label"].encode("utf-8"), ride["status"]["waitTime"], ""))

        return rides

    def getResponse(self):
        baseURL = "https://seas.te2.biz/v1/rest/venue/{}/poi/all/status".format(seaworldNameToID(self.name))
        return requests.get(baseURL, auth=("seaworld", "1393288508")).json()