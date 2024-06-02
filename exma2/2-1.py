#選擇"C:\Users\Cosmos\Desktop\0601\exma2\20240416.csv"

import os
import requests
import shutil
import tarfile
import pandas as pd

df = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\0601\exma2\\20240429.csv")

#增加一個欄位，命名為weekday，將time轉換成星期幾並放入欄位weekday，星期是從0到6，0代表星期日，6代表星期六
wk = pd.to_datetime(df["time"]).dt.dayofweek
if (wk == 6).all():
    wk = 0
else:
    wk = wk+1    
df["weekday"] = wk

#增加一個欄位，命名為hellday，如果weekday是0或是6，則再hellday放入1
df["hellday"] = 0
df.loc[(df["weekday"] == 0) | (df["weekday"] == 6), "hellday"] = 1
df.loc[(df["weekday"] == 5), "hellday"] = -1

# 將time的格式轉換為"YYYY-MM-DD"的格式
df["time"] = pd.to_datetime(df["time"]).dt.strftime("%Y-%m-%d  %H:%M:%S")
time = pd.to_datetime(df["time"]).dt.strftime("%Y-%m-%d")

# 如果time為1/1,2/8-2/14,2/28,4/4,則將hellday放入1
df.loc[(time == "2024-01-01") | (time == "2024-02-08") | (time == "2024-02-09") | (time == "2024-02-10") | (time == "2024-02-11") | (time == "2024-02-12") | (time == "2024-02-13") | (time == "2024-02-14") | (time == "2024-02-28") | (time == "2024-04-04"), "hellday"] = 1
#如果time為2/7,2/27,4/3,4/30,則將hellday放入-1
df.loc[(time == "2024-02-07") | (time == "2024-02-27") | (time == "2024-04-03") | (time == "2024-04-30"), "hellday"] = -1

#將time的格式為"YYYY-MM-DD %HH:%MM:%HH"，取出MM定義v，取出DD定義w，取出HH定義x，取出MM定義y，計算(v-1)*1440+(w-1)*288+x*12+y=z
v = pd.to_datetime(df["time"]).dt.strftime("%m").astype(int)
w = pd.to_datetime(df["time"]).dt.strftime("%d").astype(int)
x = pd.to_datetime(df["time"]).dt.strftime("%H").astype(int)
y = pd.to_datetime(df["time"]).dt.strftime("%M").astype(int)
z = ((v-1)*1440)+((w-1)*288)+(x*12)+(y/5)
df["time"] = z

#ds與df的格式為"03F3670N"，取出ds前三碼以及df前三碼，分別加入欄位WayIDFrom,WayIDTo
df["WayIDFrom"] = df["ds"].str[:3]
df["WayIDTo"] = df["df"].str[:3]   

#將ds與df的格式為"03F3670N"，取出ds第四到第七碼以及df第四到第七碼，分別加入欄位WayMilageFrom,WayMilageTo，並將她轉換成數字
try:
    df["WayMilageFrom"] = df["ds"].str[3:7].astype(int)
except:
    df["WayMilageFrom"] = df["ds"].str[4:7].astype(int)
try:
    df["WayMilageTo"] = df["df"].str[3:7].astype(int)
except:
    df["WayMilageTo"] = df["df"].str[4:7].astype(int)

#將ds與df的格式為"03F3670N"，取出ds最後一碼以及df最後一碼，分別加入欄位WayDirectionFrom,WayDirectionTo
df["WayDirectionFrom"] = df["ds"].str[-1]
df["WayDirectionTo"] = df["df"].str[-1]

#擷取speed的數字，如果speed<20，則將speed放入0，20<=speed<40，則將speed放入1，40<=speed<60，則將speed放入2，60<=speed<80，則將speed放入3，speed>80，則將speed放入4
df.loc[df["speed"] < 20, "speed"] = 0
df.loc[(df["speed"] >= 20) & (df["speed"] < 40), "speed"] = 1
df.loc[(df["speed"] >= 40) & (df["speed"] < 60), "speed"] = 2
df.loc[(df["speed"] >= 60) & (df["speed"] < 80), "speed"] = 3
df.loc[df["speed"] >= 80, "speed"] = 4

print(df)


#儲存檔案，儲存路徑為C:\Users\Cosmos\Desktop\0601\exma2\特徵化.csv
df.to_csv("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A_20240429_feature.csv", index=False)
