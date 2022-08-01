import cv2
from PIL import Image, ImageDraw, ImageFont
import random
import math
import numpy as np
import os

from sklearn import datasets

def create_watermark(image, text, x, y, font_size=12, alpha=100) -> Image:

    image = image.convert("RGBA")

    txt = Image.new('RGBA', image.size, (255,255,255,0))

    font = ImageFont.truetype("raleway/Raleway-Black.ttf", font_size)
    d = ImageDraw.Draw(txt)    

    d.text((x, y, 0), "This text should be 5 lpha", fill=(0, 0, 0, alpha), font=font)
    combined = Image.alpha_composite(image, txt)    

    return combined


def create_watermark_net(image, text) -> Image:
    PT2PX = 1.33
    width, height = image.size
    
    font_size = random.randint(10,15)

    image = image.convert("RGBA")
    txt = Image.new('RGBA', image.size, (255,255,255,0))
    font = ImageFont.truetype("raleway/Raleway-Black.ttf", font_size)
    d = ImageDraw.Draw(txt)    

    min = math.ceil(len(text)*font_size*PT2PX)
    max = int(1.2*min)

    x_spread = random.randint(min, max)
    y_spread = random.randint(min, max)/2
    
    row = 0
    margin = 0
    alpha = random.randint(150, 255)
    x, y = 5, 5
    while y < height:
        while x < width:            
            margin = (row % 2) * x_spread/2
            
            d.text((margin+x, y, 0), text, fill=(0, 0, 0, alpha), font=font)    
            x += x_spread
        x = 5
        y += y_spread
        row += 1

    image = Image.alpha_composite(image, txt)
    return image

def generate_random_text() -> str:
    
    # Get set of characters -> 1..9 + a..b + A..B
    ascii_subset = np.concatenate((np.arange(48,57), np.arange(65,90), np.arange(97,122)))

    text = ""
    for _ in range(random.randint(5,15)):
        text += chr(ascii_subset[random.randint(0, len(ascii_subset)-1)])

    return text

def generate_dataset(dir_dataset):
    ext = (".jpg", ".png", ".jpeg")
    
    parent_dir = os.path.dirname(dir_dataset)
    print(parent_dir)

    if not os.path.exists(os.path.join(parent_dir, "labeled")):
        os.mkdir(os.path.join(parent_dir, "labeled"))
        
    print(len(os.listdir(dir_dataset)))
        
    for file in os.listdir(dir_dataset):
        if file.endswith(ext):
            img = Image.open(os.path.join(dir_dataset,file))
            img = create_watermark_net(img, generate_random_text())
            img = img.convert('RGB')

            save_path = os.path.join(os.path.dirname(dir_dataset), "labeled/"+file) 
            img.save(save_path)
        else:
            continue
        

if __name__ == "__main__":

    # Some parameters
    # input_dir
    # output_dir

    generate_dataset("dataset/images")