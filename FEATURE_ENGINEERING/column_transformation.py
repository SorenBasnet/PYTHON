"""
You might have numerical columns (like Alcohol) that need scaling, and categorical columns (like Region) that need encoding.

If you try to use a standard Pipeline, it applies the same operation to everything, which would break your code. ColumnTransformer is the "traffic cop" that sends different columns to different processing paths.
"""

"""
1. The Logic of ColumnTransformer
Think of it as a parallel processor. It splits the data, applies specific transformations to specific groups of columns, and then glues (concatenates) them back together into a single matrix for the machine learning model.
"""

"""
Imagine our Wine dataset has an extra column 
called "Region" (categorical) and "Premium" 
(Boolean). Here is how you handle them 
differently in one shot.
"""

import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from sklearn.ensemble import RandomForestClassifier


#1. Create a dummy dataset with mixed types 
data = {
    'alcohol': [14.23, 13.20, 13.16, 14.37],
    'color_intensity': [5.64, 4.38, 5.68, 7.80],
    'region': ['Italy', 'France', 'Italy', 'Germany'], # Categorical
    'target': [0, 1, 0, 1]
}
df = pd.DataFrame(data)

#2. Define which columns get which treatment 
numeric_features = ['alcohol', 'color_intensity']
categorical_features = ['region']

# 3. Create the ColumnTransformer 
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features), 
        ('cat', OneHotEncoder(), categorical_features)

    ]
)

#4. put it all into a Final Pipeline 
clf = Pipeline(steps = [
    ('preprocessor', preprocessor), 
    ('classifier', RandomForestClassifier())
])

# Now you can fit the whole thing!
X = df.drop('target', axis=1)
y = df['target']
clf.fit(X, y)

print("Columns processed and model trained successfully!")




