import numpy as np 

A = np.array([
    [2,0], 
    [0,1]
])

vals, vecs = np.linalg.eig(A)

print(vals)
print(vecs)



# Verify eigenvector property 

v = vecs[:, 0]
print(A @ v)
print(vals[0] * v)


"""
| Concept           | What it really is |
| ----------------- | ----------------- |
| Broadcasting      | Shape alignment   |
| Slicing           | Matrix geometry   |
| Linear regression | Solving equations |
| Eigenvectors      | Stable directions |

"""