import pandas as pd

# 讀取 csv 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/timeyet.csv')


#分別讀取colome:Time中的前兩個字和後兩個字，分別把它們轉換成int，前兩個字*60/5+後兩個字/5
df['Time'] = df['Time'].str[:2].astype(int) * 60 / 5 + df['Time'].str[3:].astype(int) / 5

#儲存檔案，命名為time特徵化.csv
df.to_csv('/workspaces/cycu_ai2024/20240430/time特徵化.csv', index=False)


