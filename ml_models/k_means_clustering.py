import numpy as np

"""
Implement k-means clustering using only numpy
"""

# situation:
# we have a dataset and we want to assign each point to a cluster
# algorithm:
# randomly initialize the centroids
# then iterate until convergence (centroids difference is less than epsilon)
# at each stage, calculate the distance of each point to the k centroids
# assign the point to the cluster whose centroid it's closest to

def k_means_clustering(
        X: np.ndarray,
        k: int,
        tol: float = 1e-3,
        max_iter: int = 100
):
    d = X.shape[1]
    n = X.shape[0]
    # we assume the data is in R^n
    centroids = old_centroids = np.random.randn(k, d) # shape (k, d) (number centroids, dim)
    diff = np.ones((k, d)) # placeholder for first iteration
    iter = 0

    while np.all(diff > tol) or iter < max_iter:
        distances = np.array([[dist(x, centroid) for x in X] for centroid in centroids]) # shape (k, number of data points)
        assignments = np.array([np.argmin(distances[:, i]) for i in range(n)])
        
        # calculate new centroids
        old_centroids = centroids
        centroids = get_new_centroids(X, assignments, k)
        diff = centroids - old_centroids
        iter += 1

    return assignments

def dist(x: np.ndarray, y: np.ndarray):
    return np.sqrt(np.sum((x - y)**2))

def get_new_centroids(data: np.ndarray, assignments: np.ndarray, k: int):
    new_centroids = []
    for i in range(k):
        idx = assignments == i
        if not np.any(idx): # if i get an empty cluster i randomly reinitialize a centroid
            new_centroids.append(np.random.randn(1, data.shape[1]))
            continue
        points = data[idx]
        mean_i = np.mean(points, axis = 0)
        new_centroids.append(mean_i)
    return np.array(new_centroids)

if __name__ == "__main__":
    X = np.array([[1, 1, 1], [1, 1, 0], [-1, -2, -3], [4, 7, 8]])
    print("result", k_means_clustering(X, 2))