import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import boto3
import io

s3 = boto3.resource('s3', region_name='eu-central-1')
bucket = s3.Bucket('szymciemsdatasets')

for bucket_object in bucket.objects.all():
    print(bucket_object.key)

# object = bucket.Object('tiles/10/S/DG/2015/12/7/0/B01.jp2')

# file_stream = io.StringIO()
# object.download_fileobj(file_stream)
# img = mpimg.imread(file_stream)