"""
chloe rushing

this script converts images into usable pixel data in csv format. 
by utilizing a global variable and random sample variable, we are able 
to allow randomization and reproducibility. this test uses a sample size of 6.

although originally the assignment did not call for converting images to csv, 
it is useful for me to know how to implement the reconstruction and recognition 
of images when the data is originally given in csv format without image reference.

source for extracting data from images (i added a loop for multiple images!):
https://matplotlib.org/stable/tutorials/introductory/images.html
"""


# import statements
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np
import random
import os
import pandas as pd

# global variables
NUM_IMG = 6
HEIGHT = 300
WIDTH = 300

# reproducibility
random.seed(7)


def main():

    """
    this function is the sole executor of the image conversion. based on the 
    sample, it looks for and flattens the pixels from a 2d tuple to a 1d value. 
    it then saves the converted data as a grey image and writes the pixels to csv
    """

    # paths
    img_path = 'data/rgb'
    sample_path = 'eigen/sample'
    
    # get sample data of 6 images by creating an array the length of the number of total images and taking a sample of those numbers as a list
    total_img = count_img(img_path)
    num_arr = np.arange(1, total_img+1)
    sample = random.sample(list(num_arr), NUM_IMG)
    #print(sample) # [21, 10, 26, 42, 4, 5]

    # empty array to save data to
    converted_data = np.empty((NUM_IMG, HEIGHT*WIDTH))

    # loop through sample image numbers, convert to grey and save image and pixel values
    for i in range (NUM_IMG):

        # read current image based on image number (position) in sample list
        img_name = img_path + '/rgb' + str(sample[i]) + '.jpg'

        img = im.imread(img_name)
        img_fp = img/255 # to floating point between 0 and 1

        # reshape from 3d to 2d to convert from rgb to grey, converting from 2d to 1d
        tmp_reshaped = np.reshape(img_fp, (HEIGHT*WIDTH, 3))
        img_reshaped = []

        for j in range(len(tmp_reshaped)):
            pixels = tmp_reshaped[j]
            rgb_gray = (0.2989*pixels[0]) + (0.5870*pixels[1]) + (0.1140*pixels[2])
            img_reshaped.append(rgb_gray)

        # replace empty position in converted array with data, save as images
        img_reshaped = np.array(img_reshaped)
        converted_data[i] = img_reshaped
        
        gray_path = sample_path + '/gray/gray' + str(sample[i]) + '.jpg'
        plt.imsave(gray_path, np.reshape(img_reshaped,  (300, 300)), cmap='gray')
        
    # turn converted data into dataframe and export
    converted_data_df = pd.DataFrame(converted_data)
    converted_data_df.to_csv(sample_path+'/train_images_sample.csv', index=False, header=False)


def count_img(dir_path):

    """
    counts and returns total files/images contained in directory
    
    ### arguments:
    dir_path: directory containing images to count

    ### returns:
    num: total file count
    """

    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


if __name__ == '__main__':
    main()