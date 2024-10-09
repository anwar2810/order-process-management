import pandas as pd
import os

def process_two_excel_files(file_path1, sheet_name1, file_path2, sheet_name2, output_file):
    # 讀取第一個文件
    df1 = pd.read_excel(file_path1, sheet_name=sheet_name1)
    # 讀取第二個文件
    df2 = pd.read_excel(file_path2, sheet_name=sheet_name2)
    
    # 合併兩個DataFrame
    merged_df = pd.concat([df1, df2])
    
    # 創建輸出目錄（如果不存在）
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 將結果寫入新的Excel文件
    merged_df.to_excel(output_file, index=False)
    print(f"合併後的文件已保存到 {output_file}")

# 使用示例
file_path1 = "D:/github/iss-a.xlsx"
sheet_name1 = "Sheet1"
file_path2 = "D:/github/iss-b.xlsx"
sheet_name2 = "oct"
output_file = "D:/github/merged_iss.xlsx"

process_two_excel_files(file_path1, sheet_name1, file_path2, sheet_name2, output_file)
