# import statements
import numpy as np
import pandas as pd

# global variables
TEST_SIZE = 0.15
LEARNING_RATE = 0.001
COST = 1.0
EPOCHS = 100

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

    # train binary classifer
    weight, bias = train_binary_ovr(train_X, train_y, unique_y, weight, bias)

    # compute test scores
    test_preds = predict(test_X, weight, bias)

    # check accuracy of predictions
    accu = check_accuracy(test_preds, test_y)
    print(f"recognition accuracy: {accu:.2f}%")

    # export predicted vs actual values
    df = pd.DataFrame({'actual':test_y, 'predicted':test_preds})
    df.to_csv('results/linearsvc_ovr.csv', index=False)


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

    w = np.zeros((n_labels, n_cols))
    b = np.zeros(n_labels)

    return w, b


def train_binary_ovr(X, y, unique_y, W, B):

    size = len(X)

    # train classifer and update weight and bias
    for u in unique_y:

        # initizlize binaries and current weight and bias
        binary_y = np.where(y == u, 1, -1)
        w = np.zeros(X.shape[1])
        b = 0.0

        # fit training data for each row
        for e in range(EPOCHS):

            for i in range(size):
                curr_x = X[i]
                curr_y = binary_y[i]

                # compute margin and update current weight and bias
                margin = curr_y * (np.dot(w, curr_x) + b)
                if margin < 1:
                    w -= LEARNING_RATE * (w - COST * curr_y * curr_x)
                    b += LEARNING_RATE * COST * curr_y
                else:
                    w -= LEARNING_RATE * w
        
        # store weight and bias for current unique label
        W[u] = w
        B[u] = b

    return W, B


def predict(test_X, W, B):

    scores = np.dot(test_X, W.T) + B
    
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