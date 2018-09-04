mazeLayout = []

def __validateLine(line: str) -> bool:
    if line is not '' and line[0] is not '#':
        for char in line:
            if char is not '1' and char is not '0' and char is not ' ':
                return False
        return True
    return False


def __addMazeRow(line: str):
    elementList = line.split(' ')
    mazeLayout.append(elementList)


def __parseLine(line: str):
    if __validateLine(line):
        __addMazeRow(line)


def createMaze():
    mazeLayout = open('../conf/maze.txt', 'r')
    for line in mazeLayout.readlines():
        __parseLine(line.strip())