import maze.__maze as __maze
__maze.createMaze()

def __canMoveLeft(curPos: []):
    room = __maze.mazeLayout[curPos[0]][curPos[1]]
    if int(room[0]):
        return True
    else:
        return False


def __canMoveTop(curPos: []):
    room = __maze.mazeLayout[curPos[0]][curPos[1]]
    if int(room[1]):
        return True
    else:
        return False


def __canMoveRight(curPos: []):
    room = __maze.mazeLayout[curPos[0]][curPos[1]]
    if int(room[2]):
        return True
    else:
        return False


def __canMoveDown(curPos: []) -> bool:
    room = __maze.mazeLayout[curPos[0]][curPos[1]]
    if int(room[3]):
        return True
    else:
        return False


def canMoveInDirection(direction: str, curPos: []) -> bool:
    if direction == 'left':
        return __canMoveLeft(curPos)
    if direction == 'right':
        return __canMoveRight(curPos)
    if direction == 'up':
        return __canMoveTop(curPos)
    if direction == 'down':
        return __canMoveDown(curPos)
    raise Exception('Allowed values are left,right,up or down')


def moveInDirection(direction: str,
                    curPos: []) -> []:
    canMove = canMoveInDirection(direction, curPos)
    if canMove:
        if direction == 'left':
            curPos[1] = curPos[1] - 1
        elif direction == 'right':
            curPos[1] = curPos[1] + 1
        elif direction == 'up':
            curPos[0] = curPos[0] - 1
        else:
            if direction == 'down':
                curPos[0] = curPos[0] + 1
    else:
        raise Exception('Cannot move in the direction:%s in the position:[%s,%s]' % (direction, curPos[0], curPos[1]))
    return curPos


def getInitialDirection():
    firstRoom = __maze.mazeLayout[0][0]
    if firstRoom == '10000':
        return 'left'
    if firstRoom == '01000':
        return 'up'
    if firstRoom == '00100':
        return 'right'
    if firstRoom == '00010':
        return 'down'
    raise Exception("The first element of the maze layout should be one of '10000','01000','00100' or '00010'")


def moveInDirectionIfStillInsideMaze(direction: str,curPos: []) -> bool:
    try:
        moveInDirection(direction, curPos)
    except IndexError:
        return False

    return True


def isMazeSolved(curPos: []) -> bool:
    data = __maze.mazeLayout[curPos[0]][curPos[1]]
    if int(data[4]) == 1:
        return True
    return False