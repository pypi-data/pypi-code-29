
__all__ = [ 'Translator' ]

class Translator(object):
	def __init__(self, table, defaultSuffix=None):
		# Column 1 in text, column 2 is code
		self.table=table
		self.defaultSuffix=defaultSuffix
		
		self.t12={entry[0]: entry[1] for entry in table}
		self.t21={entry[1]: entry[0] for entry in table}
	
	def toCode(self, text):
		return self.t12[text]

	def toText(self, text):
		if self.defaultSuffix is not None and text not in self.t21:
			return text+self.defaultSuffix
		else:
			return self.t21[text]
	
