"""
chloe rushing

this script attempts classification of images by using a simple 
xgboost tree with gradients and steps. it allows randomization 
and reproducibility using a seed and global variables.
"""


# import statements
import numpy as np
import pandas as pd

# global variables
TEST_SIZE = 0.15
NUM_LOOPS = 10

# reproducibility
np.random.seed(7)


def main():

    # get full data and split into train test sets
    X = np.genfromtxt('data/converted_dataset.csv', delimiter=',')
    y = get_labels()
    train_X, test_X, train_y, test_y = train_test_split(X, y, TEST_SIZE, len(X))

    # fit training data
    gradients, steps = fit(train_X, train_y)

    # compute test scores
    test_preds = predict(test_X, gradients, steps)

    # check accuracy of predictions
    accu = check_accuracy(test_preds, test_y)
    print(f"recognition accuracy: {accu:.2f}%")

    # export predicted vs actual values
    df = pd.DataFrame({'actual':test_y, 'predicted':test_preds})
    df.to_csv('results/xgboost.csv', index=False)


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
    train_y: training data labels
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


def fit(train_data, train_labels):

    """
    initializes prediction with average of training data indicies and updates 
    using tree of iterations, update vector gradients, and step size scalers, 
    returning the fitted predictions
        
    ### arguments:
    train_data: training data\n
    train_labels: training data labels

    ### returns:
    gradients: feature-wise update vectors\n
    steps: scalar weights for each update
    """

    # initialize predictions
    base_pred = np.mean(train_labels)
    error = train_labels - base_pred
    gradients = []
    steps = []

    # update predictions using gradient, hessian, steps
    for i in range(NUM_LOOPS):
        grad = np.mean(train_data*error[:,None], axis=0)
        gradients.append(grad)

        predict = train_data @ grad

        step = np.dot(predict, error) / np.dot(predict, predict) + 1e-8
        steps.append(step)

        error -= step * predict

    return gradients, steps


def predict(test_data, gradients, steps):

    """
    predicts testing image indicies using tree of iterations, vector gradients, 
    and step size scalars computed from training data

    ### arguments:
    test_data: test data\n
    gradients: feature-wise update vectors\n
    steps: scalar weights for each update

    ### returns:
    array of indicies predicted to map to test data pixels
    """

    # initialize prediction
    prediction = np.zeros(len(test_data))

    # use trained steps and gradients to update predictions for test data
    for i in range(NUM_LOOPS):

        update = test_data @ gradients[i]
        prediction += steps[i] * update

    return np.round(prediction).astype(int)


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