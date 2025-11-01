"""
chloe rushing

this script attempts classification of images by using a simple 
k-nearest neighbors method to compare the test and training data 
to make predictions. it allows randomization and reproducibility 
using a seed and global variables.
"""


# import statements
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# global variables
TEST_SIZE = 0.15
K = 5

# reproducibility
np.random.seed(7)


def main():

    # get full data and split into train and test sets
    X = np.genfromtxt('data/converted_dataset.csv', delimiter=',')
    y = get_labels(len(X))

    train_X, test_X, train_y, test_y, train_ind = train_test_split(X, y, TEST_SIZE, len(X))

    # get predictions (no fit needed)
    test_preds = predict(train_X, train_y, test_X)

    # check accuracy of predictions
    accu = check_accuracy(test_preds, test_y)
    print(f"recognition accuracy: {accu:.2f}%")

    # export predicted vs actual values
    df = pd.DataFrame({'actual':test_y, 'predicted':test_preds})
    df.to_csv('results/knn.csv', index=False)


def get_labels(size):

    """
    creates array of labels corresponding to the character 
    in each image
    
    ### arguments:
    size: length of dataset

    ### returns:
    arr: numpy array containing integer labels
    """

    arr = []

    for i in range(size):
        
        # append label given img num -1
        if (i >= 0) and (i < 30):
            arr.append(0)
        elif (i >= 30) and (i < 35):
            arr.append(1)
        elif (i >= 35) and (i < 40):
            arr.append(2)
        elif (i >= 40) and (i < 45):
            arr.append(3)
        elif (i >= 47) and (i < 50):
            arr.append(4)
        elif (i >= 50) and (i < 55):
            arr.append(5)
        else:
            arr.append(6)

    return np.array(arr)


def train_test_split(X, y, test_size, data_size):

    """
    splits data array based on test set size and dataset size
    
    ### arguments:
    arr: numpy array of dataset\n
    test_size: percentage of dataset to create as test set\n
    data_size: size of dataset

    ### returns:
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
    train_X, test_X = X[train_ind,:], X[test_ind,:]
    train_y, test_y = y[train_ind], y[test_ind]

    return train_X, test_X, train_y, test_y, train_ind


def predict(train, train_label, test):

    """
    this function is the sole executor of finding the k-nearest neighbors 
    with the shortest euclidian distance for each test image.
    
    ### arguments:
    train: training data\n
    train_label: training data labels\n
    test: test data
    
    ### returns:
    preds: predictions from k-nearest neighbors
    """

    preds = []

    # loop through each test image
    for t in test:

        # compute euclidean distance between test and all train
        dist = np.linalg.norm(train - t, axis=1)

        # get indicies and labels of closest neighbors
        near_ind = np.argsort(dist)[:K]
        near_label = train_label[near_ind]

        # grab most frequent label
        vals, counts = np.unique(near_label, return_counts=True)
        freq = vals[np.argmax(counts)]

        # append
        preds.append(freq)

    return np.array(preds)


def check_accuracy(pred, actual):

    """
    this function the expected and actual image labels generated 
    from the predictions tree
    
    ### arguments:
    pred: expected image labels\n
    actual: actual image labels

    ### returns:
    error rate of exact classification using formula (measured - given) / given * 100
    """

    correct = 0

    size = len(actual)
    
    for i in range(size):
        if int(actual[i]) == int(pred[i]):
            correct += 1

    return 100 - (abs(correct-size)/size * 100)


if __name__ == '__main__':
    main()