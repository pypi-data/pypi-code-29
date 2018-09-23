import serial
import time
import sys

class RelaysManager():
    # Convert '11' to b'\x11'
    @staticmethod
    def toHexByte(instr):
        return bytes(hex(int(str(instr), 16)), 'ascii')

    @staticmethod
    def initRelay(serialCOM):
        time.sleep(1)
        serialCOM.write(RelaysManager.toHexByte('50'))
        time.sleep(0.5)
        serialCOM.write(RelaysManager.toHexByte('51'))

    @staticmethod
    def openRelay(serialCOM, relayNumber):
        initRelay(serialCOM)
        serialCOM.write(RelaysManager.toHexByte('0'+str(relayNumber)))
        time.sleep(1)

    @staticmethod
    def closeRelay(serialCOM, relayNumber):
        initRelay(serialCOM)
        serialCOM.write(RelaysManager.toHexByte('1'+str(relayNumber)))
        time.sleep(1)


if __name__ == '__main__':
    # Example : python relays.py /dev/ttyUSB0
    if len(sys.argv) is 2:
        serialCOM = serial.Serial(sys.argv[1], 9600)
        initRelay(serialCOM)
        openRelay(serialCOM, 1)
