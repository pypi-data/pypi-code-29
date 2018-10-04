#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SwissHydroData enables you to fetch data
from the Federal Office for the Environment FOEN
"""

from datetime import datetime as dt
import requests


class SwissHydroData:
    """
    SwissHydroData enables you to fetch data from
    the Federal Office for the Environment FOEN
    """

    def __init__(self):
        self.base_url = 'https://www.hydrodaten.admin.ch'
        self.data = {"level": [], "temperature": [], "discharge": []}

    def load_station_data(self, station_id=None):
        """
        load the data for a station indicated by
        its station id
        """
        if not station_id:
            raise Exception("missing station id")
        if not isinstance(station_id, int):
            raise Exception("invalid station id")
        values = [
            {"val": "level", "unit": "m ü.M."},
            {"val": "temperature", "unit": "°C"},
            {"val": "discharge", "unit": "m3/s"}
        ]
        for value in values:
            res = requests.get(
                "{0}/graphs/{1}/{2}_{1}.csv".format(
                    self.base_url,
                    station_id,
                    value['val'],
                )
            )
            if res.status_code == 200:
                # get csv data, split and fix timestamp format
                lines = [
                    (y[0][:-3]+y[0][-2:], y[1]) for y in
                    [x.split(',') for x in res.text.split('\n') if x]]
                # get rid of header line
                lines.pop(0)
                # parse data
                self.data[value["val"]] = [
                    {"timestamp": dt.strptime(y[0], "%Y-%m-%dT%H:%M:%S%z"),
                     "value": float(y[1]),
                     "unit": value["unit"]
                     } for y in lines
                ]
                self.data[value["val"]] = sorted(
                    self.data[value["val"]], key=lambda k: k['timestamp']
                )

    def get_latest_level(self):
        """ returns the latest water level measurement """
        if self.data["level"]:
            return self.data["level"][-1]
        return None

    def get_latest_temperature(self):
        """ returns the latest water temperature measurement """
        if self.data["temperature"]:
            return self.data["temperature"][-1]
        return None

    def get_latest_discharge(self):
        """ returns the latest water discharge measurement """
        if self.data["discharge"]:
            return self.data["discharge"][-1]
        return None
