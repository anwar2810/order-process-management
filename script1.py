import pandas as pd
import os
import itertools

def compare_all_columns(file_path, sheet_name, output_file):
    # 读取Excel文件
    df_a = pd.read_excel(file_path, sheet_name=sheet_name)
    # 获取所有列名
    columns = df_a.columns.tolist()
    
    # 创建一个新的DataFrame来存储比较结果
    result_df = pd.DataFrame()
    
    # 比较所有列的组合
    for col1, col2 in itertools.combinations(columns, 2):
        comparison = df_a[col1] == df_a[col2]
        result_df[f'{col1} vs {col2}'] = comparison
    
    # 创建输出目录（如果不存在）
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 将原始数据和比较结果合并
    final_df = pd.concat([df_a, result_df], axis=1)
    
    # 将结果写入新的Excel文件
    final_df.to_excel(output_file, index=False)
    print(f"比较结果已保存到 {output_file}")

# 使用示例
file_path = "D:/github/order-process-management/motput1.xlsx"
sheet_name = "out"
output_file = "D:/github/order-process-management/all_columns_comparison_result.xlsx"

compare_all_columns(file_path, sheet_name, output_file)