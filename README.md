# K-Means

K-Means Practice for Clustring Data

# Data-Mining Projects and Implementation

K-Means Projects and Implementation

## Description

K-Means Practice for Clustring Data

**`K-Means-Algorithms.cpp`**
This file contains a C++ implementation of the K-Means algorithm. It takes 10 integer numbers as input from the user, then prompts for two initial mean values. The program iteratively assigns each number to one of two clusters based on proximity to the current means (using absolute difference). After each iteration, it recalculates the cluster means by averaging the values within them and prints the clusters and their means. This process continues until the means stabilize. It utilizes older C++ libraries like `<iostream.h>` and `<conio.h>`.

**`K-Means-Algorithms.py`**
This Python script implements the K-Means++ initialization algorithm, a method for selecting better initial centroids for K-Means clustering.
- It uses `numpy` to generate four distinct clusters of 2D data points using multivariate normal distributions.
- A `plot` function using `matplotlib` visualizes the data points and the centroid selection process.
- The `initialize` function implements K-Means++: it randomly selects the first centroid, then iteratively selects subsequent centroids from data points with probabilities proportional to their squared distance from the nearest existing centroid (specifically picking the point with the maximum such distance).
- The script calls `initialize(data, k=4)` to select 4 initial centroids.

**`K-means-Practice.py`**
This Python script demonstrates a practical application of the K-Means clustering algorithm using the `scikit-learn` library.
- It defines a small 3-dimensional dataset (8 points, 3 features) using a `pandas` DataFrame.
- `matplotlib` is used to create an initial 3D scatter plot of the data.
- It applies `KMeans` from `sklearn.cluster` (with `K=2`) to cluster the data.
- Cluster labels are added to the DataFrame and printed.
- A final 3D scatter plot, with points colored by their assigned cluster, visualizes the result.

**`Practice_K_Mean.ipynb`**
This Jupyter Notebook serves as an interactive, Persian-language tutorial or practice exercise for K-Means clustering.
- It uses `pandas` to create an 8-point, 3-feature dataset (same as in `K-means-Practice.py`).
- `matplotlib` is used for 3D scatter plots of the initial data and the final clustered data (points colored by cluster).
- `KMeans` from `sklearn.cluster` (with `k=2`) is used to perform the clustering.
- Markdown cells and code comments are primarily in Persian, guiding the user through the K-Means process.

### K-means Practice 
Data x1=(1   1   4),x2=(2   2   1),x3=(7   5   6),x4=(6   5   5),x5=(1   0   2),x6=(9   8   7),x6=(4   5   7),x7=(2   1   2)
3D => 3 Dimention Data

### Use Matplotlib For plotting data

![image](https://user-images.githubusercontent.com/7605327/144722300-29655c1e-1bf3-472a-b50e-1c85c2ba8994.png)

### Add Clusters Label to DataFrame And Print Data
   F1  F2  F3  clusts
0   1   1   4       0
1   2   2   1       0
2   7   5   6       1
3   6   5   5       1
4   1   0   2       0
5   9   8   7       1
6   4   5   7       1
7   2   1   2       0

### Use Matplotlib For plotting Clustered data

![image](https://user-images.githubusercontent.com/7605327/144722449-f8985174-eb69-4409-a426-06f688135fe5.png)


## Getting Started

### Dependencies

* Python / C++ / C / Jupyter Notebook / Code Editor

## Help

list link to all algorithms

- [Cpp Implementation of Algorithms](https://github.com/aminzayer/C-Apps/tree/main/Algorithms)


## Authors

Amin Zayeromali

![Profile views](https://visitor-badge.glitch.me/badge?page_id=aminzayer.aminzayer)

[![Github](https://img.shields.io/github/followers/aminzayer?label=Follow&style=social)](https://github.com/aminzayer)

Twitter: [@AminZayeromali](https://twitter.com/aminzayeromali)

Instagram: [aminzayer](https://www.instagram.com/aminzayer/)

Linkedin: [aminzayeromali](https://ir.linkedin.com/in/aminzayeromali)

Google Scolar: [Amin Zayeromali](https://scholar.google.com/citations?user=IDR8QvcAAAAJ&hl=en)

Email : [Amin {dot} zayeromali {At} gmail {dot} com](&#109;&#097;&#105;&#108;&#116;&#111;:&#097;&#109;&#105;&#110;&#046;&#122;&#097;&#121;&#101;&#114;&#111;&#109;&#097;&#108;&#105;&#064;&#103;&#109;&#097;&#105;&#108;&#046;&#099;&#111;&#109;)


<h2> Connect with me </h2>
<a href = 'https://www.linkedin.com/in/aminzayeromali'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/linked-in-alt.svg"/></a> 
<a href = 'https://twitter.com/AminZayeromali'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a> 
<a href = 'https://aminzayer.ir/'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/portfolio.png"/></a> 
<a href = 'https://www.github.com/aminzayer'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a>
<br>


## License

This project is licensed under the GNU General Public License - see the LICENSE.md file for details
