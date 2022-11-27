# import statements
import numpy as np
import matplotlib.pyplot as plt

path = 'projects/art_facial_recognition/data/train_images_small_test.csv'

# load data
data = np.genfromtxt(path, delimiter=',')
h = 300
w = 300
#print(data.shape) #-> size (5, 90000) with 5 images 300x300 pixels (300x300=90000)

fig, axes = plt.subplots(2, 3, figsize=(10, 5))
row_nums = np.array([0, 9, 19, 30, 39, 49, 59])
for k in range(row_nums.size):
    img = np.reshape(data[row_nums[k], :], (h, w), order='F')
    axes[k // 3, k % 3].imshow(img, cmap='gray')
# find average of all images
"""avg = np.mean(data, axis=0)
plt.figure(figsize=(10, 10))
img = np.reshape(avg, (h, w), order='F')
plt.imshow(img)
plt.show()"""