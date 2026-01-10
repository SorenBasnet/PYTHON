"""
Something about cross validation that i need to know
"""

from sklearn.model_selection import GridSearchCV
import xgboost as xgb
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

data = load_wine() 
X, y = data.data, data.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#1. Define the model 
xgb_model = xgb.XGBClassifier(random_state=42)

#2. Define the "Grid" of parameters to explore 
param_grid = {
    'n_estimators': [50, 100], 
    'max_depth': [3, 4, 5], 
    'learning_rate': [0.01, 0.1, 0.2], 
    'subsample': [0.8, 1.0]
}

# 3. setup the grid search 
# cv=5 means 5 fold cross validation 
# scoring='accuracy' tells it what to optimize for 
grid_search = GridSearchCV(estimator=xgb_model, 
                           param_grid=param_grid, 
                           cv=5, 
                           scoring='accuracy', 
                           n_jobs = -1 ) # uses all cpu cores 

# 4. Run the search
grid_search.fit(X_train, y_train)

# 5. Extract results
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross-Val Score: {grid_search.best_score_:.4f}")
