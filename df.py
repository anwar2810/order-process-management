import pandas as pd

# 讀取 Excel 文件
df = pd.read_excel('your_file.xlsx', sheet_name='Sheet1')

# 生成一個布林值的 DataFrame，表示是否所有列的內容相同
comparison_df = df.eq(df.iloc[:, 0], axis=0)  # 與第一列進行比較

# 將比較結果寫入新的 Excel 文件
comparison_df.to_excel('comparison_output.xlsx', index=False)