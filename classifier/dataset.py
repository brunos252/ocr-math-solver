import cv2
import numpy as np
import os
from tensorflow.keras.utils import to_categorical
from sklearn.utils import shuffle


def get_image(root, name):
    image = cv2.imread(os.path.join(root, name))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.GaussianBlur(gray, (5, 5), 0)


def read_images():
    """load images into numpy array"""
    """values between 0 and 255 for images"""
    images = np.empty((0, 45, 45), dtype=int)
    labels = np.empty(0, dtype=int)
    label = 0
    for root, dirs, files in os.walk("./extracted_images"):
        print(root, label)
        arr_x = np.array([get_image(root, name) for name in files])
        if arr_x.shape == (0, ):
            continue
        images = np.append(images, arr_x, 0)

        arr_y = np.array([label for _ in files])
        labels = np.append(labels, arr_y, 0)
        label += 1

    np.save("./classifier/images", images)
    np.save("./classifier/labels", labels)


def load_dataset():
    """load train and test dataset"""
    images = np.load("./classifier/images.npy")
    labels = np.load("./classifier/labels.npy")

    images, labels = shuffle(images, labels)

    train_per = int(0.85 * len(images))
    trainX = images[0:train_per]
    testX = images[train_per:]
    trainY = labels[0:train_per]
    testY = labels[train_per:]

    trainX = trainX.reshape((trainX.shape[0], 45, 45, 1))
    testX = testX.reshape((testX.shape[0], 45, 45, 1))

    trainY = to_categorical(trainY)
    testY = to_categorical(testY)

    return trainX, trainY, testX, testY
