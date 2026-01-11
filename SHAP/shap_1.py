import shap 
import xgboost as xgb 
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# laod dataset 
data = load_wine() 
X, y = data.data, data.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


#1. Train the model 
model = xgb.XGBClassifier().fit(X_train, y_train)

#2. Explain the model's predictions 
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

#3.Visualize 
# This shows the distribution of impacts 
# for each feature 
shap.plots.beeswarm(shap_values[:,:,1])



"""
Master's Level Checklist for SHAP:
If you are writing a paper or a project, you must mention these axioms that SHAP satisfies:

Efficiency: The sum of all feature attributions equals the total prediction minus the average prediction.

Symmetry: If two features contribute the same to all possible coalitions, their SHAP values are identical.

Dummy: If a feature adds no value, its SHAP value is zero.

"""

# LIME is another interpretation method 
