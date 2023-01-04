import numpy as np


def main():
    path = 'projects/art_facial_recognition/final'

    # remove last column in csvs
    scores = reshaping(path+'/scores.csv')
    testing_easy = reshaping(path+'/testingE_images.csv')
    testing_medi = reshaping(path+'/testingM_images.csv')
    testing_hard = reshaping(path+'/testingH_images.csv')


"""
this method is similar to the reshaping method in reconstruct_images.py
instead of finding the average, we are only reshaping the data
arguments:
    path: path to file
"""
def reshaping(path):
    # load data
    data = np.genfromtxt(path, delimiter=',')
    l = len(data)

    # remove last column
    data_reshaped = []
    for i in range(l):
        tmp = data[i]
        length = len(tmp)
        tmp = tmp[:length-1]
        data_reshaped.append(tmp)
    
    # list to array
    data_reshaped = np.array(data_reshaped)
    return data_reshaped


if __name__ == '__main__':
    main()