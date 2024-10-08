import pandas as pd
import os

def merge_files():
    # 4 个固定的文件名
    files = [
        "tool-price.xlsx",
        "processed_data.xlsx",
        "inventory_specifications_sales-b.xlsx",
        "stock.xlsx"
    ]

    # 创建一个空的 DataFrame，用来存放合并后的数据
    merged_df = pd.DataFrame()

    # 遍历文件，检查是否存在并合并内容
    for file_name in files:
        if os.path.exists(file_name):
            print(f"读取文件: {file_name}")
            df = pd.read_excel(file_name, engine='openpyxl')
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print(f"文件 {file_name} 不存在，跳过该文件。")

    # 保存合并后的结果到新的 Excel 文件
    output_file = "merged_output.xlsx"
    merged_df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"合并完成，结果已保存到 {output_file}")

if __name__ == "__main__":
    merge_files()