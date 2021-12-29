import numpy as np
import cv2
from utils import show_bounding_boxes


def segment_characters(image):
    """
    receives an image in a form of a numpy array and for each
     detected character it returns its coordinates and a cropped image
    """
    edged = cv2.Canny(image, 30, 150)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bounding_boxes = [None] * len(contours)

    for i, c in enumerate(contours):
        bounding_boxes[i] = cv2.boundingRect(c)

    # sort contours
    (contours, bounding_boxes) = zip(*sorted(zip(contours, bounding_boxes),
                                             key=lambda b: b[1][0]))

    # crop boxes and add to output list
    cropped_images = []
    for box in bounding_boxes:
        X, Y, W, H = box
        cropped_images.append(image[Y:Y+H, X:X+W])

    # show_bounding_boxes(image, bounding_boxes)

    return cropped_images, bounding_boxes

