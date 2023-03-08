import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def import_data(file_path):
    df = pd.read_excel(file_path , sheet_name= "Final" , skiprows= 3 , usecols= 'B:K')
    df = df.set_index("Tổ")
    print(df)
    print(df.to_numpy())
    
file_path = "Congdoan.xlsx"
import_data(file_path)
