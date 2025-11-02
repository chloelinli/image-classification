import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im


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

    
if __name__ == '__main__':
    main()