import pandas as pd 

def read_dsc(file_path:str, variable_type:str) -> str: 

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