# Shape of a matrix 

import numpy as np 

A = np.array(
    [[1,2,3],
     [4,5,6]])

print(A.shape)

"""
(2, 3)   # 2 rows, 3 columns
"""

# ---------------------

# Multiplication 

B = np.array([
    [1,2],
    [2,3],
    [5,6]
])

print(A.shape)
print(B.shape)

C = A @ B 
print(C)
print(C.shape)


# Matrix manipulation 

# Transpose 

A = A.T
print(A.shape)


# -------------------------------
# Reshape
# 

x = np.array([1,2,3,4,5,6])
X = x.reshape(2,3) 

print(X)


# --------------------------------
# --------------------------------

# Add a column of ones 

X = np.array([
    [10,20],
    [30,40],
    [50,60]
])

ones = np.ones((X.shape[0], 1))
X_new = np.hstack([ones, X])

print(X_new)
