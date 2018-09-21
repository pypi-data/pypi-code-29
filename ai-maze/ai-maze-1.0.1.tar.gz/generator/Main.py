from generator.subpackage.MazeGen import MyMaze


class Main:

    maze = ['W'] * 10

    for i in range(len(maze)):
        maze[i] = ['W'] * 10

    test = MyMaze(maze)

    path = []
    location = test.makeEntry(maze)
    row = int(location[0])
    col = int(location[1])

    colNum = test.moveRight(row, col, maze, True)

    location = str(row) + str(colNum)
    row = int(location[0])
    col = int(location[1])
    maze[row][col] = 'P'

    path.append((row, col))

    coords = test.getNextMove(row, col, maze)
    row = coords[0]
    col = coords[1]

    path.append(coords)

    previous = 0, 0
    attempts = 0

    while test.checkBoundaries(row, col):

        if test.checkBoundaries(row, col):
            try:
                if maze[row][col] != 'E' and maze[row][col] != 'P':
                    maze[row][col] = 'P'
            except IndexError:
                print('oops')

        # for blah in maze:
        #     print(' '.join([str(elem) for elem in blah]))

        if coords == previous:
            attempts += 1
        else:
            attempts = 0
        if attempts == 10:
            test.exit(row, col, maze)
            break
        previous = coords
        coords = test.getNextMove(row, col, maze)
        test.recursionCount = 0
        if coords[0] == -1 or coords[1] == -1:
            if len(path) > 0:
                coords = path.pop()
                row = coords[0]
                col = coords[1]
            else:
                break
        else:
            path.append(coords)
            row = coords[0]
            col = coords[1]

        # print(coords)

    # print()
    # for row in maze:
    #     print(' '.join([str(elem) for elem in row]))

    test.saveFile(maze)

    def getGenerator(self):
        return self.test
