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
		return asserts.numberOnLine(0.25, line, deviation = 0.20)

	test.test = testMethod
	test.description = lambda : "prints the correct number of tiles that player 1 owns over player 2"
	test.timeout = lambda : 30

@t.test(10)
def correct1(test):
	def testMethod():
		output = lib.outputOf(
			_fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 1)
		return asserts.numberOnLine(1610, line, deviation = 50)

	test.test = testMethod
	test.description = lambda : "prints the correct starting money player 2 needs to compensate"
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
