from flyt_python.flyt_python import DroneApiConnector
token = '38efbf1f2e474ac02759331edf841c3b3a14df92'
vehicle_id = 'QRDXGjru'

drone = DroneApiConnector(token,vehicle_id, ip_address='localhost',wait_for_drone_response =True)

# Initialize the drone's connection
drone.connect()

print("Taking Off")
drone.takeoff(5)

print("Getting Battery Status")

battery_status = drone.get_battery_status()
print("Voltage: ", battery_status['voltage'])
print("Current: ", battery_status['current'])
print("Remaining Battery Percentage: ", battery_status['remaining'])

#disconnect the drone
drone.disconnect()