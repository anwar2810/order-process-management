import pandas as pd
import os

def process_excel(file_path, sheet_name, output_file):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # 這裡可以添加你需要的任何處理函數
    df['Combined'] = df.apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    df.to_excel(output_file, index=False)
    print(f"處理後的文件已保存到 {output_file}")
def main():
    # 設置變數
    file_path = "D:/github/iss-a.xlsx"
    sheet_name = "Sheet1"
    output_file = "D:/github/processed_iss-a.xlsx"
    
    # 呼叫處理函數
    process_excel(file_path, sheet_name, output_file)

# 呼叫主函數
if __name__ == "__main__":
    main()

