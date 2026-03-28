from sklearn.linear_model import LinearRegression
import pandas as pd 

data_file_path = "/Users/sorenbasnet/Documents/Github/PYTHON/DATA_SAMPLE/mtcars.csv"
data = pd.read_csv(data_file_path)

file_path = "/Users/sorenbasnet/Documents/Github/PYTHON/FILE_COL_NAMES/dsc.txt"

# Read the dsc file 
def read_dsc(file_path:str, variable_type: str) -> str: 

    col_name_list = []
    response_name = []
    
    with open(file_path, "r") as dsc: 

        next(dsc)

        for line in dsc : 
            col, dtype = line.strip().split()

            if dtype == "d": 
                response_name.append(col)
            if dtype == "x": 
                pass 
            elif dtype != "d": 
                col_name_list.append(col)


        if variable_type == "dependent": 
            return col_name_list 
        
        else: 
            return response_name


def data_col(data_file_path, list:list): 

    data = pd.read_csv(data_file_path)
    data = data[list]

    return data


# X needs to take values from the dsc file 
X = data_col(data_file_path, read_dsc(file_path, "dependent"))

# y needs to take values from the dsc files
y = data_col(data_file_path, read_dsc(file_path, "response"))

print(X.head())

print(y.head())

m1 = LinearRegression().fit(X, y)
print(m1.score(X, y))