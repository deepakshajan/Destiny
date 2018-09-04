import core.__directionAdapter as adapter, core
__curPosition = [0, 0]
__curDirection = ''

def moveToOnlyAvailableRoom():
    global __curDirection
    global __curPosition
    __curDirection = core.getInitialDirection()
    core.moveInDirection(__curDirection, __curPosition)


def getUserInputInUserContext() -> str:
    newDirection = input('Which direction do I have to move now(left,right,straight,back) : ')
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
    while core.canMoveInDirection(newDirection, __curPosition) == False:
        print('There is no door in that direction. Guess I will have to try another direction!')
        newDirection = getDirectionInApplicationContext()

    return newDirection


def startMaze():
    global __curDirection
    moveToOnlyAvailableRoom()
    while core.isMazeSolved(__curPosition) == False:
        newDirection = getUserInputOnDirection()
        core.moveInDirectionIfStillInsideMaze(newDirection, __curPosition)
        __curDirection = newDirection
        if core.isMazeSolved(__curPosition) ==False:
            print('Another room!!')

    print("Looks like I have finally made it out. I wonder what's next!!")


startMaze()