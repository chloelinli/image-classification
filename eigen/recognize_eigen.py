"""
chloe rushing

this script attempts classification of image by reconstructing 
and calculating SVD values to compare scores between training 
and test data split. it allows randomization and reproducibility 
using a seed and global variables.
"""


# import statements
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

# global variables
TEST_SIZE = 0.2
HEIGHT = 300
WIDTH = 300

# reproducibility
random.seed(7)


def main():

    # get full data and split into train and test sets
    data = np.genfromtxt('data/converted_dataset.csv', delimiter=',')
    train, test, train_ind, test_ind = train_test_split(data, TEST_SIZE, len(data))

    # reconstruct training data
    k_90, data_k90, k_99, data_k99, avg, V, scores = reconstruct('eigen', train, train_ind)

    # calculate accuracies
    #print(f"average for k_90 energy: {k_90}")
    #accuracy(train, data_k90)
    #print(f"average for k_99: {k_99}")
    #accuracy(train, data_k99)

    # recognition
    pred = recognition(test, avg, V, scores)

    # check accuracy for each character, save values
    accu = check_accuracy(pred, test_ind)
    print(accu)


def train_test_split(arr, test_size, data_size):

    """
    splits data array based on test set size and dataset size
    
    ### arguments:
    arr: numpy array of dataset\n
    test_size: percentage of dataset to create as test set\n
    data_size: size of dataset

    ### returns
    train: training data\n
    test: test data\n
    train_ind: indicies of training data\n
    test_ind: indicies of test data
    """

    # store mixed up indicies of array and save split sizes
    indicies = np.random.permutation(data_size)
    
    test_p = int(data_size * test_size)
    train_p = int(data_size - test_p)

    # split indicies based on split sizes then use indicies to split data to return
    train_ind, test_ind = indicies[:train_p], indicies[train_p:]
    train, test = arr[train_ind,:], arr[test_ind,:]

    # export training and test data
    train_df = pd.DataFrame(train)
    test_df = pd.DataFrame(test)

    train_df.to_csv('eigen/training.csv', index=False, header=False)
    test_df.to_csv('eigen/testing.csv', index=False, header=False)

    return train, test, train_ind, test_ind


def reconstruct(path, data, ind):
    
    """
    reconstructs and saves SVD V values and images using (data - avg of data), returns energy containing over 90 and 99% of information
    
    ### arguments:
    path: path to eigen project folder\n
    data: training data set\n
    ind: indicies corresponding to images in training data set

    ### returns
    k_90: energy with > 90% info\n
    data_k90: reconstructed images using > 90% info\n
    k_99: energy with > 99% info\n
    data_k99: reconstructed images using > 99% info\n
    avg: average of training data\n
    V: V values from training SVD\n
    scores: scores calculated from training data
    """

    size = len(ind)

    # find average of data
    avg = np.mean(data, axis=0)

    # uncomment to view
    #plt.imshow(np.reshape(avg, (HEIGHT, WIDTH)), cmap='gray')
    #plt.show()
    plt.imsave(path+'/avg.jpg', np.reshape(avg, (HEIGHT, WIDTH)), cmap='gray')

    # observe how pictures deviate from average;
    # study data by finding the reduced SVD of data - average

    # subtract average from data
    X = data - np.ones((size, 1)) @ avg.reshape((1, -1))

    # reduced svd, export v values
    U, S, VT = np.linalg.svd(X, full_matrices=False)
    V = VT.T
    v_df = pd.DataFrame(V)
    v_df.to_csv(path+'/V_values.csv', index=False, header=False)

    # empty array to save scores to
    scores_arr = np.empty((size, size))

    # calculate scores for training images and replace empty position in array
    scores = X @ V
    for i in range(size):
        s = np.array(scores[i])
        scores_arr[i] = s
    
    # export v values
    scores_df = pd.DataFrame(scores_arr)
    scores_df.to_csv('results/scores_eigen.csv', index=False, header=False)

    # training: best values to get highest accuracy in reconstruction;
    # different diagonal of s? different singular values?

    # find, plot, and save rescaled energies
    E = np.cumsum(S**2) / np.sum(S**2)

    fig, (svd_val, scaled_energies) = plt.subplots(2)

    svd_val.set_title('Singular Values')
    scaled_energies.set_title('Scaled Energies of SVDs')

    plt.subplots_adjust(hspace=0.5)

    svd_val.plot(S, 'ro')
    scaled_energies.plot(E, 'ro')

    # uncomment to view
    #plt.show()
    fig.savefig(path+'/svds_scaled_energies.jpg')

    # what is largest k such that E_k > 0.90 (90% of information)? what about 0.99?
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

    # index 36 (svd 37), index 55 (svd 56), size 60 (index 59)
    # decently sized k value so can possibly meaningfully compress data without too much memory
    # uncomment to see indices and length
    #print(k_90, k_99, len(E))

    # display and saved reconstructed images and data

    # svd containing > 90% information
    U_k90 = U[:, :k_90+1]
    S_k90 = np.diag(S[:k_90+1])
    scores_k90 = U_k90 @ S_k90
    V_k90 = V[:, :k_90+1]
    reconstructed_k90 = scores_k90 @ V_k90.T

    data_k90 = []
    for i in range(size):
        img_num = ind[i]
        img = reconstructed_k90[i, :] + avg
        data_k90.append(img)

        img = np.reshape(img, (HEIGHT, WIDTH))
        plt.imsave(path+'/reconstructed/k_90/k90_'+str(img_num+1)+'.jpg', img, cmap='gray')
    data_k90 = np.array(data_k90)

    # svd containing > 99% information
    U_k99 = U[:, :k_99+1]
    S_k99 = np.diag(S[:k_99+1])
    scores_k99 = U_k99 @ S_k99
    V_k99 = V[:, :k_99+1]
    reconstructed_k99 = scores_k99 @ V_k99.T

    data_k99 = []
    for i in range(size):
        img_num = ind[i]
        img = reconstructed_k99[i, :] + avg
        data_k99.append(img)

        img = np.reshape(img, (HEIGHT, WIDTH))
        plt.imsave(path+'/reconstructed/k_99/k99_'+str(img_num+1)+'.jpg', img, cmap='gray')
    data_k99 = np.array(data_k99)

    return k_90, data_k90, k_99, data_k99, avg, V, scores


