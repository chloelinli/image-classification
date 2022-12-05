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
import matplotlib.pyplot as plt
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

    # reshape from 3d to 2d to convert from rgb to gray, which will convert from 2d to 1d
    tmp_reshaped = np.reshape(img_fp, (90000, 3))
    img_reshaped = []
    for j in range(len(tmp_reshaped)):
        pixels = tmp_reshaped[j]
        rgb_gray = (0.2989*pixels[0]) + (0.5870*pixels[1]) + (0.1140*pixels[2])
        img_reshaped.append(rgb_gray)
    
    # save pictures to flder and csv
    img_reshaped = np.array(img_reshaped)
    gray_path = path + '/small_test/gray' + str(i+1) + '.jpg'
    plt.imsave(gray_path, np.reshape(img_reshaped,  (300, 300)), cmap='gray')
    np.savetxt(csv_path, img_reshaped, delimiter=',', newline=',')

    # new line if not last image
    if i < 5:
        csv_path.write('\n') 