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
"""
path to data
imports as dataframe
saves header
for row in data
    append row to list
return headers and list
"""
def prep(path):

    df = pd.read_csv(path)
    header = list(df.columns)

    # transpose to read each row as method
    df = df.transpose()

    lst = []

    for i,r in df.iterrows():

        # multiply for percentage format later
        temp = r*100
        lst.append(temp.to_list())

    return [header, lst]


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


"""
method and data and difficulty
"""

"""
def plot(method, data, difficulty):
    
    # prepare plot variables
    x_axis = np.arange(len(difficulty))
    width = 0.25
    mult = 0

    # method and data dictionary
    groups = {}
    for i in range(len(method)):
        groups[method[i]] = data[i]
    
    fig, ax = plt.subplots(layout='constrained')

    # place bars in chart
    for att, mea in groups.items():
        offset = width * mult
        bars = ax.bar(x_axis + offset, mea, width, label=att)
        ax.bar_label(bars, padding=3, label_type='center', fmt='%.0f%%')
        mult += 1

    # tune and format plot
    ax.set_xticks(x_axis+(width/len(method)), difficulty)
    ax.tick_params(bottom=False, left=False)
    ax.set_xlabel('Difficulty of Recognition')
    ax.set_ylabel('Accuracy (%)')
    ax.set_ylim([0, 100])
    ax.set_title('Recognition Accuracy of Machine Learning Algorithms', pad=10)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=len(method), frameon=False, fontsize=8)
    plt.show()
"""

"""
plot unrel char - unable to split without extra work (i'm lazy)
"""
def subplot(method, data, difficulty):

    """
    split data in half so only one char per difficulty
    """
    d1 = []
    d2 = []

    # for each method, split
    for i in range(len(data)):
        t1 = []
        t2 = []

        # for each difficulty, split
        for j in range(0, len(data[i]), 2):
            t1.append(data[i][j])
            t2.append(data[i][j+1])
        
        # append split method to list
        d1.append(t1)
        d2.append(t2)
    
    # method and data dictionary    
    g1 = {}
    g2 = {}
    for i in range(len(method)):
        g1[method[i]] = d1[i]
        g2[method[i]] = d2[i]

    """
    plot
    """
    # prepare plot variables
    x_axis = np.arange(len(difficulty))
    width = 0.25
    mult = 0

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    # place bars in chart
    for att, mea in g1.items():
        offset = width * mult
        bars = ax1.bar(x_axis + offset, mea, width, label=att)
        ax1.bar_label(bars, padding=3, label_type='center', fmt='%.0f%%')
        mult += 1
    
    # reset multiplier for subplot
    mult = 0
    for att, mea in g2.items():
        offset = width * mult
        bars = ax2.bar(x_axis + offset, mea, width, label=att)
        ax2.bar_label(bars, padding=3, label_type='center', fmt='%.0f%%')
        mult += 1

    """
    tune and format plot
    """
    ax1.set_ylim([0, 100])
    ax2.set_ylim([0, 100])
    ax1.tick_params(bottom=False, left=False)
    ax2.tick_params(bottom=False, left=False)

    # full plot - 2nd plot is on bottom
    ax2.set_xticks(x_axis+(width/len(method)), difficulty)
    ax2.set_xlabel('Difficulty of Recognition')
    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=len(method), frameon=False, fontsize=8)
    fig.text(0.01, 0.5, 'Accuracy (%)', va='center', rotation='vertical')
    fig.suptitle('Recognition Accuracy of Machine Learning Algorithms', fontsize=12)
    plt.show()



if __name__ == '__main__':
    main()