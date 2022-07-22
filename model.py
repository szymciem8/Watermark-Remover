import tensorflow as tf
from tensorflow import keras

from tensorflow.keras import layers, models


def cnn_model(img_size, image_width=256, image_heigh=256):
    """_summary_
    Creates CNN model. 

    Args:
        img_size (_type_): _description_
        image_width (int, optional): _description_. Defaults to 256.
        image_heigh (int, optional): _description_. Defaults to 256.

    Returns:
        _type_: _description_
    """
    
    
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3,3), activation="relu", input_shape=(image_width, image_heigh, 3)))
    model.add(layers.Conv2D(64, (3,3), activation="relu"))
    model.add(layers.Conv2D(128, (3,3), activation="relu"))
    model.add(layers.Conv2D(256, (3,3), activation="relu"))
    model.add(layers.Conv2D(512, (3,3), activation="relu"))
    model.add(layers.Conv2D(3, (3,3), activation="sigmoid"))
    
    return model

