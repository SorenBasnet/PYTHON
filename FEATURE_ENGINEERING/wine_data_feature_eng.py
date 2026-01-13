import pandas as pd 
import numpy as np 
from sklearn.datasets import load_wine 
from sklearn.preprocessing import StandardScaler

#1. Load into Pandas 
wine = load_wine() 
df = pd.DataFrame(wine.data, columns=wine.feature_names)

# 2. Feature Construction ( the "Domain Knowledge" step)
# lets create an "Intensity_Index" by combining color and alcohol

df['intensity_index'] = df['color_intensity'] * df['alcohol']


# handling outliers ( the numpy setup)
# Is a values is 3 standarf deviations away, we "cap" it 

upper_limit = df ['color_intensity'].mean() + 3*df['color_intensity'].std()
df['color_intensity'] = np.where(df['color_intensity'] > upper_limit, upper_limit, df['color_intensity'])


#4. SCALING( the "rigor" step)
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)


print("Original Alcohol Range:", df['alcohol'].min(), "-", df['alcohol'].max())
print("Scaled Alcohol Range:", df_scaled['alcohol'].min(), "-", df_scaled['alcohol'].max())
