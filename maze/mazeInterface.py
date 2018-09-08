import maze.__directionAdapter as adapter, maze
__curPosition = [0, 0]
__curDirection = ''

def moveToOnlyAvailableRoom():
    global __curDirection
    global __curPosition
    __curDirection = maze.getInitialDirection()
    maze.moveInDirection(__curDirection, __curPosition)


def getUserInputInUserContext() -> str:
    newDirection = input('Which direction do I have to move now(left,right,straight,back) : ').lower()
    valid = ('left', 'right', 'straight', 'back')
    while newDirection not in valid:
        print('Sorry, that is not a valid direction!')
        newDirection = input('Which direction do I have to move now?(left,right,straight,back) : ')

    return newDirection


def getDirectionInApplicationContext():
    direction = getUserInputInUserContext()
    direction = adapter.userContextToApplicationContext(direction, __curDirection)
    return direction


def getUserInputOnDirection() -> str:
    newDirection = getDirectionInApplicationContext()
    while maze.canMoveInDirection(newDirection, __curPosition) == False:
        print('There is no door in that direction. Guess I will have to try another direction!')
        newDirection = getDirectionInApplicationContext()

    return newDirection


def startMaze():
    global __curDirection
    moveToOnlyAvailableRoom()
    print("\n")
    while maze.isMazeSolved(__curPosition) == False:
        newDirection = getUserInputOnDirection()
        maze.moveInDirectionIfStillInsideMaze(newDirection, __curPosition)
        __curDirection = newDirection
        if maze.isMazeSolved(__curPosition) ==False:
            print('Yet another room!!')

    print("\nLooks like I have finally made it out. I wonder what's next!!")
