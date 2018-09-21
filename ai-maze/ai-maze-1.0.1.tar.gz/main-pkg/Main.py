# from subclass.BreadthFirst import BreadthSearch
from subclass.BreadthFirst import BreadthSearch
from subclass.DepthFirst import DepthSearch
from generator.Main import Main
import copy


class MainProgram:

    def __init__(self):
        test = Main()
        generator = test.getGenerator()
        # self.maze1 = generator.getMazeCopy()
        # self.maze2 = generator.getMazeCopy()
        self.maze1 = copy.deepcopy(generator.maze)
        self.maze2 = copy.deepcopy(generator.maze)

    def breadthFirst(self):
        # Run the Breadth First search
        print('Breadth First Search\n')
        search1 = BreadthSearch(self.maze1)
        search1.run()

    def depthFirst(self):
        # Run the Depth First search
        print('Depth First Search\n')
        search2 = DepthSearch(self.maze2)
        search2.run()

    def main(self):
        self.breadthFirst()
        print()
        self.depthFirst()


program = MainProgram()

program.main()
