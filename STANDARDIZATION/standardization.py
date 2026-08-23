import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Generate random skewed data (Exponential distribution)
np.random.seed(42)
raw_data = np.random.exponential(scale=2.0, size=1000)

# 2. Standardize the data
# (x - mean) / std
standardized_data = (raw_data - np.mean(raw_data)) / np.std(raw_data)

# 3. Visualize
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(raw_data, kde=True, ax=ax[0], color='blue')
ax[0].set_title(f"Original\nMean: {np.mean(raw_data):.2f} | SD: {np.std(raw_data):.2f}")

sns.histplot(standardized_data, kde=True, ax=ax[1], color='red')
ax[1].set_title(f"Standardized\nMean: {np.mean(standardized_data):.2f} | SD: {np.std(standardized_data):.2f}")

plt.show()
