import argparse

from image_preprocess import preprocess
from character_detector import segment_characters


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to image input")
    args = vars(ap.parse_args())

    image = preprocess(args['image'])
    char_images = segment_characters(image)


if __name__ == "__main__":
    main()
