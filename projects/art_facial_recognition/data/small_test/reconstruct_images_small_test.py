"""
This script attempts to reconstruct images using the mean value of all the images.

Information found to properly reshape arrays:
- https://stackoverflow.com/questions/36412762/how-to-understand-empty-dimension-in-python-numpy-array
"""


# import statements
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread


path = 'projects/art_facial_recognition/data'


"""
load and reshape data to be able to work with as pixels;
need to have each array 300x300 with 3 rgb values for each entry
"""

# load data
data = np.genfromtxt(path+'/small_test/train_images_small_test.csv', delimiter=',')
h = 300
w = 300

# remove last column of data -> empty from newline in image_to_csv
data_reshaped = []
for i in range(6):
    tmp = data[i]
    length = len(tmp)
    tmp = tmp[0:length-1]
    data_reshaped.append(tmp)

# list to array to use for plotting
data_reshaped = np.array(data_reshaped)

# find average of data
avg = np.mean(data_reshaped, axis=0)
# uncomment to view and save to local machine
#avg = np.reshape(avg, (h, w))
# uncomment to view and save to local machine
#plt.imshow(avg, cmap='gray')
#plt.show()
#plt.imsave(path+'/small_test/average.jpg', avg, cmap='gray')


"""
observe how pictures deviate from average;
study data by finding the reduced SVD of data - average
"""

# subtract average from data
X = data_reshaped - np.ones((6, 1)) @ avg.reshape((1, -1))

# reduced svd
U, S, VT = np.linalg.svd(X, full_matrices=False)
V = VT.T
#V = abs(V) # has negative numbers, must be nonnegative floating point between 0-1

# calculate scores for training images and save as csv for later
scores = X @ V
csv_path = open(path+'/small_test/scores_small_test.csv', 'w', encoding='utf8')
for i in range(6):
    np.savetxt(csv_path, scores[i], delimiter=',', newline=',') # remove last column later
    if i < 5:
        csv_path.write('\n')


"""
training: best values to get highest accuracy in reconstruction;
different diagonal of s? different singular values?
"""

# find, plot, and save rescaled energies
# # what is largest k such that E_k > 0.90? (90% of information) what about 0.99?
E = np.cumsum(S**2) / np.sum(S**2)

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
#print(k_90, k_99, len(E)) # 3, 4, 6 (last index 5); not a very small k value so cannot meaningfully compress data (most likely due to small dataset)

# reconstruct each picture using first 3 and 4 singular values/vectors - display and save
reconstruct_path = path + '/small_test/reconstructed/svd'

U_3 = U[:, 0:3]
S_3 = np.diag(S[0:3])
scores_3 = U_3 @ S_3
V_3 = V[:, 0:3]
reconstructed_3 = scores_3 @ V_3.T

data_3 = []
data_3_path = open(reconstruct_path+'3/svd_3_data.csv', 'w', encoding='utf8')

for i in range(6):
    img = reconstructed_3[i, :] + avg
    np.savetxt(data_3_path, img, delimiter=',', newline=',') # remove last column later
    img = np.reshape(img, (h, w))
    plt.imsave(reconstruct_path+'3/gray3_'+str(i+1)+'.jpg', img, cmap='gray')

U_4 = U[:, 0:4]
S_4 = np.diag(S[0:4])
scores_4 = U_4 @ S_4
V_4 = V[:, 0:4]
reconstructed_4 = scores_4 @ V_4.T

data_4 = []
data_4_path = open(reconstruct_path+'4/svd_4_data.csv', 'w', encoding='utf8')

for i in range(6):
    img = reconstructed_4[i, :] + avg
    np.savetxt(data_4_path, img, delimiter=',', newline=',') # remove last column later
    img = np.reshape(img, (h, w))
    plt.imsave(reconstruct_path+'4/gray4_'+str(i+1)+'.jpg', img, cmap='gray')
