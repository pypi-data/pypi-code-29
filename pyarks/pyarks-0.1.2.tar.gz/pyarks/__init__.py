from __future__ import print_function
from .universal.IslandsOfAdventure import IslandsOfAdventure
from .universal.UniversalStudiosFlorida import UniversalStudiosFlorida
from .universal.VolcanoBay import VolcanoBay

__version__ = "0.1.3"

name = "pyarks"

parks = {
    'islandsOfAdventure': IslandsOfAdventure,
    'universalStudiosFlorida': UniversalStudiosFlorida,
    'VolcanoBay': VolcanoBay
}

def getPark(name):
    if name == "USF" or name == "Universal Studios Florida":
        return UniversalStudiosFlorida()
    elif name == "VB" or name == "Volcano Bay":
        return VolcanoBay()
    elif name == "IOA" or name == "Islands of Adventure":
        return IslandsOfAdventure()
    else:
        print("Unsupported park name")
        print("Currently the module supports 'USF', 'VB' and 'IOA'")
        print("Returning None")
        return None
