import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def read_file(data_file_path) -> None:

     """
     Function      : Opens a dsc.txt file and documents column names along with
                     a letter signifying the type of variable in column data
     Parameters    : self
     Returns       : None but makes a dsc.txt file
     """

     data = pd.read_csv(data_file_path)

     dsc_file = open("dsc.txt", "w")

     dsc_file.write(data_file_path + "\n")

     for col_name in data.columns:
         print(type(data[col_name][0]))

         if pd.api.types.is_string_dtype(data[col_name]):
             dsc_file.write(col_name + " s\n")

         elif pd.api.types.is_numeric_dtype(data[col_name]):
             dsc_file.write(col_name + " n\n")

         elif pd.api.types.is_float_dtype(data[col_name]):
             dsc_file.write(col_name + " n\n")

         elif pd.api.types.is_int64_dtype(data[col_name]):
             dsc_file.write(col_name + " n\n")

         else:
             dsc_file.write(col_name + " o\n")

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

        return return_list


def generate_df(dsc_file_path:str):

    read_file(dsc_file_path)

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


