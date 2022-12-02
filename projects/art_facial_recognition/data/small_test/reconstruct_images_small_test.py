"""
This script attempts to reconstruct images using the mean value of all the images.

Information found to properly reshape arrays:
- https://stackoverflow.com/questions/36412762/how-to-understand-empty-dimension-in-python-numpy-array
"""


# import statements
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread


path = 'projects/art_facial_recognition/data/train_images_small_test.csv'

# load data
data = np.genfromtxt(path, delimiter=',')

data_reshaped = []
for i in range(6):
    # remove last column -> empty last column when adding images to csv
    tmp = data[i]
    length = len(tmp)
    tmp = tmp[0:length-1]

    # reshape arrays from 1d to 3d
    tmp2 = np.reshape(tmp, (90000, 3)) # 1d to 2d
    tmp_reshaped = np.reshape(tmp2, (300, 300, 3)) # 2d to 3d
    # array to list to append
    tmp_to_list = tmp_reshaped.tolist()
    data_reshaped.append(tmp_to_list)

# list to array to use for plotting
data_reshaped = np.array(data_reshaped)

# find average of data
avg = np.mean(data_reshaped, axis=0)
plt.imshow(avg)
plt.show()