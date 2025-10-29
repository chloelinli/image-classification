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


def main():

    methods = ['eigen', 'xgboost']
    colors = ['r', 'b']

    total_img = count_img('data/gray')

    # initialize plot
    fig = plt.figure(figsize=(5,5))

    # y=x line for true=prediction
    plt.plot([0,total_img], [0,total_img], 'g-')

    # set axes and title
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title('Image Classification With Various Machine Learning Methods')
    plt.axis('equal')

    # loop through methods and plot
    length = len(methods)
    for i in range(length):
        plot(methods[i], colors[i])
    
    plt.legend()
    #plt.show()

    # export graph
    fig.savefig('results/prediction_results.jpg')


def plot(method, color):

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
    plt.scatter(true_val, pred_val, color=color, label=method)


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