"""
get image location, convert it to grayscale, blur out noise,
output numpy array
"""
import cv2


def preprocess(image_location):
    # load image, convert it to grayscale and blur to reduce noise
    image = cv2.imread(image_location)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.GaussianBlur(gray, (5, 5), 0)
