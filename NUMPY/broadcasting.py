import numpy as np 

"""
Broadcasting = NumPy automatically stretches arrays so math works 
"""

X = np.array([
    [10,20,30],
    [40,50,60], 
    [70,80,90]
])

mean = X.mean(axis=0)
print(mean)


# Now subtract 
X_centered = X - mean 
print(X_centered)

