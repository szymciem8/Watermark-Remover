# import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.keras.utils import load_img
import numpy as np

from training.dataset_handler import WatermarkedImages

if __name__ == "__main__":

    input_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dataset/images")
    output_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dataset/labeled")

    print(input_dir)

    batch_size = 32
    img_height = 512
    img_width = 512

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

    # Split dataset



