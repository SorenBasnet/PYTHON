import pandas as pd 

"""
1. df.loc[0, 'age'] (Label-Based)
The loc method uses the labels (the names) of the rows and columns.

0: This refers to the Index Label. In most DataFrames, the rows are named 0, 1, 2, etc., but they could also be names like "Employee_A".

'age': This is the specific Column Name.

Plain English: "Go to the row labeled '0' and the column named 'age', and give me that value."

2. df.iloc[0, 0] (Position-Based)
The iloc method (the "i" stands for integer) cares only about the physical position (the coordinates), starting from 0. It completely ignores the names.

0: The first row (top row).

0: The first column (left-most column).

Plain English: "Go to the very first row and the very first column, regardless of what they are named."
"""

"""
     ,name (Col 0),age (Col 1),city (Col 2)
Row 0,Alice,25,New York
Row 1,Bob,30,Chicago
"""

"""
df.loc[0, 'age'] would give you 25.

df.iloc[0, 1] would also give you 25 (because 'age' is the column at position 1).
"""

