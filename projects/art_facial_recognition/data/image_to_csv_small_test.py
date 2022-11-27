"""
This code was directly taken and influenced by
https://blog.finxter.com/python-convert-image-jpg-png-to-csv/
My addition involves a loop to add desired images.

This script converts images into usable data in csv format.
"""


# import statements
from PIL import Image
import numpy as np

# initialize vars for redundancy
path = 'projects/art_facial_recognition/data'
img_name = '/images/shenhe_small_test'

# open csv to write to
img_csv = open(path+'/train_images_small_test.csv', 'w', encoding='utf8')

# loop - conversion
for i in range(5):
    # current image number
    num = i + 1
    img_num = str(num) + '.jpg'

    # open and read image
    img = Image.open(path + img_name + img_num)

    # convert to numpy array
    arr = np.asarray(img)
    # print(arr.shape)

    # convert array to list
    lst = []
    for r in arr:
        temp = []
        for c in r:
            temp.append(str(c))
        lst.append(temp)

    # save list to csv -> each image is a row, after adding remove last empty column and add newline
    index = 0
    for r in lst:
        # joining list of rgb values for pixels
        img_csv.write(','.join(r))

        # if not last pixel, add comma (fence-post for each pixel)
        if index < 299:
            img_csv.write(',')
        index += 1
    
    img_csv.write('\n')