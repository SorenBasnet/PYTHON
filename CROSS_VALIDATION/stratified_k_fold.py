from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine

# 1. Load data
data = load_wine()
X, y = data.data, data.target

# 2. Define the strategy
# shuffle=True is important to mix the data before splitting
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 3. Initialize model
model = RandomForestClassifier(n_estimators=100)

# 4. Run Cross-Validation
# This returns an array of 5 scores
scores = cross_val_score(model, X, y, cv=skf)

print(f"Scores for each fold: {scores}")
print(f"Mean Accuracy: {scores.mean():.4f}")
print(f"Standard Deviation (Variance): {scores.std():.4f}")