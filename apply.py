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
