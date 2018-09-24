from .usbtmc import Usbtmc
import time

from bennellickeng.kitdrivers.usbtmc.usbtmc import Usbtmc

class Multi_Meter_dmm6500(object):
    """ A driver for the Kielthley DMM65500 multimeter
    """
    class Mode:
        """ Utility for various commands that use a mode string
            e.g. CURR: ... VOLT: ...
        """
        CURRENT    = 0
        RESISTANCE = 1
        VOLTAGE    = 2

        @staticmethod
        def string(mode):
            if mode == Multi_Meter_dmm6500.Mode.CURRENT:
                return "CURR"

            if mode == Multi_Meter_dmm6500.Mode.RESISTANCE:
                return "RES"

            if mode == Multi_Meter_dmm6500.Mode.VOLTAGE:
                return "VOLT"

            return "UNKNOWN_MODE"

    def __init__(self, serial_number, mode):
        """ Connect to usbtmc and setup our internal mode string """
        self.device = Usbtmc.from_serial_number(serial_number)
        self.name = self.device.get_name()
        self.set_mode(mode)

        print(self.name)
        print("Mode '{0}'".format(self.mode_str))

    def set_mode(self, mode):
        """ Set our mode string and setup the device to
            the correct mode
        """
        self.mode_str = Multi_Meter_dmm6500.Mode.string(mode)
        self.device.write_str("SENS:FUNC \"{0}\"".format(self.mode_str))

    def send_reset(self):
        """ Reset device to initial default state"""
        self.device.send_reset()

    def set_power_line_sync(self, is_on):
        """ Set the power line sync for our mode """
        self.device.write_str("{0}:LINE:SYNC {1}".format(
            self.mode_str, "ON" if is_on else "OFF"            
        ))

    def set_nplc(self, rate):
        """ set power line rate for our mode """
        self.device.write_str("{0}:NPLC {1}".format(
            self.mode_str, rate
        ))

    def wait_for_trigger_then_measure(self, sleep_time=0.01):
        """ Wait for an input trigger then do a single
            measurement into our default buffer
        
            note: sleeps for a small time to ensure the trigger 
            is active
        """
        # we start by defining our trigger model
        # clear any old model
        self.device.write_str("TRIG:LOAD \"EMPTY\"")

        # TRIG:BLOC:BUFF:CLEAR 1

        # clear any unflushed EXT events
        self.device.write_str("TRIG:EXT:IN:CLEAR")

        # listen for rising edge trigger
        self.device.write_str("TRIG:EXT:IN:EDGE RIS")

        # wait for the EXT event
        self.device.write_str("TRIG:BLOC:WAIT 1, EXT")

        # perform one measurement
        self.device.write_str("TRIG:BLOC:MDIG 2, \"defbuffer1\", 1")

        # start the above trigger model
        self.device.write_str("INIT")
        self.device.write_str("*WAI")

        time.sleep(sleep_time)

    def send_trigger_then_measure(self):
        """ Notify an output trigger then do a single 
            measurement
        """
        self.device.write_str("TRIG:LOAD \"EMPTY\"")

        # set our external out stimulus to be 'NOTIFY1'
        self.device.write_str("TRIG:EXT:OUT:STIM NOT1")

        # send 'NOTIFY1'
        # it is my understanding that this should wait 
        # for and ACK from EXT to carry on as per the 'Trigger Model'
        # 
        # From 9-36 in the reference:
        #   "If ... is connected to another instrument, this causes 
        #   the trigger execution to wait fo rthe other instrument 
        #   to indicate that is is ready"
        self.device.write_str("TRIG:BLOC:NOT 1, 1")

        # perform a reading
        self.device.write_str("TRIG:BLOC:MDIG 2, \"defbuffer1\", 1")

        self.device.write_str("INIT")
        self.device.write_str("*WAI")

    def read_single_value(self):
        """ read a single value from the default 
            buffer and return it as a float
        """
        self.device.write_str("TRAC:DATA? 1, 1")
        return float(self.device.read_str(9000))

