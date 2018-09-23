import json
from datetime import timedelta

# Urls
# dev: http://localhost:8080/sg-1
# prod: https://smart.gardena.com
# prod: https://sg-api.dss.husqvarnagroup.net/sg-1
#BASE_URL = 'http://one.home:6061/sg-1'
BASE_URL = 'https://sg-api.dss.husqvarnagroup.net/sg-1'

# Paths
SESSIONS_URL = BASE_URL + '/sessions'
LOCATIONS_URL = BASE_URL + '/locations'
DEVICES_URL = BASE_URL + '/devices'

COMMAND_URL = DEVICES_URL + "/%s/abilities/%s/command?locationId=%s"
PROPERTIES_URL = DEVICES_URL + "/%s/abilities/%s/properties/%s?locationId=%s"
SETTINGS_URL = DEVICES_URL + "/%s/settings/%s?locationId=%s"

# refresh timeout
REFRESH_TIMEOUT = timedelta(minutes=30)

# Commands
# Mower
CMD_MOWER_PARK_UNTIL_NEXT_TIMER = {'name': 'park_until_next_timer'}
CMD_MOWER_PARK_UNTIL_FURTHER_NOTICE = {'name': 'park_until_further_notice'}
CMD_MOWER_START_RESUME_SCHEDULE = {'name': 'start_resume_schedule'}
CMD_MOWER_START_24HOURS = {
    'name': 'start_override_timer', 'parameters': {'duration': 1440}}
CMD_MOWER_START_3DAYS = {
    'name': 'start_override_timer', 'parameters': {'duration': 4320}}

# Sensors
CMD_SENSOR_MEASURE_AMBIENT_TEMPERATURE = {'name': 'measure_ambient_temperature'}
CMD_SENSOR_MEASURE_SOIL_TEMPERATURE = {'name': 'measure_soil_temperature'}
CMD_SENSOR_MEASURE_SOIL_HUMIDITY = {'name': 'measure_soil_humidity'}
CMD_SENSOR_MEASURE_LIGHT = {'name': 'measure_light'}
CMD_SENSOR_MEASURE_HUMIDITY = {'name': 'measure_humidity'}

# Watering computer
CMD_WATERINGCOMPUTER_START_30MIN = {
    'name': 'manual_override', 'parameters': {'duration': 30}}
CMD_WATERINGCOMPUTER_STOP = {'name': 'cancel_override'}
# # irrigation control
# WATERING_TIMER_VALVE_1,
# WATERING_TIMER_VALVE_2,
# WATERING_TIMER_VALVE_3,
# WATERING_TIMER_VALVE_4,
# WATERING_TIMER_VALVE_5,
# WATERING_TIMER_VALVE_6;

# Outlet
CMD_OUTLET_MANUAL_OVERRIDE_TIME = {'name': "outlet_manual_override_time"}
CMD_OUTLET_VALUE = {'name': 'outlet_valve'}

# Power
CMD_POWER_TIMER = {"properties":{'name':'power_timer'}}
CMD_POWER_START = {"properties":{'name':'power_timer','value':'on'}}
CMD_POWER_STOP = {"properties":{'name':'power_timer','value':'off'}}

# power control
# https://smart.gardena.com/sg-1/devices/e4047b42-2967-4b8f-be1a-2a97a1fe6bcc/abilities/power/properties/power_timer?locationId=3c3cc3ab-8f71-4850-a426-01d259f4a14b
# off
# {"properties":{"name":"power_timer","value":"off","timestamp":"2018-09-13T18:08:34.723Z","at_bound":null,"unit":null,"writeable":true,"supported_values":[],"ability":"cc0c4d53-4503-3a77-a3a6-b0501240640c"}}
# on
# {"properties":{"name":"power_timer","value":"on","timestamp":"2018-08-21T10:05:03.220Z","at_bound":null,"unit":null,"writeable":true,"supported_values":[],"ability":"cc0c4d53-4503-3a77-a3a6-b0501240640c"}}
# create and delete schedules
# HTTP Delete:
# https://smart.gardena.com/sg-1/devices/e4047b42-2967-4b8f-be1a-2a97a1fe6bcc/scheduled_events/2c31f5bb-f7cb-4c3e-bc47-2c5386d6b66d?locationId=3c3cc3ab-8f71-4850-a426-01d259f4a14b
# HTTP: POST
# https://smart.gardena.com/sg-1/devices/e4047b42-2967-4b8f-be1a-2a97a1fe6bcc/scheduled_events?locationId=3c3cc3ab-8f71-4850-a426-01d259f4a14b
# {"scheduled_events":{"start_at":"12:00","end_at":"12:30","recurrence":{"type":"weekly","weekdays":["friday"]},"valve_id":null,"device":"e4047b42-2967-4b8f-be1a-2a97a1fe6bcc"}}
