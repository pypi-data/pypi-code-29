from Factor import Factor

class PrimitiveSetGenerator:
    _FUNCTIONS_FILE_PATH = "ModelFactors.py"
    def generate(self, factors, finalReturnType):
        with open(self._FUNCTIONS_FILE_PATH, "a+") as f:
            f.write('\nclass EMD_ModelEvaluation:')
            f.write('\n\t__name__ = ""')
            f.write('\n\tdef __init__(self, nlString):')
            f.write('\n\t\tself.__name__ = "{0}\\n".format(str(nlString))')
            f.write('\n\tdef __str__(self):')
            f.write('\n\t\treturn self.__name__')
            f.write('\n\tdef __repr__(self):')
            f.write('\n\t\treturn self.__name__')
            f.write('\nfrom deap import gp')            
            f.write('\ndef getDEAPPrimitiveSet():')            
            f.write('\n\tpset = gp.PrimitiveSetTyped("main", [], EMD_ModelEvaluation)')
            for factor in factors:
                parameterString = " [ "
                for parameterType in factor.getParameterTypes():
                    parameterString = parameterString + "{0},".format(parameterType)
                parameterString = '{0} ]'.format(parameterString[:-1])
                if len(factor.getParameterTypes()) == 0 :
                    f.write('\n\tpset.addTerminal({1}({0}()), {1}, name = "{0}")'.format(factor.getSafeName(),factor.getReturnType()))
                    f.write('\n\tpset.addPrimitive({0}, [{0}], {0})'.format(factor.getReturnType()))
                else:
                    f.write('\n\tpset.addPrimitive({0}, {1}, {2}, name = "{0}")'.format(factor.getSafeName(),parameterString,factor.getReturnType()))
            f.write('\n\tpset.addPrimitive(EMD_ModelEvaluation, [{0}], EMD_ModelEvaluation)'.format(finalReturnType))
            f.write('\n\treturn pset')
        '''f.write('\npset.addPrimitive(InjectRuleAndEvaluateABM, [nlAgent], float)')
        f.write('\npset.addPrimitive(nlMinOneOf, [nlComparator, nlAgentSet], nlAgent)')

        #Terminals
        agent_sets = ["sheep","wolves","turtles"]
        for agent_set in agent_sets:    
            pset.addTerminal(nlAgentSet(agent_set), nlAgentSet,name = " '" + agent_set + "'")
        pset.addPrimitive(nlAgentSet,[nlAgentSet],nlAgentSet)
        comparator_str_set = ["energy", "distance myself"]
        for comparator_str in comparator_str_set:    
            pset.addTerminal(nlComparator(comparator_str), nlComparator, name = " '" + comparator_str + "'")
        pset.addPrimitive(nlComparator,[nlComparator],nlComparator)
        pset.addTerminal("nobody",nlAgent)
        pset.addTerminal(0,float)
        #Primitives'''