import argparse
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, save_img
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf

from dataset.dataset_handler import HotWatermarkedImagesS3
import boto3

# import cv2
import numpy as np
import os

class WatermarkRemover:
    
    def __init__(self, model_path):
        self.model = load_model(model_path)
        print(self.model.summary())


    def process_image(self, img_path):
#         s3 = boto3.resource('s3', region_name='eu-central-1')
#         bucket = s3.Bucket('szymciemsdatasets')
        
#         s3_seq = HotWatermarkedImagesS3(bucket, 5, (512,512), "images")
#         x, y = s3_seq.__getitem__(0)
        
#         save_img("input.png", x[0])
        
#         # img = cv2.imread(img_path)
        img = img_to_array(load_img(img_path, color_mode='rgb', target_size=(512, 512)))
#         print(img.shape)
        
        y = np.zeros((25,) + (512, 512) + (3,), dtype="float32")
        y[0] = img / 255
        
#         print(x)
        
        result = self.model.predict(y)
        
        # save_img("input.png", img)
        save_img("output.png", result[0])
        
#         result = self.model.predict(x)
#         print(x)
        
        # save_img("input.png", x[2])
#         save_img("output.png", result[3])

        # return result


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Watermark remover", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-img", "--image", help="Path to image", default="dataset/dataset/sample_images/wm_0.jpg")
    parser.add_argument("-m", "--model", help="Path to model", default="models/watermark_remover.h5")
    
    config = vars(parser.parse_args())
    
    
    watermark_remover = WatermarkRemover(config['model'])
    watermark_remover.process_image(config['image'])
    
    
    # print(config)