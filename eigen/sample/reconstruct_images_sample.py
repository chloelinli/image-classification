"""
chloe rushing

this script reconstructs images using the mean of all the images 
and singular value decomposition (svds). it allows randomization 
and reproducibility with a sample size of 6.
"""

# import statements
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# global variables
NUM_IMG = 6
HEIGHT = 300
WIDTH = 300

# reproducibility
random.seed(7)

def main():
    
    """
    this function is the sole executor of the image reconstruction. it reshapes 
    the sample pixel data to work with and reconstruct as images of size 300x300 
    by utilizing svds, looking for the smallest singular values containing 
    as much dataset information as possible
    """

    # paths
    img_path = 'data/rgb'
    path = 'eigen/sample'

    # get sample data of 6 images by creating an array the length of the number of total images and taking a sample of those numbers as a list
    total_img = count_img(img_path)
    num_arr = np.arange(1, total_img+1)
    sample = random.sample(list(num_arr), NUM_IMG)
    #print(sample) # [21, 10, 26, 42, 4, 5]

    # load data
    data = np.genfromtxt(path+'/train_images_sample.csv', delimiter=',')

    # find and save average of sample data pixels
    data = np.array(data)
    avg = np.mean(data, axis=0)
    #plt.imshow(np.reshape(avg, (HEIGHT, WIDTH)), cmap='gray')
    #plt.show()

    # cannot save reshape unless temp var because we're using the original shape later
    plt.imsave(path+'/avg_sample.jpg', np.reshape(avg, (HEIGHT, WIDTH)), cmap='gray')

    # observe how pictures deviate from average;
    # study data by finding the reduced SVD of data - average

    # subtract average from data
    X = data - np.ones((6, 1)) @ avg.reshape((1, -1))

    # reduced svd
    U, S, VT = np.linalg.svd(X, full_matrices=False)
    V = VT.T
    #V = abs(V) # has negative numbers, must be nonnegative floating point between 0-1

    # training: best values to get highest accuracy in reconstruction;
    # different diagonal of s? different singular values?

    # find, plot, and save rescaled energies: what is smallest k such that E_k > 0.90? (90% of information) what about 0.99?
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

    # index 3 (svd 4), index 4 (svd 5), size 6 (index 5)
    # not a very small k value so cannot meaningfully compress data (most likely due to small dataset)
    # uncomment to see indices and length
    #print(k_90, k_99, len(E)) 

    # reconstruct each picture using first 3 and 4 singular values/vectors - display and save
    reconstruct_path = path + '/reconstructed/svd'

    U_3 = U[:, 0:4]
    S_3 = np.diag(S[0:4])
    scores_3 = U_3 @ S_3
    V_3 = V[:, 0:4]
    reconstructed_3 = scores_3 @ V_3.T

    for i in range(6):
        img = reconstructed_3[i, :] + avg
        img = np.reshape(img, (HEIGHT, WIDTH))
        plt.imsave(reconstruct_path+'3/gray'+str(sample[i])+'_3.jpg', img, cmap='gray')

    U_4 = U[:, 0:5]
    S_4 = np.diag(S[0:5])
    scores_4 = U_4 @ S_4
    V_4 = V[:, 0:5]
    reconstructed_4 = scores_4 @ V_4.T

    for i in range(6):
        img = reconstructed_4[i, :] + avg
        img = np.reshape(img, (HEIGHT, WIDTH))
        plt.imsave(reconstruct_path+'4/gray'+str(sample[i])+'_4.jpg', img, cmap='gray')


def count_img(dir_path):

    """
    counts and returns total files/images contained in directory
    
    ### arguments:
    dir_path: directory containing images to count

    ### returns
    num: total file count
    """

    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


if __name__ == '__main__':
    main()