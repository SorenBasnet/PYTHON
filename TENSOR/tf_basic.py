"""
Big picture first (before code)

You are teaching the computer one simple rule:

“When x goes up by 1, y goes up by about 2.”

The model does NOT know this rule at the start.
It learns it by guessing, being wrong, and correcting itself.
"""

import tensorflow as tf
import numpy as np

# Training data
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([0, 2, 4, 6, 8], dtype=float)

# Define a simple model
"""
What does Sequential mean?

Data flows left → right

No branches, no loops
"""
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(
    optimizer='sgd', #stochastic gradient descent
    loss='mean_squared_error'
)

# Train the model
model.fit(x, y, epochs=500, verbose=0)

# Make a prediction
print(model.predict(np.array([10.0])))

