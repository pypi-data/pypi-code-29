from .universalJapanBase import UniversalJapanPark
from .universalUSBase import UniversalPark
from .seaWorldBase import SeaWorldPark

def getPark(name):
    if name == "USF" or name == "Universal Studios Florida":
        return UniversalPark("USF")
    elif name == "IOA" or name == "Islands of Adventure":
        return UniversalPark("IOA")
    elif name == "USH" or name == "Universal Studios Hollywood":
        return UniversalPark("USH")
    elif name == "USJ" or name == "Universal Studios Japan":
        return UniversalJapanPark("USJ")
    elif name == "BGT" or name == "Busch Gardens Tampa" or name == "Busch Gardens Africa":
        return SeaWorldPark("BGT")
    elif name == "BGW" or name == "Busch Gardens Williamsburg" or name == "Busch Gardens Europe":
        return SeaWorldPark("BGW")
    elif name == "SWO" or name == "SeaWorld Orlando":
        return SeaWorldPark("SWO")
    elif name == "SWSD" or name == "SeaWorld San Diego":
        return SeaWorldPark("SWSD")
    elif name == "SWSA" or name == "SeaWorld San Antonio":
        return SeaWorldPark("SWSA")
    else:
        print("Unsupported park name")
        print("Currently the module supports 'USF' and 'IOA'")
        print("Returning None")
        return None
