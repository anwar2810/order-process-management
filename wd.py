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
