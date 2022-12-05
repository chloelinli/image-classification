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


path = 'projects/art_facial_recognition/data'


"""
load and reshape data to be able to work with as pixels;
need to have each array 300x300 with 3 rgb values for each entry
"""

# load data
data = np.genfromtxt(path+'/train_images_small_test.csv', delimiter=',')

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

# find and save average of data
avg = np.mean(data_reshaped, axis=0)
# uncomment to view and save to local machine
#plt.imshow(avg)
#plt.show()
#   plt.imsave(path+'/small_test/average.jpg', avg)


"""
observe how pictures deviate from average;
study data by finding the reduced SVD of data-average
"""

# create reshaped array of avg to be same size as reshaped data
avg_reshaped = np.array([avg, avg, avg, avg, avg, avg])

# subtract average from data
X = data_reshaped - avg_reshaped

# reduced svd
U, S, V = np.linalg.svd(X, full_matrices=False)
V = abs(V) # has negative numbers, must be nonnegative floating point between 0-1

# calculate scores for training images and save as csv for later
scores = X @ V
csv_path = open(path+'/scores_small_test.csv', 'w', encoding='utf8')
for i in range(6):
    # reshape from 3d to 1d
    tmp = np.reshape(scores[i], (90000, 3))
    tmp2 = np.reshape(tmp, (270000))
    np.savetxt(csv_path, tmp2, delimiter=',', newline=',') # remove last column later
    if i < 5:
        csv_path.write('\n')

# find, plot, and save rescaled
s = np.diagonal(S, axis1=1, axis2=2)
# # what is largest k such that E_k > 0.90? (90% of information) what about 0.99?
E = np.cumsum(s**2) / np.sum(s**2)

k_90 = 0
for i in range(len(E)):
    if E[i] > 0.9:
        k_90 = i
        break
k_99 = 0
for i in range(len(E)):
    if E[i] > 0.99:
        k_99 = i
        break

# uncomment to see indices and length
#print(k_90, k_99, len(E)) # 12, 16, 18 (last index 17); not a very small k value so cannot meaningfully compress data (most likely due to small dataset)