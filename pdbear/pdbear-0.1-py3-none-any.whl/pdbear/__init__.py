import glob
import re
import json
from stringfish import strexe

CONVTABLE = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7')
BASE = 32
MAX = BASE**4 - 1

class PDBearcoder():
	"""
	This class is used to rename a set of files from a unique folder to unique 4-characters 'PDB IDs' or vice-versa. It
	writes/loads the nametable in json.
	"""
	def __init__(self, infolder, outfolder, start_index, ext='pdb'):
		self.inf = infolder
		self.outf = outfolder
		self.st_i = start_index
		self.ext = ext
		self.ntf = dict()
		self.ntr = dict()

	def encode(self, basefilename):
		self.getpdbfilenames()
		self.makenametable()
		self.writent(basefilename + '_fwd.json', self.ntf)
		self.writent(basefilename + '_rev.json', self.ntr)
		self.copytofolder()

	def copytofolder(self):
		strexe('mkdir {0}'.format(self.outf))
		strexe('rm -r {0}/*'.format(self.outf))
		for f in self.ntf.keys():
			strexe('cp {0}/{1}.{2} {3}/{4}.{2}'.format(
				self.inf, f, self.ext, self.outf, self.ntf[f]))

	def decode(self, basefilename):
		self.ntf = self.readnt(basefilename + '_fwd.json')
		self.ntr = self.readnt(basefilename + '_rev.json')

	def writent(self, filename, data):
		with open(filename, "w") as f:
			f.write(json.dumps(data))

	def readnt(self, filename):
		with open(filename) as f:
			return json.loads(f.read())

	def getfn(self, code):
		return self.ntr[code]

	def getcode(self, fn):
		return self.ntf[fn]

	def makenametable(self):
		n = len(self.pdbfns)
		for i, fn in zip(range(self.st_i, self.st_i+n), sorted(self.pdbfns)):
			code = self.makecode(i)
			self.ntf[fn] = code
			self.ntr[code] = fn

	def makecode(self, i):
		"""
		Convert i to predefined BASE (32 for now), with encoding specified in CONVTABLE. Pad with 0s to be 4-letter.
		"""
		if i > MAX:
			raise Exception("trying to use an index greater than the maximum allowed ({0})".format(MAX))
		code = ""
		while i > 0:
			r = i % BASE
			i = i // BASE
			code = CONVTABLE[r] + code
		while len(code) < 4:
			code = CONVTABLE[0] + code
		return code

	def getpdbfilenames(self):
		self.pdbfns = []
		pdbfiles = glob.glob("{0}/*.{1}".format(self.inf, self.ext))
		for f in pdbfiles:
			p = r'.*/(.+)\.{0}$'.format(self.ext)
			name = re.search(p, f).groups()[0]
			self.pdbfns.append(name)

if __name__ == "__main__":
	inf = 'mir125aWT_2_d_2018.07.13_10h43'
	outf = 'testPDBFNE'
	si = 0
	tester = PDBearcoder(inf, outf, si)
	tester.getpdbfilenames()
	tester.encode('test')
	tester.decode('test')
	print(tester.ntr)




