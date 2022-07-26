import tensorflow as tf
from tensorflow import keras

from tensorflow.keras import layers, models
from keras.layers import Conv2D, MaxPooling2D, Dense, Input, Conv2D, UpSampling2D, BatchNormalization
from keras.models import Model
from keras.optimizers import Adam


def simple_cnn(img_size):
    """_summary_
    Creates CNN model. 

    Returns:
        _type_: _description_
    """
    
    
    model = models.Sequential()
    model.add(layers.Conv2D(32, (5,5), padding='same', activation="relu", input_shape=(img_size[0], img_size[1], 3)))
    model.add(layers.Conv2D(64, (5,5), padding='same', activation="relu"))
    model.add(layers.Conv2D(128, (5,5), padding='same', activation="relu"))
    model.add(layers.Conv2D(3, (5,5), padding='same', activation="sigmoid"))
    
    return model


def encoder_decoder(img_size):
    """_summary_
    Creates Autoencoder CNN model. 

    Returns:
        _type_: _description_
    """
    
    model = models.Sequential()
    
    # Encoder
    model.add(layers.Conv2D(64, (7,7), padding='same', activation='relu', input_shape=(img_size[0], img_size[1], 3)))
    model.add(layers.MaxPooling2D(2,2, padding='same'))
    model.add(layers.Conv2D(64, (7,7), padding='same', activation='relu', input_shape=(img_size[0], img_size[1], 3)))
    model.add(layers.MaxPooling2D(2,2, padding='same'))
    
    # Decoder
    model.add(layers.Conv2DTranspose(64, (7,7), strides=2, activation='relu', padding='same'))
    model.add(layers.Conv2DTranspose(64, (7,7), strides=2, activation='relu', padding='same'))
    model.add(layers.Conv2D(3, (3,3),  padding='same', activation="sigmoid"))
    
    return model

