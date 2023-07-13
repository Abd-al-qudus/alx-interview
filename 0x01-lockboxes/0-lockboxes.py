#!/usr/bin/python3

"""lockboxes"""


def canUnlockAll(boxes):
    """try unlocking all boxes"""
    free_keys = set()
    box_id = 0

    opened_boxes = []
    num_boxes = len(boxes)
    while box_id < num_boxes:
        old_box_id = box_id
        opened_boxes.append(box_id)
        free_keys.update(boxes[box_id])
        for key in free_keys:
            if key != 0 and key < num_boxes and key not in opened_boxes:
                box_id = key
                break
        if old_box_id == box_id:
            break
        continue
    for box_id in range(num_boxes):
        if box_id not in opened_boxes and box_id != 0:
            return False
    return True
