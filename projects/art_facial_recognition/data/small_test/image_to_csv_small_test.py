"""
This script converts images into usable data in csv format.

NOTE: Although converting images to CSV is not necessary, it is useful
to know how to implement reconstruction and recognition when data is
originally given in CSV format with no image reference.

Information found to extract data from images, save 3d array to csv by reshaping to 2d:
- https://matplotlib.org/stable/tutorials/introductory/images.html
- https://www.geeksforgeeks.org/how-to-load-and-save-3d-numpy-array-to-file-using-savetxt-and-loadtxt-functions/
- https://www.pythonpool.com/numpy-reshape-3d-to-2d/
Added loop for multiple images.
"""


# import statements
import matplotlib.image as im # read data as numpy array
import numpy as np

# initialize vars for redundancy
path = 'projects/art_facial_recognition/data'

# open csv to write to
csv_path = open(path+'/train_images_small_test.csv', 'w', encoding='utf8')

# loop - conversion
for i in range(6):
    # current image name
    img_name = '/small_test/train' + str(i+1) + '.jpg'
    full_path = path + img_name

    img = im.imread(full_path)
    img_fp = img/255 # to floating point between 0 and 1

    # reshape from 3d to 2d numpy array, then 2d to 1d
    img_reshaped = np.reshape(img_fp, (90000, 3))
    img_reshaped = np.reshape(img_reshaped, (270000))

    np.savetxt(csv_path, img_reshaped, delimiter=',', newline=',')

    # new line if not last image
    if i < 5:
        csv_path.write('\n') 