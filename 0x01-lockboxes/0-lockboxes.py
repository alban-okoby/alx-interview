#!/usr/bin/python3
"""Function who unlock list of lists"""


def canUnlockAll(boxes):
    """Take a list of lists and the content
       of a list will unlock other lists
    """

    ks = [0]
    for key in ks:
        for boxKey in boxes[key]:
            if boxKey not in ks and boxKey < len(boxes):
                ks.append(boxKey)
    if len(ks) == len(boxes):
        return True
    return False
