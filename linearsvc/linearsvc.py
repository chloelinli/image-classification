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
    y = get_labels(len(X))

    # for each class, train binary classifier where 1 is the class and -1 is not
    # get unique labels/classes
    #unique y
    # initialize 
    # for c in unique classes
        # get params(train x, train y)

    # initialize

    # training

    # predict - compute scores
    # for test x:
        # scores =
        #predict class = armax of scores
    
    # preds
    # compare preds to test y, get accuracy


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
    
    
if __name__ == '__main__':
    main()