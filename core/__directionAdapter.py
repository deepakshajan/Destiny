def userContextToApplicationContext(valueToBeChanged: '', incomingDir: str=''):
    if incomingDir == 'right':
        if valueToBeChanged == 'straight':
            return 'right'
        if valueToBeChanged == 'right':
            return 'down'
        if valueToBeChanged == 'left':
            return 'up'
        if valueToBeChanged == 'back':
            return 'left'
    else:
        if incomingDir == 'left':
            if valueToBeChanged == 'straight':
                return 'left'
            if valueToBeChanged == 'right':
                return 'up'
            if valueToBeChanged == 'left':
                return 'down'
            if valueToBeChanged == 'back':
                return 'right'
        else:
            if incomingDir == 'up':
                if valueToBeChanged == 'straight':
                    return 'up'
                if valueToBeChanged == 'right':
                    return 'right'
                if valueToBeChanged == 'left':
                    return 'left'
                if valueToBeChanged == 'back':
                    return 'down'
            else:
                if incomingDir == 'down':
                    if valueToBeChanged == 'straight':
                        return 'down'
                    if valueToBeChanged == 'right':
                        return 'left'
                    if valueToBeChanged == 'left':
                        return 'right'
                    if valueToBeChanged == 'back':
                        return 'up'
    return valueToBeChanged