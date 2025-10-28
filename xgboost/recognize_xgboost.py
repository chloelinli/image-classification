"""
chloe rushing

this script attempts classification of images by using a simple 
xgboost tree with gradients and steps to ensure the training 
data fits to the indicies and ensure the testing data does not 
converge. it allows randomization and reproducibility 
using a seed and global variables.
"""


# import statements
import numpy as np
import pandas as pd

# global variables
TEST_SIZE = 0.2
NUM_LOOPS = 5

# reproducibility
np.random.seed(7)


def main():

    # get full data and split into train test sets
    data = np.genfromtxt('data/converted_dataset.csv', delimiter=',')
    train, test, train_ind, test_ind = train_test_split(data, TEST_SIZE, len(data))

    # fit training data
    gradients, steps = fit(train, train_ind)

    # compute test scores
    test_preds = predict(test, gradients, steps)

    # check accuracy of predictions
    accu = check_accuracy(test_preds, test_ind)
    print(f"recognition accuracy: {accu:.2f}%")

    # export predicted vs actual values
    df = pd.DataFrame({'predicted':test_preds, 'actual':test_ind})
    df.to_csv('results/xgboost.csv', index=False)


def train_test_split(arr, test_size, data_size):

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
    train, test = arr[train_ind,:], arr[test_ind,:]

    # export training and test data
    train_df = pd.DataFrame(train)
    test_df = pd.DataFrame(test)

    train_df.to_csv('eigen/training.csv', index=False, header=False)
    test_df.to_csv('eigen/testing.csv', index=False, header=False)

    return train, test, train_ind, test_ind


def fit(data, ind):

    """
    initializes prediction with average of training data indicies and updates 
    using tree of iterations, update vector gradients, and step size scalers, 
    returning the fitted predictions
        
    ### arguments:
    data: training data\n
    ind: training data indicies

    ### returns:
    gradients: feature-wise update vectors\n
    steps: scalar weights for each update
    """

    # initialize predictions
    base_pred = np.mean(ind)
    error = ind - base_pred
    gradients = []
    steps = []

    # update predictions using gradient, hessian, steps
    for i in range(NUM_LOOPS):
        grad = np.mean(data*error[:,None], axis=0)
        gradients.append(grad)

        predict = data @ grad

        step = np.dot(predict, error) / np.dot(predict, predict) + 1e-8
        steps.append(step)

    return gradients, steps


def predict(data, gradients, steps):

    """
    predicts testing image indicies using tree of iterations, vector gradients, 
    and step size scalars computed from training data

    ### arguments:
    data: test data\n
    gradients: feature-wise update vectors\n
    steps: scalar weights for each update

    ### returns:
    prediction: array of indicies predicted to map to test data pixels
    """

    # initialize prediction
    prediction = np.zeros(len(data))

    # use trained steps and gradients to update predictions for test data
    for i in range(NUM_LOOPS):

        update = data @ gradients[i]
        prediction += steps[i] * update

    return np.round(prediction).astype(int)

def check_accuracy(pred, actual):

    """
    this function the expected and actual image positions generated 
    from the predictions tree
    
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

    return 100 - (abs(correct-size)/size * 100)


if __name__ == '__main__':
    main()
