import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def generateVirusLength(test):
	def testMethod():
		generateVirus = lib.getFunction("generateVirus", _fileName)
		return asserts.sameLength(generateVirus(5), "A" * 5) and asserts.sameLength(generateVirus(10), "A" * 10)

	test.test = testMethod
	test.description = lambda : "generateVirus() produces viruses of the specified length"

@t.test(10)
def generateVirusElements(test):
	def testMethod():
		generateVirus = lib.getFunction("generateVirus", _fileName)
		pairs = "".join([generateVirus(10) for _ in range(1000)])
		return asserts.containsOnly(pairs, "AGTC")

	test.test = testMethod
	test.description = lambda : "generateVirus() produces viruses consisting only of A, T, G and C"

@t.test(20)
def mutateElements(test):
	def testMethod():
		mutate = lib.getFunction("mutate", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 100
		pairs = "".join([mutate(v) for v in viruses])
		return asserts.containsOnly(pairs, "AGTC")

	test.test = testMethod
	test.description = lambda : "mutate() produces viruses consisting only of A, T, G and C"

@t.test(30)
def mutateLength(test):
	def testMethod():
		mutate = lib.getFunction("mutate", _fileName)
		return all(asserts.sameLength(mutate("A" * i), "A" * i) for i in range(1, 100))

	test.test = testMethod
	test.description = lambda : "mutate() produces viruses of the same length as the parent"

@t.test(40)
def mutateOneDifference(test):
	def testMethod():
		offByOne = lambda col1, col2 : sum(a != b for a, b in zip(col1, col2)) == 1
		mutate = lib.getFunction("mutate", _fileName)
		return all(offByOne(mutate("A" * i), "A" * i) for i in range(1, 100))

	test.test = testMethod
	test.description = lambda : "mutate() produces viruses who differ exactly one genome from the parent"

@t.test(50)
def killNoNew(test):
	def testMethod():
		kill = lib.getFunction("kill", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 1000
		return asserts.containsOnly(kill(viruses, 0.25), viruses) and len(kill(viruses, 0.25)) < len(viruses)

	test.test = testMethod
	test.description = lambda : "kill() does not produce any new viruses"

@t.test(60)
def dontKillYourOwn(test):
	def testMethod():
		kill = lib.getFunction("kill", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		kill(viruses, .5)
		return asserts.sameLength(viruses, ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20)

	test.test = testMethod
	test.description = lambda : "kill() does not modify the list of viruses it accepts as argument"

@t.test(70)
def killEnough(test):
	def testMethod():
		kill = lib.getFunction("kill", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		n = 1000
		return asserts.between(sum(len(kill(viruses[:], 0.25)) for i in range(n)) / n, 70, 80)

	test.test = testMethod
	test.description = lambda : "kill() kills enough viruses according to mortalityProb"

@t.test(80)
def reproduceParents(test):
	def testMethod():
		reproduce = lib.getFunction("reproduce", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		return asserts.exact(reproduce(viruses, 0.25, 0), viruses)

	test.test = testMethod
	test.description = lambda : "reproduce() with reproductionRate = 0 produces no new viruses"

@t.test(90)
def reproduceAvg(test):
	def testMethod():
		reproduce = lib.getFunction("reproduce", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		n = 1000
		avgPopSize = sum(len(reproduce(viruses[:], 0.25, 0.50)) for _ in range(n)) / n
		return asserts.between(avgPopSize, 145, 155)

	test.test = testMethod
	test.description = lambda : "reproduce() produces enough viruses on avg according to reproductionRate"

@t.test(100)
def repProbCorrect(test):
	def testMethod():
		reproductionProbability = lib.getFunction("reproductionProbability", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		return asserts.between(reproductionProbability(viruses, 0.5, 200), 0.2499, 0.2501)

	test.test = testMethod
	test.description = lambda : "reproductionProbability() produces the correct probability"

@t.test(110)
def simulateLength(test):
	def testMethod():
		simulate = lib.getFunction("simulate", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		return asserts.exact(len(simulate(viruses, 0, 0, 0, 100, 500)), 501)

	test.test = testMethod
	test.description = lambda : "simulate() produces a list of the correct length"

@t.test(120)
def simulateFluctuations(test):
	def testMethod():
		simulate = lib.getFunction("simulate", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		return asserts.containsOnly(simulate(viruses, 0, 0, 0, 100, 500), [100])

	test.test = testMethod
	test.description = lambda : "simulate(viruses, 0, 0, 0, 100) shows no fluctuations in population size"

@t.test(130)
def simulateAvg(test):
	def testMethod():
		simulate = lib.getFunction("simulate", _fileName)
		viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
		n = 100
		timesteps = 1000
		avg = sum(sum(simulate(viruses[:], 0.25, 0.1, 0.5, 100, timesteps)) / timesteps for i in range(n)) / n
		return asserts.between(avg, 40, 45)

	test.test = testMethod
	test.description = lambda : "simulate(viruses, 0.25, 0.1, 0.5, 100)) is correct"
	test.timeout = lambda : 30
