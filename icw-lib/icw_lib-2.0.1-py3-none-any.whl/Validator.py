import re
class Validator(object):
	# Validator contstruct.
	def __init__(self, arg):
		super(Validator, self).__init__()
		self.link = arg

	# Método que valida contra una expresión regular si el link proviene de una foto de Instagram.
	def Validate(self):
		regex = r"(?:(?:http|https):\/\/)?(?:www.)?(?:instagram.com|instagr.am)\/([A-Za-z0-9-_]+)"
		if re.match(regex, self.link):
			return True
		else:
			return False
	pass
		