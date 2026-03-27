import pandas as pd 

class Read_File:

    def __init__(self, data_file_path: str) -> None: 
        self.data_file_path = data_file_path 

    def read_file(self) -> None: 
        
        data = pd.read_csv(self.data_file_path)

        dsc_file = open("dsc.txt", "w")

        dsc_file.write(self.data_file_path + "\n")
        
        for col_name in data.columns: 
            if isinstance(type(col_name), int): 
                dsc_file.write(col_name +" n" + "\n")

        dsc_file.close()

            






"""
Running tests
"""

if __name__ == "__main__": 
    read_file = Read_File("/Users/sorenbasnet/Documents/Github/PYTHON/DATA_SAMPLE/mtcars.csv")
    read_file.read_file()