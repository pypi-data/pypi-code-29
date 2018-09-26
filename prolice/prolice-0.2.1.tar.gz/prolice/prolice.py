#!/usr/bin/evn python3

import pyftdi.gpio
import pyftdi.ftdi
import pyftdi.spi
from spiflash.serialflash import SerialFlashManager

import halo

import sys
import time
import datetime
import argparse

# Add tools
pyftdi.ftdi.Ftdi.add_custom_vendor(0x15ba, "olimex")
pyftdi.ftdi.Ftdi.add_custom_product(0x15ba, 0x002b, "arm-usb-ocd-h")

# Create spinner
spinner = halo.Halo()

parser = argparse.ArgumentParser()
parser.add_argument("file",
					help="Path to firmware file")
args = parser.parse_args()

class FlasherError(Exception):
	def __init__(self, message):
		super().__init__(message)

class Flasher:

	def __init__(self):
		try:
			spinner.start("Opening ARM-USB-OCD-H")
			self.__spi = pyftdi.spi.SpiController(cs_count=1)
			self.__spi.configure("ftdi://olimex:arm-usb-ocd-h/1")
			spinner.succeed()
		except pyftdi.usbtools.UsbToolsError as e:
			spinner.fail()
			print("    {}".format(e))
			sys.exit(1)

		spinner.start("Preparing hardware")

		# Claim interface and gpios
		self.__slave = self.__spi.get_port(cs=0, freq=1E6, mode=0)
		self.__gpio = self.__spi.get_gpio()
		self.__flash = None

		# Define GPIOS
		self.__ENABLE = 4
		self.__CDONE = 7
		self.__CRESET = 8
		self.__LED = 11

		# Configure GPIOS
		dir = (1 << self.__ENABLE) | (1 << self.__LED) | (1 << self.__CRESET)
		self.__gpio.set_direction(dir, dir)
		self.__gpio.write((1 << self.__ENABLE))
		spinner.succeed()


	def __enable_buffers(self):
		self.__gpio.write((self.__gpio.read() & 0xF7EF) | (1 << self.__LED))

	def __disable_buffers(self):
		self.__gpio.write((self.__gpio.read() & 0xF7EF) | (1 << self.__ENABLE))

	def __get_cdone(self):
		return bool(self.__gpio.read() & (1 << self.__CDONE))

	def __set_creset(self, reset):
		self.__gpio.write((self.__gpio.read() & 0xFEFF) | (reset << self.__CRESET))


	def __claim_bus(self):
		'''
		'''
		start = datetime.datetime.now()

		# Enable buffers
		self.__enable_buffers()

		# Reset iCE40
		while True:
			self.__set_creset(0)
			time.sleep(0.001)
			self.__set_creset(1)
			time.sleep(0.001)
			self.__set_creset(0)
			time.sleep(0.25)

			# Check cdone
			if self.__get_cdone() == False:
				break

			if (datetime.datetime.now() - start)/datetime.timedelta(seconds=1) > 5:
				spinner.fail()
				raise FlasherError("Failed claiming the SPI bus")

	def __release_bus(self):
		# Disable buffers
		self.__disable_buffers()



	def init(self):
		'''
		Detect flash chip
		'''

		spinner.start("Detecting flash chip")
		try:
			self.__claim_bus()
			self.__flash = SerialFlashManager._get_flash(self.__slave, SerialFlashManager.read_jedec_id(self.__slave))
			self.__release_bus()
			spinner.succeed()
			print("    Found {}".format(self.__flash))
		except Exception as e:
			spinner.fail()
			print("    {}".format(e))
			sys.exit(1)



	def erase(self):
		'''
		'''

		spinner.start("Erasing the flash chip")
		try:
			self.__claim_bus()
			# self.__flash.erase(0, len(self.__flash))
			self.__flash.erase(0, (1 << 16))
			self.__release_bus()
			spinner.succeed()
		except Exception as e:
			spinner.fail()
			print("    {}".format(e))
			sys.exit(1)


	def flash(self, file):
		spinner.start("Flashing device")
		try:
			with open(file, 'rb') as f:
				data = f.read()

			# Pad data
			pad = 256 - (len(data) % 256)
			data = data + bytes([0xFF] * pad)

			self.__claim_bus()
			for addr in range(0, len(data), 256):
				spinner.text = "Flashing device (0x{:06x})".format(addr)
				self.__flash.write(addr, data[addr:addr + 256])
			self.__release_bus()

			spinner.succeed("Flashing device")

		except Exception as e:
			spinner.fail()
			print("    {}".format(e))
			sys.exit(1)

def main():
	f = Flasher()
	f.init()
	f.erase()
	f.flash(args.file)

if __name__ == "__main__":
	main()
