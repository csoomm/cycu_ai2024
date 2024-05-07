import pandas as pd

# 讀取檔案
df = pd.read_csv("/workspaces/cycu_ai2024/20240430/05A.csv")

#將第二欄中前兩個字為01的數據篩選出來，並將資料轉換成第四個字到第七個字
df = df[df['Door'].str[:2] == '01']
df['Door'] = df['Door'].str[3:8]

#篩選欄位Car為31的數據
df = df[df['Car'] == 31]

#輸出Time Door Car Speed
df = df[['Time', 'Door', 'Car', 'Speed']]
df.to_csv("/workspaces/cycu_ai2024/20240430/05A特徵化.csv", index=False)
