import numpy as np 

np.array([1, 2, 3], dtype=float)
"""
np.array([1, 2, 3], dtype=float)
This creates a simple 1D array from a Python list.

What it does: Converts the input data into a NumPy array.

The dtype=float part: Forces the numbers to be floating-point (e.g., 1. instead of 1), even if you provided integers.
"""


np.zeros((3, 4)) # What it does: Creates a 3x4 matrix (3 rows, 4 columns) where every single element is 0.
np.ones((2, 2)) # What it does: Similar to zeros, but fills the array with 1.
np.eye(5) # Creates a 5x5 Identity Matrix
np.arange(0, 10, 0.5) # Generates a sequence of numbers from a start (0) up to (but not including) a stop (10), incrementing by a specific step (0.5).
np.linspace(0, 1, 100)  # Stands for "Linear Space." It creates 100 evenly spaced numbers between 0 and 1 inclusive.


"""
Function,Focus,Common Use
zeros / ones,Initial values,Placeholders for calculations
eye,Matrix structure,Linear Algebra / Identity operations
arange,Step size,Iterating or fixed-interval sequences
linspace,Number of samples,Graphing and function sampling
"""


import numpy as np

x = np.array([1, 2, 3]) 
print(x.dtype)          # Output: int64 (on most 64-bit systems)

# Convert to float
y = x.astype(np.float64)

print(y)                # Output: [1., 2., 3.]
print(y.dtype)          # Output: float64
print(x.dtype)          # Output: int64 (Original x remains unchanged)
