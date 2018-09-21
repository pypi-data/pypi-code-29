from _collections import deque
from subclass.Node import Node


class BreadthSearch:

    def __init__(self, maze=None):
        if maze is None:
            maze = []
        self.rowSize = 10
        self.colSize = 10
        self.completedNodes = []
        self.completePath = []

        self.queue = deque([])

        self.mazeArray = maze
        if len(self.mazeArray) == 0:
            self.file = open("resources/maze1.txt", 'r').readlines()
            self.mazeArray = ['O'] * self.colSize
            self.completedNodes = []
            self.completePath = []

            for i in range(self.rowSize):
                self.mazeArray[i] = ['O'] * self.colSize

            index = 0
            for i in range(self.rowSize):
                for j in range(self.colSize):
                    self.mazeArray[i][j] = self.file[index].strip()
                    index += 1

    def findEntry(self):
        for i in range(self.colSize):
            for j in range(self.rowSize):
                if self.mazeArray[i][0] == 'E':
                    return str(i) + '0'

    def isGoal(self, node):
        if node.data == 'X':
            return True
        else:
            return False

    def checkForChildren(self, node):
        children = []
        location = node.location
        row = int(location[0])
        col = int(location[1])

        if (self.mazeArray[row + 1][col] == 'P' or self.mazeArray[row + 1][col] == 'X') and row != 0:
            children.append(str(row + 1) + str(col))

        if (self.mazeArray[row][col - 1] == 'P' or self.mazeArray[row][col - 1] == 'X') and col != 0:
            children.append(str(row) + str(col - 1))

        if (self.mazeArray[row - 1][col] == 'P' or self.mazeArray[row - 1][col] == 'X') and row != 9:
            children.append(str(row - 1) + str(col))

        if (self.mazeArray[row][col + 1] == 'P' or self.mazeArray[row][col + 1] == 'X') and col != 9:
            children.append(str(row) + str(col + 1))

        return children

    def getData(self, id):
        row = id[0]
        col = id[1]
        return self.mazeArray[int(row)][int(col)]

    def checkVisited(self, node):
        if node.location in self.completedNodes:
            return True
        else:
            return False

    def underline(self, list, path):
        for i in range(self.colSize):
            for j in range(self.rowSize):
                loc = str(i) + str(j)
                if loc in path:
                    letter = list[i][j]
                    list[i][j] = '*'

    def run(self):
        nodeid = self.findEntry()
        self.completedNodes.append(nodeid)
        self.completePath.append(nodeid)
        node = Node(nodeid, self.getData(nodeid), self.completedNodes)
        self.queue.append(node)

        if not self.isGoal(self.queue.popleft()):
            children = self.checkForChildren(node)
            for child in children:
                if child not in self.completedNodes:
                    self.completedNodes.append(child)
                    newNode = Node(child, self.getData(child), self.completePath, node)
                    self.queue.append(newNode)

        try:
            newNode
        except NameError:
            currentNode = node
        else:
            currentNode = self.queue.popleft()
            self.completePath.append(currentNode.location)

        while not self.isGoal(currentNode):

            children = self.checkForChildren(currentNode)
            index = 0
            for child in children:
                if child not in self.completedNodes:
                    self.completedNodes.append(child)
                    newNode = Node(child, self.getData(child), self.completePath, currentNode)
                    self.queue.append(newNode)
                else:
                    try:
                        if len(children) == 1:
                            currentNode = currentNode.parent
                    except ValueError:
                        '''do nothing'''
                index += 1

            try:
                currentNode = self.queue.popleft()
                self.completePath.append(currentNode.location)
            except IndexError:
                print('There is not a valid path.')
                return

            # for node in currentNode.path:
            #     print(node.location)

        finalPath = []

        for myNode in currentNode.path:
            finalPath.append(myNode.location)

        self.underline(self.mazeArray, finalPath)

        for row in self.mazeArray:
            print(' '.join([str(elem) for elem in row]))

        print()
        print(finalPath)
