"""
1. How the Algorithm "Thinks"The "$K$" stands for 
the number of groups you want. If you choose $K=3$, 
the algorithm follows these steps:Initialization: 
It picks 3 random spots in your data to be "Centroids" 
(the center points of clusters).Assignment: Every 
data point looks at the 3 centroids and joins the 
one it is closest to.Update: The centroids move to 
the actual center of their new group.Repeat: It 
keeps re-assigning points and moving centroids 
until nobody moves anymore.
"""


from sklearn.cluster import KMeans
import numpy as np 

#1. Create some random data point [x,y]
 
X = np.array([
    [1,2], [1,3], [1,4], [10,0], [10,2], [1,0]
])

#2. We want to find 2 clusters (K=2)
kmeans = KMeans(n_clusters=2, random_state=0)

#3. Fit the model 
kmeans.fit(X)

#4. See where the "centers" ended up 
print("Centroids : ", kmeans.cluster_centers_)

#5. See which group each point belongs to 
print("Labels : ", kmeans.labels_)



