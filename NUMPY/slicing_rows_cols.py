import numpy as np 

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Select rows 

A[0] # first row 
A[1:] # rows 1 to end
A[[0,2]] # rows 0 and 2

# Select columns 

A[:, 0] # first col
A[:, 1:] # columns 1 to end
A[:, [0,2]]


# Sub matrix 
A[:2, :2]