def accuracy(original, reconstructed):

    """
    calculates average accuracy of reconstructed grayscale pixel

    ### arguments:
    original: training data\n
    reconstructed: reconstructed data based on passed-in k-value
    """

    err = []
    avg = []
    size = len(original)

    # calculate error (without percent)
    for i in range(size):
        o = original[i]
        r = reconstructed[i]
        err.append(abs(o-r)/r)

    # calulate accuracy
    err = np.array(err)
    acc = np.ones((size, HEIGHT*WIDTH)) - err

    # calculate average accuracy per image
    for i in range(size):
        tmp = acc[i]
        avg.append(np.sum(tmp)/len(tmp))
    
    avg = np.array(avg)

    # uncomment for manual input into separate csv - want to compile different accuracies in the future
    print(avg)


def recognition(test_data, avg, V, scores):

    """
    this function compares training and test data scores

    ### arguments:
    test_data: array of test split\n
    avg: average of training data\n
    V: V values from SVD of training data\n
    scores: scores calculated from training data

    ### returns:
    min_ind: array of indicies with shortest distance between scores
    """

    # calculate scores for test data using average of training data
    Y = test_data - np.ones((len(test_data), 1)) @ avg.reshape((1, -1))
    scores_test = Y @ V

    # data length for loops
    scores_len = len(scores)
    scores_test_len = len(scores_test)

    # initialize placeholder arrays
    min_ind = np.zeros(scores_test_len)
    dist = np.zeros(scores_len)

    # find smallest distance between each row of scores_test and scores
    for i in range(scores_test_len):
        for j in range(scores_len):
            dist[j] = np.linalg.norm(scores_test[i] - scores[j], 2)
        ind = np.argmin(dist)
        min_ind[i] = ind
    
    return min_ind


def check_accuracy(pred, actual):

    """
    this function the expected and actual image positions generated 
    from the recognitino method
    
    ### arguments:
    pred: expected image indicies\n
    actual: actual image indicies

    ### returns:
    error rate of exact classification using formula (measured - given) / given * 100
    """

    correct = 0

    size = len(actual)
    
    for i in range(size):
        if int(actual[i]) == int(pred[i]):
            correct += 1

    return abs(correct-size)/size * 100


if __name__ == '__main__':
    main()