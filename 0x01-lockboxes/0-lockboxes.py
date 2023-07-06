#!/usr/bin/python3

from collections import deque


""" lockboxes """


def canUnlockAll(boxes):
    """ try unlocking the boxes by unlocking box 1 """
    opened_boxes = set([0])
    queue = deque([0])
    while queue:
        box = queue.popleft()
        keys = boxes[box]
        for key in keys:
            if key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == len(boxes)
