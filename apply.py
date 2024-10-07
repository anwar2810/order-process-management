import pandas as pd

# 读取合并后的 Excel 文件
merged_data = pd.read_excel('order-process-management/product-item-details/merged-product-details.xlsx')

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
