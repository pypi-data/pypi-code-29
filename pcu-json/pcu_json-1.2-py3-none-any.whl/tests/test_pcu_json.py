import unittest

from pcu_json.json_configuration import setKeys
from pcu_json.json_parser import JSONParser

class test_pcu_pdf(unittest.TestCase):

	def test_JSONParser(self):
		setKeys("_id\nname_fr")
		textfilename = JSONParser("data/test.json")
		try:
			textfile = open(textfilename,"r")
		except IOError:
			print('cannot open')
		else:
			text = textfile.read()
			print(text)
		self.assertIn('Scandi', text)
		textfile.close()

if __name__ == '__main__':
	unittest.main()