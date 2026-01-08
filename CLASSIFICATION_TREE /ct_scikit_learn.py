""" 
A Classification Tree is a type of Decision Tree used when your target variable is categorical (e.g., "Spam" vs. "Not Spam", or "Red" vs. "Blue").

It works by repeatedly splitting the data into smaller groups based on feature values. The goal is to create "pure" leaf nodes where almost all the data points belong to a single category.

1. How it Makes Decisions

Instead of just splitting randomly, the tree uses a mathematical metric to find the "best" split. The most common metrics are:

Gini Impurity: Measures how often a randomly chosen element from the set would be incorrectly labeled. A Gini of 0 means the node is perfectly pure (all elements are the same class).

Entropy: Measures the "disorder" or uncertainty in the data.
"""


"""
As you mentioned, scikit-learn is the industry standard for this. It is highly optimized and easy to use.
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 

#1. load data 
iris = load_iris() 
X, y = iris.data, iris.target 

#2. Split into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= 42)

#3. create and train the model 
# max-depth  = 3 prevents the tree from becoming too complex ( over fitting )
clf = DecisionTreeClassifier(criterion='gini', max_depth=3) # when is it okay to choose between gini and another 
clf.fit(X_train, y_train)

#4. Predict and evaluate 
accuracy = clf.score(X_test, y_test) 
print(f"Model Accuracy : {accuracy *100:.2f}%")

# Visualize the tree 
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names = iris.target_names)
plt.show()


