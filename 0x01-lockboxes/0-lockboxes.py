#!/usr/bin/python3
"""
lockboxes returns true when all boxes can be unlocked and vice versa
"""


def canUnlockAll(boxes):
    """ try to unlock all boxes """
    status = False
    if boxes[0]:
        lck_keys = boxes[0]
        for key in lck_keys:
            if boxes[key]:
                status = True
            else:
                status = False
        return status
