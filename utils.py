import numpy as np
import cv2


def join_digits(infix_tokens):
    """given a list of chars,
    join consecutive digits in a number"""
    ret = []
    for token in infix_tokens:
        if token.isdigit() and len(ret) > 0 and ret[-1].isdigit():
            ret[-1] = ret[-1] + token
        else:
            ret.append(token)
    return ret


def show_bounding_boxes(image, bounding_boxes):
    """draw and display bounding boxes on an image"""
    drawing = np.copy(image)
    color = (124, 252, 0)
    for i in range(len(bounding_boxes)):
        cv2.rectangle(drawing, (int(bounding_boxes[i][0]), int(bounding_boxes[i][1])),
                      (int(bounding_boxes[i][0] + bounding_boxes[i][2]),
                       int(bounding_boxes[i][1] + bounding_boxes[i][3])), color, 2)

    cv2.imshow('Bounding boxes', drawing)
    cv2.waitKey(0)
