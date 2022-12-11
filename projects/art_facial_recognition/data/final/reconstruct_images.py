"""
This script attempts to reconstruct image through the mean of all
images and singular values. Data is expected to be in CSV format
with each row representing an image and its 300x300=90000 pixels,
as well as the pixels being in grayscale.
"""

# import statements
import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    path = 'projects/art_facial_recognition/data/final'

    # get total training images
    num = count_img(path+'/training/gray')

    # reshape data and calculate average
    data, avg = reshaping(path, num)

    # reconstruction
    k_90, k_99 = reconstruct(data, avg, path+'/scores.csv', num, path+'/reconstructed/k_9')

"""
counts and returns total files/images contained in directory
arguments:
    dir_path: directory containing images to count
"""
def count_img(dir_path):
    num = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        num += len(files)
    return num


"""
reshapes data from csv to remove last empty column and use for comparison later, returns data and average
arguments:
    path: directory to save to
    count: number of images
"""
def reshaping(path, count):
    """
    load and reshape data to be able to work with as pixels;
    need to have each array 300x300 with 3 rgb values for each entry
    """

    # load data
    data = np.genfromtxt(path+'/training_images.csv', delimiter=',')
    h = w = 300

    # remove last column of data -> empty from newline in image_to_csv
    data_reshaped = []
    for i in range(count):
        tmp = data[i]
        length = len(tmp)
        tmp = tmp[0:length-1]
        data_reshaped.append(tmp)

    # list to array to use for plotting
    data_reshaped = np.array(data_reshaped)


    # find average of data
    avg = np.mean(data_reshaped, axis=0)
    # uncomment to view
    #plt.imshow(np.reshape(avg, (h, w)), cmap='gray')
    #plt.show()
    plt.imsave(path+'/average.jpg', np.reshape(avg, (h, w)), cmap='gray')

    return data_reshaped, avg


"""
reconstructs images using data - avg of data and checks accuracy using svd
arguments:
    data: array of data pulled from csv
    avg: average of data
    scores_path: path containing scores of data
    count: number of images
    path: directory to hold reconstructed images
"""
def reconstruct(data, avg, scores_path, count, path):

    """
    observe how pictures deviate from average;
    study data by finding the reduced SVD of data - average
    """

    # subtract average from data
    X = data - np.ones((count, 1)) @ avg.reshape((1, -1))

    # reduced svd
    U, S, VT = np.linalg.svd(X, full_matrices=False)
    V = VT.T
    #V = abs(V) # has negative numbers, must be nonnegative floating point between 0-1

    # calculate scores for training images and save as csv for later
    scores = X @ V
    csv_path = open(scores_path, 'w', encoding='utf8')
    for i in range(count):
        np.savetxt(csv_path, scores[i], delimiter=',', newline=',') # remove last column later
        if i < (count-1):
            csv_path.write('\n')

    """
    training: best values to get highest accuracy in reconstruction;
    different diagonal of s? different singular values?
    """

    # find, plot, and save rescaled energies
    # what is largest k such that E_k > 0.90 (90% of information)? what about 0.99?
    E = np.cumsum(S**2) / np.sum(S**2)

    k_90 = 0
    for i in range(len(E)):
        if E[i] > 0.9:
            k_90 = i
            break

    k_99 = 0
    for i in range(len(E)):
        if E[i] > 0.99:
            k_99 = i
            break

    # index 19 (svd 20), index 27 (svd 28), size 30 (index 29)
    # not a very small k value so cannot meaningfully compress data (most likely due to small dataset)
    # uncomment to see indices and length
    #print(k_90, k_99, len(E))

    """
    display and saved reconstructed images and data using svds containing > 90% and > 99% information
    return reconstructed data
    """
    h = w = 300

    U_k90 = U[:, :k_90+1]
    S_k90 = np.diag(S[:k_90+1])
    scores_k90 = U_k90 @ S_k90
    V_k90 = V[:, :k_90+1]
    reconstructed_k90 = scores_k90 @ V_k90.T

    data_k90 = []
    for i in range(count):
        img = reconstructed_k90[i, :] + avg
        data_k90.append(img)
        img = np.reshape(img, (h, w))
        plt.imsave(path+'0/k90_'+str(i+1)+'.jpg', img, cmap='gray')
    data_k90 = np.array(data_k90)

    U_k99 = U[:, :k_99+1]
    S_k99 = np.diag(S[:k_99+1])
    scores_k99 = U_k99 @ S_k99
    V_k99 = V[:, :k_99+1]
    reconstructed_k99 = scores_k99 @ V_k99.T

    data_k99 = []
    for i in range(count):
        img = reconstructed_k99[i, :] + avg
        data_k99.append(img)
        img = np.reshape(img, (h, w))
        plt.imsave(path+'9/k99_'+str(i+1)+'.jpg', img, cmap='gray')
    data_k99 = np.array(data_k99)

    return data_k90, data_k99


if __name__ == '__main__':
    main()