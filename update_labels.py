import os
import pandas as pd
import numpy as np


# get missing labels
# get img names
# get curr labels
# compare to get missing labels
# for each img plt.show()
#   prompt string input
#   if one word and exists in string-label map, save as [img, str, label]
#   append to curr labels
# rewrite csv


def main():

    # current labels
    curr_labels = pd.read_csv('data/labels.csv', header=None)
    cols = ['img', 'label']
    curr_labels.columns = cols

    # get labeled images
    labeled_img = curr_labels['img'].tolist()

    # get all image names from directory
    total_img = get_img('data/gray')
    print(list(set(total_img)-set(labeled_img)))

    """
    # get total images
    path = 'data/gray'
    num_img = count_img(path)
    labels = get_labels(num_img)
    img_label = map_img_labels(path, num_img)
    df = pd.DataFrame.from_dict(img_label.items())
    df.to_csv('data/labels.csv', index=False, header=False)
    """


def get_img(path):

    num = 0
    for root_dir, cur_dir, files in os.walk(path):
        num += len(files)
    

    files_lst = []
    for root_dir, cur_dir, files in os.walk(path):
        for f in files:
            files_lst.append(f)
    
    for i in range(num):
        f = files_lst[i]
        f = f[0:-4]
        files_lst[i] = f
    
    return files_lst


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


def map_name_label():

    mapping = {
        'shenhe':0,
        'mai':1,
        'chitoge':2,
        'mio':3,
        'echidna':4,
        'vladilena':5,
        'yue':6
    }

    return mapping


def map_img_labels(path, count):

    files_lst = []
    for root_dir, cur_dir, files in os.walk(path):
        for f in files:
            files_lst.append(f)
    
    for i in range(count):
        f = files_lst[i]
        f = f[0:-4]
        files_lst[i] = f

    img_label = {}

    for i in range(count):
        name = files_lst[i]
        num = int(name[4:])

        if (num > 0) and (num <= 30):
            img_label[name] = 0
        elif (num > 30) and (num <= 35):
            img_label[name] = 1
        elif (num > 35) and (num <= 40):
            img_label[name] = 2
        elif (num > 40) and (num <= 45):
            img_label[name] = 3
        elif (num > 47) and (num <= 50):
            img_label[name] = 4
        elif (num > 50) and (num <= 55):
            img_label[name] = 5
        else:
            img_label[name] = 6
    
    return img_label

    
if __name__ == '__main__':
    main()