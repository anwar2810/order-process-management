import os
import pandas as pd

file_path = 'd:/git/merged_output.xlsx'

if os.path.exists(file_path):
    df1 = pd.read_excel(file_path)
    print("File read successfully.")
else:
    print(f"File not found: {file_path}")