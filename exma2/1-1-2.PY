import os
import requests
import shutil
import tarfile
import pandas as pd

#檔案如下:[https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240416/00/TDCS_M05A_20240416_000000.csv]

#定義URL和儲存路徑
url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240430/"

for i in range(24):
    for j in range(00,60,5):
        url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240430/"+str(i).zfill(2)+"/TDCS_M05A_20240430_"+str(i).zfill(2)+str(j).zfill(2)+"00.csv"
        #建立資料夾，命名為0416，放在C:\Users\Cosmos\Desktop\0601\exma2中
        save_path = "C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\20240430"
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        #下載檔案
        response = requests.get(url, stream=True)
        with open(save_path+"\\TDCS_M05A_20240430_"+str(i).zfill(2)+str(j).zfill(2)+"00.csv", "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #讀取檔案
        df = pd.read_csv(save_path+"\\TDCS_M05A_20240430_"+str(i).zfill(2)+str(j).zfill(2)+"00.csv")
        #儲存路徑
        output_dir = "C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\20240430"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

#將資料夾中的CSV檔加上column names
column_names = ["time", "ds", "df", "type", "speed", "number"]
for root, dirs, files in os.walk(save_path):
    for file in files:
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(root, file))
            column_first = df.columns
            df = df.shift(periods=1, axis=0)
            df.iloc[0] = column_first
            df.columns = column_names
            df.to_csv(os.path.join(root, file), index=False)
#將所有CSV檔合併成一個檔案，依照time排序
all_csv = []
for root, dirs, files in os.walk(output_dir):
    for file in files:
        if file.endswith(".csv"):
            all_csv.append(os.path.join(root, file))
df = pd.concat([pd.read_csv(csv) for csv in all_csv], ignore_index=True)
df = df.sort_values("time")
df.to_csv("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A_20240430.csv", index=False)

#刪除資料夾output_dir
shutil.rmtree(output_dir)




