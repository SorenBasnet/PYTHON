"""
In Machine Learning, we call this the Bias-Variance Tradeoff.

If max_depth is too low, the model is too simple and misses patterns (Underfitting).

If max_depth is too high, the model memorizes the training data noise and fails on new data (Overfitting).

The Validation Curve Code

This script will run the Decision Tree multiple times with different depths and plot the results so you can see exactly where the model starts to "fail."
"""

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


#1. Setup Data 
data = load_wine()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#2. Test depths from 1 to 10 
depths = range(1, 11)
train_scores = []
test_scores = []

for d in depths: 
    clf = DecisionTreeClassifier(max_depth=d, random_state = 42)
    clf.fit(X_train, y_train)

    # Record accuracy for both training and testing sets 
    train_scores.append(clf.score(X_train, y_train))
    test_scores.append(clf.score(X_test, y_test))


# 3. Plot Visualization curve 
plt.figure(figsize=(10,6))
plt.plot(depths, train_scores, '-o', label='Training Accuracy', color='blue')
plt.plot(depths, test_scores, '-o', label='Testing Accuracy', color='red')

plt.xlabel('Tree Depth (max depth)')
plt.ylabel('Accuracy')
plt.title('Finding the Sweet spot : Training vs Testing Accuracy')
plt.legend()
plt.grid(True)
plt.xticks(depths)
plt.show()
