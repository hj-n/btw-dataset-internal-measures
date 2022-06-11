import numpy as np

def centroid(X):
	"""
	Compute the centroid of a set of vectors.
	:param X: The set of vectors.
	:return: The centroid.
	"""
	return np.mean(X, axis=0)

def euc_dis(vec_1, vec_2):
	"""
	Compute the euclidean distance between two vectors.
	:param vec_1: The first vector.
	:param vec_2: The second vector.
	:return: The distance.
	"""
	return np.linalg.norm(vec_1 - vec_2)

def min_max_pairwise_distance(entire_dist):
	np.fill_diagonal(entire_dist, -np.inf)
	max_entire_dist = np.max(entire_dist)
	np.fill_diagonal(entire_dist, np.inf)
	min_entire_dist = np.min(entire_dist)

	return min_entire_dist, max_entire_dist

def min_max_dist(dist):
	min_dist = np.min(dist)
	max_dist = np.max(dist)
	return min_dist, max_dist
