import signal

from pdb import set_trace
from threading import Thread
from time import sleep

from os.path import exists

class super_debugger(object):
	"""
	Import:
		from super_debugger import super_debugger
	
	Usage:
		# The simplest basic usage:
		sd = super_debugger(turn_on_filepath='a.txt', sleeping_time=1) # sleeping time is 60 by default

		# To turn off debugger from scipt:
		sd.turn_off = True 

		# We can turn off debuger by file also, be_verbose=2 tell us what's going on with our thread
		super_debugger(turn_on_filepath='a.txt', turn_off_filepath='b.txt', sleeping_time=1, be_verbose=2)
		
		# We can call debugger by ctrl-c
		super_debugger(ctrl_c_turn_on=True, sleeping_time=2)
	"""

	def __init__(self, turn_on_filepath=None, turn_off_filepath=None, ctrl_c_turn_on=None, be_verbose=False, sleeping_time=60):

		if turn_on_filepath == None and ctrl_c_turn_on == None:
			raise ValueError("You have to define turn_on_filepath or keybord_shortcut_turn_on parameter.")

		self.turn_on_filepath = turn_on_filepath
		self.turn_off_filepath = turn_off_filepath

		self.ctrl_c_turn_on = ctrl_c_turn_on

		self.be_verbose = be_verbose
		self.sleeping_time = sleeping_time

		self.turn_off = False

		if self.ctrl_c_turn_on:
			signal.signal(signal.SIGINT, self.signal_handler)
		else:
			self.trigger_thread = Thread(target=self.trigger_loop, name='trigger_loop')
			self.trigger_thread.start()

			if self.be_verbose:
				print('super_debugger finished')

	def trigger_loop(self):

		if self.be_verbose:
			print('super_debugger started')

		while True:
			sleep(self.sleeping_time)

			if self.be_verbose:
				print('super_debugger is active')

			if self.turn_on_filepath:
				if exists(self.turn_on_filepath):
					self.debug()

			if self.turn_off_filepath:
				if exists(self.turn_off_filepath):
					return

			if self.turn_off:
				return

	def signal_handler(self, sig, frame):
		self.debug()

	def debug(self):
		if self.be_verbose:
			print('-' * 10, 'Super debugger:', '-' * 10)
		set_trace()

