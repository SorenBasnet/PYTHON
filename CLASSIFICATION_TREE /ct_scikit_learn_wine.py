"""
we will use the Wine Dataset (which has 13 features) and explore how different settings change the tree's behavior. We will also look at Feature Importance, which tells us which data points actually matter most to the model.
"""

import matplotlib.pyplot as plt 
from sklearn.datasets import load_wine 
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns # For a prettier heatmap 

#1. Load data
data = load_wine()
X, y = data.data, data.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Configure the tree with hyperparameters 
# min_samples_leaf :requires at least 5 samples to create a leaf  
# ccp_alpha : used for 'cost complexity pruning' to prevent overfitting 
clf = DecisionTreeClassifier(
    criterion = 'entropy', #Uses information gain instead of Gini
    max_depth = 4, #limits how deep the tree goes 
    min_samples_split=10, #A node must have 10 samples to split 
    random_state=42
)

"""
Questions, 
chosing optimal max_depth, 
optimal min_samples_splot, 
criterion 
"""

clf.fit(X_train, y_train)

#3. Detailed Evaluation 
y_pred = clf.predict(X_test)

print(" --- Detailed Classification Report --- ")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 4. Feature Importance 
# This shows which features ( e.g. alcohol content, color intensity)
# the tree relied on mose to make its decision 

print(" \n --- Feature Importance --- ")

for name, importance in zip(data.feature_names, clf.feature_importances_): 
    if importance > 0: 
        print(f"{name}: {importance: .4f}")

# 5. Visualizing a complex tree
plt.figure(figsize=(20,10))
plot_tree(clf, 
          filled=True, 
          feature_names=data.feature_names, 
          class_names=data.target_names,
          rounded=True,
          fontsize=10)
plt.title("Pruned Decision Tree for Wine Classification")
plt.show()


# ------------- Confusion matrix ____________ 

#1. Generate the matrix 
cm = confusion_matrix(y_test, y_pred)

# 2. print the raw matrix 
print(" \n --- Raw Confusion Matrix --- ")
print(cm)

print()

#3. Visualize it with a heat map 
plt.figure(figsize=(8,6)) 
sns.heatmap(cm, annot=True, 
            fmt='d', cmap='Blues', 
            xticklabels=data.target_names, 
            yticklabels=data.target_names)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix Heatmap')
plt.show()


"""
Comments : 

Entropy vs. Gini

1. Pruning and Constraints

Notice min_samples_split and max_depth. Without these, the tree would continue splitting until every single training example was perfectly classified. This usually leads to Overfitting, where the tree learns the "noise" in the data rather than the actual pattern.


3. Feature Importance

You'll notice that many features have an importance of 0.0. This is one of the coolest parts of Decision Trees—they perform automatic "Feature Selection." They ignore columns that don't help in separating the classes.

4. The Confusion Matrix

In the code output, look for the Confusion Matrix. It tells you exactly which classes are being confused. For example, is the model consistently mistaking "Class 1" wine for "Class 2"?
"""


"""
How to Read the Results

The Confusion Matrix is a grid that compares the Actual values (rows) vs. the Predicted values (columns):

The Diagonal (Top-Left to Bottom-Right): These are your "True Positives." You want the highest numbers to be here. This means the model predicted "Class A" and it actually was "Class A."

Off-Diagonal Cells: These are your errors.

If you see a 3 in the row for "Class 1" and the column for "Class 2," it means the model accidentally labeled 3 samples of Class 1 as Class 2.

Why this is "Advanced"

In the real world, accuracy isn't everything. For example:

In Cancer Diagnosis, a "False Negative" (saying someone is healthy when they are sick) is much worse than a "False Positive."

The Confusion Matrix allows you to see if your tree is biased toward one specific class, which often happens if your dataset is imbalanced (e.g., 90% of samples are Class A and only 10% are Class B).
"""