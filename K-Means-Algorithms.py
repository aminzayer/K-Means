"""
K-Means++ Initialization and Visualization.

This module demonstrates the K-Means++ initialization algorithm for clustering.
It generates synthetic data using multivariate normal distributions and visualizes
the step-by-step selection of initial centroids.

The script performs the following steps:
1. Generates four clusters of 2D data points.
2. Combines and shuffles the data.
3. Initializes centroids using the K-Means++ strategy.
4. Visualizes the selection process using Matplotlib.
"""

# importing dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# creating data
mean_01 = np.array([0.0, 0.0])
cov_01 = np.array([[1, 0.3], [0.3, 1]])
dist_01 = np.random.multivariate_normal(mean_01, cov_01, 100)

mean_02 = np.array([6.0, 7.0])
cov_02 = np.array([[1.5, 0.3], [0.3, 1]])
dist_02 = np.random.multivariate_normal(mean_02, cov_02, 100)

mean_03 = np.array([7.0, -5.0])
# Note: cov_03 and cov_04 are defined but not used in data generation below.
# dist_03 and dist_04 use cov_01.
cov_03 = np.array([[1.2, 0.5], [0.5, 1, 3]])
dist_03 = np.random.multivariate_normal(mean_03, cov_01, 100)

mean_04 = np.array([2.0, -7.0])
cov_04 = np.array([[1.2, 0.5], [0.5, 1, 3]])
dist_04 = np.random.multivariate_normal(mean_04, cov_01, 100)

data = np.vstack((dist_01, dist_02, dist_03, dist_04))
np.random.shuffle(data)

# function to plot the selected centroids


def plot(data, centroids):
    """
    Plots the data points and the selected centroids.

    Visualizes the current state of centroid selection, showing all data points,
    previously selected centroids (in black), and the newly selected centroid (in red).

    Args:
        data (numpy.ndarray): A 2D array of shape (N, 2) containing the data points.
        centroids (numpy.ndarray): A 2D array of shape (M, 2) containing the selected centroids.
            The last element in this array is considered the 'next' or most recently added centroid.

    Returns:
        None
    """
    plt.scatter(data[:, 0], data[:, 1], marker='.',
                color='gray', label='data points')
    plt.scatter(centroids[:-1, 0], centroids[:-1, 1],
                color='black', label='previously selected centroids')
    plt.scatter(centroids[-1, 0], centroids[-1, 1],
                color='red', label='next centroid')
    plt.title('Select % d th centroid' % (centroids.shape[0]))

    plt.legend()
    plt.xlim(-5, 12)
    plt.ylim(-10, 15)
    plt.show()

# function to compute euclidean distance


def distance(p1, p2):
    """
    Computes the squared Euclidean distance between two points.

    Args:
        p1 (numpy.ndarray): The first point (1D array).
        p2 (numpy.ndarray): The second point (1D array).

    Returns:
        float: The squared Euclidean distance between p1 and p2.
    """
    return np.sum((p1 - p2)**2)


# initialization algorithm
def initialize(data, k):
    """
    Initializes centroids using the K-Means++ algorithm.

    This function selects the initial centroids for K-Means clustering. The first centroid
    is chosen randomly. Subsequent centroids are chosen from the remaining data points
    with probability proportional to the squared distance from the nearest existing centroid.
    In this implementation, the point with the maximum distance to the nearest centroid
    is deterministically selected as the next centroid.

    Args:
        data (numpy.ndarray): A 2D array of shape (N, 2) containing the data points.
        k (int): The number of clusters (centroids) to select.

    Returns:
        list: A list of selected centroids, where each centroid is a numpy array of shape (2,).
    """
    # initialize the centroids list and add
    # a randomly selected data point to the list
    centroids = []
    centroids.append(data[np.random.randint(
        data.shape[0]), :])
    plot(data, np.array(centroids))

    # compute remaining k - 1 centroids
    for c_id in range(k - 1):

        # initialize a list to store distances of data
        # points from nearest centroid
        dist = []
        for i in range(data.shape[0]):
            point = data[i, :]
            d = sys.maxsize

            # compute distance of 'point' from each of the previously
            # selected centroid and store the minimum distance
            for j in range(len(centroids)):
                temp_dist = distance(point, centroids[j])
                d = min(d, temp_dist)
            dist.append(d)

        # select data point with maximum distance as our next centroid
        dist = np.array(dist)
        next_centroid = data[np.argmax(dist), :]
        centroids.append(next_centroid)
        dist = []
        plot(data, np.array(centroids))
    return centroids


# call the initialize function to get the centroids
centroids = initialize(data, k=4)
