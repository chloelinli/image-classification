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


# import statements
import matplotlib.pyplot as plt
import matplotlib.image as im # read data as numpy array
import numpy as np
import os
"""
# initialize vars for redundancy
path = 'projects/art_facial_recognition/data/small_test'

# open csv to write to
csv_path = open(path+'/train_images_small_test.csv', 'w', encoding='utf8')

# loop - conversion
for i in range(6):
    # current image name
    img_name = '/training/train' + str(i+1) + '.jpg'
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
    
    # save pictures to folder and csv
    img_reshaped = np.array(img_reshaped)
    gray_path = path + '/training/gray' + str(i+1) + '.jpg'
    plt.imsave(gray_path, np.reshape(img_reshaped,  (300, 300)), cmap='gray')
    np.savetxt(csv_path, img_reshaped, delimiter=',', newline=',')

    # new line if not last image
    if i < 5:
        csv_path.write('\n')"""


def main():
    path = 'projects/art_facial_recognition/data/final'

    # get total images for each conversion
    train_count = count_img(path+'/training/rgb')
    testE_count = count_img(path+'/testing/rgb/easy') # easy
    testM_count = count_img(path+'/testing/rgb/medium') # medium
    testH_count = count_img(path+'/testing/rgb/hard') # hard

    # convert each directory of images

"""
method looks through given directory and returns total files/images contained in it
"""
def count_img(dir_path):
    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


if __name__ == '__main__':
    main()