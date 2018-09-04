import core.__directionAdapter as adapter, core
__curPosition = [
 0, 0]
__curDirection = ''

def moveToOnlyAvailableRoom():
    global __curDirection
    global __curPosition
    __curDirection = core.getInitialDirection()
    core.moveInDirection(__curDirection, __curPosition)


def getUserInputInUserContext() -> str:
    newDirection = input('Which direction do you want to move(left,right,straight,back)')
    valid = ('left', 'right', 'straight', 'back')
    while newDirection not in valid:
        print('Sorry, that is not a valid direction!')
        newDirection = input('Which direction do you want to move(left,right,straight,back)')
        print('current pos -> [%s,%s]' % (__curPosition[0], __curPosition[1]))

    return newDirection


def getDirectionInApplicationContext():
    direction = getUserInputInUserContext()
    direction = adapter.userContextToApplicationContext(direction, __curDirection)
    return direction


def getUserInputOnDirection() -> str:
    newDirection = getDirectionInApplicationContext()
    while core.canMoveInDirection(newDirection, __curPosition) == False:
        print('Sorry, there is no door in that direction!')
        print('Room -> ' + str(__curPosition))
        newDirection = getDirectionInApplicationContext()

    return newDirection


def startMaze():
    global __curDirection
    moveToOnlyAvailableRoom()
    while core.isMazeSolved(__curPosition) == False:
        newDirection = getUserInputOnDirection()
        core.moveInDirectionIfStillInsideMaze(newDirection, __curPosition)
        __curDirection = newDirection

    print('Congratz you finally made it out...')


startMaze()