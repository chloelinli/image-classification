import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im


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

    # get all image names from directory and find unlabeled images
    total_img = get_img('data/gray')
    unlabeled_img = list(set(total_img)-set(labeled_img))

    new_labels = {}
    mapping = map_name_label()

    for u in unlabeled_img:
        img = im.imread('data/gray/'+u+'.jpg')
        plt.imshow(img)
        plt.show(block=False)
        name = input('who is this character? ')
        if name in mapping.keys():
            new_labels[u] = mapping[name]
    
    new_df = pd.DataFrame.from_dict(new_labels.items())
    new_df.columns = cols
    df = pd.concat([curr_labels, new_df], ignore_index=True)
    df.to_csv('data/labels.csv', index=False, header=False)

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