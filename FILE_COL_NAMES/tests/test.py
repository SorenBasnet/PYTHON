from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from execute_dsc import generate_df

X, y = generate_df("/Users/sorenbasnet/Documents/Github/PYTHON/FILE_COL_NAMES/dsc.txt")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

    # Evaluation metrics
mse = mean_squared_error(y_test, y_pred)

print(mse)

