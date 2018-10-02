# CONTUINO GENERATED CODE, EDIT TEMPLATE IN /templates/main_template.py
import network
import time
import urequests
import json
import machine

API_URL = "http://%s:%s/contuino/api/boards"
REMOVE_FIELDS_FOR_SERVER = ['wifi_ssid', 'wifi_password']

station = network.WLAN(network.STA_IF)
board_data = json.loads('{"board_port": "COM3", "baud_rate": 115200, "server_address": "192.168.0.11", "server_port": "", "wifi_ssid": "", "wifi_password": "", "username": "testhash", "name": "board name", "message": "board message", "actions": [{"pin": 2, "analog": false, "event": "Events.SHOOT", "value": null, "sensor": "Sensors.TOUCH", "sensor_code": "XXXX1234"}, {"pin": 0, "analog": true, "event": "Events.SHOOT", "value": null, "sensor": "Sensors.TOUCH", "sensor_code": "XXXX1234"}]}')

ANALOG_MAX_VALUE = 1024
ANALOG_MIN_VALUE = 0
STR_WIFI_CONNECT_ATTEMPT = "attempting to connect to wifi"
STR_CONNECTING_TO_WIFI = "connecting to wifi"
STR_SENDING_DATA = "sending data"


def ap_connect():
    print(STR_CONNECTING_TO_WIFI)
    if station.isconnected() == True:
        print("Connected to AP", board_data['ssid'])
        print("ifconfig", station.ifconfig())
        return

    station.active(True)
    station.connect(board_data['wifi_ssid'], board_data['wifi_password'])

    while station.isconnected() == False:
        print(STR_WIFI_CONNECT_ATTEMPT)
        pass


def send_data():
    try:
        r = urequests.post(API_URL % (board_data['server_address'], str(
            board_data['server_port'])), json=server_prepare_board_data(board_data))
        print(r.text)
        r.close()
    except Exception as e:  # TODO pep8 OSError, TypeError, IndexError
        print(str(e))
        pass


def server_prepare_board_data(board_data_dict):
    for action in board_data_dict['actions']:
        if action['analog']:
            pin = machine.ADC(int(action['pin']))
            analog_value = pin.read()
            action_value = round(normalize_analog(
                analog_value, ANALOG_MAX_VALUE, ANALOG_MIN_VALUE), 2)
        else:
            pin = machine.Pin(int(action['pin']), machine.Pin.IN)
            action_value = pin.value()
        action['value'] = action_value
    # TODO find simpler solution
    for field in REMOVE_FIELDS_FOR_SERVER:
        if field in board_data_dict:
            del board_data_dict[field]
    return board_data_dict


def game_loop():
    while(True):
        print(STR_SENDING_DATA)
        send_data()


def debug_board_data():
    while(True):
        print(board_data)
        print(server_prepare_board_data(board_data))
        time.sleep(1)


def normalize_analog(value, max_value, min_value):
    return (value - min_value) / (max_value - min_value)


# debug_board_data()
ap_connect()
game_loop()
