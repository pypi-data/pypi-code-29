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
def correctDistance(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.numberOnLine(10.86, line, deviation = 0.02)

    test.test = testMethod
    test.description = lambda : "prints the distance travelled"
    test.timeout = lambda : 30

@t.test(10)
def correctSecondsFasterThan50(test):
    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 1)
        return asserts.numberOnLine(330, line, deviation = 0.1)

    test.test = testMethod
    test.description = lambda : "prints the number of seconds that the car drives faster than 50km/h"
    test.timeout = lambda : 30

@t.test(20)
def showsGraph(test):
    test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "plot") or \
        asserts.fileContainsFunctionCalls(_fileName, "bar")
    test.description = lambda : "shows a graph"

@t.test(30)
def hasLabels(test):
    test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "xlabel", "ylabel")
    test.description = lambda : "graph has labels along the x-axis and y-axis"

@t.test(40)
def hasTitle(test):
    test.test = lambda : asserts.fileContainsFunctionCalls(_fileName, "title")
    test.description = lambda : "graph has a title"
