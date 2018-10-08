#!/usr/bin/evn python3

import pyftdi.ftdi
import pyftdi.usbtools
from spiflash.serialflash import SerialFlashManager

from . import tools

import halo

import argparse
import datetime
import sys
import time

# Add tools
pyftdi.ftdi.Ftdi.add_custom_vendor(0x15ba, "olimex")
pyftdi.ftdi.Ftdi.add_custom_product(0x15ba, 0x002b, "arm-usb-ocd-h")
pyftdi.ftdi.Ftdi.add_custom_product(0x15ba, 0x002a, "arm-usb-tiny-h")

# Create spinner
spinner = halo.Halo()

# Global variables
tool = None
flash = None

# Create arguments
parser = argparse.ArgumentParser()
parser.add_argument("file",
					help="Path to firmware file")
parser.add_argument("-t", "--tool",
					action="store",
					choices=["arm-usb-ocd-h", "arm-usb-tiny-h"],
					help="Manual select flasher tool")
args = parser.parse_args()


def detect_flash():
	global flash
	spinner.start("Detecting flash chip")
	try:
		tool.claim_bus()
		flash = SerialFlashManager._get_flash(tool._slave, SerialFlashManager.read_jedec_id(tool._slave))
		tool.release_bus()
		spinner.succeed()
		print("    Found {}".format(flash))
	except Exception as e:
		spinner.fail()
		print("    {}".format(e))
		cleanup()
		sys.exit(1)


def write_flash(file):
	try:
		with open(file, 'rb') as f:
			data = f.read()

		# Pad data
		pad = 4096 - (len(data) % 4096)
		data = data + bytes([0xFF] * pad)

		tool.claim_bus()

		# Erase the device
		spinner.start("Erasing the flash chip")
		flash.erase(0, len(data))
		spinner.succeed()

		spinner.start("Writting the flash chip")
		for addr in range(0, len(data), 256):
			spinner.text = "Writting the flash chip (0x{:06x})".format(addr)
			flash.write(addr, data[addr:addr + 256])
		tool.release_bus()
		spinner.succeed("Writting the flash chip")

	except Exception as e:
		spinner.fail()
		print("    {}".format(e))
		cleanup()
		sys.exit(1)

def initialize_hardware():
	global tool
	try:
		if args.tool == "arm-usb-ocd-h":
			spinner.start("Searching for ARM-USB-OCD-H")
			tool = tools.ARM_USB_OCD_H()
		elif args.tool == "arm-usb-tiny-h":
			spinner.start("Searching for ARM-USB-TINY-H")
			tool = tools.ARM_USB_TINY_H()
		else:
			try:
				spinner.start("Searching for ARM-USB-OCD-H")
				tool = tools.ARM_USB_OCD_H()
			except Exception as e:
				spinner.fail()
				print("    {}".format(e))
				try:
					spinner.start("Searching for ARM-USB-TINY-H")
					tool = tools.ARM_USB_TINY_H()
				except Exception as e:
					spinner.fail()
					print("    {}".format(e))
					sys.exit(1)
		spinner.succeed()
	except Exception as e:
		spinner.fail()
		print("    {}".format(e))
		cleanup()
		sys.exit(1)

def main():
	initialize_hardware()
	detect_flash()
	write_flash(args.file)
	tool._spi_controller.terminate()

def cleanup():
	spinner.start("Cleaning up")
	time.sleep(0.1)
	if tool:
		tool.release_bus()
		tool._spi_controller.terminate()
	spinner.succeed()

if __name__ == "__main__":
	main()
