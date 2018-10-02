# -*- coding: utf-8 -*-

from contuino_core import Board, Action
from .contuino_micropython import mp_helpers
import json

DEFAULT_BAUD_RATE = 115200

INFO_RUN_ONCE = "\r\nYou only need to flash micropython firmware once\r\n"
INFO_PORT_MISSING = "\r\nBoard port missing. Check device manager on Windows and lsusb on unix\r\n"


class MyBoard(Board):
    """MyBoard class"""
    baud_rate = DEFAULT_BAUD_RATE

    def __init__(self, board_port=None, baud_rate=DEFAULT_BAUD_RATE, server_address=None, server_port=None, wifi_ssid=None, wifi_password=None, username=None, name=None, message=None, actions=[]):
        self.board_port = board_port
        self.baud_rate = baud_rate
        self.server_address = server_address
        self.server_port = server_port
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password
        super().__init__(username, name, message, actions)

    def flash_micropython(self):
        print(INFO_RUN_ONCE)
        mp_helpers.install_ampy()
        mp_helpers.install_esptool()
        if self.board_port == None:
            print(INFO_PORT_MISSING)
            return
        mp_helpers.flash_micropython(self.board_port, self.baud_rate)

    def init_contuino(self):
        mp_helpers.generate_main(str(self))
        mp_helpers.deploy_main(self.board_port)

    def putty_serial_prompt(self):
        mp_helpers.serial_prompt(self.board_port, self.baud_rate)


class GpioAction(Action):

    def __init__(self, pin=None, event=None, sensor=None, sensor_code=None, analog=False, value=None):
        self.pin = pin
        self.analog = analog
        super().__init__(event, value, sensor, sensor_code)
