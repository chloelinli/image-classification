"""
This script converts images into usable data in csv format.

NOTE: Although converting images to CSV is not necessary, it is useful
to know how to implement reconstruction and recognition when data is
originally given in CSV format with no image reference. Images are expected
to be 300x300 pixels.

Information found to extract data from images:
- https://matplotlib.org/stable/tutorials/introductory/images.html
Added loop for multiple images.
"""

"""
file description and disclaimer?
"""

# import statements
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np
import random
import os
import pandas as pd

# global var for image sample size
NUM_IMG = 6

# reproducibility
random.seed(7)

def main():

    # paths
    img_path = 'data/rgb'
    sample_path = 'eigen/sample'
    csv_path = open(sample_path+'/train_images_sample.csv', 'w', encoding='utf8')
    
    # get sample data of 6 images by creating an array the length of the number of total images and taking a sample of those numbers as a list
    total_img = count_img(img_path)
    num_arr = np.arange(1, total_img+1)
    sample = random.sample(list(num_arr), NUM_IMG)
    #print(sample_6) -> [21, 10, 26, 42, 4, 5]

    # loop through sample image numbers, convert to grey and save image and pixel values
    for i in range (NUM_IMG):

        # read current image based on image number (position) in sample list
        img_name = img_path + '/rgb' + str(sample[i]) + '.jpg'

        img = im.imread(img_name)
        img_fp = img/255 # to floating point between 0 and 1

        # reshape from 3d to 2d to convert from rgb to grey, converting from 2d to 1d
        tmp_reshaped = np.reshape(img_fp, (90000, 3))
        img_reshaped = []

        for j in range(len(tmp_reshaped)):
            pixels = tmp_reshaped[j]
            rgb_gray = (0.2989*pixels[0]) + (0.5870*pixels[1]) + (0.1140*pixels[2])
            img_reshaped.append(rgb_gray)

        # save as images, append pixel data to array
        img_reshaped = np.array(img_reshaped)
        gray_path = sample_path + '/gray/gray' + str(sample[i]) + '.jpg'
        plt.imsave(gray_path, np.reshape(img_reshaped,  (300, 300)), cmap='gray')
        np.savetxt(csv_path, img_reshaped, delimiter=',', newline=',')

        # new line if not last image
        if i < (NUM_IMG-1):
            csv_path.write('\n')


def count_img(dir_path):

    """
    counts and returns total files/images contained in directory
    
    ### arguments:
    dir_path: directory containing images to count
    """

    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


if __name__ == '__main__':
    main()