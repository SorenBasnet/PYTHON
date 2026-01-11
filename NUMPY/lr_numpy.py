"""
Linear Regression from scratch ( no sklearn )
"""

import numpy as np 

X = np.array([
    [1,2],
    [1,4],
    [1,3]
]) # first column = ones (bias)

y = np.array([2,3,4])


"""
Normal equation
w^=(XTX)−1XTy
"""

XtX = X.T @ X 
XtX_inv = np.linalg.inv(XtX)
Xty = X.T @ y

w = XtX_inv @ Xty

print(w)

