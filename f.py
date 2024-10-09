import pandas as pd

# 1. 讀取 d:/git/merged_output.xlsx
df1 = pd.read_excel('d:/git/merged_output.xlsx')

# 生成一個布林值的 DataFrame，表示是否所有列的內容相同
comparison_df = df1.eq(df1.iloc[:, 0], axis=0)  # 與第一列進行比較

# 2. 讀取 d:/github/order-process-management/merged_output1.xlsx
df2 = pd.read_excel('d:/github/order-process-management/merged_output1.xlsx')

# 將所有列的內容合併為一個新的列
df2['Combined'] = df2.apply(lambda row: ' '.join(row.astype(str)), axis=1)

# 3. 合併結果到一個新的 DataFrame
merged_result = pd.concat([comparison_df, df2[['Combined']]], axis=1)

# 將合併的結果寫入新的 Excel 文件
merged_result.to_excel('d:/git/merged_final_output.xlsx', index=False)
import pandas as pd
df1 = pd.read_excel('d:\\git\\merged_output.xlsx')
print(df1)

print("生成完成！")