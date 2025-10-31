# import statements
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# global variables
TEST_SIZE = 0.2
HEIGHT = 300
WIDTH = 300

# reproducibility
np.random.seed(7)


def main():

    # get full data and split into train and test sets
    X = np.genfromtxt('data/converted_dataset.csv', delimiter=',')
    y = get_labels(len(X))

    train_X, test_X, train_y, test_y, train_ind = train_test_split(X, y, TEST_SIZE, len(X))


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

    # export training and test data
    train_df = pd.DataFrame(train_X)
    test_df = pd.DataFrame(test_X)

    train_df.to_csv('eigen/training.csv', index=False, header=False)
    test_df.to_csv('eigen/testing.csv', index=False, header=False)

    return train_X, test_X, train_y, test_y, train_ind


if __name__ == '__main__':
    main()