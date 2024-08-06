import numpy as np

def dominant_value(matrix):
    eigenvalues, e = np.linalg.eig(matrix)
    dominant_eigenvalue = np.max(np.abs(eigenvalues))
    return dominant_eigenvalue, e

def inverse_matrix(matrix):
    inverse = np.linalg.inv(matrix)
    return inverse

def identity_matrix(matrix):
    dimension = matrix.shape[0]
    identity = np.eye(dimension)
    return identity

matrix = np.array([[4, 2],[1, 3]])
    
dominant = dominant_value(matrix)
print("Largest magnitude and Eigenvalues: ", dominant )
    
inv = inverse_matrix(matrix)
print("Inverse Matrix:")
print(inv)
    
I = identity_matrix(matrix)
print("Identity Matrix:")
print(I)
