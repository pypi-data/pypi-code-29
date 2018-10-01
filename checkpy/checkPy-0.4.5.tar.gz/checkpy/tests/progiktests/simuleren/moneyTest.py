import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts
import importlib

def before():
	try:
		import matplotlib
		matplotlib.use("Agg")
		import matplotlib.pyplot as plt
		plt.switch_backend("Agg")
		lib.neutralizeFunction(plt.pause)
	except ImportError:
		pass

def after():
	try:
		import matplotlib.pyplot as plt
		plt.switch_backend("TkAgg")
		importlib.reload(plt)
	except ImportError:
		pass

@t.test(0)
def correct0(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 0)
		return asserts.numberOnLine(227, line, deviation = 7)

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws for 0 starting money"
	test.timeout = lambda : 30

@t.test(10)
def correct500(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 1)
		return asserts.numberOnLine(213, line, deviation = 7)

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws for 500 starting money"
	test.timeout = lambda : 30

@t.test(20)
def correct1000(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 2)
		return asserts.numberOnLine(199, line, deviation = 7)

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws for 1000 starting money"
	test.timeout = lambda : 30

@t.test(30)
def correct1500(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 3)
		return asserts.numberOnLine(187, line, deviation = 7)

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws for 1500 starting money"
	test.timeout = lambda : 30

@t.test(40)
def correct2000(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 4)
		return asserts.numberOnLine(172, line, deviation = 7)

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws for 2000 starting money"
	test.timeout = lambda : 30

@t.test(50)
def correct2500(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 5)
		return asserts.numberOnLine(159, line, deviation = 7)

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws for 2500 starting money"
	test.timeout = lambda : 30

@t.test(100)
def plotsGraph(test):
	test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "plot") or \
		asserts.fileContainsFunctionCalls(_fileName, "bar")
	test.description = lambda : "plots a graph"

@t.test(110)
def hasLabels(test):
	test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "xlabel", "ylabel")
	test.description = lambda : "graph has labels along the x-axis and y-axis"

@t.test(120)
def hasTitle(test):
	test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "title")
	test.description = lambda : "graph has a title"
