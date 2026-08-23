import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score, r2_score
from sklearn.model_selection import LeaveOneOut, cross_val_score

# 1) single sample, clearly wrong prediction
print(explained_variance_score([1.0], [2.0]))  # 1.0, no warning
print(r2_score([1.0], [2.0]))                  # nan + UndefinedMetricWarning

# 2) the practical impact: LeaveOneOut on pure noise
#rng = np.random.RandomState(0)
#X, y = rng.normal(size=(12, 3)), rng.normal(size=12)

#ev = cross_val_score(LinearRegression(), X, y, cv=LeaveOneOut(),
#                     scoring="explained_variance")
#r2 = cross_val_score(LinearRegression(), X, y, cv=LeaveOneOut(), scoring="r2")
#print(ev.mean())  # 1.0   <- perfect score on noise, silently
#print(r2.mean())  # nan   <- correctly undefined
