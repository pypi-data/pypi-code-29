def get_gpio_driver():
    from . import gpio_driver
    return gpio_driver.GPIODriver()

def get_i2c_driver(address, bus):
    from . import i2c_driver
    return i2c_driver.I2CDeviceDriver(address, bus)

def get_one_wire_driver(address):
    from . import one_wire
    return one_wire.OneWireDeviceDriver(address)

def default_i2c_bus():
    return 0

def get_camera_driver(source):
    from . import camera_driver
    return camera_driver.CameraDriver()

def service_commands(commands, app_name, app_id, script_path):
    print("rpi service commands: ", commands, app_name, app_id, script_path)
    from . import service
    service.handle_command(commands, app_name, app_id, script_path)

def get_user_inputs():
    import inputs
    return inputs.devices

def getrevision():
  # Extract board revision from cpuinfo file
  my_revision = "?"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:8]=='Revision':
        length=len(line)
        my_revision = line[11:length-1]
    f.close()
  except:
    my_revision = "?"
 
  return my_revision

def detect_devices():
    import inputs

    import subprocess
    c = subprocess.check_output(["vcgencmd", "get_camera"])
    c = c[:-1].decode("utf-8")
    cam = ""
    try:
        c.index("supported=1")
        try:
            c.index("detected=1")
            cam = "connected"
        except ValueError:
            cam = "not connected"
    except ValueError:
        cam = "not enabled in raspi config"
        
        

    input_devices = {}
    for device in inputs.devices:
        type = None
        if isinstance(device, inputs.Keyboard):
            type = "keyboard"
        if isinstance(device, inputs.Mouse):
            type = "mouse"
        if isinstance(device, inputs.GamePad):
            type = "game_pad"

        if isinstance(device, inputs.OtherDevice):
            type = "other_device"

        if type:
            if not type in input_devices.keys():
                input_devices[type] = [] 
            input_devices[type] += [{
                "name": device.name,
                "path": "?" #device.get_char_device_path()
            }]
    
    return {
        "Hardware platform": [{
            "name": "Raspberry pi",
            "revision": getrevision()
        }],
        "inputs": input_devices,
        "cams":{
            "PI Camera" : cam
        }
    }