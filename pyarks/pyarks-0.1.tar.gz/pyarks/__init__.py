from __future__ import print_function
from .universal.UniversalStudiosJapan import UniversalStudiosJapan
from .universal.IslandsOfAdventure import IslandsOfAdventure

name = "pyarks"

parks = {
    'islandsOfAdventure': IslandsOfAdventure,
    'universalStudiosJapan': UniversalStudiosJapan
}

def getPark(name):
    if name == "USF" or name == "Universal Studios Florida":
        return UniversalStudiosJapan()
    elif name == "IOA" or name == "Islands of Adventure":
        return IslandsOfAdventure()
    else:
        print("Unsupported park name")
        print("Currently the module supports 'USF' and 'IOA'")
        print("Returning None")
        return None
