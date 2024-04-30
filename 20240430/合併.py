import os
import pandas as pd

# 資料夾的路徑
folder_path = "/workspaces/cycu_ai2024/20240430/M05A"

# 找出資料夾中所有的csv檔案
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 創建一個新的DataFrame，並設定欄位名稱
df_new = pd.DataFrame(columns=['Time', 'Door', 'Door2', 'Car', 'Speed', 'Vehical'])

# 對每一個csv檔案，讀取資料，並將資料加入df_new中
for csv_file in csv_files:
    df = pd.read_csv(os.path.join(folder_path, csv_file))
    df = df.shift(1)
    df.columns = ['Time', 'Door', 'Door2', 'Car', 'Speed', 'Vehical']
    df['Time'] = df['Time'].str.split(' ').str[1]
    df_new = pd.concat([df_new, df])

# 儲存新的csv檔案
df_new.to_csv("/workspaces/cycu_ai2024/20240430/05A.csv", index=False)