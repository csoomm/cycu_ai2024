import pandas as pd

# 讀取 csv 檔案
df1 = pd.read_csv('/workspaces/cycu_ai2024/20240430/03A特徵化.csv')
df2 = pd.read_csv('/workspaces/cycu_ai2024/20240430/05A特徵化.csv')

# 使用 'Time' 和 'Door' 欄位合併兩個 DataFrame
merged_df = pd.merge(df1, df2[['Time', 'Door', 'Speed']], on=['Time', 'Door'], how='left')

# 儲存結果到新的 csv 檔案
merged_df.to_csv('/workspaces/cycu_ai2024/20240430/merged.csv', index=False)