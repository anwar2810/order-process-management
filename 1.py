import pandas as pd

# 固定脚本逻辑，用于处理 Excel 文件
def process_excel(file_path, sheet_name, comparison_func):
    # 读取 Excel 文件的指定工作表
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # 打印读取的数据
    print(f"Data from {sheet_name} in {file_path}:")
    print(df)
    
    # 使用传入的函数进行自定义处理
    comparison_df = comparison_func(df)
    
    # 保存比较结果到新文件
    output_file = file_path.replace('.xlsx', '_comparison_output.xlsx')
    comparison_df.to_excel(output_file, index=False)
    
    print(f"Comparison output saved to: {output_file}")

# 默认比较函数（作为示例）
def default_comparison(df):
    # 比较每一列与第一列的数据
    return df.eq(df.iloc[:, 0], axis=0)

# 主程序入口
if __name__ == "__main__":
    # 固定的文件路径和工作表名称
    file_path = 'd:/github/order-process-management/motput1.xlsx'
    sheet_name = 'out'
    
    # 传入变动的函数，默认使用 `default_comparison`
    process_excel(file_path, sheet_name, default_comparison)
