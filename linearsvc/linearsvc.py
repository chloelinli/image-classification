# import statements
import numpy as np
import pandas as pd

# global variables
TEST_SIZE = 0.15

# reproducibility
np.random.seed(7)


def main():

    # get full data and split into train test sets
    X = np.genfromtxt('data/converted_dataset.csv', delimiter=',')
    y = get_labels()
    train_X, test_X, train_y, test_y = train_test_split(X, y, TEST_SIZE, len(X))

    # get unique labels
    unique_y = np.unique(y)

    # initialize weight and bias
    weight, bias = initialize_params(train_X, train_y)

    # learning rate

    """
    for each unique label
        temp_array = if l in y is label, then 1, else -1
        init temp (labels, features) and (labels)

        for epoch
            for each (x, y) in x and temp_array
                m = y * (dot(temp_feat, x) + temp_labels)

                if m < 1
                    temp_feat = teamp_feat - lr * (temp_feat - C * x * y)
                    temp_labels = temp_labels + lr * C * y
                else
                    temp_feat = temp_feat - lr * temp_feat
        append temp labels and feat to init
    """

    """
    for test
        scores = dot(features, x) + labels
        predict label = argmax(scores)
    """


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


def initialize_params(X, y):

    n_labels = len(np.unique(y))
    n_cols = X.shape[1]

    w = np.zeros((n_labels, n_cols)).astype(int)
    b = np.zeros(n_labels).astype(int)

    return w, b
    
if __name__ == '__main__':
    main()