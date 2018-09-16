"""
The main python wrapper around the Tankerkoening API.

Author  Iulius Gutberlet
"""

import json
import requests
from functools import reduce
from .station import Station
from .station import OpeningTime
from .station import OpeningTimes


class TankerkoenigAPI:
    """
    The Service wrapper around the Tankerkoening API.

    Author  Iulius Gutberlet
    """

    def __init__(self, api_key):
        """
        Instantiate a Tankerkoenig API accessor.

        :arg api_key    Your API to use with the Tankerkoenig API
        """
        self.base_url = "https://creativecommons.tankerkoenig.de/json"
        self.api_key = api_key

    def proximity_search(self, latitude, longitude, gas_type,
                         radius=5, sort_by="price"):
        """
        Perform a proximity search around the given coordinates.

        :arg latitude    the latitude of the position
        :arg longitude   the longitude of the position
        :arg gas_type    the type of gas you want prices for. Valid values are:
                         - e5
                         - e10
                         - diesel
                         - all
        :arg radius      the radius around the given location in km
                         min: 1, max: 25
        :arg sort_by     the sorting criteria. Valid values are price or dist.
                         With gas_type=all only dist
        """
        if radius < 1:
            print("Error: radius too small")
            radius = 1
        if radius > 25:
            print("Error: radius too big")
            radius = 25

        if gas_type != "e5" and gas_type != "e10" and\
                gas_type != "diesel" and gas_type != "all":
            print("Error: unknown gas type")

        if sort_by != "price" and sort_by != "dist":
            print("Error: sort by criteria unkown")

        if gas_type == "all" and sort_by != "dist":
            print("Warning: gas_type is all, hence can only sort by distance")
            sort_by = "dist"

        if latitude > 180.0 or latitude < -180.0:
            print("Error: latitude must be greater (incl.) -180.0 " +
                  "and less than (incl.) 180.0")

        if longitude > 90.0 or longitude < -90.0:
            print("Error: longitude must be greater (incl.) -90.0 " +
                  "and less than (incl.) 90.0")

        proximity_search_response = requests.get(self.base_url + "/list.php",
                                                 params={
                                                    "lat": latitude,
                                                    "lng": longitude,
                                                    "type": gas_type,
                                                    "rad": radius,
                                                    "sort": sort_by,
                                                    "apikey": self.api_key
                                                 })

        if proximity_search_response.status_code is 200:
            response = json.loads(proximity_search_response.text)
            if response["ok"]:
                result = []
                for station_dict in response["stations"]:
                    station = TankerkoenigAPI.\
                                __process_station(station_dict, gas_type)
                    if station is not None:
                        result.append(station)
                return result
            else:
                return None
        else:
            return None

    def __process_station(self, station_dict, gas_type):
        result = None
        if station_dict["isOpen"]:
            if (gas_type != "all" and
                "price" in station_dict and
                station_dict["price"] is not None) or \
                (gas_type == "all" and (
                    ("e5" in station_dict and
                     station_dict["e5"] is not None) or
                    ("e10" in station_dict and
                     station_dict["e10"] is not None) or
                    ("diesel" in station_dict and
                     station_dict["diesel"] is not None))):
                station = Station()
                station.id = station_dict["id"]
                station.open = True
                station.name = station_dict["name"]
                station.brand = station_dict["brand"]
                station.address.street = station_dict["street"]
                station.address.city = station_dict["place"]
                station.address.coords.latitude = station_dict["lat"]
                station.address.coords.longitude = station_dict["lng"]

                if gas_type == "all":
                    if station_dict["e5"] is not None:
                        station.prices.e5 = station_dict["e5"]
                    if station_dict["e10"] is not None:
                        station.prices.e10 = station_dict["e10"]
                    if station_dict["diesel"] is not None:
                        station.prices.diesel = station_dict["diesel"]
                elif gas_type == "e5":
                    station.prices.e5 = station_dict["price"]
                elif gas_type == "e10":
                    station.prices.e10 = station_dict["price"]
                elif gas_type == "diesel":
                    station.prices.diesel = station_dict["price"]

                station.address.house_number = station_dict["houseNumber"]
                station.address.zip_code = station_dict["postCode"]
                result = station
            else:
                print()
        return result

    def query_prices(self, gas_stations):
        """
        Query prices for particular gas station(s).

        :arg gas_stations   One station id (str) or multiple station ids (list)
        """
        stations = []
        if isinstance(gas_stations, str):
            stations.append(gas_stations)
        elif isinstance(gas_stations, list):
            stations = gas_stations

        station_ids = reduce((lambda x, y: x + "," + y), stations)

        query_prices_response = requests.get(self.base_url + "/prices.php",
                                             params={
                                                "ids": station_ids,
                                                "apikey": self.api_key
                                             })

        result = []

        if query_prices_response.status_code is 200:
            json_response = json.loads(query_prices_response.text)
            if json_response["ok"]:
                prices = json_response["prices"]
                for key, value in prices.items():
                    if key != "xxx" and value["status"] != "no stations":
                        station = Station()
                        station.id = key
                        station.open = value["status"] is "open"
                        if value["status"] is "open":
                            if isinstance(value["e5"], float):
                                station.prices.e5 = value["e5"]
                            if isinstance(value["e10"], float):
                                station.prices.e5 = value["e10"]
                            if isinstance(value["diesel"], float):
                                station.prices.e5 = value["diesel"]
                        result.append(station)
                    else:
                        print("query did not return result")
        return result

    def query_details_for_gas_station(self, station):
        """
        Query details for a particular gas station.

        :arg station    the gas station id
        """
        query_details = requests.get(self.base_url + "/detail.php", params={
            "id": station.id,
            "apikey": self.api_key
        })
        if query_details.status_code is 200:
            response = json.loads(query_details.text)
            if response["ok"]:
                detailed_station = response["station"]
                station.opening_times = OpeningTimes()
                station.opening_times.whole_day = detailed_station["wholeDay"]
                for override in detailed_station["overrides"]:
                    station.opening_times.exceptions.append(override)
                for time in detailed_station["openingTimes"]:
                    opening_time = OpeningTime()
                    opening_time.text = time["text"]
                    opening_time.start = time["start"]
                    opening_time.end = time["end"]
                    station.opening_times.regular_times.append(opening_time)
            else:
                return None
        else:
            return None
        return station

    def report_error(self, station_id, complaint_type, correction=None):
        """
        Report an error in the current data.

        :arg station_id the ID of the gas station
        :arg complaint_type the type of complaint. Valid values are:
                - wrongPetrolStationName
                - wrongStatusOpen
                - wrongStatusClosed
                - wrongPriceE5
                - wrongPriceE10
                - wrongPriceDiesel
                - wrongPetrolStationBrand
                - wrongPetrolStationStreet
                - wrongPetrolStationHouseNumber
                - wrongPetrolStationPostcode
                - wrongPetrolStationPlace
                - wrongPetrolStationLocation
        :arg correction the corrected value if applicable
        """
        if complaint_type != "wrongPetrolStationName" and \
           complaint_type != "wrongStatusOpen" and \
           complaint_type != "wrongStatusClosed" and \
           complaint_type != "wrongPriceE5" and \
           complaint_type != "wrongPriceE10" and \
           complaint_type != "wrongPriceDiesel" and \
           complaint_type != "wrongPetrolStationBrand" and \
           complaint_type != "wrongPetrolStationStreet" and \
           complaint_type != "wrongPetrolStationHouseNumber" and \
           complaint_type != "wrongPetrolStationPostcode" and \
           complaint_type != "wrongPetrolStationPlace" and \
           complaint_type != "wrongPetrolStationLocation":
            print("Error: Invalid complaint type!")

        if (complaint_type == "wrongStatusOpen" or
           complaint_type == "wrongStatusClosed") and \
           correction is not None:
            print("Correction ignored as not applicable for complaint_type")

        data = {
            "id": station_id,
            "apikey": self.api_key,
            "type": complaint_type
        }

        if complaint_type != "wrongStatusOpen" and\
           complaint_type != "wrongStatusClosed":
            data.correction = correction

        complaint_response = requests.post(self.base_url + "/complaint.php",
                                           json=data)

        if complaint_response.status_code == 200:
            complaint_json = json.loads(complaint_response.text)
            if complaint_json["ok"]:
                print("Complaint raised")
            else:
                print("Complaint failed! Error: " + complaint_json["message"])
