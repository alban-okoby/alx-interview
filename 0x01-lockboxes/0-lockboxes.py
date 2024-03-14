#!/usr/bin/python3
''' Unlock list of lists'''


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    """
    keys = [0]
    
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    
    return len(keys) == len(boxes)

