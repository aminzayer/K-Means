# K-Means Clustering Algorithms

This repository contains implementations and examples of K-Means clustering algorithms in Python and C++. It demonstrates standard K-Means clustering as well as K-Means++ initialization.

## Table of Contents
- [Description](#description)
- [Files](#files)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Authors](#authors)
- [License](#license)

## Description

K-Means is a popular unsupervised machine learning algorithm used for clustering data. This repository provides:
1.  **Python Implementations**:
    *   **K-Means++ Initialization**: A demonstration of the K-Means++ algorithm for better centroid initialization, visualizing the selection steps.
    *   **Scikit-Learn Example**: A practical example using `sklearn.cluster.KMeans` on a 3D dataset.
2.  **C++ Implementation**:
    *   **Basic 1D K-Means**: A simple console application implementing K-Means from scratch for 1D integer data.

## Files

*   **`K-Means-Algorithms.py`**:
    *   **Language**: Python
    *   **Purpose**: Demonstrates the K-Means++ initialization strategy. It generates synthetic 2D data using multivariate normal distributions and visualizes the probabilistic selection of initial centroids.

*   **`K-means-Practice.py`**:
    *   **Language**: Python
    *   **Purpose**: Uses the `scikit-learn` library to cluster a small 3D dataset. It visualizes the data before and after clustering using 3D scatter plots.

*   **`K-Means-Algorithms.cpp`**:
    *   **Language**: C++ (Legacy/Turbo C++)
    *   **Purpose**: A basic implementation of K-Means for 1D data. It asks the user for numbers and initial means, then iteratively clusters them.
    *   *Note*: This file uses `<iostream.h>` and `<conio.h>`, which are deprecated in modern C++ standards. It is intended for older compilers or as an educational reference for logic.

*   **`Practice_K_Mean.ipynb`**:
    *   **Language**: Jupyter Notebook (Python)
    *   **Purpose**: An interactive notebook (with Persian comments) guiding through the same example as `K-means-Practice.py`.

## Getting Started

### Prerequisites

*   **Python**: Version 3.x
*   **C++ Compiler**: Turbo C++ (for the `.cpp` file) or any standard compiler (if code is modified).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/aminzayer/K-Means-Algorithms.git
    cd K-Means-Algorithms
    ```

2.  Install Python dependencies:
    ```bash
    pip install numpy pandas matplotlib scikit-learn
    ```

## Usage

### Running the Python Scripts

To run the K-Means++ visualization:
```bash
python K-Means-Algorithms.py
```

To run the Scikit-Learn practice script:
```bash
python K-means-Practice.py
```

### Running the C++ Program

The `K-Means-Algorithms.cpp` file is written for legacy environments (like Turbo C++ on DOS/Windows).
To run it on a modern Linux system with `g++`, you would need to modify the headers (replace `<iostream.h>` with `<iostream>`, remove `<conio.h>`, and update namespace usage).

## Authors

*   **Amin Zayeromali**
    *   [GitHub](https://github.com/aminzayer)
    *   [LinkedIn](https://ir.linkedin.com/in/aminzayeromali)
    *   [Twitter](https://twitter.com/AminZayeromali)

## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.
