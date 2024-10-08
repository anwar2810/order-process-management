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
