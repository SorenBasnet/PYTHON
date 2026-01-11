import numpy as np 

names = np.array(["Alice", "Bob", "Charlie"])
scores = np.array([88,95,70])

np.sort(scores) # You lose track of who got which score.



# ---------------------
# ---------------------

names = np.array(["Alice", "Bob", "Charlie"])
scores = np.array([88,95,70])

# Get indices that would sort scores 
order = np.argsort(scores)

# Apply the same order to both arrays 
sorted_scores = scores[order]
sorted_names = names[order]

print(sorted_names)
print(sorted_scores)


# Descending order 
order = np.argsort(scores)[::-1]

"""
# | Operation       | Meaning          |
| --------------- | ---------------- |
| `np.sort(x)`    | Sort values      |
| `np.argsort(x)` | Sort **indices** |
| `x[argsort(x)]` | Sorted x         |
| `y[argsort(x)]` | y sorted by x    |

"""
