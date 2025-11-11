# import statements
import numpy as np
import pandas as pd

# global variables
TEST_SIZE = 0.15
LEARNING_RATE = 0.005
EPOCHS = 100
THRESHOLD = 0.5

# reproducibility
np.random.seed(7)


def main():

    # get full data and split into train test sets
    X = np.genfromtxt('data/converted_dataset.csv', delimiter=',')
    y = get_labels()
    train_X, test_X, train_y, test_y = train_test_split(X, y, TEST_SIZE, len(X))

    # fit data to compute weight and bias
    weight, bias = train_binary_logreg(train_X, train_y)

    # compute prediction scores
    test_preds = predict(test_X, weight, bias)

    # check accuracy of predictions
    accu = check_accuracy(test_preds, test_y)
    print(f"recognition accuracy: {accu:.2f}%")


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


def sigmoid(z):

    return 1 / (1 + np.exp(-z))


def train_binary_logreg(X, y):

    # initialize weight and bias
    n_samples, n_cols = X.shape
    weight = np.zeros(n_cols)
    bias = 0.0

    for e in range(EPOCHS):

        # raw score
        z = np.dot(X, weight) + bias

        # probability
        prob = sigmoid(z)

        error = prob - y
        w = np.dot(X.T, error) / n_samples
        b = np.mean(error)

        weight -= LEARNING_RATE * w
        bias -= LEARNING_RATE * b

    return weight, bias


def predict(test_X, W, B):
    
    z = np.dot(test_X, W) + B
    prob = sigmoid(z)

    return (prob >= THRESHOLD).astype(int)


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