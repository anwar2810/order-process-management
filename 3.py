import pandas as pd

# 固定的 Excel 处理脚本
def process_excel(file_path, sheet_name, process_func):
    # 读取 Excel 文件的指定工作表
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # 打印读取的数据
    print(f"Data from {sheet_name} in {file_path}:")
    print(df)
    
    # 使用传入的处理函数进行自定义操作
    result_df = process_func(df)
    
    # 保存处理后的结果为新的 Excel 文件
    output_file = file_path.replace('.xlsx', '_processed_output.xlsx')
    result_df.to_excel(output_file, index=False)
    
    print(f"Processed output saved to: {output_file}")

# 合并所有列的处理函数
def combine_columns(df):
    # 将所有列的内容转换为字符串后合并为一列
    df['Combined'] = df.apply(lambda row: ' '.join(row.astype(str)), axis=1)
    return df

# 主程序入口
if __name__ == "__main__":
    # 固定的文件路径和工作表名称
    file_path = 'd:/github/order-process-management/motput1.xlsx'
    sheet_name = 'out'
    
    # 使用合并列的函数
    process_excel(file_path, sheet_name, combine_columns)
