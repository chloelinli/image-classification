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
    classifiers = train_binary_logreg(train_X, train_y)

    # compute prediction scores
    test_preds = predict(test_X, classifiers)

    # check accuracy of predictions
    accu = check_accuracy(test_preds, test_y)
    print(f"recognition accuracy: {accu:.2f}%")

    # export predicted vs actual values
    df = pd.DataFrame({'actual':test_y, 'predicted':test_preds})
    df.to_csv('results/logistic_regression.csv', index=False)


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

    """
    flatten input to a range between 0 and 1
    
    ### arguments:
    z: linear combination of inputs and weights
    
    ### returns:
    standardized value
    """

    return 1 / (1 + np.exp(-z))


def train_binary_logreg(X, y):

    """
    train model using gradient descent for each unique label
    
    ### arguments:
    X: training data pixels\n
    y: training data labels
    
    ### returns:
    classifiers: dictionary mapping weight and bias for each label
    """

    # initialize weight and bias
    n_samples, n_cols = X.shape
    labels = np.unique(y)
    weight = np.zeros(n_cols)
    bias = 0.0

    classifiers = {}

    for l in labels:

        # initizlize binaries and current weight and bias
        binary_y = np.where(y == l, 1, -1)
        w = np.zeros(X.shape[1])
        b = 0.0

        for e in range(EPOCHS):

            # raw score
            z = np.dot(X, weight) + bias

            # probability
            prob = sigmoid(z)

            error = prob - y
            w = np.dot(X.T, error) / n_samples
            b = np.mean(error)

            w -= LEARNING_RATE * w
            b -= LEARNING_RATE * b
        
        classifiers[l] = (w, b)

    return classifiers


def predict(test_X, classifiers):

    """
    computes scores and labels for each test image using weight and bias

    ### arguments:
    test_X: test data pixels\n
    classifiers: dictionary mapping weight and bias for each unique label

    ### returns:
    numpy array containing predicted labels
    """

    scores = []

    # for each unique weight, predict labels
    for c in classifiers:

        w, b = classifiers[c]
        z = np.dot(test_X, w) + b
        prob = sigmoid(z)
        scores.append(prob)
    
    scores = np.array(scores).T

    # return highest probability for each image label
    return np.argmax(scores, axis=1)


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