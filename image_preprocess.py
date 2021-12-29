import cv2


def preprocess(image):
    """get image, scale, convert it to grayscale, blur out noise,
    output black and white as numpy array"""

    f = 400. / image.shape[0]
    width = int(image.shape[0] * f)
    height = int(image.shape[1] * f)
    image = cv2.resize(image, (height, width))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (5, 5), 0)
    (thresh, bnwimage) = cv2.threshold(gauss, 127, 255, cv2.THRESH_BINARY)
    return bnwimage
