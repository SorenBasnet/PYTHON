import pandas as pd
import os
import sys
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def read_file(data_file_path, dependent_variable) -> None:

     """
     Function      : Opens a dsc.txt file and documents column names along with
                     a letter signifying the type of variable in column data
     Parameters    : self
     Returns       : None but makes a dsc.txt file
     """

     dependent_variable_found = False
     data = pd.read_csv(data_file_path)

     dsc_file = open("dsc.txt", "w")

     dsc_file.write(data_file_path + "\n")

     for col_name in data.columns:
         print(type(data[col_name][0]))

         if data[col_name] == dependent_variable:
             dependent_variable_found = True
             dsc_file.write(col_name + " s\n")

         elif pd.api.types.is_string_dtype(data[col_name]):
             dsc_file.write(col_name + " s\n")

         elif pd.api.types.is_numeric_dtype(data[col_name]):
             dsc_file.write(col_name + " n\n")

         elif pd.api.types.is_float_dtype(data[col_name]):
             dsc_file.write(col_name + " n\n")

         elif pd.api.types.is_int64_dtype(data[col_name]):
             dsc_file.write(col_name + " n\n")
         else:
             dsc_file.write(col_name + " o\n")

     if dependent_variable_found == False:
         sys.exit(f"ERROR : Dependent variable {dependent_variable} not found.")

     dsc_file.close()

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

        print(return_list)

        return return_list


def generate_df(dsc_file_path:str, dependent_variable:str):

    read_file(dsc_file_path, dependent_variable)


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

    generate_df("/Users/sorenbasnet/Documents/Github/PYTHON/FILE_COL_NAMES/src/dsc2/dsc.txt", "mpg")


