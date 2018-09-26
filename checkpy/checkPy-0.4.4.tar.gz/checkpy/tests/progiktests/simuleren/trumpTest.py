import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def throwAvg(test):
	def testMethod():
		throw = lib.getFunction("throw", _fileName)
		n = 10000
		s = sum(throw() for i in range(n))
		return asserts.between(s / n, 6.5, 7.5)

	test.test = testMethod
	test.description = lambda : "throw() returns 7 on average"

@t.test(10)
def throwNums(test):
	def testMethod():
		throw = lib.getFunction("throw", _fileName)
		return asserts.containsOnly([throw() for i in range(10000)], list(range(2,13)))

	test.test = testMethod
	test.description = lambda : "throw() returns only the numbers 2 to 12"

@t.test(15)
def throwEvenDist(test):
	def testMethod():
		throw = lib.getFunction("throw", _fileName)
		throws = [throw() for i in range(100000)]
		dist = [0] * 13
		for t in throws:
			if 0 <= t < 13:
				dist[t] += 1
		return (dist[2] * 3) < dist[7] and dist[2] != 0

	test.test = testMethod
	test.description = lambda : "throw() returns some occurences (7) more than others (2)"

@t.test(20)
def possessionType(test):
	def testMethod():
		import monopoly
		possession = lib.getFunction("possession", _fileName)
		return asserts.sameType(possession(monopoly.Board()), dict())

	test.test = testMethod
	test.description = lambda : "possession() returns a dictionary"

@t.test(30)
def possessionKeys(test):
	def testMethod():
		import monopoly
		possession = lib.getFunction("possession", _fileName)
		correct = {
			'dorpstraat': False, 'brink': False,
			'station zuid': False, 'steenstraat': False,
			'ketelstraat': False, 'velperplein': False,
			'barteljorisstraat': False, 'elecriciteitsbedrijf': False,
			'zijlweg': False, 'houtstraat': False,
			'station west': False, 'neude': False,
			'biltstraat': False, 'vreeburg': False,
			'a-kerkhof': False, 'groote markt': False,
			'heerestraat': False, 'station noord': False,
			'spui': False, 'plein': False,
			'waterleiding': False, 'lange poten': False,
			'hofplein': False, 'blaak': False,
			'coolsingel': False, 'station oost': False,
			'leidschestraat': False, 'kalverstraat': False
		}
		return asserts.exact(set(possession(monopoly.Board()).keys()), set(correct.keys()))

	test.test = testMethod
	test.description = lambda : "possession() returns a dictionary with the correct keys"

@t.test(40)
def possessionValues(test):
	def testMethod():
		import monopoly
		possession = lib.getFunction("possession", _fileName)
		return asserts.containsOnly(possession(monopoly.Board()).values(), [False])

	test.test = testMethod
	test.description = lambda : "possession() returns a dictionary where all values are False"

@t.test(100)
def correct(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 0)
		return asserts.numberOnLine(147, line, deviation = 5), "hint: make sure the number of throws is on the first line of the output"

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws to buy everything"
	test.timeout = lambda : 30
