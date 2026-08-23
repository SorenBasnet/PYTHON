import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


# Reproducibility
np.random.seed(42)

# Generate fake customer data
n = 1000

age = np.random.randint(18, 70, n)
monthly_spend = np.random.uniform(20, 150, n)
number_of_logins = np.random.randint(1, 30, n)
days_since_last_login = np.random.randint(0, 30, n)

X = np.column_stack([
    age,
    monthly_spend,
    number_of_logins,
    days_since_last_login
])

# Create a synthetic churn rule
probability = (
    0.02 * days_since_last_login
    - 0.04 * number_of_logins
    + 0.005 * monthly_spend
)

churn_probability = 1 / (1 + np.exp(-probability))

y = np.random.binomial(1, churn_probability)


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = LogisticRegression()

model.fit(X_train, y_train)


# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.3f}")


# Save model
joblib.dump(model, "model.pkl")

print("Model saved to model.pkl")
