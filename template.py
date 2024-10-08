import pandas as pd

# 定义读取 Excel 文件的函数
def read_excel_file(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# 定义处理数据的函数
def process_data(data):
    # 在这里添加处理逻辑，例如数据清洗、合并等
    processed_data = data  # 这里是占位符，实际处理逻辑请自行添加
    return processed_data

# 定义保存数据的函数
def save_data(data, output_path):
    try:
        data.to_excel(output_path, index=False)
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

# 主程序
if __name__ == "__main__":
    input_file = 'D:/github/order-process-management/五金工具.xlsx'  # 输入文件路径
    output_file = 'D:/github/order-process-management/processed_data.xlsx'  # 输出文件路径

    data = read_excel_file(input_file)
    if data is not None:
        processed_data = process_data(data)
        save_data(processed_data, output_file)
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

# 定义处理数据的函数
def process_data(data):
    # 在这里添加处理逻辑，例如数据清洗、合并等
    processed_data = data  # 这里是占位符，实际处理逻辑请自行添加
    return processed_data

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

    # 遍历输入目录中的所有 Excel 文件
    for file_name in os.listdir(input_directory):
        if file_name.endswith('.xlsx'):  # 只处理 .xlsx 文件
            input_file = os.path.join(input_directory, file_name)
            data = read_excel_file(input_file)
            if data is not None:
                processed_data = process_data(data)
                output_file = os.path.join(output_directory, f'processed_{file_name}')  # 添加前缀
                save_data(processed_data, output_file)
