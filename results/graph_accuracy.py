"""
chloe rushing

this script takes each predicted vs actual indicies results 
and graphs the values to compare to a y=x line representing 
perfect predictions.
"""


# imports
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# global variable
CURR_MAX = 6


def main():

    methods = ['eigen', 'xgboost', 'knn', 'linearsvc_ovr', 'logistic_regression']
    colors = ['y', 'r', 'b', 'g', 'c']
    size = [150, 100, 60, 30, 10]

    total_img = count_img('data/gray')

    # grab actual test labels from one file
    actual = np.genfromtxt('results/eigen.csv', delimiter=',', skip_header=1).astype(int)[:, 0]

    # initialize plot
    fig = plt.figure(figsize=(6,6))

    # y=x line for true=prediction
    plt.plot([0, CURR_MAX], [0, CURR_MAX], 'k--', label='Perfect Prediction (y=x)')
    # set axes and title
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title('Image Classification With Various Machine Learning Methods')
    plt.axis('equal')

    # loop through methods and plot
    length = len(methods)
    for i in range(length):
        plot(methods[i], colors[i], size[i])
    
    plt.legend()
    plt.show()

    # export graph
    fig.savefig('results/prediction_results.jpg')

    # plot confusion matrix for each method
    for i in range(length):
        plot_confusion_matrix(methods[i])


def plot(method, color, size):

    """
    plots predicted vs. true image index position in directory 
    by machine learning method

    ### arguments:
    method: current classification method\n
    color: corresponding color to method
    """

    # get actual and predicted indicies
    indicies = np.genfromtxt('results/'+method+'.csv', delimiter=',', skip_header=1).astype(int)
    true_val = indicies[:, 0]
    pred_val = indicies[:, 1]
    plt.scatter(true_val, pred_val, color=color, label=method, s=size)


def plot_confusion_matrix(method):
    
    # get actual and predicted indicies
    indicies = np.genfromtxt('results/'+method+'.csv', delimiter=',', skip_header=1).astype(int)
    true_val = indicies[:, 0]
    pred_val = indicies[:, 1]
    
    cm = confusion_matrix(true_val, pred_val, labels=sorted(set(true_val)))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=sorted(set(true_val)))
    disp.plot(cmap='Blues', xticks_rotation=45)
    plt.title(f"Confusion Matrix - {method}")
    plt.show()


def count_img(dir_path):

    """
    counts and returns total files/images contained in directory
    
    ### arguments:
    dir_path: directory containing images to count

    ### returns:
    num: total file count
    """

    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


if __name__ == '__main__':
    main()