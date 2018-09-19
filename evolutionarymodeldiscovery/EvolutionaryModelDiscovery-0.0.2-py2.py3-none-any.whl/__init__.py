from NetLogoWriter import NetLogoWriter
from FactorGenerator import FactorGenerator
from PrimitiveSetGenerator import PrimitiveSetGenerator
from ABMEvaluator import ABMEvaluator
import math 
import time
import importlib
import nl4py
import numpy
from deap import algorithms
from deap import gp
from deap import creator
from deap import base
from deap import tools
from scoop import futures
import scoop
from multiprocessing import Process, current_process

isInitialized = False
evolved = False
class EvolutionaryModelDiscovery:
    def __init__(self,modelPath, setupCommands, measurementCommands, ticksToRun):
        self.initialize(modelPath, setupCommands, measurementCommands, ticksToRun)
    def initialize(self,modelPath, setupCommands, measurementCommands, ticksToRun):
        self.startup(modelPath)
        #if __name__ == '__main__':
            
        global modelPath_
        modelPath_ = modelPath
        global pset
        with open("ModelFactors.py") as f:
            ModelFactors = importlib.import_module('ModelFactors',package="*")
        pset = ModelFactors.getDEAPPrimitiveSet()

        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)
        global toolbox
        toolbox = base.Toolbox()
        # Attribute generator
        toolbox.register("expr_init", gp.genHalfAndHalf, pset=pset, min_=2, max_=4)
        # Structure initializers
        toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)
        global setupCommands_
        global measurementCommands_
        global ticksToRun_
        setupCommands_ = setupCommands
        measurementCommands_ = measurementCommands
        ticksToRun_ = ticksToRun
        #toolbox.register("setupCommands", tools.initRepeat, setupCommands )

        toolbox.register("evaluate", self.evaluate)
        toolbox.register("select", tools.selTournament, tournsize=7)
        toolbox.register("mate", gp.cxOnePoint)
        toolbox.register("expr_mut", gp.genFull, min_=2, max_=5)
        toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
        toolbox.register("map", futures.map)
        global pop
        pop = toolbox.population(n=10)
        global hof
        hof = tools.HallOfFame(1)
        global stats
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("std", numpy.std)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)    

    def evolve(self):
        global isInitialized
        global evolved
        try:
            isScoopMain = scoop.IS_ORIGIN and scoop.IS_RUNNING
        except:
            isScoopMain = True
        if isScoopMain and isInitialized and not evolved:
            print('Evolving!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            evolved = True
            initialized = False
            algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 3, stats, halloffame=hof)        
            return pop, hof, stats
    def startup(self,modelPath):
        global isInitialized
        global evolved
        try:
            isScoopMain = scoop.IS_ORIGIN and scoop.IS_RUNNING
        except:
            isScoopMain = True
        if isScoopMain and not isInitialized:
            print('Starting!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            nl4py.startServer("C:/Program Files/NetLogo 6.0.2")
            netLogoWriter = NetLogoWriter(modelPath)
            #Read in annotations from .nlogo file and generate EMD factors
            factorGenerator = FactorGenerator()
            factorGenerator.generate(netLogoWriter.getFactorsFilePath())
            #Generate the ModelFactors.py file
            primitiveSetGenerator = PrimitiveSetGenerator()
            primitiveSetGenerator.generate(factorGenerator.getFactors(), netLogoWriter.getEMDReturnType())  
            isInitialized = True
            evolved = False
    def evaluate(self,individual):
        newRule = str(gp.compile(individual, pset))
        print(newRule)
        netLogoWriter = NetLogoWriter(modelPath_)
        newModelPath = netLogoWriter.injectNewRule(newRule)
        abmEvaluator = ABMEvaluator()
        abmEvaluator.initialize (setupCommands_, measurementCommands_, ticksToRun_)
        fitness = abmEvaluator.evaluateABM(newModelPath)
        return fitness,
