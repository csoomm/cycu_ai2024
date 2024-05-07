#"/workspaces/cycu_ai2024/20240430/M03A/TDCS_M03A_20240429_000000.csv"
#讀取檔案
import pandas as pd

# 讀取檔案
df = pd.read_csv("/workspaces/cycu_ai2024/20240430/03A.csv")

#將第二欄中前兩個字為01的數據篩選出來，並將資料轉換成第四個字到第七個字
df = df[df['Door'].str[:2] == '01']
df['Door'] = df['Door'].str[3:8]

#篩選出Time Door Direction 皆相同的橫列合併，新增欄位31.0,32.0,41.0,42.0,5.0，將相同Time Door Direction的Number放入欄位
df = df.groupby(['Time', 'Door', 'Direction']).agg({'Car': 'first', 'Number': list}).reset_index()
df['31.0'] = df['Number'].apply(lambda x: x[0] if len(x) > 0 else 0)
df['32.0'] = df['Number'].apply(lambda x: x[1] if len(x) > 1 else 0)
df['41.0'] = df['Number'].apply(lambda x: x[2] if len(x) > 2 else 0)
df['42.0'] = df['Number'].apply(lambda x: x[3] if len(x) > 3 else 0)
df['5.0'] = df['Number'].apply(lambda x: x[4] if len(x) > 4 else 0)
df = df.drop(columns=['Number'])

#儲存檔案
df.to_csv("/workspaces/cycu_ai2024/20240430/03A特徵化.csv", index=False)

print(df)

