import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

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
        import importlib
        import matplotlib.pyplot as plt
        plt.switch_backend("TkAgg")
        importlib.reload(plt)
    except ImportError:
        pass

@t.test(0)
def correctMaxTemp(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.numberOnLine(36.8, line)

    test.test = testMethod
    test.description = lambda : "prints the maximum temperature measured"
    test.timeout = lambda : 30

@t.test(10)
def correctDayMaxTemp(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line.lower(), "27 jun 1947")

    test.test = testMethod
    test.description = lambda : "prints the day of the maximum temperature"
    test.timeout = lambda : 30

@t.test(20)
def correctMinTemp(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 1)
        return asserts.numberOnLine(-11.3, line)

    test.test = testMethod
    test.description = lambda : "prints the minimum temperature measured"
    test.timeout = lambda : 30

@t.test(30)
def correctDayMinTemp(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 1)
        return asserts.contains(line.lower(), "20 dec 1938")

    test.test = testMethod
    test.description = lambda : "prints the day of the minimum temperature"
    test.timeout = lambda : 30

@t.test(40)
def correctLongestFreezingPeriod(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 2)
        return asserts.numberOnLine(21, line)

    test.test = testMethod
    test.description = lambda : "prints the length of the longest freezing period"
    test.timeout = lambda : 30

@t.test(50)
def correctLastDayFreezingPeriod(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 2)
        return asserts.contains(line.lower(), "24 feb 1947")

    test.test = testMethod
    test.description = lambda : "prints the last day of the longest freezing period"
    test.timeout = lambda : 30

@t.test(60)
def showsGraph(test):
    test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "plot") or \
        asserts.fileContainsFunctionCalls(_fileName, "bar")
    test.description = lambda : "shows a graph for the number of summer days"

@t.test(70)
def hasLabels(test):
	test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "xlabel", "ylabel")
	test.description = lambda : "graph has labels along the x-axis and y-axis"

@t.test(80)
def hasTitle(test):
	test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "title")
	test.description = lambda : "graph has a title"

@t.test(90)
def correctYearHeatwave(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 3)
        return asserts.numberOnLine(1911, line)

    test.test = testMethod
    test.description = lambda : "prints the year of the first heatwave"
    test.timeout = lambda : 30
