import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def isResistentAAA(test):
	def testMethod():
		isResistent = lib.getFunction("isResistent", _fileName)
		return asserts.exact(isResistent("AAA"), True)

	test.test = testMethod
	test.description = lambda : "isResistent(\"AAA\") produces True"

@t.test(10)
def isResistentAAGGAA(test):
	def testMethod():
		isResistent = lib.getFunction("isResistent", _fileName)
		return asserts.exact(isResistent("AAGGAA"), False)

	test.test = testMethod
	test.description = lambda : "isResistent(\"AAGGAA\") produces False"

@t.test(20)
def isResistentATGCAATGCAATGGGCCCCTTTAAACCCT(test):
	def testMethod():
		isResistent = lib.getFunction("isResistent", _fileName)
		return asserts.exact(isResistent("ATGCAATGCAATGGGCCCCTTTAAACCCT"), True)

	test.test = testMethod
	test.description = lambda : "isResistent(\"ATGCAATGCAATGGGCCCCTTTAAACCCT\") produces True"

@t.test(30)
def simulateLength(test):
	def testMethod():
		simulate = lib.getFunction("simulate", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		return asserts.exact(len(simulate(viruses, 0, 0, 0, 100, 500)), 501)

	test.test = testMethod
	test.description = lambda : "simulate() produces a list of the correct length"

@t.test(40)
def simulateFluctuations(test):
	def testMethod():
		simulate = lib.getFunction("simulate", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		return asserts.containsOnly(simulate(viruses, 0, 0, 0, 100, 500), [100])

	test.test = testMethod
	test.description = lambda : "simulate(viruses, 0, 0, 0, 100) shows no fluctuations in population size"

@t.test(50)
def simulateAvg(test):
	def testMethod():
		simulate = lib.getFunction("simulate", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		n = 100
		timesteps = 1000
		avg = sum(sum(simulate(viruses[:], 0.1, 0.1, 0.5, 100, timesteps)) / timesteps for i in range(n)) / n
		return asserts.between(avg, 50, 75)

	test.test = testMethod
	test.description = lambda : "simulate(viruses, 0.1, 0.1, 0.5, 100)) is correct"
	test.timeout = lambda : 60

@t.test(60)
def experimentCorrect(test):
	def testMethod():
		experiment = lib.getFunction("experiment", _fileName)
		avg = experiment(100)
		return asserts.between(avg, 33, 99)

	test.test = testMethod
	test.description = lambda : "experiment() is correct"
	test.timeout = lambda : 60
