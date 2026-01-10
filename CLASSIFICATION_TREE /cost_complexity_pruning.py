"""
Excellent choice. Cost-Complexity Pruning (CCP) is a more 
sophisticated way to handle overfitting than just setting an 
arbitrary max_depth.Essentially, we want to minimize the 
Cost-Complexity 
measure:$$R_\alpha(T) = R(T) + \alpha|T|$$Where $R(T)$ is the 
misclassification rate, $|T|$ is the number of terminal nodes, 
and $\alpha$ is the penalty for complexity.Here is the workflow 
using the Wine dataset. This script extracts the possible values 
for $\alpha$, trains a series of trees, and helps you find the 
"sweet spot."

"""

# Python Implementation: Finding the Optimal Alpha

import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier

# load dataset 
data = load_wine() 
X, y = data.data, data.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#2. Compute the pruning path 
clf = DecisionTreeClassifier(random_state=42)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

#3. Train a tree for each alpha 
clfs = []
for ccp_alpha in ccp_alphas: 
    clf = DecisionTreeClassifier(random_state=42, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)


# 4. Remove the last element ( its a trivial tree with only one node)
clfs = clfs[:-1]
ccp_alphas = ccp_alphas[:-1]

#5. Plot Accuracy vs Alpha 
train_scores = [clf.score(X_train, y_train) for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots()
ax.set_xlabel("alpha")
ax.set_ylabel("accuracy")
ax.set_title("Accuracy vs alpha for training and testing sets")
ax.plot(ccp_alphas, train_scores, marker='o', label="train", drawstyle="steps-post")
ax.plot(ccp_alphas, test_scores, marker='o', label="test", drawstyle="steps-post")
ax.legend()
plt.show()


