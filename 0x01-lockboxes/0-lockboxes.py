#!/usr/bin/python3
"""
lockboxes returns true when all boxes can be unlocked and vice versa
"""


def canUnlockAll(boxes):
    status = False
    if boxes[0]:
        lck_keys = boxes[0]
        for key in lck_keys:
            if boxes[key] and not len(boxes[key]) == 0:
                status = True
            else:
                status = False
        return status
