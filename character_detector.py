"""
The implementation receives an image in a form of a numpy array
and for each detected character it should return its coordinates,
and a cropped image
"""
import numpy as np
import cv2


def segment_characters(image):
    # edge detection, find contours in the edge map, and sort the resulting contours
    # from left to right
    edged = cv2.Canny(image, 30, 150)
    contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours
    bounding_boxes = [cv2.boundingRect(c) for c in contours]
    (contours, bounding_boxes) = zip(*sorted(zip(contours, bounding_boxes),
                                             key=lambda b: b[1][0]))





