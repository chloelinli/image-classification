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
    y = get_labels()

    train_X, test_X, train_y, test_y = train_test_split(X, y, TEST_SIZE, len(X))

    # get predictions (no fit needed)
    test_preds = predict(train_X, train_y, test_X)

    # check accuracy of predictions
    accu = check_accuracy(test_preds, test_y)
    print(f"recognition accuracy: {accu:.2f}%")

    # export predicted vs actual values
    df = pd.DataFrame({'actual':test_y, 'predicted':test_preds})
    df.to_csv('results/knn.csv', index=False)


def get_labels():

    """
    grabs array of labels corresponding to the character 
    in each image

    ### returns:
    numpy array containing integer labels
    """

    labels = pd.read_csv('data/labels.csv', header=None)
    cols = ['img', 'label']
    labels.columns = cols
    labels_lst = labels['label'].tolist()

    return np.array(labels_lst)


def train_test_split(X, y, test_size, data_size):

    """
    splits data array based on test set size and dataset size
    
    ### arguments:
    X: numpy array of dataset\n
    y: dataset label\n
    test_size: percentage of dataset to create as test set\n
    data_size: size of dataset

    ### returns:
    train_X: training data split\n
    test_X: testing data split\n
    train_y: training data labels\n
    test_y: test data actual labels
    """

    # store mixed up indicies of array and save split sizes
    indicies = np.random.permutation(data_size)
    
    test_p = int(data_size * test_size)
    train_p = int(data_size - test_p)

    # split indicies based on split sizes then use indicies to split data to return
    train_ind, test_ind = indicies[:train_p], indicies[train_p:]
    train_X, test_X = X[train_ind,:], X[test_ind,:]
    train_y, test_y = y[train_ind], y[test_ind]

    return train_X, test_X, train_y, test_y


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