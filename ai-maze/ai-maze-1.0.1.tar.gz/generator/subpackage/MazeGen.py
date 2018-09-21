import random
import os
from pathlib import Path

FOLDER = Path.home()
FILE = os.path.join(FOLDER, 'maze.txt')


class MyMaze:

    def __init__(self, maze):
        self.colSize = 10
        self.rowSize = 10
        self.maze = maze

    recursionCount = 0

    def makeEntry(self, maze):
        num = random.randint(1, 8)
        maze[num][0] = 'E'
        return str(num) + '0'

    def checkBoundaries(self, x, y):
        if 0 <= x <= 9 or 0 <= y <= 9:
            return True
        else:
            return False

    def moveRight(self, row, col, maze, entry=False, check=False):
        if entry:
            return col + 1
        if row < 1 or row > 8 or col < 1 or row > 8:
            return col
        elif maze[row - 1][col] == 'P' and maze[row - 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return col
        elif maze[row + 1][col] == 'P' and maze[row + 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return col
        else:
            newCol = col + 1
            if newCol < 1 or newCol > 8:
                return -1
            elif maze[row - 1][newCol] == 'P' and maze[row - 1][newCol + 1] == 'P':
                return -1
            elif maze[row + 1][newCol] == 'P' and maze[row + 1][newCol + 1] == 'P':
                return -1
            else:
                return newCol

    def moveLeft(self, row, col, maze, check=False):
        if row < 1 or row > 8 or col < 1 or row > 8:
            return col
        elif maze[row - 1][col] == 'P' and maze[row - 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return col
        elif maze[row + 1][col] == 'P' and maze[row + 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return col
        else:
            newCol = col - 1
            if newCol < 1 or newCol > 8:
                return -1
            elif maze[row - 1][newCol] == 'P' and maze[row - 1][newCol - 1] == 'P':
                return -1
            elif maze[row + 1][newCol] == 'P' and maze[row + 1][newCol - 1] == 'P':
                return -1
            else:
                return newCol

    def moveUp(self, row, col, maze, check=False):
        if row < 1 or row > 8 or col < 1 or row > 8:
            return row
        elif maze[row][col - 1] == 'P' and maze[row - 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return row
        elif maze[row][col + 1] == 'P' and maze[row - 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return row
        else:
            newRow = row - 1
            if newRow < 1 or newRow > 8:
                return -1
            elif maze[newRow][col - 1] == 'P' and maze[newRow - 1][col - 1] == 'P':
                return -1
            elif maze[newRow][col + 1] == 'P' and maze[newRow - 1][col + 1] == 'P':
                return -1
            else:
                return newRow

    def moveDown(self, row, col, maze, check=False):
        if row < 1 or row > 8 or col < 1 or row > 8:
            return row
        elif maze[row][col - 1] == 'P' and maze[row + 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return row
        elif maze[row][col + 1] == 'P' and maze[row + 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return row
        else:
            newRow = row + 1
            if newRow < 1 or newRow > 8:
                return -1
            elif maze[newRow][col - 1] == 'P' and maze[newRow + 1][col - 1] == 'P':
                return -1
            elif maze[newRow][col + 1] == 'P' and maze[newRow + 1][col + 1] == 'P':
                return -1
            else:
                return newRow

    def checkSpaces(self, row, col, maze):
        if maze[row - 1][col] == 'P' and maze[row - 1][col + 1] == 'P':
            return False
        elif maze[row + 1][col] == 'P' and maze[row + 1][col + 1] == 'P':
            return False
        elif maze[row - 1][col] == 'P' and maze[row - 1][col - 1] == 'P':
            return False
        elif maze[row + 1][col] == 'P' and maze[row + 1][col - 1] == 'P':
            return False
        elif maze[row][col - 1] == 'P' and maze[row - 1][col - 1] == 'P':
            return False
        elif maze[row][col + 1] == 'P' and maze[row - 1][col + 1] == 'P':
            return False
        elif maze[row][col - 1] == 'P' and maze[row + 1][col - 1] == 'P':
            return False
        elif maze[row][col + 1] == 'P' and maze[row + 1][col + 1] == 'P':
            return False
        else:
            return True

    def exit(self, row, col, maze):
        if row == 1:
            maze[row - 1][col] = 'X'
        elif row == 8:
            maze[row + 1][col] = 'X'
        elif col == 8:
            maze[row][col + 1] = 'X'
        else:
            first = []
            second = []
            third = []

            for i in range(self.colSize):
                if maze[1][i] == 'P':
                    first.append((1, i))

            for i in range(self.colSize):
                if maze[8][i] == 'P':
                    second.append((8, i))

            for i in range(self.colSize):
                if maze[i][8] == 'P':
                    third.append((i, 8))

            done = False
            while not done:
                num = random.randint(1, 3)

                if num == 1:
                    '''first'''
                    if len(first) != 0:
                        done = True
                        anotherNum = random.randint(0, len(first) - 1)
                        coords = first[anotherNum]
                        maze[0][coords[1]] = 'X'
                elif num == 2:
                    '''two'''
                    if len(second) != 0:
                        done = True
                        anotherNum = random.randint(0, len(second) - 1)
                        coords = second[anotherNum]
                        maze[9][coords[1]] = 'X'
                elif num == 3:
                    '''three'''
                    if len(third) != 0:
                        done = True
                        anotherNum = random.randint(0, len(third) - 1)
                        coords = third[anotherNum]
                        maze[coords[0]][9] = 'X'

    def saveFile(self, maze):
        file = open(FILE, 'w')
        for i in range(self.rowSize):
            for j in range(self.colSize):
                file.write(maze[i][j] + '\n')
        file.close()
        # print('success')

    def getMazeCopy(self):
        return self.maze.copy()

    def getNextMove(self, row, col, maze):
        num = random.randint(1, 4)
        if self.moveRight(row, col, maze, False, True) == -1 and self.moveLeft(row, col, maze, True) == -1 and \
                self.moveUp(row, col, maze, True) == -1 and self.moveDown(row, col, maze, True) == -1:
            return row, col

        if self.recursionCount == 20:
            return -1, -1

        if num == 1:
            newCol = self.moveRight(row, col, maze)

            if newCol == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newCol):
                return row, newCol
            if maze[row][newCol] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return row, newCol
        elif num == 2:
            newCol = self.moveLeft(row, col, maze)

            if newCol == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newCol):
                return row, newCol
            if maze[row][newCol] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return row, newCol
        elif num == 3:
            newRow = self.moveUp(row, col, maze)

            if newRow == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newRow):
                return row, newRow
            if maze[newRow][col] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return newRow, col
        elif num == 4:
            newRow = self.moveDown(row, col, maze)

            if newRow == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newRow):
                return row, newRow
            if maze[newRow][col] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return newRow, col
