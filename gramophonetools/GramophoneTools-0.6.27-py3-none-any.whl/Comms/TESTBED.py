import Gramophone
from time import sleep

grams = Gramophone.find_devices()

G = grams[0xa0002]
G.verbose = True
G.ping()
G.read_firmware_info()
G.read_product_info()
G.read_dev_state()
vel = G.read_param(0x11)
print('The velocity was', vel)
G.read_sensors()
G.read_time()
G.read_position()
G.read_velocity()
G.read_output(2)

print()
G.read_params(0xAA)
G.read_voltages()

print()
G.read_time()
G.reset_time()
G.read_time()

# print()
# G.start_burst(1, 0.1, 0.1)
# sleep(1)
# G.stop_burst(1)

print()
G.start_reader(name='pos', param='recorder', freq=5)
# G.start_reader(name='vel', param='velocity', freq=10)
sleep(2)
G.stop_reader(name=None)
