import argparse

import solver
import utils
from image_preprocess import preprocess
from character_detector import segment_characters
from image_postprocess import postprocess
from classifier import model
import cv2


def evaluate(image):
    """for a given image of a math expression return its result"""
    preprocessed_image = preprocess(image)
    char_images, _ = segment_characters(preprocessed_image)
    square_images = postprocess(char_images)

    inferred = [model.predict(x) for x in square_images]
    chars = utils.join_digits(inferred)
    expression = " ".join(chars)

    print(expression)

    return solver.solve(expression)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to image input")
    args = vars(ap.parse_args())

    image = cv2.imread(args['image'])

    print("=", evaluate(image))


if __name__ == "__main__":
    main()
