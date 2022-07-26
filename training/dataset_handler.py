# import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.keras.utils import load_img
import numpy as np

class WatermarkedImages(keras.utils.Sequence):
    """_summary_
    Helps to iterate over the dataset
    Args:
        keras (_type_): _description_
    """
    
    def __init__(self, batch_size, img_size, input_img_paths, output_img_paths):
        self.batch_size = batch_size
        self.img_size = img_size
        self.input_img_paths = input_img_paths
        self.output_img_paths = output_img_paths
        
    def __len__(self):
        return len(self.output_img_paths) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, output) that corresponds to batch idx"""
        
        i = idx * self.batch_size
        batch_input_image_paths = self.input_img_paths[i : i + self.batch_size]
        batch_output_image_paths = self.output_img_paths[i : i + self.batch_size]
        x = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        for j, path in enumerate(batch_input_image_paths):
            img = np.array(keras.preprocessing.image.img_to_array(load_img(path, target_size=self.img_size)))
            x[j] = img/255.0
            
        y = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        for j, path in enumerate(batch_output_image_paths):
            img = np.array(keras.preprocessing.image.img_to_array(load_img(path, target_size=self.img_size)))
            y[j] = img/255.0
            
        return x, y

if __name__ == "__main__":

    input_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dataset/images")
    output_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dataset/labeled")

    print(input_dir)

    batch_size = 32
    img_height = 180
    img_width = 180

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