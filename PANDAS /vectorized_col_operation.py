import pandas as pd 

df['score_z'] = (df['score'] - df['score'].mean()) / df['score'].std()
