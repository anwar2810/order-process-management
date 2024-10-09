import pandas as pd
import os

file_path = 'd:/git/merged_output.xlsx'

if os.path.exists(file_path):
    df1 = pd.read_excel(file_path)
    print("File loaded successfully.")
else:
    print(f"File not found: {file_path}")