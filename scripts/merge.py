import pandas as pd 



# 读取 CSV 和 Excel 文件
csv_file = pd.read_csv('order-process-management/product-item-details/your-csv-file.csv')
xlsx_file = pd.read_excel('order-process-management/product-item-details/your-xlsx-file.xlsx')

# 合并数据（假设两个文件有相同的列）
merged_file = pd.concat([csv_file, xlsx_file])

# 将合并后的数据保存为 Excel 文件
merged_file.to_excel('order-process-management/product-item-details/merged-product-details.xlsx', index=False)

print("合并文件已保存为 merged-product-details.xlsx")
# 读取 CSV 和 Excel 文件
csv_file = pd.read_csv('order-process-management/product-item-details/your-csv-file.csv')
xlsx_file = pd.read_excel('order-process-management/product-item-details/your-xlsx-file.xlsx')

# 合并数据（假设两个文件有相同的列）
merged_file = pd.concat([csv_file, xlsx_file])

# 将合并后的数据保存为 Excel 文件
merged_file.to_excel('order-process-management/product-item-details/merged-product-details.xlsx', index=False)

print("文件已成功合并并保存为 merged-product-details.xlsx")