"""
chloe rushing

this script converts images into usable pixel data in csv format. 

although originally the assignment did not call for converting images to csv, 
it is useful for me to know how to implement the reconstruction and recognition 
of images when the data is originally given in csv format without image reference. 
the images are expected to be 300x300 pixels.

source for extracting data from images (i added a loop for multiple images!):
https://matplotlib.org/stable/tutorials/introductory/images.html
"""


# import statements
import matplotlib.pyplot as plt
import matplotlib.image as im # read data as numpy array
import numpy as np
import os
import pandas as pd

# global variables
HEIGHT = 300
WIDTH = 300


def main():

    """
    main function launching functions to count and convert data
    """

    path = 'data'

    # get total images
    train_count = count_img(path+'/rgb')

    # convert
    data = rgb_to_gray(path+'/rgb/rgb', train_count, path+'/gray/gray', path+'/converted_dataset.csv')


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


def rgb_to_gray(rgb_path, num_img, gray_path, csv_name):
    
    """
    converts and saves pictures from rgb to grayscale, and outputs data into csv
    
    ### arguments:
    rgb_path: relative path to dir containing images\n
    num_img: total images in given dir\n
    gray_path: relative path to dir to save images to\n
    csv_name: name of csv to create/write to
    """

    # empty array to save data to
    converted_data = np.empty((num_img, HEIGHT*WIDTH))

    # loop - conversion
    for i in range(num_img):
        # current image name
        img_path = rgb_path + str(i+1) + '.jpg'
        img_gray = gray_path + str(i+1) + '.jpg'
        
        img = im.imread(img_path)
        img_fp = img/255 # to floating point between 0 and 1
        
        # reshape from 3d to 2d to convert from rgb to gray, which will convert from 2d to 1d
        tmp_reshaped = np.reshape(img_fp, (HEIGHT*WIDTH, 3))
        img_reshaped = []
        for j in range(len(tmp_reshaped)):
            pixels = tmp_reshaped[j]
            rgb_gray = (0.2989*pixels[0]) + (0.5870*pixels[1]) + (0.1140*pixels[2])
            img_reshaped.append(rgb_gray)
        
        # save pictures
        img_reshaped = np.array(img_reshaped)
        plt.imsave(img_gray, np.reshape(img_reshaped,  (HEIGHT, WIDTH)), cmap='gray')
        
        # replace empty position in converted array with data
        converted_data[i] = img_reshaped

    # turn converted data into dataframe and export
    converted_data_df = pd.DataFrame(converted_data)
    converted_data_df.to_csv(csv_name, index=False, header=False)


if __name__ == '__main__':
    main()