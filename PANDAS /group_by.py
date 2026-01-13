import pandas as pd 

df = pd.DataFrame({
    'dept': ['A', 'A', 'B', 'B'],
    'salary': [50, 60, 55, 65]
})

df.groupby('dept')['salary'].mean()



# Multiple aggregations ( Importatnt )
df.groupby('dept')['salary'].agg(['mean', 'std', 'count'])


# Transform vs agg  ( Important )
df['salary_centered'] = df.groupby('dept')['salary'].transform(lambda x: x - x.mean())
