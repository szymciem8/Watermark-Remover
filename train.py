# import tensorflow as tf
from gc import callbacks
import os
from tensorflow import keras
from tensorflow.keras.utils import load_img
import numpy as np
from training.dataset_handler import *
import random
from model import *

from training.dataset_handler import WatermarkedImages

if __name__ == "__main__":

    input_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "training/dataset/images")
    output_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "training/dataset/labeled")

    batch_size = 4
    img_height = 512
    img_width = 512
    img_size = (img_width, img_height)

    # Get data
    input_img_paths = sorted(
        [
            os.path.join(input_dir, fname)
            for fname in os.listdir(input_dir)
        ]
    )

    output_img_paths = sorted(
        [
            os.path.join(input_dir, fname)
            for fname in os.listdir(output_dir)
        ]
    )

    print('Number of samples:', len(input_img_paths))

    for input_path, output_path in zip(input_img_paths[:10], output_img_paths[:10]):
        print(input_path, "|", output_path)

    # Prepare dataset sequence
    val_samples = 1000
    random.Random(42).shuffle(input_img_paths)
    random.Random(42).shuffle(output_img_paths)
    train_input_img_paths = input_img_paths[:-val_samples]
    train_output_img_paths = output_img_paths[:-val_samples]
    val_input_img_paths = input_img_paths[-val_samples:]
    val_output_img_paths = output_img_paths[-val_samples:]
    
    train_gen = WatermarkedImages(
        batch_size, img_size, train_input_img_paths, train_output_img_paths
    )
    
    val_gen = WatermarkedImages(batch_size, img_size, val_input_img_paths, val_output_img_paths)
    
    keras.backend.clear_session()
    
    # Load and train the model
    model = cnn_model(img_size)
    model.compile(optimizer="rmsprop", loss="sparse_categorical_crossentropy")
    
    callbacks = [
        keras.callbacks.ModelCheckpoint("watermark_remover.h5", save_best_only=True)
    ]
    
    epochs = 15
    model.fit(train_gen, epochs=epochs, validation_data=val_gen, callbacks=callbacks)