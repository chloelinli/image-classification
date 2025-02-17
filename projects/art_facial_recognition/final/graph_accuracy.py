# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():

    path = 'projects/art_facial_recognition/final/results/'

    # grab headers and data as list
    [init_methods, init_rows] = prep(path+'initial.csv')
    [unrel_methods, unrel_rows] = prep(path+'unrelated.csv')

    # plot initial character as normal
    plot(init_methods, init_rows, ['Easy', 'Medium', 'Hard'])

    # subplot unrelated character
    subplot(unrel_methods, unrel_rows, ['Easy', 'Medium', 'Hard'])


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


"""
method and data and difficulty
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
    ax.set_xticks(x_axis, difficulty)
    ax.set_xlabel('Difficulty of Recognition')
    ax.set_ylabel('Accuracy (%)')
    ax.set_ylim([0, 100])
    ax.set_title('Recognition Accuracy of Machine Learning Algorithms', pad=10)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=len(method), frameon=False, fontsize=8)
    plt.show()


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

    # full plot - 2nd plot is on bottom
    ax2.set_xticks(x_axis, difficulty)
    ax2.set_xlabel('Difficulty of Recognition')
    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=len(method), frameon=False, fontsize=8)
    fig.text(0.01, 0.5, 'Accuracy (%)', va='center', rotation='vertical')
    fig.suptitle('Recognition Accuracy of Machine Learning Algorithms', fontsize=12)
    plt.show()



if __name__ == '__main__':
    main()