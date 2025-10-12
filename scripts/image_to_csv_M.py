"""
This script is a direct copy of image_to_csv.py but
only converts easy difficulty test images due to previous
unknown complications when running recognize_images.py.

This script converts the medium difficulty testing data.
"""


# import statements
import matplotlib.pyplot as plt
import matplotlib.image as im # read data as numpy array
import numpy as np
import os


def main():

    path = 'projects/art_facial_recognition/final'

    # get total images
    testM_count = count_img(path+'/testing/rgb/medium') # medium

    # convert
    rgb_to_gray(path+'/testing/rgb/medium/test_rgb', testM_count, path+'/testing/gray/medium/test_gray', path+'/testingM_images.csv')


"""
counts and returns total files/images contained in directory
arguments:
    dir_path: directory containing images to count
"""
def count_img(dir_path):

    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


"""
converts and saves pictures from rgb to grayscale, and outputs data into csv
arguments:
    rgb_path: relative path to directory containing images
    num_img: total images within given directory
    gray_path: relative path to directory to save images to
    csv_name: name of csv to write to
"""
def rgb_to_gray(rgb_path, num_img, gray_path, csv_name):

    #initialize dimensions
    h = 300
    w = 300

    # open csv to write to
    csv_path = open(csv_name, 'w', encoding='utf8')
    
    # loop - conversion
    for i in range(num_img):
        # current image name
        img_path = rgb_path + str(i+1) + '.jpg'
        img_gray = gray_path + str(i+1) + '.jpg'
        
        img = im.imread(img_path)
        img_fp = img/255 # to floating point between 0 and 1
        
        # reshape from 3d to 2d to convert from rgb to gray, which will convert from 2d to 1d
        tmp_reshaped = np.reshape(img_fp, (h*w, 3))
        img_reshaped = []
        for j in range(len(tmp_reshaped)):
            pixels = tmp_reshaped[j]
            rgb_gray = (0.2989*pixels[0]) + (0.5870*pixels[1]) + (0.1140*pixels[2])
            img_reshaped.append(rgb_gray)

        # save pictures to folder and csv
        img_reshaped = np.array(img_reshaped)
        plt.imsave(img_gray, np.reshape(img_reshaped,  (h, w)), cmap='gray')
        np.savetxt(csv_path, img_reshaped, delimiter=',', newline=',')
        
        # new line if not last image
        if i < (num_img-1):
            csv_path.write('\n')



if __name__ == '__main__':
    main()