#!/usr/bin/python3
""" try unlocking all boxes """

if __name__ == '__main__':
    from collections import deque

    def canUnlockAll(boxes):
        """ check a key to unlock the boxes"""
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
