# Start of apply.py
import pandas as pd

# 读取合并后的 Excel 文件
merged_data = pd.read_excel

# 查找某个品名的详细信息
item_name = input("请输入品名: ")
item_details = merged_data[merged_data['品名'] == item_name]

# 输出该品名的详细信息
if not item_details.empty:
    print(item_details)
else:
    print(f"没有找到品名为 {item_name} 的数据。")
<<<<<<< HEAD
=======
import pandas as pd 

# 读取 CSV 和 Excel 文件
csv_file = pd.read_csv('order-process-management/product-item-details/your-csv-file.csv')
xlsx_file = pd.read_excel('order-process-management/product-item-details/your-xlsx-file.xlsx')

# 合并数据（假设两个文件有相同的列）
merged_file = pd.concat([csv_file, xlsx_file])

# 将合并后的数据保存为 Excel 文件
merged_file.to_excel('order-process-management/product-item-details/merged-product-details.xlsx', index=False)

print("文件已成功合并并保存为 merged-product-details.xlsx")
>>>>>>> master

# End of apply.py

# Start of compare_excel.py
<<<<<<< HEAD
import pandas as pd

# 确保文件路径正确
file1_path = "D:/github/order-process-management/processed_tool.xlsx"
file2_path = "D:/github/order-process-management/tool.xlsx"
output_path = "D:/github/order-process-management/比较结果.xlsx"

# 读取两个 Excel 文件
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
comparison.to_excel(output_path)
# 确保文件路径正确
file1_path = "D:/github/order-process-management/processed_tool.xlsx"
file2_path = "D:/github/order-process-management/tool.xlsx"
output_path = "D:/github/order-process-management/比较结果.xlsx"

# 读取两个 Excel 文件
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
comparison.to_excel(output_path)

# 确保文件路径正确
file1_path = "D:\\github\\order-process-management\\processed_tool.xlsx"
file2_path = "D:\\github\\order-process-management\\tool.xlsx"
output_path = "D:\\github\\order-process-management\\比较结果.xlsx"

# 读取两个 Excel 文件
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
=======
import pandas as pd

# 确保文件路径正确
file1_path = "D:/github/order-process-management/processed_tool.xlsx"
file2_path = "D:/github/order-process-management/tool.xlsx"
output_path = "D:/github/order-process-management/比较结果.xlsx"

# 读取两个 Excel 文件
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
comparison.to_excel(output_path)
# 确保文件路径正确
file1_path = "D:/github/order-process-management/processed_tool.xlsx"
file2_path = "D:/github/order-process-management/tool.xlsx"
output_path = "D:/github/order-process-management/比较结果.xlsx"

# 读取两个 Excel 文件
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
comparison.to_excel(output_path)

# 确保文件路径正确
file1_path = "D:\\github\\order-process-management\\processed_tool.xlsx"
file2_path = "D:\\github\\order-process-management\\tool.xlsx"
output_path = "D:\\github\\order-process-management\\比较结果.xlsx"

# 读取两个 Excel 文件
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
>>>>>>> 196f7c2d69f4ec745c838a0c7b00bff488059884
comparison.to_excel(output_path)
# End of compare_excel.py

# Start of dpt.py
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

# End of dpt.py

# Start of gs.py
import os

def git_status():
    os.system('git status')

def git_commit(message):
    os.system(f'git add .')  # 添加所有更改
    os.system(f'git commit -m "{message}"')

def git_push(branch='main'):
    os.system(f'git push origin {branch}')

if __name__ == "__main__":
    git_status()  # 查看当前状态
    commit_message = input("Enter your commit message: ")
    git_commit(commit_message)  # 提交更改
    git_push()  # 推送到远程仓库

# End of gs.py

# Start of merge.py
import pandas as pd 



# 读取 CSV 和 Excel 文件
csv_file = pd.read_csv('order-process-management/product-item-details/your-csv-file.csv')
xlsx_file = pd.read_excel('order-process-management/product-item-details/your-xlsx-file.xlsx')

# 合并数据（假设两个文件有相同的列）
merged_file = pd.concat([csv_file, xlsx_file])

# 将合并后的数据保存为 Excel 文件
merged_file.to_excel('order-process-management/product-item-details/merged-product-details.xlsx', index=False)

print("合并文件已保存为 merged-product-details.xlsx")

# End of merge.py

# Start of merge_files.py
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
# End of merge_files.py

# Start of query_item.py
import pandas as pd

# 读取 Excel 文件
file_path = 'order-process-management/product-item-details/厨房衛浴成本 (1).xlsx'
data = pd.read_excel(file_path)

# 查找某个品名的详细信息
item_name = input("请输入要查询的品名: ")
item_details = data[data['品名'] == item_name]

# 输出该品名的详细信息
if not item_details.empty:
    print(item_details)
else:
    print(f"没有找到品名为 {item_name} 的数据。")

# End of query_item.py

# Start of start_over.py
def new_begin():
    # 这里是您希望调用的内容
    instructions = """
    1. 使用 dpt.py 作为数据处理模板。
    2. 读取 Excel 文件并清洗数据。
    3. 合并多个文件，并保存处理后的数据。
    4. 使用 X X=(文件名, 扩展名, 存放位置)
    5. 使用 next 代表下一步任务。.
    """
    print(instructions)

# 调用函数
if __name__ == "__main__":
    new_begin()

# End of start_over.py

# Start of template.py
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

# End of template.py

# Start of wd.py
<<<<<<< HEAD
import pandas as pd

# 读取两个 Excel 文件
file1 = pd.read_excel("D:/github/order-process-management/processed_五金工具.xlsx")
file2 = pd.read_excel("D:/github/order-process-management/五金工具.xlsx")

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
comparison.to_excel("D:/github/order-process-management/比较结果.xlsx")
=======
import pandas as pd

# 读取两个 Excel 文件
file1 = pd.read_excel("D:/github/order-process-management/processed_五金工具.xlsx")
file2 = pd.read_excel("D:/github/order-process-management/五金工具.xlsx")

# 找出不同的地方
comparison = file1.compare(file2)

# 输出比较结果
print(comparison)

# 保存比较结果到新的 Excel 文件
comparison.to_excel("D:/github/order-process-management/比较结果.xlsx")
>>>>>>> 196f7c2d69f4ec745c838a0c7b00bff488059884

# End of wd.py

