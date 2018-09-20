import sys
import requests
import urllib.request
from bs4 import BeautifulSoup

class Crawler(object):
	def __init__(self, link):
		super(Crawler, self).__init__()
		self.link = link
	pass

	# Recibe el codigo fuente directo del enlace.
	def Crawl(self):
		source = requests.get(self.link)
		plain  = source.text
		soup   = BeautifulSoup(plain, 'html5lib')
		return soup
	pass

	# Busca y devuelve el enlace directo del codigo fuente.
	def GetLink(self, soupper):
		for line in soupper.findAll('meta', {'property': 'og:image'}):
			link = line.get('content')
			return link
	pass

	# Busca y devuelve el nombre de la cuenta desde el codigo fuente.
	def GetAccountname(self, soupper):
		for line in soupper.findAll('meta', {'property': 'og:description'}):
			account = line.get('content')

			clean_first  = account.split('(')
			clean_second = clean_first[1].split(',')

			clean_third  = clean_second[0].split(')')
			clean_arroba = clean_third[0].split('@')

			clean        = clean_arroba[1]
			return clean
	pass
		