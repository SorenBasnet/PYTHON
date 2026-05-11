import pandas as pd 
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#
# read_dsc : Read the file 
#
def read_dsc(file_path:str) -> list: 

    col_name_list = []
    response_name = [] 
    return_list = []

    with open(file_path, "r") as dsc: 
        data_file_path = next(dsc).strip()

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

        # Conditional statement to check if the list 
        # contains dependent variable
        if not response_name: 
            print (f"Error in the DSC file. There needs to be a dependent variable declared.")
            return
        return_list.append([data_file_path])
        return_list.append(response_name)
        return_list.append(col_name_list)
        
        return return_list


def generate_df(dsc_file_path:str): 
    dsc = read_dsc(dsc_file_path)

    data_file_path  = dsc[0][0]
    dsc_dependent = dsc[1]
    dsc_response_name = dsc[2]
    y = pd.read_csv(data_file_path, usecols=dsc_dependent)
    X = pd.read_csv(data_file_path, usecols=dsc_response_name)

    return X, y

"""
def execute_LR(dsc_file_path:str): 

    X, y = generate_df(dsc_file_path)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    reg = linear_model.LinearRegression()
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test) 

    # Evaluation metrics 
    mse = mean_squared_error(y_test, y_pred)
    
    print(mse)
"""

if __name__=='__main__': 
    generate_df(dsc_file_path)


