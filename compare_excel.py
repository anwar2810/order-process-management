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
comparison.to_excel(output_path)