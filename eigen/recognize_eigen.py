import numpy as np
import pandas as pd


def main():

    # get data
    avg_data = np.genfromtxt('eigen/avg_data.csv', delimiter=',')
    V_vals = np.genfromtxt('eigen/V_values.csv', delimiter=',')
    test_data = np.genfromtxt('eigen/testing.csv', delimiter=',')
    scores = np.genfromtxt('results/scores_eigen.csv', delimiter=',')

    # recognition
    recog = recognition(test_data, avg_data, V_vals, scores)

    # check accuracy for each character, save values
    #[init, unrel] = check_tuple(testE_reco, testM_reco, testH_reco)

    # export to csv
    #to_csv(path+'/results', init, unrel)


def recognition(test_data, avg, V, scores):

    """
    this function compares training and test data scores

    ### arguments:
    test_data: array of test split\n
    avg: average of training data\n
    V: V values from SVD of training data\n
    scores: scores calculated from training data

    ### returns:
    min_ind: array of indicies with shortest distance between scores
    """

    # calculate scores for test data using average of training data
    Y = test_data - np.ones((len(test_data), 1)) @ avg.reshape((1, -1))
    scores_test = Y @ V

    # data length for loops
    scores_len = len(scores)
    scores_test_len = len(scores_test)

    # initialize placeholder arrays
    min_ind = np.zeros(scores_test_len)
    dist = np.zeros(scores_len)

    # find smallest distance between each row of scores_test and scores
    for i in range(scores_test_len):
        for j in range(scores_len):
            dist[j] = np.linalg.norm(scores_test[i] - scores[j], 2)
        ind = np.argmin(dist)
        min_ind[i] = ind
    
    return min_ind


"""
this method passes in tuples containg values for comparison
arguments:
    testE_reco: easy smallest difference index
    testM_reco: medium smallest difference index
    testH_reco: hard smallest difference index
returns list of counts of actual image matches
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
arguments:
    temp tuple containing the following values that we will index
        indicies: array holding estimated indicies from recognition
        start: expected starting index for checking
        end: expected ending index for checking
            [start, end)
        in_start: starting index for estimated indicies
        in_end: ending index for estimated indicies
returns percentage of actual matches
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

     init_df.to_csv(path+'/initial.csv', index=False, header=['SVDs'])
     unrel_df.to_csv(path+'/unrelated.csv', index=False, header=['SVDs'])


if __name__ == '__main__':
    main()