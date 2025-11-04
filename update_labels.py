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

    # if contains unlabeled image, map label
    if len(unlabeled_img) > 0:
        
        new_df = map_new_img(unlabeled_img)
        new_df.columns = cols
        curr_labels = pd.concat([curr_labels, new_df], ignore_index=True)
    
    else:
        print('no unlabeled images')
    
    # rewrite labels
    curr_labels = sort_imgs(curr_labels)
    curr_labels.to_csv('data/labels.csv', index=False, header=False)


def get_img(path):

    """
    counts and returns file image names without extension
    
    ### arguments:
    path: directory containing images

    ### returns:
    files_lst: list of file names
    """

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

    """
    currently used characters for mapping

    ### returns:
    mapping: dictionary containing name to integer label map
    """

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


def map_new_img(lst):

    """
    maps images to label
    
    ### arguments:
    lst: list containing image names that have not been mapped

    ### returns:
    dataframe conversion of dictionary containing mapped images
    """

    new_labels = {}
    mapping = map_name_label()

    for u in lst:
        img = im.imread('data/gray/'+u+'.jpg')
        plt.imshow(img)
        plt.show(block=False)
        name = input('who is this character? ')
        if name in mapping.keys():
            new_labels[u] = mapping[name]

    return pd.DataFrame.from_dict(new_labels.items())


def sort_imgs(df):

    """
    sorts dataframe by integer image position
    
    ### arguments:
    df: dataframe of mapped images

    ### returns:
    sorted dataframe
    """

    df['img_num'] = df['img'].str[4:].astype(int)
    df = df.sort_values('img_num', ignore_index=True)
    return df.drop('img_num', axis=1)


if __name__ == '__main__':
    main()