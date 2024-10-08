import pandas as pd
import os

# 定义读取 Excel 文件的函数
def read_excel_file(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# 定义合并和清洗数据的函数
def process_data(dataframes):
    combined_data = pd.concat(dataframes, ignore_index=True)  # 合并所有 DataFrame
    cleaned_data = combined_data.dropna().drop_duplicates()  # 清洗数据：去除空值和重复行
    return cleaned_data

# 定义保存数据的函数
def save_data(data, output_path):
    try:
        data.to_excel(output_path, index=False)
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

# 主程序
if __name__ == "__main__":
    input_directory = 'D:/github/order-process-management/'  # 输入目录路径
    output_directory = 'D:/github/order-process-management/processed/'  # 输出目录路径

    # 确保输出目录存在
    os.makedirs(output_directory, exist_ok=True)

    # 存储所有 DataFrame 的列表
    dataframes = []

    # 遍历输入目录中的所有 Excel 文件
    for file_name in os.listdir(input_directory):
        if file_name.endswith('.xlsx') and '特定关键词' in file_name:  # 过滤文件名
            input_file = os.path.join(input_directory, file_name)
            data = read_excel_file(input_file)
            if data is not None:
                dataframes.append(data)  # 添加到列表中

    # 处理数据
    if dataframes:
        processed_data = process_data(dataframes)
        output_file = os.path.join(output_directory, 'combined_processed_data.xlsx')  # 合并后的文件名
        save_data(processed_data, output_file)
    else:
        print("No valid Excel files found.")
import pandas as pd
import os

# 定义读取 Excel 和 CSV 文件的函数
def read_file(file_path):
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        return None

# 定义读取文本文件的函数
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 定义合并和清洗数据的函数
def process_data(dataframes):
    combined_data = pd.concat(dataframes, ignore_index=True)  # 合并所有 DataFrame
    cleaned_data = combined_data.dropna().drop_duplicates()  # 清洗数据：去除空值和重复行
    return cleaned_data

# 主程序
if __name__ == "__main__":
    input_directory = 'D:/github/order-process-management/'  # 输入目录路径
    output_file = 'D:/github/order-process-management/processed/all_combined_data.xlsx'  # 输出文件路径

    # 存储所有 DataFrame 的列表
    dataframes = []
    text_contents = []  # 用于存储文本内容

    # 遍历输入目录中的所有文件
    for file_name in os.listdir(input_directory):
        input_file = os.path.join(input_directory, file_name)
        if file_name.endswith(('.xlsx', '.csv')):
            data = read_file(input_file)
            if data is not None:
                dataframes.append(data)  # 添加到列表中
        elif file_name.endswith('.md'):
            text_content = read_text_file(input_file)
            text_contents.append(text_content)  # 添加到文本内容列表中

    # 处理数据
    if dataframes:
        processed_data = process_data(dataframes)
        save_data(processed_data, output_file)
    
    # 将文本内容合并到一个文件
    if text_contents:
        with open('D:/github/order-process-management/processed/combined_text.md', 'w', encoding='utf-8') as f:
            for text in text_contents:
                f.write(text + "\n\n")  # 添加分隔
