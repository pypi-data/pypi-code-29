#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SwissHydroData enables you to fetch data
from the Federal Office for the Environment FOEN
"""

from datetime import datetime, timedelta
import requests


class SwissHydroData:
    """
    SwissHydroData enables you to fetch data from
    the Federal Office for the Environment FOEN
    """

    def __init__(self):
        self.base_url = 'https://www.hydrodaten.admin.ch'
        self.values = {
            "level": "m ü.M",
            "temperature": "°C",
            "discharge": "m3/s"
        }
        self.data = {}

    def load_station_data(self, station_id=None):
        """
        load the data for a station indicated by
        its station id
        """
        if not station_id:
            raise Exception("missing station id")
        if not isinstance(station_id, int):
            raise Exception("invalid station id")
        self.data = {}
        data = {}
        for value in self.values.keys():
            res = requests.get(
                "{0}/graphs/{1}/{2}_{1}.csv".format(
                    self.base_url,
                    station_id,
                    value,
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
                data[value] = [
                    {"timestamp": datetime.strptime(y[0], "%Y-%m-%dT%H:%M:%S%z"),
                     "value": float(y[1]),
                     } for y in lines
                ]
                # order by timestamp
                data[value] = sorted(
                    data[value],
                    key=lambda k: k['timestamp'],
                    reverse=True
                )
        if not data:
            raise Exception("no data for given station id")
        self._analyze_data(data)

    def _analyze_data(self, data):
        for value, unit in self.values.items():
            if value in data:
                self.data[value] = {
                    "unit": unit,
                    "min": {},
                    "max": {},
                    "mean": 0
                }
                self.data[value]["latest"] = data[value][0]
                latest = data[value][0]["timestamp"]
                first = latest - timedelta(days=1)
                count = 0
                for entry in data[value]:
                    if entry["timestamp"] >= first:
                        count += 1
                        if "value" not in self.data[value]["min"] or \
                           self.data[value]["min"]["value"] > entry["value"]:
                            self.data[value]["min"] = entry
                        if "value" not in self.data[value]["max"] or \
                           self.data[value]["max"]["value"] < entry["value"]:
                            self.data[value]["max"] = entry
                        self.data[value]["mean"] += entry["value"]
                self.data[value]["latest"]["unit"] = unit
                self.data[value]["min"]["unit"] = unit
                self.data[value]["max"]["unit"] = unit
                self.data[value]["mean"] = {
                    "value": self.data[value]["mean"] / count,
                    "unit": unit
                }

    def get_latest_level(self):
        """ returns the latest water level measurement """
        return self.data.get("level", {}).get("latest")

    def get_max_level(self):
        """ returns the maximum water level in the last 24h """
        return self.data.get("level", {}).get("max")

    def get_min_level(self):
        """ returns the minimum water level in the last 24h """
        return self.data.get("level", {}).get("min")

    def get_mean_level(self):
        """ returns the mean water level in the last 24h """
        return self.data.get("level", {}).get("mean")

    def get_latest_temperature(self):
        """ returns the latest water temperature measurement """
        return self.data.get("temperature", {}).get("latest")

    def get_max_temperature(self):
        """ returns the maximum water temperature in the last 24h """
        return self.data.get("temperature", {}).get("max")

    def get_min_temperature(self):
        """ returns the minimum water temperature in the last 24h """
        return self.data.get("temperature", {}).get("min")

    def get_mean_temperature(self):
        """ returns the mean water temperature in the last 24h """
        return self.data.get("temperature", {}).get("mean")

    def get_latest_discharge(self):
        """ returns the latest water discharge measurement """
        return self.data.get("discharge", {}).get("latest")

    def get_max_discharge(self):
        """ returns the maximum water discharge in the last 24h """
        return self.data.get("discharge", {}).get("max")

    def get_min_discharge(self):
        """ returns the minimum water discharge in the last 24h """
        return self.data.get("discharge", {}).get("min")

    def get_mean_discharge(self):
        """ returns the mean water discharge in the last 24h """
        return self.data.get("discharge", {}).get("mean")
