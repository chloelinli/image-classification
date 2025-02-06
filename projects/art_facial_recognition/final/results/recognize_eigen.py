import numpy as np
import pandas as pd


def main():
    path = 'projects/art_facial_recognition/final'
    eigen = path + '/eigen'

    # remove last column in csvs
    scores = reshaping(eigen+'/scores.csv')
    test_easy = reshaping(path+'/testingE_images.csv')
    test_medi = reshaping(path+'/testingM_images.csv')
    test_hard = reshaping(path+'/testingH_images.csv')
    v_val = reshaping(eigen+'/V_values.csv')

    # recognition
    
    """
    given:
        train[0:30], testE[0:10], testM[0:10], testH[0:10] = initial character
        train[30:35], testE[10:15] = unrelated 1
        train[35:40], testE[15:]   = unrelated 2
        train[40:45], testM[10:15] = unrelated 3
        train[45:50], testM[15:]   = unrelated 4
        train[50:55], testH[10:15] = unrelated 5
        train[55:],   testH[15:]   = unrelated 6
    expected:
        indE[0:10], indM[0:10], indH[0:10] = 0 to 29
        indE[10:15] = 30 to 34
        indE[15:]   = 35 to 39
        indM[10:15] = 40 to 44
        indM[15:]   = 45 to 49
        indH[10:15] = 50 to 54
        undH[15:]   = 55 to 59
    """
    testE_reco = recognition(test_easy, scores, v_val)
    testM_reco = recognition(test_medi, scores, v_val)
    testH_reco = recognition(test_hard, scores, v_val)

    # check accuracy for each character, save values
    [init, unrel] = check_tuple(testE_reco, testM_reco, testH_reco)

    # export to csv
    to_csv(path+'/results', init, unrel)


"""
this method is similar to the reshaping method in reconstruct_images.py but we are are only reshaping the data
returns data
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


"""
this method compares testing and training scores
    first 30 of training images are initial character
    last 30 are split evenly among six unrelated characters;
    first 10 of each set of test images are initial character
    last 10 of each set are split evenly among two unrelated characters
returns index of shortest distance between scores corresponding to image with smallest difference
arguments:
    test_data: testing data of each difficulty
    scores: scores of training data
    V: V values from training SVD
"""
def recognition(test_data, scores, V):
    avg = np.mean(test_data)
    Y = test_data - np.ones((len(test_data), 1)) @ avg.reshape((1, -1))
    scores_test = Y @ V

    scores_len = len(scores)
    scores_test_len = len(scores_test)

    min_ind = np.zeros(scores_test_len)
    dist = np.zeros(scores_len)

    """
    find difference between each row of scores_test and scores
    smallest distance correctly identifies each character?
    """
    for i in range(scores_test_len):
        for j in range(scores_len):
            dist[j] = np.linalg.norm(scores_test[i] - scores[j], 2)
        ind = np.argmin(dist)
        min_ind[i] = ind
    
    return min_ind


"""
this method passes in tuples containg values for comparison
returns list of counts of actual image matches
arguments:
    testE_reco: easy smallest difference index
    testM_reco: medium smallest difference index
    testH_reco: hard smallest difference index
"""
def check_tuple(testE_reco, testM_reco, testH_reco):
    # initial character
    e_init = (testE_reco, 0, 30, 0, 10)
    m_init = (testM_reco, 0, 30, 0, 10)
    h_init = (testH_reco, 0, 30, 0, 10)
    init = [e_init, m_init, h_init]
    init_actual = []

    for i in range(len(init)):
        init_actual.append(accu(init[i]))
    
    # unrelated characters, e/m/h
    e_1 = (testE_reco, 30, 35, 10, 15)
    e_2 = (testE_reco, 35, 40, 15, 20)

    m_1 = (testM_reco, 40, 45, 10, 15)
    m_2 = (testM_reco, 45, 50, 15, 20)

    h_1 = (testH_reco, 50, 55, 10, 15)
    h_2 = (testH_reco, 55, 60, 15, 20)

    unrelated = [e_1, e_2, m_1, m_2, h_1, h_2]
    unrel_actual = []

    for j in range(len(unrelated)):
        unrel_actual.append(accu(unrelated[j]))
    
    return [init_actual, unrel_actual]


"""
this method compares the expected and actual results of the
recognition method
returns percentage of actual matches
arguments:
    temp tuple containing the following values that we will index
        indicies: array holding estimated indicies from recognition
        start: expected starting index for checking
        end: expected ending index for checking
            [start, end)
        in_start: starting index for estimated indicies
        in_end: ending index for estimated indicies
"""
def accu(temp):

    indicies = temp[0]
    start = temp[1]
    end = temp[2]
    in_start = temp[3]
    in_end = temp[4]

    actual = 0

    for i in range(in_start, in_end):
        if indicies[i] >= start and indicies[i] < end:
            actual += 1
    
    accuracy = actual / len(indicies[in_start:in_end])

    return accuracy


"""
this method converts the actual count lists to dataframes and exports to csv
arguments:
    path: path to save csvs
    init: list holding results from initial comparison
    unrel: list holding results from unrelated comparison
"""
def to_csv(path, init, unrel):
     
     init_df = pd.DataFrame(init)
     unrel_df = pd.DataFrame(unrel)

     init_df.to_csv(path+'/initial.csv', index=False, header=['eigen'])
     unrel_df.to_csv(path+'/unrelated.csv', index=False, header=['eigen'])


if __name__ == '__main__':
    main()