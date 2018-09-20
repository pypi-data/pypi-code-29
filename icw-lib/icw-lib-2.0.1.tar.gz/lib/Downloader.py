import os.path
import random
import requests
import urllib.request

class Downloader(object):
	def __init__(self, link, filename):
		super(Downloader, self).__init__()
		self.link = link
		filename = filename

		if filename is False:
			self.filename = str(random.randint(50, 1000))
		else
			self.filename = filename
	pass
	
	# Descarga del archivo.
	def Download(self):
		route = "images/"
		saver = self.Saver()

		if saver == False:
			fullname = route + self.AddSufix(self.filename)
		else:
			fullname = route + self.AddSufix(saver)

		process  = urllib.request.urlretrieve(self.link, fullname)
	pass

	# Revisa si el archivo ha sido escrito anteriormente.
	def Saver(self):
		route = "images/" + self.AddSufix(self.filename)
		if os.path.exists(route):
			return self.filename + str(random.randint(0, 10000))
		else: 
			return False;
	pass

	# Añade un sufijo al nombre
	def AddSufix(self, arg):
		return arg + ".jpg"
	pass





