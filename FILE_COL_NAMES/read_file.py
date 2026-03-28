import pandas as pd 

class Read_File:

    def __init__(self, data_file_path: str) -> None: 
        self.data_file_path = data_file_path 

    def read_file(self) -> None: 
        
        data = pd.read_csv(self.data_file_path)
        #print(data.dtypes)

        dsc_file = open("dsc.txt", "w")

        dsc_file.write(self.data_file_path + "\n")
        
        for col_name in data.columns: 
            print(type(data[col_name][0]))

            if pd.api.types.is_string_dtype(data[col_name]):
                dsc_file.write(col_name + " s\n")

            elif pd.api.types.is_numeric_dtype(data[col_name]):
                dsc_file.write(col_name + " n\n")

            else:
                dsc_file.write(col_name + " o\n")
            

        dsc_file.close()

            

"""
Running tests
"""

if __name__ == "__main__": 
    read_file = Read_File("/Users/sorenbasnet/Documents/Github/PYTHON/DATA_SAMPLE/mtcars.csv")
    read_file.read_file()