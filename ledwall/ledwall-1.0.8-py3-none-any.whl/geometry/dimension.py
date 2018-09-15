class Dimension( object ):

	def __init__(self, width, height):
		self._width  = int(width)
		self._height = int(height)

	@property
	def height(self):
		return self._height

	@property
	def width(self):
		return self._width

	def __iter__(self):
		yield self._width
		yield self._height

	def __len__(self):
		return 2

	def __repr__(self):
		return "Dimension({:d},{:d})".format(self._width, self._height)

	def __str__(self):
		return "({:d},{:d})".format(self._width, self._height)
		