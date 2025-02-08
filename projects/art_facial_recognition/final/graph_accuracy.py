# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
format multi bar chart
https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
"""

def main():

    path = 'projects/art_facial_recognition/final/results/'

    # grab headers and data as list
    [init_methods, init_rows] = prep(path+'initial.csv')
    [unrel_methods, unrel_rows] = prep(path+'unrelated.csv')

    plot(init_methods, init_rows, ['Easy', 'Medium', 'Hard'])
    plot(unrel_methods, unrel_rows, ['Easy', 'Medium', 'Hard'])


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

    lst = []

    for i,r in df.itertuples():
        lst.append(r)

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
        ax.bar_label(bars, padding=3)
        mult += 1

    # tune and format plot    
    ax.set_xticks(x_axis, difficulty)
    ax.set_xlabel("Difficulty of Recognition")
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim([0, 1])
    ax.set_title("Recognition Accuracy of Machine Learning Algorithms", y=1.1)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, ncol=len(method))
    plt.show()


if __name__ == '__main__':
    main()