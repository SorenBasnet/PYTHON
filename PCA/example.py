import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#1. scale the data ( Mean = 0, Variance = 1)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(data=pca_data, columns=['PC1','PC2'])
