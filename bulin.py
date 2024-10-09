import pandas as pd

# 1. 讀取 d:/git/merged_output.xlsx 並生成布林值的 DataFrame
df1 = pd.read_excel('d:/git/merged_output.xlsx')

# 生成一個布林值的 DataFrame，表示是否所有列的內容相同
comparison_df = df1.eq(df1.iloc[:, 0], axis=0)  # 與第一列進行比較

# 將比較結果寫入新的 Excel 文件
comparison_df.to_excel('d:/git/comparison_output.xlsx', index=False)

# 2. 讀取 d:/github/order-process-management/merged_output1.xlsx 並合併所有列的內容
df2 = pd.read_excel('d:/github/order-process-management/merged_output1.xlsx')

# 將所有列的內容合併為一個新的列
df2['Combined'] = df2.apply(lambda row: ' '.join(row.astype(str)), axis=1)

# 將結果寫入新的 Excel 文件
df2.to_excel('d:/github/order-process-management/combined_output.xlsx', index=False)

print("生成完成！")