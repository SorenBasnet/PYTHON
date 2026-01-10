"""
Boosting is where things get intellectually exciting. If Bagging is a "committee of equals," Boosting is a "relay race of specialists."

While Bagging (Random Forest) trains trees in parallel, Boosting trains them sequentially. Each new tree is specifically designed to fix the mistakes made by the team of trees that came before it.
"""



"""
1. The Gradient Boosting IntuitionIn standard Gradient Boosting, we don't just "weight" the misclassified points (that's AdaBoost). Instead, we train each tree on the Residuals (the errors) of the previous step.Tree 1: Makes an initial prediction. It gets some things wrong.Calculate Residuals: $Error = Actual - Predicted$.Tree 2: Instead of trying to predict the Wine target, it tries to predict the Residuals from Tree 1.Update: New Prediction = Tree 1 + (Learning Rate $\times$ Tree 2).Repeat: Repeat this hundreds of times until the residuals are near zero.2. Why "XGBoost" is the "Extreme" VersionXGBoost (eXtreme Gradient Boosting) is essentially Gradient Boosting on steroids. It became "the hype" because it dominated Kaggle competitions for years. For a Master's student, you should know the three specific technical reasons why it's better:A. Second-Order Derivatives (Newton Boosting)Traditional boosting only uses the first derivative (gradient) of the loss function. XGBoost uses the second derivative (Hessian) via a Taylor Expansion. This allows the algorithm to understand the "curvature" of the loss surface, helping it converge to the optimal solution much faster and more accurately.B. Built-in Regularization ($L1$ and $L2$)XGBoost adds a penalty for complexity directly into its objective function.$$Obj = \sum L(y_i, \hat{y}_i) + \sum \Omega(f_k)$$The $\Omega$ term penalizes the number of leaves and the magnitude of leaf weights (similar to Lasso and Ridge regression). This is why XGBoost is much harder to overfit than standard Gradient Boosting.C. System OptimizationIt’s not just about the math; it’s about the engineering. XGBoost uses:Parallel Processing: It builds tree levels in parallel across CPU cores.Sparsity Awareness: It has a built-in way to handle missing values (it learns a "default direction" for them).Cache-aware access: It organizes data in memory to make the hardware run faster.
"""

import xgboost as xgb
from sklearn.metrics import classification_report
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Initialize the model 
# eta is the 'learning_rate' - the most important hyperparameter 
# gamma is the 'min_split_loss' = a regularization parameter 

model = xgb.XGBClassifier(
    n_estimators = 100, 
    learning_rate = 0.1, 
    max_depth = 4, 
    gamma = 0.1, 
    random_state = 42
)

# laod dataset 
data = load_wine() 
X, y = data.data, data.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))


"""
Parameter,Meaning,Master's Tip
learning_rate (eta),How much we trust each new tree.,"Lower is better, but requires more n_estimators."
gamma,Minimum loss reduction to split a node.,"Acts as a ""pruning"" tool during training."
subsample,% of data used to train each tree.,Helps prevent overfitting (usually 0.5 to 0.8).
colsample_bytree,% of features used for each tree.,Similar to Random Forest's feature sampling.
"""

