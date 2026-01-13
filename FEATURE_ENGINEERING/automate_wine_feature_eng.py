import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.datasets import load_wine 

"""
Step 1: Analyze with a Correlation Heatmap
A correlation heatmap helps you spot Multicollinearity. If two features have a correlation of 0.95, they are essentially telling the model the same thing. Keeping both adds noise and makes the model harder to interpret.
"""

#1. Load dataset 
data = load_wine() 
df = pd.DataFrame(data.data, columns=data.feature_names)

#2. Create Correlation Matrix 
corr_matrix = df.corr() 

#3. Plot Heatmap 
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Wine Feature Correlation Matrix")
plt.show()


"""
Step 2: Automate with Scikit-Learn Pipelines
Now that you know which features to scale or transform, you don't want to apply those steps manually every time you get new data. A Pipeline bundles your preprocessing and your model into a single object.

This prevents Data Leakage because the pipeline ensures that the scaling parameters (like the mean) are only calculated on the training data, never the test data.
"""

from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#1. Spllit Data 
X_train, X_test, y_train, y_test = train_test_split(df, data.target, test_size=0.2, random_state=42)

#2. Define the Pipeline 
# Step 1 : scale the date 
# Step 2 : Reduce dimensionality (Optional, using PCA)
# Step 3 : The classifier 
pipe = Pipeline([
    ('scaler', StandardScaler()), 
    ('pca', PCA(n_components=5)), 
    ('classifier', RandomForestClassifier(n_estimators=100)) # n_estimators=100 → 100 decision trees
])

# 3. Fit the entire pipeline 
pipe.fit(X_train, y_train) # Trains on scaled data

# 4. Predict(the pipeline automatically handles scaling the test data!)
score = pipe.score(X_test, y_test) # .score() (Predicts and compares to $y$)
print(f"Pipeline Accuracy: {score:.4f}")












