import keras.models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import SGD
import tensorflow as tf
from classifier.dataset import load_dataset


model_input_shape = (45, 45, 1)
model_classes_number = 17
translate_key = {0: "(", 1: ")", 2: "+", 3: "-", 4: "0", 5: "1", 6: "2", 7: "3", 8: "4",
                 9: "5", 10: "6", 11: "7", 12: "8", 13: "9", 14: "=", 15: "/", 16: "x"}


def scale_pixels(data):
    """normalize pixels to range 0-1"""
    data_norm = data.astype('float32')
    data_norm = data_norm / 255.0
    return data_norm


def define_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=model_input_shape))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(model_classes_number, activation='softmax'))

    opt = SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def run_train():
    trainX, trainY, testX, testY = load_dataset()

    trainX = scale_pixels(trainX)
    testX = scale_pixels(testX)

    model = define_model()

    model.fit(trainX, trainY, epochs=10, batch_size=32, validation_data=(testX, testY), verbose=0)
    _, acc = model.evaluate(testX, testY, verbose=0)
    print('> %.3f' % (acc * 100.0))

    model.save("./classifier/model.h5")


def predict(image):
    """
    :param image: single character image
    :return: model predicted classification of image
    """
    image = scale_pixels(image)
    image = image.reshape((1, model_input_shape[0], model_input_shape[1], 1))

    model = keras.models.load_model("./classifier/model.h5")

    evl = model.predict_step(image)
    char = translate_key[int(tf.math.argmax(evl, 1))]

    return char


if __name__ == "__main__":
    run_train()
