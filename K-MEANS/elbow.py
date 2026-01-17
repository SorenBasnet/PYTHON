"""
The biggest question in K-Means is:
 "How do I know what $K$ should be?" 
 If you pick a $K$ that is too small, 
 your groups are too broad. If it’s too big, 
 every point becomes its own group.We use the 
 Elbow Method. We plot a graph of the "Inertia"
 (how far points are from their centers) for 
 different values of $K$.As $K$ increases, 
 Inertia drops.You look for the "elbow" of 
 the arm—the point where the drop slows down 
 significantly. That’s your ideal $K$.
"""


import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


# 1. Create dummy data (3distinct groups)
X, _ = make_blobs(n_samples=500, 
                  centers = 3, 
                  cluster_std=1.0, 
                  random_state=42)

#2. Loop through different K values 
inertia_values = []
k_range = range(1, 11)

for k in k_range: 
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    # .inertia_ is the sum of squared distances to the closest centroid
    inertia_values.append(kmeans.inertia_)


# 3. Plot the results
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia_values, marker='o', linestyle='--')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (WCSS)')
plt.xticks(k_range)
plt.grid(True)
plt.show()