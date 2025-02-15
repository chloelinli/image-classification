import numpy as np
import pandas as pd


def main():

    # paths
    path = 'projects/art_facial_recognition/final'

    # import and reshape data
    training = reshape(path+'/training_images.csv')
    test_easy = reshape(path+'/testingE_images.csv')
    test_medi = reshape(path+'/testingM_images.csv')
    test_hard = reshape(path+'/testingH_images.csv')

    # compute training scores
    scores = train(path+'/xgboost', training)

    # compute test scores
    score_e = test_scores(scores, test_easy)
    score_m = test_scores(scores, test_medi)
    score_h = test_scores(scores, test_hard)

    # recognition
    reco_e = recognize(scores, score_e)
    reco_m = recognize(scores, score_m)
    reco_h = recognize(scores, score_h)

    # check accuracy for each character, save values
    [init, unrel] = check_tuple(reco_e, reco_m, reco_h)

    # to csv, as xgboost
    to_csv(path+'/results/initial.csv', path+'/results/unrelated.csv', init, unrel)


"""
this method is a direct copy from recognize_eigen
arguments:
    path: path to csv
returns data
"""
def reshape(path):
    
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
this method initializes the prediction with the average of the training data
and updates the prediction with the prediction, data, and number of iterations, 
and then saves the final prediction as a csv
argument:
    path: folder to save data to
    data: training data to compute initial prediction score
returns final prediction
"""
def train(path, data):

    # initialize predictions with average
    prediction = np.mean(data)
    prediction = np.full_like(data, prediction)

    # update predictions
    prediction = update_predictions(prediction, data, 5)

    # save to csv
    df = pd.DataFrame(prediction)
    df.to_csv(path+'/scores.csv', index=False)

    return prediction


"""
this method updates prediction scores using xgboost from scratch
arguments:
    prediction: predicted values to update
    data: data representing true values
    num_iterations: number of times to update prediction
returns final prediction scores
"""
def update_predictions(prediction, data, num_iterations):

    # for each iteration, compute gradient and hessian, update predictions
    for i in range(num_iterations):

        # compute gradient and hessian
        grad, hess = gradient_hessian_helper(data, prediction)

        # compute optimal step size to update predictions
        step = np.sum(grad) / np.sum(hess)

        # update predictions
        prediction = prediction - step * grad
        
    return prediction


"""
this method computes the gradient boosting and hessian values
for the current prediction
arguments:
    data: data containing true values
    pred: current prediction values
returns gradient and hessian
"""
def gradient_hessian_helper(data, pred):

    grad = pred - data

    # hessian is always 1 for mean squared error (2nd derivative)
    hess = np.ones_like(pred)

    return grad, hess


"""
this method computes testing scores with the test data and training 
prediction scores. to avoid any issues with array broadcasting, we 
can cut off part of the prediction values to the same size of the data
arguments:
    pred: final prediction from training data
    data: test data
returns final testing prediction scores
"""
def test_scores(pred, data):

    temp = pred[:data.shape[0]]
    model_prediction = update_predictions(temp, data, 10)

    return model_prediction


"""
this method is a direct copy from recognize_eigen, with the exception of 
specific snippets regarding SVDs. the main similarity is the nested loop 
finding the smallest squared difference between both sets of scores
arguments:
    scores: training scores
    scores_test: testing scores
returns index of shortest distance between scores corresponding to image with smallest difference
"""
def recognize(scores, scores_test):

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
this method is a direct copy from recognize_eigen, pasing in tuples 
containg values for comparison
arguments:
    reco_e: easy smallest difference index
    reco_m: medium smallest difference index
    reco_h: hard smallest difference index
returns list of counts of actual image matches
"""
def check_tuple(reco_e, reco_m, reco_h):

    """
    given:
        train[0:30], reco_e[0:10], reco_m[0:10], reco_h[0:10] = initial character
        train[30:35], reco_e[10:15] = unrelated 1
        train[35:40], reco_e[15:]   = unrelated 2
        train[40:45], reco_m[10:15] = unrelated 3
        train[45:50], reco_m[15:]   = unrelated 4
        train[50:55], reco_h[10:15] = unrelated 5
        train[55:],   reco_h[15:]   = unrelated 6
    expected:
        indE[0:10], indM[0:10], indH[0:10] = 0 to 29
        indE[10:15] = 30 to 34
        indE[15:]   = 35 to 39
        indM[10:15] = 40 to 44
        indM[15:]   = 45 to 49
        indH[10:15] = 50 to 54
        undH[15:]   = 55 to 59
    """

    # initial character
    e_init = (reco_e, 0, 30, 0, 10)
    m_init = (reco_m, 0, 30, 0, 10)
    h_init = (reco_h, 0, 30, 0, 10)
    init = [e_init, m_init, h_init]
    init_actual = []

    for i in range(len(init)):
        init_actual.append(accu(init[i]))
    
    # unrelated characters, e/m/h
    e_1 = (reco_e, 30, 35, 10, 15)
    e_2 = (reco_e, 35, 40, 15, 20)

    m_1 = (reco_m, 40, 45, 10, 15)
    m_2 = (reco_m, 45, 50, 15, 20)

    h_1 = (reco_h, 50, 55, 10, 15)
    h_2 = (reco_h, 55, 60, 15, 20)

    unrelated = [e_1, e_2, m_1, m_2, h_1, h_2]
    unrel_actual = []

    for j in range(len(unrelated)):
        unrel_actual.append(accu(unrelated[j]))
    
    return [init_actual, unrel_actual]


"""
this method is a direct copy from recognize_eigen, comparing 
the expected and actual results of the recognition method
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
this method reads in the initial and unrelated accuracy percentages
as dataframes, adds a new column for the xgboost values, and re-exports
arguments:
    p_init: path to initial values csv
    p_unrel: path to unrelated values csv
    init: initial character accuracy
    unrel: unrelated character accuracy
"""
def to_csv(p_init, p_unrel, init, unrel):

    # read csv of previous accuracy values
    init_df = pd.read_csv(p_init)
    unrel_df = pd.read_csv(p_unrel)

    # add column for xgboost
    init_df['Xgboost'] = init
    unrel_df['Xgboost'] = unrel

    init_df.to_csv(p_init, index=False)
    unrel_df.to_csv(p_unrel, index=False)



if __name__ == '__main__':
    main()