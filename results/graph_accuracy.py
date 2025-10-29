# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
        fig = plot(fig, methods[i], colors[i])
    
    plt.legend()
    plt.show()


def plot(fig, method, color):

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

    ### returns
    num: total file count
    """

    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


if __name__ == '__main__':
    main()