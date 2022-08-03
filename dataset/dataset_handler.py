import os
from tensorflow import keras
from tensorflow.keras.utils import load_img
import tensorflow as tf
import numpy as np
import boto3
from PIL import Image
import io

from dataset.watermark_generator import create_watermark, create_watermark_net, generate_random_text

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
    
    
class HotWatermarkedImages(WatermarkedImages):
    """_summary_
    Create watermarked images automatically. 
    Args:
        WatermarkedImages (_type_): _description_
    """
    
    def __getitem__(self, idx):
        i = idx * self.batch_size
        batch_input_image_paths = self.input_img_paths[i : i + self.batch_size]
        x = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        y = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        for j, path in enumerate(batch_input_image_paths):
            img = np.array(keras.preprocessing.image.img_to_array(load_img(path, target_size=self.img_size)))
            x[j] = img / 255.0
            y[j] = create_watermark_net(img, generate_random_text()) / 255.0
            
        return x, y
    
    
class HotWatermarkedImagesS3(keras.utils.Sequence):
    """_summary_
    Use images stored in AWS S3 instance. Create watermarked imges each time the batch is loaded. 
    Args:
        keras (_type_): _description_
    """
    
    def __init__(self, bucket, batch_size, img_size, dir_name="images"):
        self.bucket = bucket
        self.batch_size = batch_size
        self.img_size = img_size
        self.files = np.array([obj.key for obj in bucket.objects.filter(Prefix=dir_name+"/")])
        
        
    def load_image(self, key):
        object = self.bucket.Object(key)
        response = object.get()
        file_stream = response['Body']
        im = Image.open(file_stream)
        return np.array(im)
        
    def __len__(self):
        return len(self.files) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, output) that corresponds to batch idx"""
        
        i = idx * self.batch_size
        batch_input_image_paths = self.files[i : i + self.batch_size]
        x = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        y = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        for j, path in enumerate(batch_input_image_paths):
            img = np.array(tf.image.resize(self.load_image(path), self.img_size))
            x[j] = img / 255.0
            y[j] = create_watermark_net(x[j], generate_random_text()) / 255
            
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