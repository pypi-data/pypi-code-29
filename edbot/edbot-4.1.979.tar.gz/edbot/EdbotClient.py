#
# Edbot Python API.
#
# Copyright (c) Robots in Schools Ltd. All rights reserved.
#

import json
import threading
import http.client
import urllib.parse
import getpass
import copy
import time
import random

from ws4py.client.threadedclient import WebSocketClient

class EdbotClient(WebSocketClient):
	def __init__(self, server, port, client="Python"):
		self.client = client
		self.server = server
		self.port = port
		self.auth = "AUTH_NONE"
		self.data = {}
		self.name = "noname"
		self.bypass = False
		self.connected = False
		self.ready_event = threading.Event()
		self.active_event = {}
		self.motion_seq = random.randint(1000000,1000000000)
		self.motion_busy = {}
		self.motion_event = {}
		self.speech_seq = random.randint(1000000,1000000000)
		self.speech_busy = {}
		self.speech_event = {}
		self.callback = None

	###########################################################################
	#
	# Common functions.
	#
	###########################################################################

	def get_server(self):
		return self.server

	def get_port(self):
		return self.port

	def connect(self, callback=None):
		if not self.connected:
			self.callback = callback
			url = "ws://" + self.server + ":" + str(self.port) + "/api/reporter/" + \
				self.enc(getpass.getuser()) + "/" + self.enc(self.client) + "/2"
			WebSocketClient.__init__(self, url)
			WebSocketClient.connect(self)
			t = threading.Thread(target=self.run_forever)
			t.setDaemon(True)
			t.start()
			self.ready_event.wait()

	def disconnect(self):
		if self.connected:
			WebSocketClient.close(self, code=1000, reason="Closed by client")

	def get_edbot_names(self):
		return list(self.data["edbots"].keys())

	def get_edbot(self, name=None):
		if name is None:
			name = self.name
		return self.data["edbots"][name]

	def get_data(self):
		return self.data

	def is_active(self, name=None):
		if name is None:
			name = self.name
		if self.bypass is True:
			return True
		return self.data["edbots"][name]["activeUser"] == self.data["user"]

	def wait_until_active(self, name=None):
		if name is None:
			name = self.name
		if not self.is_active(name=name):
			self.active_event[name] = threading.Event()
			# Don't use the more efficient wait() - it isn't interruptible.
			while self.bypass is False and not self.active_event[name].is_set():
				time.sleep(0.1)
		return

	def set_edbot_name(self, name):
		if name in self.data["edbots"].keys():
			self.name = name
			return True
		else:
			return False

	def set_servo_torque(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/servo_torque/" + self.enc(name) + "/" + path)

	def set_servo_speed(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/servo_speed/" + self.enc(name) + "/" + path)

	def set_servo_position(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/servo_position/" + self.enc(name) + "/" + path)

	def say(self, text, wait=True, speech_seq=None, name=None):
		if speech_seq is None:
			self.speech_seq += 1
			speech_seq = self.speech_seq
		if name is None:
			name = self.name
		#
		# Check if we are waiting for this Edbot to finish speaking. If so, wait.
		# This could happen in a multi-threaded environment :-)
		#
		if name in self.speech_event.keys():
			self.speech_event[name].wait()
		url = "/api/say/" + self.enc(name) + "/" + self.enc(text);
		params = { "busy": speech_seq }
		if wait == False:
			return self.api_request(url, params)
		else:
			self.speech_busy[name] = speech_seq
			self.speech_event[name] = threading.Event()
			resp = self.api_request(url, params)
			if resp["success"] == True:
				self.speech_event[name].wait()
			else:
				self.speech_event[name].set()
			return resp

	def reset(self, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/reset/" + self.enc(name))

	def set_options(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/options/" + self.enc(name) + "/" + path)

	###########################################################################
	#
	# Edbot functions.
	#
	###########################################################################

	def run_motion(self, motion, wait=True, motion_seq=None, name=None):
		if motion_seq is None:
			self.motion_seq += 1
			motion_seq = self.motion_seq
		if name is None:
			name = self.name
		#
		# Check if we are waiting for this Edbot to finish a motion. If so, wait.
		# This could happen in a multi-threaded environment :-)
		#
		if name in self.motion_event.keys():
			self.motion_event[name].wait()
		url = "/api/motion/" + self.enc(name) + "/" + str(motion);
		params = { "busy": motion_seq }
		if wait == False:
			return self.api_request(url, params)
		else:
			self.motion_busy[name] = motion_seq
			self.motion_event[name] = threading.Event()
			resp = self.api_request(url, params)
			if resp["success"] == True:
				self.motion_event[name].wait()
			else:
				self.motion_event[name].set()
			return resp

	def set_servo_led(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/servo_led/" + self.enc(name) + "/" + path)

	def set_servo_pid(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/servo_pid/" + self.enc(name) + "/" + path)

	###########################################################################
	#
	# Edbot Dream functions.
	#
	###########################################################################

	def set_servo_mode(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/servo_mode/" + self.enc(name) + "/" + path)

	def set_buzzer(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/buzzer/" + self.enc(name) + "/" + path)	

	def set_custom(self, path, name=None):
		if name is None:
			name = self.name
		return self.api_request("/api/custom/" + self.enc(name) + "/" + path)

	###########################################################################
	#
	# Private.
	#
	###########################################################################

	def opened(self):
		self.connected = True

	def closed(self, code, reason=None):
		# Stop waiting.
		for name in self.motion_busy:
			self.motion_event[name].set()
		for name in self.speech_busy:
			self.speech_event[name].set()
		self.ready_event.set()

		# Reset status.
		self.connected = False
		self.auth = "AUTH_NONE"
		self.data = {}
		self.name = None

	def received_message(self, m):
		msg = json.loads(m.data.decode("UTF-8"))
		self.data = self.dict_merge(self.data, msg)
		if "auth" in self.data.keys():
			self.auth = self.data["auth"]
			self.ready_event.set()
		if "bypass" in self.data.keys():
			self.bypass = self.data["bypass"]
		for name in self.data["edbots"].keys():
			edbot = self.data["edbots"][name]
			if edbot["activeUser"] == self.data["user"]:
				try:
					self.active_event[name].set()
				except:
					pass	
			if edbot["connected"] == True:
				try:
					if edbot["reporters"]["motion-complete"] == self.motion_busy[name]:
						self.motion_event[name].set()
				except:
					pass
				try:
					if edbot["reporters"]["speech-complete"] == self.speech_busy[name]:
						self.speech_event[name].set()
				except:
					pass
			else:
				if name in self.motion_event:
					self.motion_event[name].set()
				if name in self.speech_event:
					self.speech_event[name].set()
		if self.callback is not None:
			self.callback(msg)

	def api_request(self, url, params=None):
		if params is not None:
			url = url + "?" + urllib.parse.urlencode(params)
		conn = http.client.HTTPConnection(self.server, self.port)
		conn.request("GET", url, headers={ "X-Edbot-Auth" : self.auth })
		response = conn.getresponse()
		data = response.read()
		conn.close()
		dic = json.loads(data.decode("UTF-8"))
		return dic["status"]

	def enc(self, str, safe=""):
		return urllib.parse.quote(str, safe)

	def dict_merge(self, target, *args):
		# Merge multiple dicts.
		if len(args) > 1:
			for obj in args:
				self.dict_merge(target, obj)
			return target

		# Recursively merge dicts and set non-dict values.
		obj = args[0]
		if not isinstance(obj, dict):
			return obj
		for k, v in obj.items():
			if v is None:
				target[k] = None
			elif k in target and isinstance(target[k], dict):
				self.dict_merge(target[k], v)
			else:
				target[k] = v
		return target