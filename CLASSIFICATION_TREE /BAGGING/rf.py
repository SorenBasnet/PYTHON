"""
1. The Core Logic: "The Wisdom of the Crowd"
The biggest weakness of a Decision Tree is High Variance. This means that if you change the training data just a little bit, the tree structure can change completely. Bagging fixes this using two main steps:

A. Bootstrapping (The "B" in Bagging)
Instead of giving every tree the exact same data, we create multiple "sub-datasets" by sampling the original data with replacement.

If your dataset has 100 rows, a "bootstrap sample" might take 100 rows but include some rows twice and miss others entirely.

This ensures each tree in the ensemble sees a slightly different version of reality.

B. Aggregating (The "Agg" in Bagging)
Once you have trained, say, 100 different trees on these different bootstrap samples:

For Classification: You take a Majority Vote. If 70 trees say "Red Wine" and 30 say "White Wine," the model predicts Red.

For Regression: You take the Average of all the trees' predictions.

2. Why does this work?
In a Master's program, you’ll often hear the term Bias-Variance Tradeoff.

Individual trees are High Variance but Low Bias (they are very complex and capture every detail).

By averaging them, the "errors" or "noise" of individual trees cancel each other out.

The result is a model that maintains the low bias of a tree but significantly reduces the variance.

3. The King of Bagging: Random Forest
The most famous application of Bagging is the Random Forest. However, Random Forest adds one extra layer of "randomness" to make the trees even more diverse:

Row Sampling: Each tree gets a bootstrap sample of the rows (Standard Bagging).

Feature Sampling: At every split in the tree, the algorithm only looks at a random subset of features (e.g., only 3 out of 10 columns).

Why feature sampling? If one feature in the Wine dataset (like "Alcohol content") is extremely dominant, every single bagged tree will split on it first. This makes the trees too similar (correlated). By forcing some trees to ignore "Alcohol content," they are forced to find patterns in other features (like "Color intensity" or "Magnesium").
"""


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Initialize the Forest 
# n_estimators = number of trees in the committee 
# max_features = 'sqrt' is the standard for feature sampling 

rf = RandomForestClassifier(n_estimators=100, 
                            max_features='sqrt', 
                            random_state=42)

# load dataset 
data = load_wine() 
print(type(data))
X, y = data.data, data.target
print(type(X))
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    random_state=42)

rf.fit(X_train, y_train)
print(f"Random Forest Accuracy : {rf.score(X_test, y_test):.4f}")



