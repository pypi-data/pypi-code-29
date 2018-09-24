from __future__ import print_function
from .usbtmc import Usbtmc
import time


# class DCload_array_3720a(object):
class DC_Load_Array_3720a(object):
    class Mode:
        CCL = "CCL"
        CCH = "CCH"
        CV = "CV"
        CPC = "CPC"
        CPV = "CPV"
        CRL = "CRL"
        CRM = "CRM"
        CRH = "CRH"
        
    def __init__(self, device_file):
        self.device = Usbtmc(device_file)
        self.name = self.device.get_name()

        print(self.name)

    def _write(self, command):
        """Send an arbitrary command directly to the load"""
        self.device.write_str(command)        
        # time.sleep(0.1)

    def _read(self, length):
        """Read an arbitrary amount of data directly from the scope"""
        return self.device.read(length)

    def _read_str(self, length):
        """Read an arbitrary amount of data directly from the scope"""
        return self.device.read_str(length)
    
    def reset(self):
        """Reset the instrument"""
        self.device.send_reset()
      
        
    def set_mode(self, mode):
        self._write(":MODE {0}".format(mode))
        
    def set_current(self, level):
        """Set current in A"""
        self._write(":CURR {0}A".format(level))

    def set_voltage(self, level):
        """Set Voltage in A"""
        self._write(":VOLT {0}V".format(level))

    def set_resistance(self, level):
        """Set resistance in Ohms"""
        self._write(":RES {0}Ω".format(level))

    def set_power(self, level):
        """Set resistance in W"""
        self._write(":POW {0}W".format(level))
        
        
    def input_enable(self):
        self._write(":INP ON")
        # time.sleep(0.1)

    def input_disable(self):
        self._write(":INP OFF")

    def _read_measurement(self, quantity):
        # self.device.write(":MEAS:{0}?".format(quantity))
        self._write(":MEAS:{0}?".format(quantity))
        return float(self._read_str(9000))

    def get_current(self):
        return self._read_measurement("CURR")

    def get_voltage(self):
        return self._read_measurement("VOLT")

    def get_resistance(self):
        return self._read_measurement("RES")

    def get_power(self):
        return self._read_measurement("POW")
    
    
