import cv2
import numpy as np


def postprocess(images):
    """
    given a list of images (arrays), make them square,
    resize to fit the classifier and output as numpy array
    """
    ret = np.zeros((0, 45, 45, 1), dtype=np.uint8)
    for img in images:
        h, w = img.shape
        if h > w:
            x = y = h
        else:
            x = y = w
        square = np.full((x, y), 255, dtype=np.uint8)
        square[int((y - h) / 2):int(y - (y - h) / 2), int((x - w) / 2):int(x - (x - w) / 2)] = img
        square = cv2.resize(square, (45, 45))
        square = square.reshape((1, 45, 45, 1))
        ret = np.append(ret, square, 0)

    return ret
