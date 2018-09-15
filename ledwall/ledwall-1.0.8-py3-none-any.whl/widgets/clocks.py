from datetime import datetime

class Clock(object):
	def __init__(self):
		self._x = 0
		self._y = 0
		
		self._hourColorHigh    = (128,0,128)
		self._hourColorLow     = (5,0,5)
		
		self._minuteColorHigh  = (0,128,128)
		self._minuteColorLow   = (0,5,5)

		self._secondColorHigh  = (0,128,0)
		self._secondColorLow   = (0,5,0)

		self._display = None

	@property
	def hourColor(self):
		return (self._hourColorHigh, self._hourColorLow)

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, value):
		self._y = value

	@property
	def position(self):
		return (self.x, self.y)	

	@property
	def display(self):
		return self._display

	@display.setter
	def display(self, display):
		self._display = display

	def update(self, update):
		pass

class BinaryCodedSexagesimalClock(Clock):
	def __init__(self, x, y):
		Clock.__init__(self)
		self.x = x
		self.y = y

	def update(self, update=False):
		d  = self.display
		if not d:
			return

		t = datetime.now()
		d.write_bitmask(self.y, t.hour, self._hourColorHigh, self._hourColorLow)
		d.write_bitmask(self.y + 1, t.minute, self._minuteColorHigh, self._minuteColorLow)
		d.write_bitmask(self.y + 2, t.second, self._secondColorHigh, self._secondColorLow)
		d.update(update)


